from typing import NamedTuple
import numpy as np
import pandas as pd
import catboost

# Definir la estructura de los datos de entrada
class PrediccionInput(NamedTuple):
    rendimiento_sem1: float
    evaluaciones_sem1: float
    materias_matriculadas_sem2: int
    curso: int
    matricula_al_dia: int
    tasa_inflacion: float
    edad_matriculacion: int

# Cargar el modelo CatBoost previamente entrenado
model = catboost.CatBoostRegressor()
model.load_model('modelos/catboost_model.cbm')

def predecir_cluster(datos: PrediccionInput) -> float:
    # Convertimos los datos a un DataFrame (o array de NumPy)
    datos_df = pd.DataFrame([{
        'rendimiento_sem1': datos.rendimiento_sem1,
        'evaluaciones_sem1': datos.evaluaciones_sem1,
        'materias_matriculadas_sem2': datos.materias_matriculadas_sem2,
        'curso': datos.curso,
        'matricula_al_dia': datos.matricula_al_dia,
        'tasa_inflacion': datos.tasa_inflacion,
        'edad_matriculacion': datos.edad_matriculacion
    }])

    # Realizamos la predicción
    prediccion = model.predict(datos_df)
    return prediccion[0]
