Parking Space Recognition System
================================

The **Parking Space Recognition System** is designed to detect and manage parking spaces in real time using computer vision and machine learning. This system includes several modules for data preparation, classification, and real-time parking spot analysis.

This documentation explains the primary functionalities and key parts of the implementation.

Contents
--------

.. toctree::
   :maxdepth: 2
   :caption: Documentation Sections

   introduction
   key_modules
   svm_vs_yolov8
   how_it_works
   technical_details
   next_steps

Introduction
------------

This project aims to solve the problem of parking space detection by leveraging:
- **Support Vector Machines (SVM)** for classification.
- **YOLOv8** for object detection.
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

4. **app.py**:
   - A Flask-based web application to serve parking detection results.
   - Provides an interface for users to upload videos or select live streams for analysis.

   **Key Features**:
   - Routes:
     - `/`: Renders the homepage with video upload options.
     - `/process`: Processes the uploaded video and returns annotated output.

     ```python
     @app.route('/')
     def home():
         return render_template('index.html')
     ```

   - Uses YOLOv8 for real-time parking spot detection.

5. **yolo_page.py**:
   - Demonstrates the integration of YOLOv8 for detecting parking spaces.
   - **Key Functions**:
     - `run_yolo_inference`: Loads YOLOv8 model and applies it to video frames.
     - `annotate_frame`: Draws bounding boxes for detected parking spots.

     ```python
     results = model.predict(source=frame)
     for box in results.boxes:
         cv2.rectangle(frame, ...)
     ```

   - Includes YOLO's post-processing for bounding box predictions.

6. **SVM vs YOLOv8**:
   - A detailed comparison of the performance and use cases of SVM and YOLOv8.

   **Comparison Table**:
   | Feature               | SVM               | YOLOv8            |
   |-----------------------|-------------------|-------------------|
   | Model Type            | Classifier        | Object Detector   |
   | Accuracy (Test Data)  | ~85%             | ~95%              |
   | Real-time Capability  | Limited          | Excellent         |
   | Implementation Effort | Medium           | High              |

   **Conclusion**:
   - YOLOv8 is better for real-time applications with high accuracy requirements, while SVM is suitable for smaller datasets and simpler setups.

How It Works
------------

1. **Model Training**:
   - A dataset with labeled parking images is prepared and used to train an SVM classifier.
   - The trained model is serialized for future use.

2. **Real-time Detection**:
   - A video feed is processed frame by frame.
   - Parking spots are identified using a pre-defined mask.
   - The system uses the trained SVM or YOLOv8 to determine the status of each spot.

3. **Visualization**:
   - Displays parking status on the video in real time with visual indicators for reserved spots.

Technical Details
-----------------

- **Libraries Used**:
  - Computer Vision: `OpenCV`
  - Machine Learning: `scikit-learn`
  - Image Processing: `scikit-image`
  - Object Detection: `YOLOv8`
  - Web Framework: `Flask`
  - Data Visualization: `Matplotlib`, `Seaborn`

- **Inputs**:
  - A mask image for identifying parking regions.
  - A video stream of the parking lot.

- **Outputs**:
  - Real-time annotated video feed indicating parking occupancy.

Next Steps
----------

- Expand the dataset to improve classifier accuracy.
- Integrate YOLOv8 fully into the Flask application.
- Implement a REST API to integrate with external applications.

For further details, refer to the source code and the examples provided.
