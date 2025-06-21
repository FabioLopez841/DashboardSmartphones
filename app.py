import streamlit as st
import pandas as pd
import plotly.express as px

# Leer archivo CSV
df = pd.read_csv("smartphones.csv")

st.set_page_config(page_title="Dashboard de Smartphones", layout="wide")

# Encabezado del dashboard
st.title("📱 Dashboard de Análisis de Smartphones")
st.markdown("Este dashboard interactivo permite explorar características clave de smartphones.")

# Filtros
marcas = df["brand_name"].unique()
marca_seleccionada = st.sidebar.multiselect("Filtrar por marca:", marcas, default=marcas)

df_filtrado = df[df["brand_name"].isin(marca_seleccionada)]

# Métricas clave
col1, col2, col3 = st.columns(3)
col1.metric("Precio Promedio", f"${df_filtrado['price'].mean():,.0f}")
col2.metric("Promedio de RAM", f"{df_filtrado['ram_capacity'].mean():.1f} GB")
col3.metric("Tamaño Promedio de Pantalla", f"{df_filtrado['screen_size'].mean():.2f}\"")

st.markdown("---")

# Gráfico: Histograma del precio
st.subheader("Distribución del Precio")
fig1 = px.histogram(df_filtrado, x="price", nbins=30, title="Histograma de Precios")
st.plotly_chart(fig1, use_container_width=True)

# Gráfico: Dispersión entre batería y pantalla
st.subheader("Relación entre Batería y Tamaño de Pantalla")
fig2 = px.scatter(
    df_filtrado,
    x="battery_capacity",
    y="screen_size",
    size="price",
    color="brand_name",
    hover_data=["model"],
    title="Batería vs. Tamaño de Pantalla"
)
st.plotly_chart(fig2, use_container_width=True)

# Tabla de datos
st.subheader("Vista de Datos Filtrados")
st.dataframe(df_filtrado)

