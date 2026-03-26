import streamlit as st
import pytesseract
from PIL import Image

st.title("⚖️ Doc Processor")

# Direct uploader
f = st.file_uploader("Upload 1 Photo to Test", type=['jpg', 'jpeg', 'png'])

if f is not None:
    st.write("File uploaded successfully.")
    if st.button("Read Text"):
        img = Image.open(f).convert("RGB")
        # Resize immediately to save cloud memory
        img.thumbnail((1000, 1000))
        result = pytesseract.image_to_string(img)
        st.text_area("Found Text:", result, height=200)
