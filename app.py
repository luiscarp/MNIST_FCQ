import streamlit as st
st.title("Mi aplicación")
st.sidebar.header("Esta aplicación es solo un demo")
st.sidebar.image("http://fcq.uach.mx/images/institucionales/Escudos/Plano.png")
boton = st.button("globos")
if boton:
  st.balloons()
