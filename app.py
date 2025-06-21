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

#-----
st.title("📱 Dashboard de Smartphones")
st.markdown("Visualizaciones interactivas y análisis de datos de smartphones")

# --- CARGA DE DATOS ---
@st.cache_data
def load_data():
    df = pd.read_csv('smartphones.csv')
    return df

df = load_data()
st.success("Datos cargados correctamente.")

# --- VISUALIZACIÓN 1: Histograma de precios ---
st.subheader("1. Distribución de precios")
fig1, ax1 = plt.subplots()
sns.histplot(df['price'], bins=30, kde=True, ax=ax1)
st.pyplot(fig1)

# --- VISUALIZACIÓN 2: Boxplot de rating por marca ---
st.subheader("2. Rating por marca")
fig2, ax2 = plt.subplots(figsize=(12, 5))
sns.boxplot(data=df, x='brand_name', y='rating', ax=ax2)
plt.xticks(rotation=45)
st.pyplot(fig2)

# --- VISUALIZACIÓN 3: Precio vs batería (scatter) ---
st.subheader("3. Precio vs batería")
fig3, ax3 = plt.subplots()
ax3.scatter(df['battery_capacity'], df['price'], alpha=0.6)
ax3.set_xlabel("Capacidad de batería (mAh)")
ax3.set_ylabel("Precio")
ax3.set_title("Precio vs Capacidad de batería")
st.pyplot(fig3)

# --- VISUALIZACIÓN 4: Mapa de calor de correlaciones ---
st.subheader("4. Correlación entre variables numéricas")
fig4, ax4 = plt.subplots(figsize=(10, 8))
sns.heatmap(df.select_dtypes('number').corr(), annot=True, cmap='coolwarm', fmt=".2f", ax=ax4)
st.pyplot(fig4)

# --- VISUALIZACIÓN 5: Pie chart de 5G ---
st.subheader("5. Porcentaje de teléfonos con 5G")
fig5, ax5 = plt.subplots()
df['has_5g'].value_counts().plot.pie(labels=["Sin 5G", "Con 5G"], autopct='%1.1f%%', ax=ax5)
ax5.set_ylabel("")
st.pyplot(fig5)

# --- VISUALIZACIÓN 6: Plotly interactivo rating vs precio ---
st.subheader("6. Gráfico interactivo: Rating vs Precio")
fig6 = px.scatter(df, x="rating", y="price", size="screen_size", color="brand_name", hover_name="model")
st.plotly_chart(fig6, use_container_width=True)

# --- VISUALIZACIÓN 7: Prueba estadística NFC ---
st.subheader("7. ¿Los smartphones con NFC tienen mejor rating?")
nfc_yes = df[df['has_nfc'] == True]['rating'].dropna()
nfc_no = df[df['has_nfc'] == False]['rating'].dropna()
t_stat, p_val = ttest_ind(nfc_yes, nfc_no, equal_var=False)

st.write(f"T-Statistic: `{t_stat:.2f}`, p-value: `{p_val:.4f}`")

fig7, ax7 = plt.subplots()
sns.boxplot(data=df, x='has_nfc', y='rating', ax=ax7)
ax7.set_xticklabels(['Sin NFC', 'Con NFC'])
ax7.set_title("Rating según presencia de NFC")
st.pyplot(fig7)
#-----

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
