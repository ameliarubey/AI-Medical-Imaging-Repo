# 🩻 Medical Imaging Diagnosis Agent

A Medical Imaging Diagnosis Agent built with Python, Streamlit, and Google Gemini that provides AI-assisted analysis of medical images. The agent uses Gemini's multimodal capabilities to analyze uploaded medical images and provide structured observations, diagnostic context, and patient-friendly explanations.


## 🚀 Getting Started

### Prerequisites

- Python 3.11
- A Google Gemini API key
- Internet connection


### 1. Clone the Repository

```bash
git clone https://github.com/ameliarubey/AI-Medical-Imaging-Repo.git

cd AI-Medical-Imaging-Repo
```


### 2. Create a Virtual Environment

```bash
python3.11 -m venv venv
```

Activate it on macOS/Linux:

```bash
source venv/bin/activate
```


### 3. Install Dependencies

```bash
pip install -r requirements.txt
```


### 4. Run the Application

```bash
streamlit run ai_medical_imaging.py
```

The application will open locally at:

`http://localhost:8501`


## ✨ Features

### Comprehensive Image Analysis

- Image Type Identification (X-ray, MRI, CT scan, ultrasound)
- Anatomical Region Detection
- Key Findings and Observations
- Potential Abnormalities Detection
- Image Quality Assessment
- Patient-Friendly Explanations


## 🔑 API Key Setup

The application requires a Google Gemini API key.

1. Create an API key through Google AI Studio.
2. Start the Streamlit application.
3. Enter the API key in the sidebar.
4. Upload a medical image.
5. Select **Analyze Image**.

The API key is entered at runtime and is not hardcoded into the source code.

> **Security:** Never commit API keys, passwords, or other credentials to GitHub.


## 📂 Project Structure

```text
AI-Medical-Imaging-Repo/
│
├── ai_medical_imaging.py
├── requirements.txt
├── README.md
├── .gitignore
└── venv/
```

The `venv/` directory is excluded from version control through `.gitignore`.


## ⚙️ How It Works

1. The user uploads a medical image through the Streamlit interface.

2. Pillow loads and preprocesses the image.

3. The application converts the processed image into PNG bytes.

4. The Google GenAI SDK sends the image and analysis prompt to Gemini.

5. Gemini performs multimodal image understanding.

6. The generated response is displayed as structured analysis in the Streamlit interface.


## 🧠 Analysis Workflow

The application asks Gemini to organize its response into several sections.


### Image Type & Region

Identifies the imaging modality, anatomical region, positioning, and image quality.


### Key Findings

Summarizes visible structures and potential abnormalities based on the supplied image.


### Diagnostic Assessment

Provides an AI-generated assessment and identifies potentially relevant findings.


### Patient-Friendly Explanation

Translates the analysis into simpler language.


### Clinical Context

Provides general contextual information while distinguishing it from direct observations.


## ⚠️ Limitations

- AI-generated medical-image interpretations can contain errors.
- The application does not replace a qualified radiologist or healthcare professional.
- Results should not be used as the sole basis for medical decisions.
- The current implementation performs basic image preprocessing and resizing.
- Image resolution may be reduced during preprocessing.
- The application is intended as an educational software project rather than a clinical diagnostic system.


## 🔮 Future Improvements

- DICOM-specific image handling and metadata processing
- Improved preservation of diagnostic image resolution
- More robust API error handling and retry mechanisms
- Secure environment-variable based API configuration
- Automated unit and integration testing
- Support for additional medical imaging workflows
- Optional integration with verified medical literature sources
- Improved accessibility and user experience

## 📸 Project Preview

Application screenshots are available in the [`screenshots/`](screenshots/) folder.

## 👩‍💻 Author

**Amelia Rubey**

B.Tech Information Technology  
IIIT Allahabad