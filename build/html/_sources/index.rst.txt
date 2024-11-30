Parking Space Recognition System
================================

The **Parking Space Recognition System** is designed to detect and manage parking spaces in real time using computer vision and machine learning. This system includes several modules for data preparation, classification, and real-time parking spot analysis.

This documentation explains the primary functionalities and key parts of the implementation.

Contents
--------

.. toctree::
   :maxdepth: 1



Introduction
------------

This project aims to solve the problem of parking space detection by leveraging:
- **Support Vector Machines (SVM)** for classification.
- Computer vision techniques for image processing.
- Real-time video analysis to monitor parking occupancy.

Key Modules
-----------

1. **ParkingSpaceRecognition.py**:
   - Handles data preparation, model training, and evaluation.
   - Trains an SVM model to classify parking spots as "empty" or "not empty."
   - Saves the trained model using Python's `pickle` library.

   **Key Code Explanations:**
   - **Data Preparation**:
     Images are resized to `(15, 15)` for uniformity, flattened, and labeled.

     ```python
     img = resize(img, (15, 15))
     data.append(img.flatten())
     ```

   - **Model Training**:
     A `GridSearchCV` is used to tune hyperparameters like `gamma` and `C` for the SVM classifier.

     ```python
     parameters = [{'gamma': [0.01, 0.001, 0.0001], 'C': [1, 10, 100, 1000]}]
     grid_search = GridSearchCV(classifier, parameters)
     grid_search.fit(x_train, y_train)
     ```

   - **Evaluation**:
     The system evaluates model performance using a confusion matrix.

     ```python
     conf_matrix = confusion_matrix(y_test, y_prediction)
     sns.heatmap(conf_matrix, annot=True, cmap="Blues")
     ```

2. **util.py**:
   - Contains utility functions for parking spot detection and classification.
   - **Key Functions**:
     - `empty_or_not`: Determines if a parking spot is empty using the trained SVM model.
     - `get_parking_spots_bboxes`: Extracts bounding boxes for detected parking spots.

     **Example Usage**:
     ```python
     result = empty_or_not(spot_bgr)
     print(f"Result: {result}")
     ```

3. **main.py**:
   - Integrates the utilities and processes a video to detect parking spots.
   - Uses a pre-defined mask to locate parking regions in the video.

   **Key Features**:
   - Tracks changes in parking occupancy over time using frame differences.

     ```python
     diffs[spot_indx] = calc_diff(spot_crop, previous_frame[y1:y1 + h, x1:x1 + w, :])
     ```

   - Highlights parking spots in green (empty), red (occupied), or blue (reserved).

     ```python
     frame = cv2.rectangle(frame, (x1, y1), (x1 + w, y1 + h), (0, 255, 0), 2)
     ```

How It Works
------------

1. **Model Training**:
   - A dataset with labeled parking images is prepared and used to train an SVM classifier.
   - The trained model is serialized for future use.

2. **Real-time Detection**:
   - A video feed is processed frame by frame.
   - Parking spots are identified using a pre-defined mask.
   - The system uses the trained SVM to determine the status of each spot.

3. **Visualization**:
   - Displays parking status on the video in real time with visual indicators for reserved spots.

Technical Details
-----------------

- **Libraries Used**:
  - Computer Vision: `OpenCV`
  - Machine Learning: `scikit-learn`
  - Image Processing: `scikit-image`
  - Data Visualization: `Matplotlib`, `Seaborn`

- **Inputs**:
  - A mask image for identifying parking regions.
  - A video stream of the parking lot.

- **Outputs**:
  - Real-time annotated video feed indicating parking occupancy.

Next Steps
----------

- Expand the dataset to improve classifier accuracy.
- Implement a REST API to integrate with external applications.

For further details, refer to the source code and the examples provided.

