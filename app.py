import streamlit as st
import pytesseract
from PIL import Image

st.title("⚖️ Doc Reader Test")

# Test with just one file first
uploaded_file = st.file_uploader("Upload 1 Photo", type=['jpg', 'jpeg', 'png'])

if uploaded_file is not None:
    st.success("File received by server!")
    if st.button("Read Text"):
        with st.spinner("Analyzing..."):
            img = Image.open(uploaded_file).convert("RGB")
            # Shrink image to save memory
            img.thumbnail((800, 800))
            text = pytesseract.image_to_string(img)
            st.text_area("Found Text:", text, height=300)
