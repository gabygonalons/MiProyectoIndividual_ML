# Machine Learning Operations - Proyecto Individual
## Mi Proyecto Individual N°1 - Gabriela Beatriz Goñalons
  <img src=https://fotografias.larazon.es/clipping/cmsimages01/2022/09/15/10F6EC7E-8DEE-449A-848E-3ED3AFD9DD85/98.jpg>

# Proyecto:  _"Sistema de Recomendación de Películas"_

# Tareas:

1 -**ETL**: Dados dos archivos en formato .csv "Movies_DataSets" y "Credits" en los que se disponía de la información necesaria para alimentar a la API se inicia el proceso de ETL. El proceso de ETL incluyó desanidado de los campos belongs_to_collection, genres, production_companies y spoken_languages de la tabla de películas y los campos cast y crew de la tabla créditos. Además se debió realizar entre otras acciones: cambio de tipos de datos, eliminación de nulos, eliminación de columnas innecesarias y generación de nuevas columnas.
Finalizado en ETL y generado un nuevo archivo movies_ETL.

2 -**Funciones**: Se inicia el proceso de desarrollo de las funciones que a posteriori deberían alimentar la API. Una vez elaboradas y probadas las funciones se procedió a la creación y preparación de un entorno virtual para correr _FastAPI_ y luego deployar la web con _Render_. Dadas las limitaciones de memoria de éste software se procedió a limitar los registros utilizados a las películas estrenadas en los últimos 10 años y se tomaron para el deploy exclusivamnente los campos requeridos.

3 -**EDA**: El paso siguiente consistió en el EDA o Análisis Exploratorio de los Datos que culminó con la re-organización de los datos en un nuevo archivo .csv los cuales fueron modificados acorde a las necesidades del sistema de recomedación.

4 -**Deployado**: El último paso consistió en el desarrollo del _Sistema de Recomendación de películas basado en similaridad_ a partir del slogan o tagline disponible, dado que no se pudo realizar con el campo overview por ser demasiado extenso. Con **sklearn** y sus funcionalidades se logró elaborar una matriz de similaridades con el campo tagline a la que se sumo otra matriz basada en el género asignado a las películas. De esta manera se logró desarrollar una función que dado el título de la película retorna las 5 películas más similares acordes a las matrices citadas.

#Enlace al deploy del render:
https://proyecto-gabygonalons.onrender.com/
