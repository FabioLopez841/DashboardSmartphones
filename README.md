# 📊 Dashboard Interactivo: Análisis del Mercado de Smartphones

## 🧭 Objetivo

Diseñar un **dashboard interactivo** que permita explorar y analizar información clave del mercado global de smartphones, facilitando la toma de decisiones basada en datos.

---

## 📈 Descripción del Proyecto

Este proyecto consiste en el desarrollo de un panel de control visual e intuitivo que presenta una visión integral del mercado de teléfonos inteligentes. El dashboard permite:

- Comparar el rendimiento de marcas líderes
- Analizar la evolución de precios y participación de mercado
- Visualizar tendencias tecnológicas (pantallas, cámaras, baterías, etc.)
- Evaluar características técnicas más populares por segmento

---

## 🗃️ Conjunto de Datos

Los datos provienen de múltiples fuentes (ej. Kaggle, GSMArena, Statista) y fueron consolidados en un único conjunto para facilitar el análisis. Entre los atributos disponibles se encuentran:

- Marca y modelo  
- Fecha de lanzamiento  
- Precio estimado  
- Especificaciones (RAM, almacenamiento, batería, procesador, pantalla, etc.)  
- Sistema operativo  
- Popularidad y calificación de usuarios

---

## 🧪 KPIs Visualizados en el Dashboard

- 📌 **Top 10 marcas por volumen de modelos lanzados**
- 💰 **Evolución de precios por categoría**
- 🔋 **Tendencias de especificaciones técnicas** (batería, RAM, cámara)
- 📱 **Segmentación por tamaño de pantalla y tipo de procesador**
- 🌍 **Distribución regional del mercado**
- 📊 **Comparador dinámico entre modelos**

---

## 🛠️ Herramientas Utilizadas

- **Power BI** / **Tableau** / **Plotly Dash** (según la tecnología empleada)
- Python (Pandas, NumPy) para preparación de datos
- SQL (si se usó una base de datos)
- Diseño de interfaz UX/UI para visualizaciones efectivas

---

## 📷 Vista del Dashboard

![Smartphone Market Dashboard](images/smartphone_dashboard_sample.png)

> *La imagen es solo una muestra, el dashboard completo está disponible en el repositorio o en línea.*

---

## 🧠 Principales Insights

- **Samsung y Xiaomi** dominan en variedad de modelos lanzados por año.
- Las especificaciones técnicas han mejorado notablemente en la gama media en los últimos 5 años.
- La mayoría de los dispositivos se concentran entre **6.1” y 6.7” de pantalla**.
- La relación precio/especificaciones favorece a ciertas marcas emergentes en Asia.

---

## 🚀 Acceso al Dashboard

Puedes acceder al dashboard en línea aquí:  
🔗 [Enlace al Dashboard Interactivo](https://tudashboard.example.com)

O explorar el archivo local en formato `.pbix` / `.twbx` / `.ipynb` según la herramienta utilizada.

---

## 📁 Estructura del Repositorio

```bash
├── data/
│   └── smartphones_market_data.csv
├── dashboard/
│   └── smartphone_dashboard.pbix
├── scripts/
│   └── data_cleaning.py
├── images/
│   └── smartphone_dashboard_sample.png
├── README.md
