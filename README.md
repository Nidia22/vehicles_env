# vehicles_env
sprint7

Análisis

Descripción del proyecto

Este proyecto consiste en una aplicación web desarrollada con Python y Streamlit para explorar y visualizar datos de anuncios de vehículos usados en Estados Unidos.

La aplicación permite:

- Visualizar la distribución de los precios mediante un histograma.
- Explorar la relación entre el año del modelo y el precio mediante un gráfico de dispersion.
- Interactuar con gráficas creadas con Plotly Express.
- Aplicación desplegada
- Enlace a Render: https://vehicles-env-1-3ixr.onrender.com

Estructura del repositorio

vehicles_env/
--app.py
-- vehicles_us.csv
-- requirements.txt
-- README.md
-- notebooks/
    -- EDA.ipynb

* app.py: código de la aplicación web de Streamlit.
* vehicles_us.csv: conjunto de datos de anuncios de vehículos.
* requirements.txt: bibliotecas necesarias para ejecutar el proyecto.
* README.md: documentación del proyecto e instrucciones.
* notebooks/EDA.ipynb: notebook dedicado al análisis exploratorio de los datos.

Librerias utilizadas 

-Python
-Pandas
-Streamlit
-Plotly Express
-Jupyter Notebook

Cómo ejecutar el proyecto

1. Clonar el repositorio
git clone https://github.com/Nidia22/vehicles_env.git
cd vehicles_env

2. Crear un entorno virtual
python -m venv .venv

3. Activar el entorno virtual en Windows
.venv\Scripts\activate

4. Instalar las dependencias
python -m pip install -r requirements.txt

5. Ejecutar la aplicación
streamlit run app.py

Análisis exploratorio de datos

El notebook contiene el análisis exploratorio del conjunto de datos, incluyendo la revisión de su estructura, tipos de datos, valores faltantes, registros duplicados, estadísticas descriptivas, visualizaciones y conclusiones principales.