#Importación de librerías
import pandas as pd
import plotly.express as px
import streamlit as st
#Encabezado
st.header('Visualización de datos de anuncios de venta de coches.')
#Instrucciones
st.write('Elija la que información desea visualizar:')
#Lectura de datos
car_data = pd.read_csv('vehicles_us.csv') 
#Casilla de verificación para el histograma
build_histogram = st.checkbox('Histograma: Distancia recorrida')
#Condicional de la casilla de verificación
if build_histogram:
    #Información de la elección
    st.write('La opción "Histograma" fue seleccionada.\nA continuación, se presenta el gráfico...')     
    #Se genera un histograma con 'plotly'
    fig = px.histogram(car_data, x="odometer", labels={"odometer": "Distancia recorrida (Millas)"})
    #Se definen los títulos del histograma
    #Se define la etiqueta del eje 'y' del histograma
    fig.update_layout(
        title_text="Distribución de la distancia total (Millas)",
        title_font_size=20,
        title_x=0.25,
        title_subtitle_text="La distribución se concentra entre las 0 y 0.3 M",
        title_subtitle_font_size=18,
        yaxis_title="Frecuencia"
    )
    #Se muestra el gráfico interactivo
    st.plotly_chart(fig, use_container_width=True)

#Casilla de verificación para el histograma
build_scatter = st.checkbox('Gráfico de dispersión: Distancia total y precio')
#Condicional de la casilla de verificación
if build_scatter:
    #Título del gráfico de dispersión
    st.write('La opción "Gráfico de dispersión" fue seleccionado.\nA continuación, se presenta el gráfico...')
    #Se calcula el coeficiente de correlación
    coe_cor=car_data["odometer"].corr(car_data["price"])    
    #Se genera un gráfico de dispersión con 'plotly'
    fig = px.scatter(car_data, x="odometer", y="price", labels={"odometer": "Distancia recorrida (Millas)", "price": "Precio ($)"})
    #Se definen los títulos del gráfico de dispersión
    fig.update_layout(
        title_text="Relación entre la distancia total del vehículo y su precio",
        title_font_size=20,
        title_x=0.2,
        title_subtitle_text="Correlación negativa: {:.2f}".format(coe_cor),
        title_subtitle_font_size=18
        )
    #Se muestra el gráfico interactivo
    st.plotly_chart(fig, use_container_width=True)