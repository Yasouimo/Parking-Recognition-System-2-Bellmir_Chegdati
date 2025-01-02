# Parking Recognition system
Project for 4th Year "Modélisation et Simulation en IA" 2024-2025"

By Students Bellmir Yahya&Chegdati Chouaib


Supervised by: Mr.Masrour Tawfik

# Project Structure
Directory structure:
└── Yasouimo-Parking-Recognition-System-2-Bellmir_Chegdati/
    ├── README.md
    ├── packages.txt
    ├── requirementProject.txt
    ├── requirements.txt
    ├── .readthedocs.yaml
    ├── Colab/
    │   └── ParkingDetection_Bellmir_Chegdati.ipynb
    ├── Readthedocs/
    │   ├── README.md
    │   ├── make.bat
    │   ├── build/
    │   │   ├── doctrees/
    │   │   │   ├── environment.pickle
    │   │   │   ├── index.doctree
    │   │   │   └── main_code.doctree
    │   │   └── html/
    │   │       ├── genindex.html
    │   │       ├── index.html
    │   │       ├── main_code.html
    │   │       ├── objects.inv
    │   │       ├── search.html
    │   │       ├── searchindex.js
    │   │       ├── .buildinfo
    │   │       ├── _sources/
    │   │       │   ├── index.rst.txt
    │   │       │   └── main_code.rst.txt
    │   │       └── _static/
    │   │           ├── _sphinx_javascript_frameworks_compat.js
    │   │           ├── alabaster.css
    │   │           ├── basic.css
    │   │           ├── custom.css
    │   │           ├── doctools.js
    │   │           ├── documentation_options.js
    │   │           ├── jquery.js
    │   │           ├── language_data.js
    │   │           ├── pygments.css
    │   │           ├── searchtools.js
    │   │           ├── sphinx_highlight.js
    │   │           ├── css/
    │   │           │   ├── badge_only.css
    │   │           │   ├── theme.css
    │   │           │   └── fonts/
    │   │           │       ├── Roboto-Slab-Bold.woff
    │   │           │       ├── Roboto-Slab-Bold.woff2
    │   │           │       ├── Roboto-Slab-Regular.woff
    │   │           │       ├── Roboto-Slab-Regular.woff2
    │   │           │       ├── fontawesome-webfont.eot
    │   │           │       ├── fontawesome-webfont.ttf
    │   │           │       ├── fontawesome-webfont.woff
    │   │           │       ├── fontawesome-webfont.woff2
    │   │           │       ├── lato-bold-italic.woff
    │   │           │       ├── lato-bold-italic.woff2
    │   │           │       ├── lato-bold.woff
    │   │           │       ├── lato-bold.woff2
    │   │           │       ├── lato-normal-italic.woff
    │   │           │       ├── lato-normal-italic.woff2
    │   │           │       ├── lato-normal.woff
    │   │           │       └── lato-normal.woff2
    │   │           ├── fonts/
    │   │           │   ├── Lato/
    │   │           │   │   ├── lato-bold.eot
    │   │           │   │   ├── lato-bold.ttf
    │   │           │   │   ├── lato-bold.woff
    │   │           │   │   ├── lato-bold.woff2
    │   │           │   │   ├── lato-bolditalic.eot
    │   │           │   │   ├── lato-bolditalic.ttf
    │   │           │   │   ├── lato-bolditalic.woff
    │   │           │   │   ├── lato-bolditalic.woff2
    │   │           │   │   ├── lato-italic.eot
    │   │           │   │   ├── lato-italic.ttf
    │   │           │   │   ├── lato-italic.woff
    │   │           │   │   ├── lato-italic.woff2
    │   │           │   │   ├── lato-regular.eot
    │   │           │   │   ├── lato-regular.ttf
    │   │           │   │   ├── lato-regular.woff
    │   │           │   │   └── lato-regular.woff2
    │   │           │   └── RobotoSlab/
    │   │           │       ├── roboto-slab-v7-bold.eot
    │   │           │       ├── roboto-slab-v7-bold.ttf
    │   │           │       ├── roboto-slab-v7-bold.woff
    │   │           │       ├── roboto-slab-v7-bold.woff2
    │   │           │       ├── roboto-slab-v7-regular.eot
    │   │           │       ├── roboto-slab-v7-regular.ttf
    │   │           │       ├── roboto-slab-v7-regular.woff
    │   │           │       └── roboto-slab-v7-regular.woff2
    │   │           └── js/
    │   │               ├── badge_only.js
    │   │               ├── theme.js
    │   │               └── versions.js
    │   └── source/
    │       ├── Makefile
    │       ├── conf.py
    │       ├── index.rst
    │       ├── main_code.rst
    │       └── Readthedocs/
    │           └── build/
    │               ├── doctrees/
    │               │   ├── environment.pickle
    │               │   ├── index.doctree
    │               │   └── main_code.doctree
    │               └── html/
    │                   ├── genindex.html
    │                   ├── index.html
    │                   ├── main_code.html
    │                   ├── objects.inv
    │                   ├── search.html
    │                   ├── searchindex.js
    │                   ├── .buildinfo
    │                   ├── _sources/
    │                   │   ├── index.rst.txt
    │                   │   └── main_code.rst.txt
    │                   └── _static/
    │                       ├── _sphinx_javascript_frameworks_compat.js
    │                       ├── basic.css
    │                       ├── doctools.js
    │                       ├── documentation_options.js
    │                       ├── jquery.js
    │                       ├── language_data.js
    │                       ├── pygments.css
    │                       ├── searchtools.js
    │                       ├── sphinx_highlight.js
    │                       ├── css/
    │                       │   ├── badge_only.css
    │                       │   ├── theme.css
    │                       │   └── fonts/
    │                       │       ├── Roboto-Slab-Bold.woff
    │                       │       ├── Roboto-Slab-Bold.woff2
    │                       │       ├── Roboto-Slab-Regular.woff
    │                       │       ├── Roboto-Slab-Regular.woff2
    │                       │       ├── fontawesome-webfont.eot
    │                       │       ├── fontawesome-webfont.ttf
    │                       │       ├── fontawesome-webfont.woff
    │                       │       ├── fontawesome-webfont.woff2
    │                       │       ├── lato-bold-italic.woff
    │                       │       ├── lato-bold-italic.woff2
    │                       │       ├── lato-bold.woff
    │                       │       ├── lato-bold.woff2
    │                       │       ├── lato-normal-italic.woff
    │                       │       ├── lato-normal-italic.woff2
    │                       │       ├── lato-normal.woff
    │                       │       └── lato-normal.woff2
    │                       ├── fonts/
    │                       │   ├── Lato/
    │                       │   │   ├── lato-bold.eot
    │                       │   │   ├── lato-bold.ttf
    │                       │   │   ├── lato-bold.woff
    │                       │   │   ├── lato-bold.woff2
    │                       │   │   ├── lato-bolditalic.eot
    │                       │   │   ├── lato-bolditalic.ttf
    │                       │   │   ├── lato-bolditalic.woff
    │                       │   │   ├── lato-bolditalic.woff2
    │                       │   │   ├── lato-italic.eot
    │                       │   │   ├── lato-italic.ttf
    │                       │   │   ├── lato-italic.woff
    │                       │   │   ├── lato-italic.woff2
    │                       │   │   ├── lato-regular.eot
    │                       │   │   ├── lato-regular.ttf
    │                       │   │   ├── lato-regular.woff
    │                       │   │   └── lato-regular.woff2
    │                       │   └── RobotoSlab/
    │                       │       ├── roboto-slab-v7-bold.eot
    │                       │       ├── roboto-slab-v7-bold.ttf
    │                       │       ├── roboto-slab-v7-bold.woff
    │                       │       ├── roboto-slab-v7-bold.woff2
    │                       │       ├── roboto-slab-v7-regular.eot
    │                       │       ├── roboto-slab-v7-regular.ttf
    │                       │       ├── roboto-slab-v7-regular.woff
    │                       │       └── roboto-slab-v7-regular.woff2
    │                       └── js/
    │                           ├── badge_only.js
    │                           ├── theme.js
    │                           └── versions.js
    ├── clf-data/
    │   ├── empty/
    │   └── not_empty/
    ├── data/
    ├── mask/
    ├── models/
    │   ├── best.pt
    │   └── model.p
    ├── src/
    │   ├── ParkingSpaceRecognition.py
    │   ├── app.py
    │   ├── main.py
    │   ├── model.py
    │   ├── util.py
    │   └── yolo_page.py
    └── .devcontainer/
        └── devcontainer.json


# Project Report(Rapport du Projet)
![Page de Garde (1)_page-0001](https://github.com/user-attachments/assets/f772df07-53d7-46d7-a386-31b18c06b51c)
For more information please visit the link below:
https://acrobat.adobe.com/id/urn:aaid:sc:eu:183ccef1-418f-464a-ad53-d241eb26c243

# Readthedocs
U can access Readthedocs through the link below
https://parking-recognition-system-2.readthedocs.io/en/latest/

# SVM model
The **SVM** (Support Vector Machine) model is a supervised learning algorithm used for classification and regression tasks, aiming to find the hyperplane that best separates different classes in a dataset. In your application, it is located in the models/model.p file, likely as a serialized model ready for predictions.

# Yolov8 model
The **YOLOv8** (You Only Look Once version 8) model is a state-of-the-art deep learning algorithm used for real-time object detection, capable of detecting and classifying objects in images and videos. In your application, it is stored in the models/best.pt file, likely as a trained PyTorch model ready for inference.

# Training Steps
U can find the details and steps we took to train our yolov8 model in **colab/ParkingDetection_Bellmir_Chegdati.ipynb**

# Requirement 
To download requirement use the following command

!pip install **-r requirements.txt**

# Running the app
To run the app use the following command

**streamlit run app.py**

# App on streamlit
Visit the link below to visualise the app on streamlitcloud
https://parking-recognition-system-2-bellmirchegdati-v1.streamlit.app/

**Warning**: Please note that some features of the app may be less functional or behave differently due to the limitations of Streamlit Cloud. We recommend using the app locally for the best experience.



