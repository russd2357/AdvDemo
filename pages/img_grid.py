import streamlit as st
import glob

def load_image():
    images_files = glob.glob("logos/*.png")
    st.write(len(images_files))
    for image_file in images_files:
        st.image(image_file, use_column_width=True)
        st.write(image_file)
    return images_files
        

st.title("Demo Image Grid Display")
image_files = load_image()