import streamlit as st
import pytesseract
from pdf2image import convert_from_bytes
import re

st.title("⚖️ Cloud Document Processor")

# Optimized for a single pre-batched PDF from your phone
uploaded_pdf = st.file_uploader("Upload Scanned PDF Batch", type=['pdf'])

if uploaded_pdf:
    if st.button("Process Batch"):
        # Convert PDF to images (one page at a time to save RAM)
        pages = convert_from_bytes(uploaded_pdf.read())
        
        full_text = ""
        progress_bar = st.progress(0)
        
        for i, page in enumerate(pages):
            text = pytesseract.image_to_string(page)
            full_text += f"\n--- Page {i+1} ---\n{text}"
            progress_bar.progress((i + 1) / len(pages))
            
        st.success("✅ Analysis Complete")
        st.download_button("Download Itinerary", full_text, "Itinerary.txt")
        st.text_area("Preview:", full_text, height=300)