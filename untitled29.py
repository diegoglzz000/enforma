import numpy as np
import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier
st.title("estado físico ")
st.write("Modelo basado en Árbol de Decisión (igual que el Titanic).")

edad = st.number_input("Edad", 1, 100, 30)
peso = st.number_input("Peso (kg)", 20, 200, 70)
frecuencia = st.number_input("Frecuencia cardiaca", 40.0, 150.0, 70.0)
presion = st.number_input("Presión arterial (sistólica)", 80.0, 200.0, 120.0)
sueño = st.number_input("Horas de sueño", 0.0, 12.0, 7.0)
nutricion = st.slider("Calidad nutricional (0 a 10)", 0.0, 10.0, 7.0)
actividad = st.slider("Índice de actividad (1 a 5)", 1.0, 5.0, 3.0)

genero = st.selectbox("Género", ["F", "M"])
fuma = st.selectbox("¿Fuma?", ["No", "Sí"])

genero_val = 1 if genero == "M" else 0
fuma_val = 1 if fuma == "Sí" else 0


test = pd.DataFrame({
    'edad':[edad],
    'peso_kg':[peso],
    'frecuencia_cardiaca':[frecuencia],
    'presión_arterial':[presion],
    'horas_sueño':[suenio],
    'calidad_nutricional':[nutricion],
    'índice_actividad':[actividad],
    'fuma':[fuma_val],
    'género':[genero_val]
})

if st.button("Predecir"):
    pred = dtree.predict(test)[0]
    if pred == 1:
        st.success("La persona está en forma.")
    else:
        st.error("La persona no está en forma.")
