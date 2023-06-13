from fastapi import FastAPI
from datetime import datetime
import pandas as pd


app = FastAPI()
#http://127.0.0.1:8000


movies = pd.read_csv("movies_API.csv", dtype=str)


#API 1 - Cantidad de Filmaciones al Mes
@app.get('/cantidad_filmaciones_mes/{mes}')
def cantidad_filmaciones_mes(mes: str) -> dict:
    meses = {
        'enero': 1,
        'febrero': 2,
        'marzo': 3,
        'abril': 4,
        'mayo': 5,
        'junio': 6,
        'julio': 7,
        'agosto': 8,
        'septiembre': 9,
        'octubre': 10,
        'noviembre': 11,
        'diciembre': 12
    }

    movies['release_date'] = pd.to_datetime(movies['release_date'])

    movies['mes'] = movies['release_date'].dt.month

    mes_numero = meses.get(mes.lower())

    if mes_numero is None:
        raise ValueError('Mes no válido')

    peliculas_mes = movies[movies['mes'] == mes_numero]
    cantidad_peliculas = len(peliculas_mes)
    resultado = {
        'mes': mes,
        'cantidad_peliculas': cantidad_peliculas
    }
    return resultado

#API 2 - Cantidad de Filmaciones por día
@app.get('/cantidad_filmaciones_dia/{dia}')
def cantidad_filmaciones_dia(dia: str) -> dict:
    dias_semana = {
        'lunes': 0,
        'martes': 1,
        'miércoles': 2,
        'jueves': 3,
        'viernes': 4,
        'sábado': 5,
        'domingo': 6
    }

    movies['release_date'] = pd.to_datetime(movies['release_date'])

    movies['dia_semana'] = movies['release_date'].dt.weekday

    dia_semana_numero = dias_semana.get(dia_semana.lower())

    if dia_semana_numero is None:
        raise ValueError('Día de la semana no válido')

    peliculas_dia_semana = movies[movies['dia_semana'] == dia_semana_numero]
    cantidad_peliculas = len(peliculas_dia_semana)

    resultado = {
        'dia_semana': dia_semana,
        'cantidad_peliculas': cantidad_peliculas
    }

    return resultado

#API 3 - Puntaje por Título
class Movie:
    def __init__(self, titulo, estreno, puntuacion):
        self.titulo = titulo
        self.estreno = estreno
        self.puntuacion = puntuacion

@app.get('/score_titulo/{titulo}')
def score_titulo(titulo: str) -> dict:
    peliculas = movies[movies['title'] == titulo]

    if peliculas.empty:
        return None
    
    pelicula_reciente = peliculas.loc[peliculas['release_year'].astype(int).idxmax()]

    titulo = pelicula_reciente['title']
    estreno = pelicula_reciente['release_year']
    puntuacion = pelicula_reciente['popularity']

    return {'titulo': titulo, 'anio': estreno, 'popularidad': puntuacion}

#API 4 - Votos por título
@app.get('/votos_titulo/{titulo}')
def votos_titulo(titulo: str) -> dict:
    peliculas = movies[movies['title'] == titulo]

    if peliculas.empty:
        return None

    pelicula = peliculas.iloc[0]

    titulo = pelicula['title']
    voto_total = int(pelicula['vote_count'])
    voto_promedio = pelicula['vote_average']

    if voto_total < 2000:
        return "La película no cumple con la condición de tener al menos 2000 valoraciones."

    return {'titulo': titulo, 'anio': pelicula['release_year'], 'voto_total': voto_total, 'voto_promedio': voto_promedio}

#API 5 - Éxito de Actores
@app.get('/get_actor/{nombre_actor}')
def get_actor(nombre_actor: str) -> dict:
    actores_no_directores = movies[movies['directors'] != nombre_actor]
    
    peliculas_actor = actores_no_directores[actores_no_directores['actors'].str.contains(nombre_actor)]
    
    cantidad_peliculas = len(peliculas_actor)
    
    peliculas_actor['return'] = pd.to_numeric(peliculas_actor['return'], errors='coerce')
    
    retorno_total = peliculas_actor['return'].sum()
    promedio_retorno = peliculas_actor['return'].mean()
    
    resultados = {
        'cantidad_peliculas': str(cantidad_peliculas),
        'retorno_total': str(retorno_total),
        'promedio_retorno': str(promedio_retorno)
    }
    
    return resultados

#Sistema de Recomendación
@app.get('/get_pelicula/{nombre_pelicula}')
def get_pelicula(titulo: str) -> dict:
    indice_pelicula = movies[movies['title'] == titulo].index[0]
    
    fila_similitudes = cosine_sims[indice_pelicula]
    
    indices_ordenados = fila_similitudes.argsort()[::-1]
    
    indices_similares = indices_ordenados[1:6]
    
    titulos_similares = movies.loc[indices_similares, 'title'].values
    generos_similares = movies.loc[indices_similares, 'genres'].values
    
    peliculas_similares = {
        i: (titulo, genero)
        for i, (titulo, genero) in enumerate(zip(titulos_similares, generos_similares), 1)
    }
    
    return peliculas_similares

