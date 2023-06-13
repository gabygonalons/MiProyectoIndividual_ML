# Machine Learning Operations - Proyecto Individual
Mi Proyecto Individual N°1 - Gabriela Beatriz Goñalons

# Actividad:
Se requiere el desarrollo de un _"Sistema de Recomendación de Películas"_ para lo cuál es necesario llevar adetante una serie de tareas tendientes al cumplimiento del objetivo propuesto.

# Tareas:
1 - Dados dos archivos en formato .csv "Movies_DataSets" y "Credits" en los que se disponía de la información necesaria para alimentar a la API se inicia el proceso de ETL. El proceso de ETL incluyó desanidado de los campos belongs_to_collection, genres, production_companies y spoken_languages de la tabla de Películas y los campos cast y crew de la traba Créditos. Además se debió realizar entre otras acciones: cambio de tipos de datos, eliminación de nulos, eliminación de columnas innecesarias y generación de nuevas columnas.
2 - Finalizado en ETL y generado un nuevo archivo movies_ETL. Se inicia el proceso de desarrollo de las funciones que a posteriori deberían alimentar la API. Una vez elaboradas y probadas las funciones se procedió a la creación y preparación de un entorno virtual para correr FastAPI y luego deployar la web con Render. Dadas las limitaciones de memoria de éste software se procedió a limitar los registros utilizados a las películas estrenadas en los últimos 10 años y se tomaron para el deploy exclusivamnente los campos requeridos.
3 - El paso siguiente consistió en el EDA o Análisis Exploratorio de los Datos que culminó con la re-elaboración de los datos en un nuevo archivo .csv los cuales fueron modificados acorde a las necesidades del sistema de recomedación.
4 - El último paso consistió en el desarrollo del Sistema de Recomendación de películas basado en similaridad a partir del slogan o tagline disponible, dado que no se pudo realizar con el campo overview por ser demasiado extenso. Con sklearn y sus funcionalidades se logró elaborar una matriz de similaridades con el campo tagline a la que se sumo otra matriz basada en el género asignado a las películas. De esta manera se logró desarrollar una función que dado el título de la película retorna las 5 películas más similares acordes a las matrices citadas.

#Enlace al deploy del render:
https://proyecto-gabygonalons.onrender.com/
