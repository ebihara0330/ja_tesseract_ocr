import streamlit as st
import pytesseract
from PIL import Image
import cv2
import numpy as np

# Streamlit UI
st.title("Convert Image >>> Japanese text")

uploaded_file = st.file_uploader("Choose an Image", type=["png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='target', use_column_width=True)

    # 文字抽出
    result = pytesseract.image_to_string(image, lang="jpn")
    st.write(result)