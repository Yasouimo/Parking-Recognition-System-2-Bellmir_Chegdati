import cv2
import numpy as np
from util import get_parking_spots_bboxes, empty_or_not


# Fonction pour calculer la différence entre deux images
def calc_diff(im1, im2):
    return np.abs(np.mean(im1) - np.mean(im2))


# Initialisation des chemins des fichiers
mask = 'mask/mask_1920_1080.png'
video_path = 'data/parking_1920_1080.mp4'

# Chargement du masque et ouverture de la vidéo
mask = cv2.imread(mask, 0)
cap = cv2.VideoCapture(video_path)

# Extraire les composants connectés du masque pour détecter les places de parking
connected_components = cv2.connectedComponentsWithStats(mask, 4, cv2.CV_32S)
spots = get_parking_spots_bboxes(connected_components)
spots_status = [None for _ in spots]  # Statut des places (occupée ou libre)
diffs = [None for _ in spots]  # Différence entre les images

previous_frame = None
frame_nmr = 0
ret = True
step = 30
place_a_reserver = None  # Initialement, aucune place n'est réservée

# Affichage de la vidéo sans marquage de réservation
while ret:
    ret, frame = cap.read()

    if frame_nmr % step == 0 and previous_frame is not None:
        for spot_indx, spot in enumerate(spots):
            x1, y1, w, h = spot
            spot_crop = frame[y1:y1 + h, x1:x1 + w, :]
            diffs[spot_indx] = calc_diff(spot_crop, previous_frame[y1:y1 + h, x1:x1 + w, :])

    if frame_nmr % step == 0:
        if previous_frame is None:
            arr_ = range(len(spots))
        else:
            arr_ = [j for j in np.argsort(diffs) if diffs[j] / np.amax(diffs) > 0.4]
        for spot_indx in arr_:
            spot = spots[spot_indx]
            x1, y1, w, h = spot
            spot_crop = frame[y1:y1 + h, x1:x1 + w, :]
            spot_status = empty_or_not(spot_crop)
            spots_status[spot_indx] = spot_status

    if frame_nmr % step == 0:
        previous_frame = frame.copy()

    # Affichage de l'image avec le marquage
    for spot_indx, spot in enumerate(spots):
        spot_status = spots_status[spot_indx]
        x1, y1, w, h = spots[spot_indx]
        if spot_status:
            frame = cv2.rectangle(frame, (x1, y1), (x1 + w, y1 + h), (0, 255, 0), 2)  # Place libre (vert)
        else:
            frame = cv2.rectangle(frame, (x1, y1), (x1 + w, y1 + h), (0, 0, 255), 2)  # Place occupée (rouge)

        # Affichage de l'ID des places
        text = f'ID: {spot_indx + 1}'
        (text_width, text_height), _ = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)
        center_x = x1 + w // 2
        center_y = y1 + h // 2
        text_x = center_x - (text_width // 2)
        text_y = center_y + (text_height // 2)
        cv2.putText(frame, text, (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

        # Marquer la place réservée
        if place_a_reserver == spot_indx + 1:  # Si cette place est réservée
            frame = cv2.rectangle(frame, (x1, y1), (x1 + w, y1 + h), (255, 0, 0), 2)  # Bleu pour la place réservée

    # Afficher la vidéo en temps réel avec les places marquées
    cv2.imshow('Parking Spots Reservation', frame)

    # Vérification si l'utilisateur appuie sur une touche pour changer la place réservée
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):  # Quitter la vidéo
        break
    elif key == ord('r'):  # Appuyer sur 'r' pour réserver ou changer la place
        print(f"Entrez l'ID de la place à réserver (1 à {len(spots)}): ")
        try:
            new_place = int(input())
            if new_place >= 1 and new_place <= len(spots):
                # Vérifier si la place est libre (True signifie libre, False signifie occupée)
                if spots_status[new_place - 1] is True:  # Si la place est libre (True)
                    place_a_reserver = new_place
                    spots_status[place_a_reserver - 1] = False  # Réserver la place (la marquer comme occupée)
                    print(f"Place {place_a_reserver} réservée pour vous!")
                else:
                    print(f"La place {new_place} est déjà occupée. Choisissez une autre place.")
            else:
                print("ID invalide, essayez à nouveau.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")

    frame_nmr += 1

cap.release()
cv2.destroyAllWindows()







































