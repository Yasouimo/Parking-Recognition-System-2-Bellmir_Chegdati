import os
import pickle
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
import seaborn as sns

#SVM : C'est un modèle de machine learning supervisé qui trouve un hyperplan dans un espace à haute dimension pour séparer les classes. Il fonctionne bien avec des marges maximales et utilise des noyaux (kernels) pour séparer les données non linéaires. Un SVM ne nécessite pas de couches de neurones, et il n'est pas conçu pour apprendre de manière hiérarchique, contrairement aux réseaux de neurones.
#Réseau de Neurones : Un réseau de neurones, surtout un réseau profond, est composé de plusieurs couches qui apprennent des représentations hiérarchiques des données, ce qui permet de capturer des relations complexes. Il apprend grâce à la rétropropagation et l'optimisation d'une fonction de coût par des mises à jour successives des poids.
#scikit_image && scikit_learn for data preprocessing
from skimage.io import imread
from skimage.transform import resize
import numpy as np
#training
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
#test
from sklearn.metrics import accuracy_score

# prepare data
input_dir = 'clf-data'
categories = ['empty', 'not_empty']

data = []
labels = []
for category_idx, category in enumerate(categories):
    for file in os.listdir(os.path.join(input_dir, category)):
        img_path = os.path.join(input_dir, category, file)
        img = imread(img_path)
        img = resize(img, (15, 15))
        data.append(img.flatten())
        labels.append(category_idx)

data = np.asarray(data)
labels = np.asarray(labels)



# train / test split
x_train, x_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, shuffle=True, stratify=labels)
#Dans les modèles d'apprentissage supervisé utilisant des réseaux de neurones, où l'entraînement se fait généralement en lots, on spécifie souvent un batch size pour indiquer combien d'images (ou exemples) seront traitées à la fois. Ce paramètre est généralement défini lors de l'appel à une méthode d'entraînement comme fit() dans des bibliothèques comme TensorFlow/Keras ou PyTorch. Pour un modèle SVM, cependant, le concept de "batch" ne s'applique pas vraiment, car l'entraînement est généralement réalisé sur l'ensemble complet des données d'entraînement en une seule passe (ou itération), sans traitement par lots.
# train classifier
classifier = SVC()

parameters = [{'gamma': [0.01, 0.001, 0.0001], 'C': [1, 10, 100, 1000]}]

grid_search = GridSearchCV(classifier, parameters)

grid_search.fit(x_train, y_train)

# test performance
best_estimator = grid_search.best_estimator_

y_prediction = best_estimator.predict(x_test)

score = accuracy_score(y_prediction, y_test)

print('{}% of samples were correctly classified'.format(str(score * 100)))

pickle.dump(best_estimator, open('model.p', 'wb'))

# matrice de confusion

# Prédictions sur l'ensemble de test
y_prediction = best_estimator.predict(x_test)

# Calcul de la matrice de confusion
conf_matrix = confusion_matrix(y_test, y_prediction)

# Affichage de la matrice de confusion
plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, fmt="d", cmap="Blues", xticklabels=categories, yticklabels=categories)
plt.xlabel("Predicted Label")
plt.ylabel("True Label")
plt.title("Confusion Matrix")
plt.show()









