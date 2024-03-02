import streamlit as st
import os
import subprocess
from PIL import Image

detect_script_path = "yolov5/detect.py"
weights_path = "yolov5/best.pt"
output_dir = "tested_images"

st.title("SIGN LANGUAGE DETECTION")
st.header('Trained & Developed by Sai Kiran Patnana')

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image_path = "test_image.jpg"
    with open(image_path, "wb") as f:
        f.write(uploaded_file.getvalue())

    detect_command = f"python {detect_script_path} --weights {weights_path} --img 640 --conf 0.4 --source {image_path}"
    subprocess.run(detect_command, shell=True)
    
    output_image_path = os.path.join(output_dir, "test_image.jpg")
    if os.path.exists(output_image_path):
        detected_image = Image.open(output_image_path)
        st.image(detected_image, caption="Sign Language Recognition Result", use_column_width=True)
    else:
        st.write("Error: Output image not found")

    os.remove(image_path)

# model size: 15 mb