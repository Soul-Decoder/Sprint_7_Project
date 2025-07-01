#Importación de librerías
import pandas as pd
import plotly.express as px
import streamlit as st
#Encabezado
st.header('Visualización de datos de anuncios de venta de coches')
#Instrucciones
st.write('A continuación elija que información que desea visualizar:')
#Lectura de datos
car_data = pd.read_csv('vehicles_us.csv') 
#Casilla de verificación para el histograma
build_histogram = st.checkbox('Histograma: Distancia recorrida (Millas)')
#Condicional de la casilla de verificación
if build_histogram:
    #Título del histograma
    st.write('Distribución de la distancia total (Millas)')     
    #Se genera un histograma con 'plotly'
    fig = px.histogram(car_data, x="odometer")
    #Se muestra el gráfico interactivo
    st.plotly_chart(fig, use_container_width=True)

#Casilla de verificación para el histograma
build_scatter = st.checkbox('Gráfico de dispersión: Distancia total y precio')
#Condicional de la casilla de verificación
if build_scatter:
    #Título del gráfico de dispersión
    st.write('Relación entre la distancia total del vehículo y su precio')     
    #Se genera un gráfico de dispersión con 'plotly'
    fig = px.scatter(car_data, x="odometer", y="price")
    #Se muestra el gráfico interactivo
    st.plotly_chart(fig, use_container_width=True)