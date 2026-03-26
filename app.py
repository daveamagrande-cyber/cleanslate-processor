import streamlit as st
import pytesseract
from PIL import Image
import io

st.set_page_config(page_title="Doc Processor", layout="centered")
st.title("⚖️ Document Processor")

# Force a simple file uploader to prevent the "Connecting" hang
uploaded_files = st.file_uploader("Select Photos", type=['png', 'jpg', 'jpeg'], accept_multiple_files=True)

if uploaded_files:
    st.info(f"Ready to process {len(uploaded_files)} files.")
    
    if st.button("Start Extraction"):
        full_text = ""
        progress_bar = st.progress(0)
        
        for i, f in enumerate(uploaded_files):
            # Open image and convert to RGB (fixes many mobile upload errors)
            img = Image.open(f).convert("RGB")
            
            # OCR logic
            text = pytesseract.image_to_string(img)
            full_text += f"\n--- Page {i+1} ---\n{text}"
            
            # Update progress
            progress_bar.progress((i + 1) / len(uploaded_files))
        
        st.success("✅ Complete")
        st.text_area("Results:", full_text, height=300)
        st.download_button("Download Text", full_text, "itinerary.txt")
