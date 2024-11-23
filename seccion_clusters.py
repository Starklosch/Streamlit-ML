import streamlit as st

from clusters import ClusterInput, predecir_cluster_de_3, predecir_cluster_de_7
from comun import pedir_rendimiento_con_modal
from descripciones import clusters_3, clusters_7

def seccion_clusters(key):
    # Cabecera
    st.header("Ingresa datos del estudiante")
    st.markdown("Introduce datos del estudiante para obtener una predicción sobre el grupo al que pertenece.")

    # Edad al matricularse
    edad_matriculacion = st.number_input("Edad al matricularse", min_value=15, max_value=100, value=20, key=f"edad_matriculacion_{key}")

    rendimiento_anual = pedir_rendimiento_con_modal(key)

    # Otros datos del estudiante
    situacion = st.selectbox("Situación del estudiante", options=["Matriculado", "Abandonado", "Graduado"], key=f"situacion_{key}")
    beca = st.selectbox("¿Tiene beca?", options=["Sí", "No"], key=f"beca_{key}")
    asistencia_dia_noche = st.radio("Asistencia", options=["Día", "Noche"], key=f"asistencia_dia_noche_{key}")
    desplazado = st.selectbox("¿Es desplazado?", options=["Sí", "No"], key=f"desplazado_{key}")
    matricula_al_dia = st.selectbox("¿Tiene la matrícula al día?", options=["Sí", "No"], key=f"matricula_al_dia_{key}")

    if st.button("Predecir", key=f"boton_predecir_{key}"):
        # Diccionario de situaciones
        situaciones = {
            "Matriculado": "Enrolled",
            "Abandonado": "Dropout",
            "Graduado": "Graduate"
        }

        # Convertir las respuestas en valores numéricos
        situacion = situaciones[situacion]
        beca = 1 if beca == "Sí" else 0
        asistencia_dia_noche = 1 if asistencia_dia_noche == "Día" else 0
        desplazado = 1 if desplazado == "Sí" else 0
        matricula_al_dia = 1 if matricula_al_dia == "Sí" else 0

        # Llamada a la función de predicción (aún no definida)
        datos = ClusterInput(edad_matriculacion, rendimiento_anual, situacion, beca, asistencia_dia_noche, desplazado, matricula_al_dia)
        resultado_de_3 = predecir_cluster_de_3(datos)
        resultado_de_7 = predecir_cluster_de_7(datos)

        # Mostrar el resultado
        cluster_de_3 = clusters_3[resultado_de_3]
        cluster_de_7 = clusters_7[resultado_de_7]
        st.write(f"El estudiante forma parte del **{cluster_de_3.nombre}** en el **modelo de 3 clusters**.")
        st.write(f"El estudiante forma parte del **{cluster_de_7.nombre}** en el **modelo de 7 clusters**.")

    st.header("Descripción de los Clusters")

    # Modelo de 3 Clusters
    st.subheader("Modelo de 3 Clusters")
    for cluster, keywords, description in clusters_3:
        with st.expander(f"{cluster} - {keywords}"):
            st.write(description)

    # Modelo de 7 Clusters
    st.subheader("Modelo de 7 Clusters")
    for cluster, keywords, description in clusters_7:
        with st.expander(f"{cluster} - {keywords}"):
            st.write(description)

