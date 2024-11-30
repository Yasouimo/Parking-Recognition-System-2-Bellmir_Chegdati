import streamlit as st
import cv2
import numpy as np
from util import get_parking_spots_bboxes, empty_or_not

# Import additional pages
import yolo_page  # Assurez-vous que `yolo_page.py` est dans le même répertoire

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Select a page:", ["Parking Surveillance", "YOLO Detection"])

if page == "Parking Surveillance":
    # Original parking surveillance logic
    mask_path = 'mask_1920_1080.png'
    video_path = 'data/parking_1920_1080_loop.mp4'

    # Chargement du masque et de la vidéo
    mask = cv2.imread(mask_path, 0)
    if mask is None:
        st.error(f"Erreur : Le fichier de masque '{mask_path}' est introuvable.")
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        st.error(f"Erreur : Le fichier vidéo '{video_path}' est introuvable ou illisible.")

    # Détection des places de parking à partir du masque
    connected_components = cv2.connectedComponentsWithStats(mask, 4, cv2.CV_32S)
    spots = get_parking_spots_bboxes(connected_components)
    spots_status = [None for _ in spots]  # Initialisation du statut des places
    diffs = [None for _ in spots]

    previous_frame = None
    frame_nmr = 0
    step = 60
    place_a_reserver = None

    st.title("Surveillance des places de parking")
    st.write("Affichage en temps réel de l'occupation des places de parking")

    # Sélection de la place à réserver
    place_input = st.text_input("Entrez l'ID de la place à réserver :")
    reserve_button = st.button("Réserver")

    # Placeholder pour l'affichage de la vidéo
    frame_placeholder = st.empty()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break  # Sortir de la boucle si la vidéo est terminée

        if frame_nmr % step == 0 and previous_frame is not None:
            for spot_indx, spot in enumerate(spots):
                x1, y1, w, h = spot
                spot_crop = frame[y1:y1 + h, x1:x1 + w]
                diffs[spot_indx] = np.abs(np.mean(spot_crop) - np.mean(previous_frame[y1:y1 + h, x1:x1 + w]))

        if frame_nmr % step == 0:
            if previous_frame is None:
                arr_ = range(len(spots))
            else:
                arr_ = [j for j in np.argsort(diffs) if diffs[j] / np.amax(diffs) > 0.4]
            for spot_indx in arr_:
                x1, y1, w, h = spots[spot_indx]
                spot_crop = frame[y1:y1 + h, x1:x1 + w]
                spots_status[spot_indx] = empty_or_not(spot_crop)

            previous_frame = frame.copy()

        # Affichage des rectangles autour des places
        for spot_indx, spot in enumerate(spots):
            spot_status = spots_status[spot_indx]
            x1, y1, w, h = spots[spot_indx]
            if spot_status:
                color = (0, 255, 0)  # Place libre (vert)
            else:
                color = (0, 0, 255)  # Place occupée (rouge)

            # Vérifier si cette place est réservée et la marquer en bleu
            if place_a_reserver == spot_indx + 1:
                color = (255, 0, 0)  # Place réservée (bleu)

            frame = cv2.rectangle(frame, (x1, y1), (x1 + w, y1 + h), color, 2)

            # Affichage de l'ID des places
            text = f'ID: {spot_indx + 1}'
            (text_width, text_height), _ = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)
            text_x = x1 + (w // 2) - (text_width // 2)
            text_y = y1 + (h // 2) + (text_height // 2)
            cv2.putText(frame, text, (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

        # Gestion de la réservation via Streamlit
        if reserve_button and place_input.isnumeric():
            try:
                new_place = int(place_input)
                if 1 <= new_place <= len(spots):
                    if spots_status[new_place - 1]:  # Place libre
                        place_a_reserver = new_place
                        spots_status[place_a_reserver - 1] = False  # Marquer comme occupée
                        st.success(f"Place {place_a_reserver} réservée avec succès!")
                    else:
                        st.warning(f"La place {new_place} est déjà occupée.")
                else:
                    st.error("ID invalide. Essayez avec un numéro de place valide.")
            except ValueError:
                st.error("Entrée invalide, veuillez entrer un numéro.")

        # Convertir en RGB et afficher l'image
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_placeholder.image(frame_rgb, channels="RGB")

        frame_nmr += 1

    cap.release()

elif page == "YOLO Detection":
    yolo_page.run()  # Appeler la fonction `run` dans `yolo_page.py`
