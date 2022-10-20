import streamlit as st
from img_classification import teachable_machine_classification
import keras
from PIL import Image, ImageOps
import numpy as np

st.title('Aplicacion de identificacion de los Simpson')


uploaded_file = st.file_uploader("Carga una imagen ...", type=["jpg","jpeg"])
if uploaded_file is not None:
  image = Image.open(uploaded_file)
  st.sidebar.subheader('Hola, bienvenido')
  st.sidebar.subheader('Esta es tu imagen seleccionada')
  st.sidebar.image(image)
  label = teachable_machine_classification(image, 'keras_model.h5') 
  if label == 0:
    st.subheader('Homero Simpson')
  elif label == 1:
    st.subheader('Marge Simpson')
  elif label == 2:
    st.subheader('Bart Simpson')
  elif label == 3:
    st.subheader('Lisa Simpson')
