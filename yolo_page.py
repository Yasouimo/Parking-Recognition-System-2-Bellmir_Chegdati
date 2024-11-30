import streamlit as st
import cv2
import numpy as np
from ultralytics import YOLO

# Charger votre modèle YOLO
weights_path = 'best.pt'  # Remplacez par le chemin de votre modèle
model = YOLO(weights_path)

# Définir un seuil
threshold = 0.5
reserved_spots = []  # Liste des places réservées (par ID)

def process_image(image):
    """Traitement des images avec YOLO"""
    # Charger l'image
    frame = cv2.imdecode(np.frombuffer(image, np.uint8), cv2.IMREAD_COLOR)
    if frame is None:
        st.error("Erreur : Impossible de charger l'image.")
        return

    # Dimensions
    H, W, _ = frame.shape

    # Créer une copie pour le masque
    mask = frame.copy()

    # Effectuer l'inférence YOLO
    results = model(frame)[0]

    # Boucler sur les détections
    for idx, result in enumerate(results.boxes.data.tolist()):
        x1, y1, x2, y2, score, class_id = result
        if score > threshold:
            # Couleur : Vert pour vide (class_id = 0), Rouge pour occupé (class_id = 1)
            color = (0, 255, 0) if class_id == 0 else (0, 0, 255)

            # Vérifier si cette place est réservée et la marquer en bleu
            if idx + 1 in reserved_spots:
                color = (255, 0, 0)  # Bleu pour réservée

            # Dessiner un rectangle rempli avec de la transparence
            overlay = mask.copy()
            cv2.rectangle(overlay, (int(x1), int(y1)), (int(x2), int(y2)), color, -1)
            cv2.addWeighted(overlay, 0.3, mask, 0.7, 0, mask)

            # Ajouter une bordure autour du rectangle
            cv2.rectangle(mask, (int(x1), int(y1)), (int(x2), int(y2)), color, 3)

            # Ajouter une étiquette (numéro de place)
            label = f"Spot {idx + 1}"
            font_scale = 0.6
            font_thickness = 2
            text_x = int(x1)
            text_y = int(y1) - 10 if y1 > 20 else int(y1) + 20
            cv2.putText(mask, label, (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, font_scale, (255, 255, 255),
                        font_thickness)

    return cv2.cvtColor(mask, cv2.COLOR_BGR2RGB)

def run():
    """Page Streamlit pour le traitement YOLO"""
    st.title("Démo YOLO avec Réservation")
    st.write("Téléchargez une image ou une vidéo pour la traiter avec YOLO et réserver des places.")

    # Téléchargement du fichier
    uploaded_file = st.file_uploader("Téléchargez une image ou une vidéo", type=["jpg", "jpeg", "png", "mp4"])

    # Interface pour réserver une place
    place_input = st.text_input("Entrez l'ID de la place à réserver :")
    reserve_button = st.button("Réserver")

    if reserve_button and place_input.isnumeric():
        place_id = int(place_input)
        if place_id > 0:
            if place_id not in reserved_spots:
                reserved_spots.append(place_id)
                st.success(f"Place {place_id} réservée avec succès!")
            else:
                st.warning(f"La place {place_id} est déjà réservée.")

    if uploaded_file:
        file_type = uploaded_file.type

        if "image" in file_type:
            st.write("Traitement de l'image...")
            image = uploaded_file.read()
            result_image = process_image(image)
            if result_image is not None:
                st.image(result_image, caption="Image traitée", use_column_width=True)

        elif "video" in file_type:
            st.write("Traitement de la vidéo...")
            video_bytes = uploaded_file.read()
            temp_file = "temp_video.mp4"

            with open(temp_file, "wb") as f:
                f.write(video_bytes)

            cap = cv2.VideoCapture(temp_file)
            frame_placeholder = st.empty()

            while cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    break

                result_frame = process_image(cv2.imencode('.jpg', frame)[1].tobytes())
                if result_frame is not None:
                    frame_placeholder.image(result_frame, caption="Traitement en cours...", use_column_width=True)

            cap.release()
