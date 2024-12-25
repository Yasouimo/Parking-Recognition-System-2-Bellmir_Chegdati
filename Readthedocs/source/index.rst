Parking Space Recognition System
================================

**Project for 4th Year Students**  
**Year 2024-2025**  
**Bellmir & Chegdati**  
**Modélisation et Simulation en IA**  

Supervised by:  
**Mr. Tawfik Masrour**

The **Parking Space Recognition System** is designed to detect and manage parking spaces in real-time using computer vision and machine learning. This system includes several modules for data preparation, classification, and real-time parking spot analysis.

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
Parking management has always been a major concern for growing cities. Traditional parking management systems use inefficient means that are not well-suited to today's urban environments. Manual processing such as automatic ticketing, barriers, and human surveillance are common features of traditional parking management. However, it has served for decades, despite its limitations in terms of delay, human error, and inefficiency during peak hours.

Continued urbanization is increasing the number of vehicles, a direct consequence of more advanced parking systems. Another problem is that old parking systems did not adapt well to growing parking demands in densely populated areas. Cities would grow and develop into even more complex systems, and with them, finding available parking spaces would become a nightmare. This would also result in traffic congestion and frustration for the average driver. Conventional systems would not even provide real-time monitoring capabilities, creating longer wait times for drivers and underutilization of parking lots.

All these inefficiencies would not only cause inconvenience to drivers but would ultimately affect the entire traffic flow of the city. In addition to this, modern cities value parking space detection and reservation to improve traffic congestion and more efficient use of spaces. In this project, we have developed an intelligent system that detects parking spaces from images and reserves parking spaces through intuitive interfaces.

The project aims to apply the convergence of computer vision and a Support Vector Machine (SVM) based classifier for efficient, easy, and optimal parking management by a user. This system improves the ability to manage parking resources more efficiently, reducing time spent searching for spaces and minimizing traffic disruption. Ultimately, it provides a smart and scalable solution to the growing challenges of urban parking management, ensuring a smoother and more convenient experience for drivers and urban planners.

For more information about this project, we invite you to visit the link below:  
https://acrobat.adobe.com/id/urn:aaid:sc:eu:183ccef1-418f-464a-ad53-d241eb26c243

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

   **Key Code Explanations**:
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
   +-----------------------+-------------------+-------------------+
   | Feature               | SVM               | YOLOv8            |
   +-----------------------+-------------------+-------------------+
   | Model Type            | Classifier        | Object Detector   |
   | Accuracy (Test Data)  | ~85%              | ~95%              |
   | Real-time Capability  | Limited           | Excellent         |
   | Implementation Effort | Medium            | High              |
   +-----------------------+-------------------+-------------------+

   **Conclusion**:
   - YOLOv8 is better for real-time applications with high accuracy requirements, while SVM is suitable for smaller datasets and simpler setups.

7. **Parking Spot Detection Model Training**
   - Training a YOLOv8 model to detect "empty" and "not_empty" parking spots using a dataset of 1700 images.

   **Training Steps**:
   1. **Dataset Preparation**:  
      A dataset of 1700 labeled images was prepared and stored in the specified directory.
   2. **Library Installation**:  
      Installed required libraries:
      - `ultralytics` using `!pip install ultralytics`
      - `supervision` using `!pip install supervision`
   3. **Model Initialization**:  
      A pretrained YOLOv8 model (`yolov8n.pt`) was loaded with:
      ```python
      from ultralytics import YOLO
      model = YOLO('yolov8n.pt')
      ```
   4. **Training Configuration**:  
      Dataset path was set using:
      ```python
      ROOT_DIR = "/content/drive/MyDrive/Parking detection"
      ```
      Model training executed for 100 epochs:
      ```python
      results = model.train(data=os.path.join(ROOT_DIR, "data.yaml"), epochs=100)
      ```
   5. **Validation**:  
      Model performance on the validation set was evaluated with:
      ```python
      results = model.val()
      ```
   6. **Visualization**:  
      Training results and images were displayed using:
      ```python
      from IPython.display import display, Image
      ```

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
