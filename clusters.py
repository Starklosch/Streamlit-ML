from typing import NamedTuple
import numpy as np
from onnxruntime import InferenceSession

class ClusterInput(NamedTuple):
    edad_matriculacion: int
    rendimiento_anual: float
    situacion: str
    beca: int
    asistencia_dia_noche: int
    desplazado: int
    matricula_al_dia: int

def crear_registro(datos: ClusterInput):
    return {
      "edad_matriculacion": np.array([np.array([datos.edad_matriculacion], dtype=np.int64)]),
      "rendimiento_anual": np.array([np.array([datos.rendimiento_anual], dtype=np.float32)]),
      "situacion": np.array([np.array([datos.situacion])]),
      "beca": np.array([np.array([datos.beca], dtype=np.int64)]),
      "asistencia_dia_noche": np.array([np.array([datos.asistencia_dia_noche], dtype=np.int64)]),
      "desplazado": np.array([np.array([datos.desplazado], dtype=np.int64)]),
      "matricula_al_dia": np.array([np.array([datos.matricula_al_dia], dtype=np.int64)]),
    }

kmeans_3_session = InferenceSession("modelos/kmeans_3_clusters.onnx", providers=["CPUExecutionProvider"])
def predecir_cluster_de_3(datos: ClusterInput):
    registro = crear_registro(datos)

    cluster, distancias = kmeans_3_session.run(None, registro)
    return cluster[0]


kmeans_7_session = InferenceSession("modelos/kmeans_7_clusters.onnx", providers=["CPUExecutionProvider"])
def predecir_cluster_de_7(datos: ClusterInput):
    registro = crear_registro(datos)

    cluster, distancias = kmeans_7_session.run(None, registro)
    return cluster[0]
