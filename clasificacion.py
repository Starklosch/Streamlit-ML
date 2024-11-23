from typing import NamedTuple
import numpy as np
from onnxruntime import InferenceSession
import pandas as pd

# Definimos la estructura de datos con los nuevos atributos
class ClasificationInput(NamedTuple):
    estado_civil: float
    modo_postulacion: float
    curso: float
    asistencia_dia_noche: float
    calificacion_previa: float
    nacionalidad: float
    calificacion_madre: float
    calificacion_padre: float
    ocupacion_madre: float
    ocupacion_padre: float
    desplazado: float
    necesidades_educativas_especiales: float
    deudor: float
    matricula_al_dia: float
    genero: float
    beca: float
    edad_matriculacion: float
    materias_sin_evaluaciones: float
    tasa_desempleo: float
    tasa_inflacion: float
    PIB: float
    materias_matriculadas: float
    materias_aprobadas: float
    rendimiento_anual: float
    promedio_anual_normalizado: float

# Función para crear el registro
def crear_registro(datos: ClasificationInput):
    return {
        "estado_civil": np.array([[datos.estado_civil]], dtype=np.float32),
        "modo_postulacion": np.array([[datos.modo_postulacion]], dtype=np.float32),
        "curso": np.array([[datos.curso]], dtype=np.float32),
        "asistencia_dia_noche": np.array([[datos.asistencia_dia_noche]], dtype=np.float32),
        "calificacion_previa": np.array([[datos.calificacion_previa]], dtype=np.float32),
        "nacionalidad": np.array([[datos.nacionalidad]], dtype=np.float32),
        "calificacion_madre": np.array([[datos.calificacion_madre]], dtype=np.float32),
        "calificacion_padre": np.array([[datos.calificacion_padre]], dtype=np.float32),
        "ocupacion_madre": np.array([[datos.ocupacion_madre]], dtype=np.float32),
        "ocupacion_padre": np.array([[datos.ocupacion_padre]], dtype=np.float32),
        "desplazado": np.array([[datos.desplazado]], dtype=np.float32),
        "necesidades_educativas_especiales": np.array([[datos.necesidades_educativas_especiales]], dtype=np.float32),
        "deudor": np.array([[datos.deudor]], dtype=np.float32),
        "matricula_al_dia": np.array([[datos.matricula_al_dia]], dtype=np.float32),
        "genero": np.array([[datos.genero]], dtype=np.float32),
        "beca": np.array([[datos.beca]], dtype=np.float32),
        "edad_matriculacion": np.array([[datos.edad_matriculacion]], dtype=np.float32),
        "materias_sin_evaluaciones": np.array([[datos.materias_sin_evaluaciones]], dtype=np.float32),
        "tasa_desempleo": np.array([[datos.tasa_desempleo]], dtype=np.float32),
        "tasa_inflacion": np.array([[datos.tasa_inflacion]], dtype=np.float32),
        "PIB": np.array([[datos.PIB]], dtype=np.float32),
        "materias_matriculadas": np.array([[datos.materias_matriculadas]], dtype=np.float32),
        "materias_aprobadas": np.array([[datos.materias_aprobadas]], dtype=np.float32),
        "rendimiento_anual": np.array([[datos.rendimiento_anual]], dtype=np.float32),
        "promedio_anual_normalizado": np.array([[datos.promedio_anual_normalizado]], dtype=np.float32),
    }


session = InferenceSession("modelos/random_forest.onnx", providers=["CPUExecutionProvider"])
def clasificar(datos: ClasificationInput):
    registro = crear_registro(datos)

    prediccion, probabilidades = session.run(None, registro)
    return prediccion[0]


# datos = pd.DataFrame({'estado_civil': {847: 1, 3927: 1, 524: 1, 223: 1, 3198: 1, 2179: 1, 3592: 1, 3688: 5, 699: 1, 791: 1}, 'modo_postulacion': {847: 8, 3927: 1, 524: 1, 223: 16, 3198: 4, 2179: 1, 3592: 4, 3688: 12, 699: 14, 791: 12}, 'curso': {847: 9, 3927: 15, 524: 13, 223: 12, 3198: 11, 2179: 15, 3592: 14, 3688: 10, 699: 7, 791: 12}, 'asistencia_dia_noche': {847: 1, 3927: 1, 524: 1, 223: 1, 3198: 1, 2179: 1, 3592: 1, 3688: 1, 699: 1, 791: 1}, 'calificacion_previa': {847: 1, 3927: 1, 524: 1, 223: 1, 3198: 3, 2179: 1, 3592: 3, 3688: 1, 699: 1, 791: 1}, 'nacionalidad': {847: 1, 3927: 1, 524: 18, 223: 1, 3198: 1, 2179: 1, 3592: 1, 3688: 1, 699: 1, 791: 1}, 'calificacion_madre': {847: 13, 3927: 23, 524: 5, 223: 13, 3198: 13, 2179: 23, 3592: 16, 3688: 13, 699: 22, 791: 3}, 'calificacion_padre': {847: 14, 3927: 27, 524: 3, 223: 1, 3198: 14, 2179: 27, 3592: 27, 3688: 28, 699: 28, 791: 3}, 'ocupacion_madre': {847: 10, 3927: 6, 524: 2, 223: 6, 3198: 4, 2179: 6, 3592: 4, 3688: 10, 699: 6, 791: 3}, 'ocupacion_padre': {847: 10, 3927: 4, 524: 2, 223: 10, 3198: 4, 2179: 6, 3592: 4, 3688: 11, 699: 8, 791: 3}, 'desplazado': {847: 0, 3927: 1, 524: 1, 223: 0, 3198: 0, 2179: 1, 3592: 1, 3688: 0, 699: 0, 791: 0}, 'necesidades_educativas_especiales': {847: 0, 3927: 0, 524: 0, 223: 0, 3198: 0, 2179: 0, 3592: 0, 3688: 0, 699: 0, 791: 0}, 'deudor': {847: 0, 3927: 1, 524: 0, 223: 0, 3198: 0, 2179: 0, 3592: 0, 3688: 0, 699: 0, 791: 0}, 'matricula_al_dia': {847: 1, 3927: 0, 524: 1, 223: 1, 3198: 1, 2179: 1, 3592: 1, 3688: 1, 699: 1, 791: 0}, 'genero': {847: 0, 3927: 0, 524: 0, 223: 0, 3198: 1, 2179: 0, 3592: 1, 3688: 1, 699: 1, 791: 1}, 'beca': {847: 0, 3927: 0, 524: 0, 223: 1, 3198: 0, 2179: 0, 3592: 0, 3688: 0, 699: 0, 791: 0}, 'edad_matriculacion': {847: 19, 3927: 18, 524: 18, 223: 19, 3198: 35, 2179: 19, 3592: 27, 3688: 34, 699: 39, 791: 36}, 'materias_sin_evaluaciones': {847: 0, 3927: 0, 524: 0, 223: 0, 3198: 0, 2179: 0, 3592: 0, 3688: 0, 699: 0, 791: 0}, 'tasa_desempleo': {847: 11.1, 3927: 13.9, 524: 16.2, 223: 11.1, 3198: 16.2, 2179: 9.4, 3592: 9.4, 3688: 12.4, 699: 13.9, 791: 15.5}, 'tasa_inflacion': {847: 0.6, 3927: -0.3, 524: 0.3, 223: 0.6, 3198: 0.3, 2179: -0.8, 3592: -0.8, 3688: 0.5, 699: -0.3, 791: 2.8}, 'PIB': {847: 2.02, 3927: 0.79, 524: -0.92, 223: 2.02, 3198: -0.92, 2179: -3.12, 3592: -3.12, 3688: 1.79, 699: 0.79, 791: -4.06}, 'materias_matriculadas': {847: 10, 3927: 12, 524: 15, 223: 15, 3198: 12, 2179: 12, 3592: 23, 3688: 12, 699: 10, 791: 13}, 'materias_aprobadas': {847: 7, 3927: 11, 524: 4, 223: 12, 3198: 0, 2179: 12, 3592: 15, 3688: 9, 699: 4, 791: 2}, 'rendimiento_anual': {847: 0.365, 3927: 0.6035714285714285, 524: 0.1714285714285714, 223: 0.5140401785714285, 3198: 0.0, 2179: 0.6345238095238095, 3592: 0.4107954545454545, 3688: 0.45, 699: 0.345, 791: 0.09583333333333333}, 'promedio_anual_normalizado': {847: 0.5229166666666666, 3927: 0.6535714285714286, 524: 0.3, 223: 0.6510714285714284, 3198: 0.0, 2179: 0.6345238095238095, 3592: 0.6375, 3688: 0.5962500000000001, 699: 0.8583333333333332, 791: 0.2875}})
# for dato in datos.iterrows():
#     print(clasificar(ClasificationInput(**dato[1])))
