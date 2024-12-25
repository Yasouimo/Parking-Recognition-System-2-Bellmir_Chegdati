# opencv , scikit_learn , pandas , pillow , scikit_image , matplotlib
import pickle
import matplotlib.pyplot as plt
from skimage.transform import resize
import numpy as np
import cv2


EMPTY = True
NOT_EMPTY = False

MODEL = pickle.load(open("models/model.p", "rb"))


def empty_or_not(spot_bgr):

    flat_data = []

    img_resized = resize(spot_bgr, (15, 15, 3))
    flat_data.append(img_resized.flatten())
    flat_data = np.array(flat_data)

    y_output = MODEL.predict(flat_data)
    print(f"Sortie du modèle : {y_output}")
    if y_output == [0]:
        return EMPTY
    else:
        return NOT_EMPTY # false


def get_parking_spots_bboxes(connected_components):
    (totalLabels, label_ids, values, centroid) = connected_components

    slots = []
    coef = 1
    for i in range(1, totalLabels):

        # Now extract the coordinate points
        x1 = int(values[i, cv2.CC_STAT_LEFT] * coef)
        y1 = int(values[i, cv2.CC_STAT_TOP] * coef)
        w = int(values[i, cv2.CC_STAT_WIDTH] * coef)
        h = int(values[i, cv2.CC_STAT_HEIGHT] * coef)

        slots.append([x1, y1, w, h])

    return slots


# verification 1 :


# Charger une image de test (par exemple une image de place de parking)
# Assure-toi que l'image est dans le bon répertoire ou spécifie le chemin complet
image_path = 'clf-data/not_empty/00000000_00000005.jpg'
spot_bgr = cv2.imread(image_path)



# Appeler la fonction empty_or_not pour cette image
result = empty_or_not(spot_bgr)

# Afficher le résultat
#print(f"Résultat de la prédiction : {result}")

# verification 2

# Créer une image de test (par exemple une image binaire avec des formes)
image = np.zeros((200, 200), dtype="uint8")

# Dessiner quelques rectangles pour simuler des places de parking
cv2.rectangle(image, (10, 10), (60, 60), 255, -1)
cv2.rectangle(image, (80, 10), (130, 60), 255, -1)
cv2.rectangle(image, (10, 80), (60, 130), 255, -1)

# Obtenir les composants connectés
connected_components = cv2.connectedComponentsWithStats(image, connectivity=8, ltype=cv2.CV_32S)
(totalLabels, label_ids, values, centroid) = connected_components

# Créer un masque en noir et blanc pour visualiser chaque composant connecté
bw_mask = np.zeros(image.shape, dtype="uint8")
for label in range(1, totalLabels):  # Ignore le label 0 pour le fond
    bw_mask[label_ids == label] = 255  # Définir les composants connectés en blanc

slots =  get_parking_spots_bboxes(connected_components)
 #Afficher les résultats
print("Boîtes englobantes détectées :")
for i, slot in enumerate(slots):
    x, y, w, h = slot
    print(f"Slot {i+1}: x={x}, y={y}, largeur={w}, hauteur={h}")
# Afficher le masque coloré
#plt.figure(figsize=(6, 6))
#plt.title("Masque en noir et blanc des composants connectés")
#plt.imshow(bw_mask, cmap="gray")
#plt.axis("off")
#plt.show()







