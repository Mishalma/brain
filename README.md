# Brain Tumor Detection Web Application

A Streamlit web application for detecting brain tumors from MRI scan images using deep learning.

## Features

- Upload MRI scan images (JPG, JPEG, PNG)
- Real-time brain tumor detection
- Confidence scores and probability distribution
- Clean and intuitive user interface

## Installation

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Make sure the `Model.h5` file is in the same directory as `app.py`

2. Run the Streamlit app:
```bash
streamlit run app.py
```

3. Open your browser and navigate to the URL shown in the terminal (typically `http://localhost:8501`)

4. Upload an MRI scan image and get instant predictions

## Model Details

- Input size: 224x224 RGB images
- Classes: No Tumor, Tumor Detected
- Architecture: CNN-based deep learning model

## Disclaimer

This is a demonstration tool and should not be used for actual medical diagnosis. Always consult with qualified healthcare professionals for medical advice.
