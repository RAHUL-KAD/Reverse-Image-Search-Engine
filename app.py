from turtle import shape
import streamlit as st
import model
from PIL import Image
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import re

st.title("Reverse Image Search Engine")
st.header("Search for similar Images")

uploaded_file = st.file_uploader("Choose an Image you wish to search for ...", type=['jpg', 'png', 'jpeg', 'PNG'])
count =1
if uploaded_file is not None:
    image_data = uploaded_file.read()
    image = Image.open(uploaded_file)
    image_re = image.resize((224, 224))

    st.image(image, caption='Uploaded Image', use_column_width=True)

    if st.button("Show Similar images"):
        st.write("Similar Images are ... ")
        processed_image = model.extract_features(image_re, model.ResNet50_finetuned_model)
        distances, indices = model.neighbors.kneighbors([processed_image])

        # Don't take the first closest image as it will be the same image
        similar_image_paths = [model.filenames[indices[0][i]] for i in range(1, 50)]
        st.image(similar_image_paths, caption= similar_image_paths, use_column_width=False, width=300)


