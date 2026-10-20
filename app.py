import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')

st.header('Analisis')

hist_button = st.button('Construir histograma de precios')
if hist_button:
    st.write('Distribución de los precios de los vehículos')
    fig = px.histogram(
        car_data,
        x='price',
        title='Distribución de precios de los vehículos',
        labels={'price': 'Precio ($)'}
    )

    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button('Construir gráfico de dispersión')
if scatter_button:
    st.write('Relación entre el año del modelo y el precio')
    fig = px.scatter(
        car_data.dropna(subset=['model_year', 'price', 'model']),
        x='model_year',
        y='price',
        color='model',
        title='Año del modelo vs. precio',
        labels={
            'model_year': 'Año del modelo',
            'price': 'Precio ($)',
            'model': 'Modelo del vehículo'
        }
    )
    st.plotly_chart(fig, use_container_width=True)