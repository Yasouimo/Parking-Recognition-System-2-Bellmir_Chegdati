ParkingSpaceRecognition.py
--------------------------
This script handles the core machine learning logic, including:

- Preprocessing parking images
- Training a Support Vector Machine (SVM) classifier
- Evaluating model performance with accuracy and confusion matrix

Example:
- Input directories: `clf-data/empty` and `clf-data/not_empty`
- Output: Model stored in `model.p`

Highlight:
- SVM is trained using a grid search for hyperparameter optimization.

.. code-block:: python

   from sklearn.svm import SVC
   parameters = [{'gamma': [0.01, 0.001], 'C': [1, 10]}]
   grid_search = GridSearchCV(SVC(), parameters)
   grid_search.fit(x_train, y_train)

Util.py
-------
This module contains utility functions such as:
- `empty_or_not`: Determines if a parking spot is empty.
- `get_parking_spots_bboxes`: Extracts bounding boxes of parking spots from images.
