import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import streamlit as st
from scipy.stats import ttest_ind

# Leer el archivo CSV
df = pd.read_csv("smartphones.csv")  # Asegúrate de que 'datos.csv' contenga las columnas indicadas

# Encabezado de la aplicación
st.header("Visualización Interactiva de Smartphones")

# Mostrar una vista previa del conjunto de datos
st.write("Vista previa de los datos:")
st.write(df.head())

# Selección de columna numérica para el histograma
columnas_numericas = [
    'price', 'rating', 'num_cores', 'processor_speed',
    'battery_capacity', 'fast_charging', 'ram_capacity',
    'internal_memory', 'screen_size', 'refresh_rate',
    'num_rear_cameras', 'num_front_cameras',
    'primary_camera_rear', 'primary_camera_front',
    'extended_upto', 'resolution_width', 'resolution_height'
]

# Filtrar solo columnas que existen realmente en el dataframe (por si faltan algunas)
columnas_disponibles = [col for col in columnas_numericas if col in df.columns]

# Mostrar el selector solo si hay columnas numéricas disponibles
if columnas_disponibles:
    columna = st.selectbox("Selecciona una variable numérica para el histograma:", columnas_disponibles)

    # Botón para mostrar el histograma
    if st.button("Mostrar histograma"):
        fig = px.histogram(df, x=columna, title=f"Histograma de {columna}")
        st.plotly_chart(fig)
else:
    st.warning("No se encontraron columnas numéricas en el archivo.")
