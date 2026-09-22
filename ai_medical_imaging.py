import os
from PIL import Image as PILImage
import streamlit as st
from google import genai
from google.genai import types

if "GOOGLE_API_KEY" not in st.session_state:
    st.session_state.GOOGLE_API_KEY = None

with st.sidebar:
    st.title("ℹ️ Configuration")
    
    if not st.session_state.GOOGLE_API_KEY:
        api_key = st.text_input(
            "Enter your Google API Key:",
            type="password"
        )
        st.caption(
            "Get your API key from [Google AI Studio]"
            "(https://aistudio.google.com/apikey) 🔑"
        )
        if api_key:
            st.session_state.GOOGLE_API_KEY = api_key
            st.success("API Key saved!")
            st.rerun()
    else:
        st.success("API Key is configured")
        if st.button("🔄 Reset API Key"):
            st.session_state.GOOGLE_API_KEY = None
            st.rerun()
    
    st.info(
        "This tool provides AI-powered analysis of medical imaging data using "
        "advanced computer vision and radiological expertise."
    )
    st.warning(
        "⚠DISCLAIMER: This tool is for educational and informational purposes only. "
        "All analyses should be reviewed by qualified healthcare professionals. "
        "Do not make medical decisions based solely on this analysis."
    )

gemini_client = (
    genai.Client(api_key=st.session_state.GOOGLE_API_KEY)
    if st.session_state.GOOGLE_API_KEY
    else None
)
if not gemini_client:
    st.warning("Please configure your API key in the sidebar to continue")
# Medical Analysis Query
query = """
You are a highly skilled medical imaging expert with extensive knowledge in radiology and diagnostic imaging. Analyze the patient's medical image and structure your response as follows:

### 1. Image Type & Region
- Specify imaging modality (X-ray/MRI/CT/Ultrasound/etc.)
- Identify the patient's anatomical region and positioning
- Comment on image quality and technical adequacy

### 2. Key Findings
- List primary observations systematically
- Note any abnormalities in the patient's imaging with precise descriptions
- Include measurements and densities where relevant
- Describe location, size, shape, and characteristics
- Rate severity: Normal/Mild/Moderate/Severe

### 3. Diagnostic Assessment
- Provide primary diagnosis with confidence level
- List differential diagnoses in order of likelihood
- Support each diagnosis with observed evidence from the patient's imaging
- Note any critical or urgent findings

### 4. Patient-Friendly Explanation
- Explain the findings in simple, clear language that the patient can understand
- Avoid medical jargon or provide clear definitions
- Include visual analogies if helpful
- Address common patient concerns related to these findings

### 5. Research Context
- Briefly mention relevant clinical context if it can be inferred from the image.
- Clearly distinguish observations from general medical information.
- Do not claim to have performed external literature searches.

Format your response using clear markdown headers and bullet points. Be concise yet thorough.
"""

st.title("🏥 Medical Imaging Diagnosis Agent")
st.write("Upload a medical image for professional analysis")

# Create containers for better organization
upload_container = st.container()
image_container = st.container()
analysis_container = st.container()

with upload_container:
    uploaded_file = st.file_uploader(
        "Upload Medical Image",
        type=["jpg", "jpeg", "png", "dicom"],
        help="Supported formats: JPG, JPEG, PNG, DICOM"
    )

if uploaded_file is not None:
    with image_container:
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            image = PILImage.open(uploaded_file)
            width, height = image.size
            aspect_ratio = width / height
            new_width = 500
            new_height = int(new_width / aspect_ratio)
            resized_image = image.resize((new_width, new_height))
            
            st.image(
                resized_image,
                caption="Uploaded Medical Image",
                use_container_width=True
            )
            
            analyze_button = st.button(
                "🔍 Analyze Image",
                type="primary",
                use_container_width=True
            )
    
    with analysis_container:
        if analyze_button:
            with st.spinner("🔄 Analyzing image... Please wait."):
                try:
                    temp_path = "temp_resized_image.png"
                    resized_image.save(temp_path)
                    
                    # Read the image as bytes
                    with open(temp_path, "rb") as image_file:
                        image_bytes = image_file.read()

                    # Send the image and analysis prompt directly to Gemini
                    response = gemini_client.models.generate_content(
                        model="gemini-3.5-flash-lite",
                        contents=[
                            types.Part.from_bytes(
                                data=image_bytes,
                                mime_type="image/png"
                            ),
                            query
                        ]
                    )
                    st.markdown("### 📋 Analysis Results")
                    st.markdown("---")
                    st.markdown(response.text)
                    st.markdown("---")
                    st.caption(
                        "Note: This analysis is generated by AI and should be reviewed by "
                        "a qualified healthcare professional."
                    )
                except Exception as e:
                    st.error(f"Analysis error: {e}")
else:
    st.info("👆 Please upload a medical image to begin analysis")
