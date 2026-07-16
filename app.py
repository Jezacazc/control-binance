import streamlit as st
import pandas as pd

# Configuración básica
st.set_page_config(page_title="Mi App Binance", layout="centered")

st.title("📊 Control de Operaciones")

# Datos de prueba
datos = [
    {"Fecha": "2026-07-15", "Tipo": "Compra", "Monto_USD": 100, "Precio_Bs": 390},
    {"Fecha": "2026-07-15", "Tipo": "Venta", "Monto_USD": 100, "Precio_Bs": 395}
]
df = pd.DataFrame(datos)

st.write("Aquí verás tus operaciones:")
st.dataframe(df)

st.success("La aplicación está funcionando correctamente.")