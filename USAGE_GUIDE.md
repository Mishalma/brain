# Brain Tumor Detection - Usage Guide

## Features

### 1. **AI-Powered Brain Tumor Detection**
- Upload MRI scan images (JPG, JPEG, PNG)
- Get instant predictions with confidence scores
- View probability distribution for both classes

### 2. **Gemini AI Medical Report Generation**
- Click "Generate Detailed Medical Report" button
- AI analyzes the MRI scan and prediction results
- Generates comprehensive medical report with:
  - Clinical Findings
  - AI Analysis Summary
  - Radiological Observations
  - Recommendations for physicians
  - Additional Notes

### 3. **PDF Report Download**
- Professional PDF report generation
- Includes patient information
- AI prediction results
- Detailed Gemini analysis
- Medical disclaimer
- Timestamped filename

## How to Use

### Step 1: Enter Patient Information (Optional)
- In the sidebar, enter:
  - Patient Name
  - Patient ID

### Step 2: Upload MRI Scan
- Click "Choose an MRI scan image..."
- Select an MRI image file
- Image will be displayed automatically

### Step 3: View Prediction
- AI model analyzes the image
- Results show:
  - Prediction (No Tumor / Tumor Detected)
  - Confidence percentage
  - Probability distribution

### Step 4: Generate Medical Report
- Click "Generate Detailed Medical Report"
- Wait for Gemini AI to analyze
- Review the comprehensive medical analysis

### Step 5: Download PDF Report
- Click "📥 Download PDF Report"
- PDF includes all information and analysis
- Filename format: `brain_tumor_report_YYYYMMDD_HHMMSS.pdf`

## Technical Details

- **Model Input Size:** 224x224 RGB images
- **AI Model:** CNN-based deep learning
- **Report Generation:** Google Gemini 1.5 Flash
- **Classes:** No Tumor, Tumor Detected

## Important Notes

⚠️ **Medical Disclaimer:**
This is a demonstration tool and should NOT be used for actual medical diagnosis. All findings must be reviewed and validated by qualified radiologists or physicians before making any clinical decisions.

## Troubleshooting

### App won't start
```bash
pip install -r requirements.txt
streamlit run app.py
```

### Model not found
Ensure `Model.h5` is in the same directory as `app.py`

### Gemini API error
Check that your `.env` file contains a valid `GEMINI_API_KEY`

## Support

For issues or questions, please refer to the README.md file.
