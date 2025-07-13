# 🅿️ Parking Space Recognition System

An intelligent computer vision system that detects and classifies parking spaces in real-time using machine learning algorithms.

[![Documentation](https://img.shields.io/badge/docs-readthedocs-blue)](https://parking-recognition-system-2.readthedocs.io/en/latest/)
[![Streamlit App](https://img.shields.io/badge/app-streamlit-red)](https://parking-recognition-system-2-bellmirchegdati-v1.streamlit.app/)
[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Models](#models)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Documentation](#documentation)
- [Demo](#demo)
- [Performance](#performance)
- [Contributing](#contributing)
- [Authors](#authors)
- [License](#license)

## 🎯 Overview

This project addresses the growing challenge of urban parking management by leveraging advanced computer vision and machine learning techniques. The system can automatically detect and classify parking spaces as "empty" or "occupied" from video streams or images.

**Academic Project Details:**
- **Course:** Modélisation et Simulation en IA (4th Year)
- **Academic Year:** 2024-2025
- **Institution:** [Your University Name]
- **Supervisor:** Mr. Tawfik Masrour

![Page de Garde (1)_page-0001](https://github.com/user-attachments/assets/f772df07-53d7-46d7-a386-31b18c06b51c)

## ✨ Features

- **Real-time Detection:** Process video streams for live parking space monitoring
- **Dual Model Support:** Choose between SVM and YOLOv8 models based on your requirements
- **Web Interface:** User-friendly Streamlit application for easy interaction
- **High Accuracy:** Achieves ~85% accuracy with SVM and ~95% with YOLOv8
- **Scalable Architecture:** Modular design for easy integration and expansion
- **Visual Analytics:** Comprehensive performance metrics and confusion matrices

## 🧠 Models

### Support Vector Machine (SVM)
- **File:** [`models/model.p`](models/model.p)
- **Type:** Classification model
- **Accuracy:** ~85%
- **Use Case:** Suitable for smaller datasets and simpler setups
- **Training:** Grid search optimization for hyperparameters

### YOLOv8 (You Only Look Once v8)
- **File:** [`models/best.pt`](models/best.pt)
- **Type:** Object detection model
- **Accuracy:** ~95%
- **Use Case:** Real-time applications with high accuracy requirements
- **Training:** 100 epochs on 1700 labeled images

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Git (for cloning the repository)

### Clone the Repository
```bash
git clone https://github.com/yourusername/parking-space-recognition.git
cd parking-space-recognition
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Additional Requirements (if needed)
```bash
pip install -r requirementProject.txt
```

## 💻 Usage

### Running the Streamlit Application
```bash
streamlit run src/app.py
```

### Training Models
For detailed training steps and model development, refer to:
- **Jupyter Notebook:** [`Notebook/ParkingDetection_Bellmir_Chegdati.ipynb`](Notebook/ParkingDetection_Bellmir_Chegdati.ipynb)
- **Training Script:** [`src/ParkingSpaceRecognition.py`](src/ParkingSpaceRecognition.py)

### Using Individual Components
```python
# Example usage of the SVM model
from src.model import load_model
from src.util import empty_or_not

# Load the trained model
model = load_model('models/model.p')

# Classify a parking spot
result = empty_or_not(model, image_crop)
```

## 📁 Project Structure

```
parking-space-recognition/
├── 📁 src/                          # Source code
│   ├── app.py                       # Streamlit web application
│   ├── main.py                      # Main execution script
│   ├── model.py                     # Model utilities
│   ├── ParkingSpaceRecognition.py   # SVM training and evaluation
│   ├── util.py                      # Utility functions
│   └── yolo_page.py                 # YOLOv8 integration
├── 📁 models/                       # Trained models
│   ├── model.p                      # SVM model (pickle)
│   └── best.pt                      # YOLOv8 model (PyTorch)
├── 📁 data/                         # Dataset and videos
│   └── parking_1920_1080.mp4       # Sample parking video
├── 📁 mask/                         # Parking spot masks
│   ├── mask_1920_1080.png          # Main mask file
│   └── mask_crop.png               # Cropped mask
├── 📁 clf-data/                     # Classification dataset
│   ├── empty/                       # Empty parking spots
│   └── not_empty/                   # Occupied parking spots
├── 📁 Notebook/                     # Jupyter notebooks
│   └── ParkingDetection_Bellmir_Chegdati.ipynb
├── 📁 Readthedocs/                  # Documentation
├── requirements.txt                 # Python dependencies
├── requirementProject.txt           # Additional requirements
└── README.md                        # This file
```

## 📚 Documentation

Comprehensive documentation is available on ReadTheDocs:
**[📖 View Documentation](https://parking-recognition-system-2.readthedocs.io/en/latest/)**

### Key Documentation Sections:
- **Technical Implementation:** Detailed code explanations
- **Model Comparison:** SVM vs YOLOv8 performance analysis
- **API Reference:** Function and class documentation
- **Training Guide:** Step-by-step model training process

## 🌐 Demo

### Live Demo
Experience the system in action:
**[🚀 Try the Live Demo](https://parking-recognition-system-2-bellmirchegdati-v1.streamlit.app/)**

> **Note:** Some features may be limited on Streamlit Cloud. For the best experience, run the application locally.

### Project Report
For comprehensive project details and research methodology:
**[📄 View Full Report](https://acrobat.adobe.com/id/urn:aaid:sc:eu:183ccef1-418f-464a-ad53-d241eb26c243)**

## 📊 Performance

| Feature | SVM | YOLOv8 |
|---------|-----|---------|
| **Model Type** | Classifier | Object Detector |
| **Accuracy** | ~85% | ~95% |
| **Real-time Capability** | Limited | Excellent |
| **Implementation Effort** | Medium | High |
| **Dataset Size** | Smaller datasets | Large datasets |
| **Use Case** | Simple setups | Production environments |

## 🛠️ Technical Stack

- **Computer Vision:** OpenCV
- **Machine Learning:** scikit-learn
- **Deep Learning:** YOLOv8 (Ultralytics)
- **Web Framework:** Streamlit
- **Image Processing:** scikit-image
- **Data Visualization:** Matplotlib, Seaborn
- **Data Handling:** NumPy, Pandas

## 🤝 Contributing

We welcome contributions to improve the system! Here's how you can help:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/AmazingFeature`)
3. **Commit** your changes (`git commit -m 'Add some AmazingFeature'`)
4. **Push** to the branch (`git push origin feature/AmazingFeature`)
5. **Open** a Pull Request

## 👥 Authors

**Students:**
- **Bellmir Yahya** - [Github](https://github.com/Yasouimo) | [LinkedIn](https://www.linkedin.com/in/yahya-bellmir-a54176284/)
- **Chegdati Chouaib** - [Chegdati Chouaib](https://github.com/chouaibneuralnets) | [LinkedIn](https://www.linkedin.com/in/chouaib-chegdati-75a3a3302/)

**Supervisor:**
- **Mr. Tawfik Masrour** - Academic Supervisor

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔮 Future Enhancements

- [ ] Expand dataset for improved accuracy
- [ ] Implement REST API for external integrations
- [ ] Add support for multiple camera angles
- [ ] Integrate with parking management systems
- [ ] Mobile application development
- [ ] Real-time notifications for available spaces

## 📞 Contact

For questions, suggestions, or collaboration opportunities:

- **Email:** [your.email@example.com]
- **Project Link:** [https://github.com/yourusername/parking-space-recognition]
- **Documentation:** [https://parking-recognition-system-2.readthedocs.io/en/latest/]

---

⭐ **Star this repository if you found it helpful!** ⭐



