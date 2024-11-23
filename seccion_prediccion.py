import streamlit as st
from comun import pedir_rendimiento_con_modal
from prediccion import PrediccionInput, predecir_cluster  # Asumimos que estas clases y funciones están en prediccion.py
from diccionarios import dic_curso  # Importa el diccionario de cursos

def seccion_prediccion(key):
    # Título de la app
    st.header("Predicción de desempeño en el segundo semestre")

    evaluaciones_sem1 = st.number_input("Evaluaciones del primer semestre", min_value=0, key=f"evaluaciones_sem1_{key}")
    materias_matriculadas_sem2 = st.number_input("Número de materias matriculadas en el segundo semestre", min_value=1, value=6, key=f"materias_matriculadas_sem2_{key}")
    curso = st.selectbox("Curso", options=list(dic_curso.values()), index=0, key=f"curso_{key}")
    matricula_al_dia = st.radio("¿Matrícula al día?", options=["Sí", "No"], index=0, key=f"matricula_al_dia_{key}")
    tasa_inflacion = st.number_input("Tasa de inflación (%)", min_value=0.0, max_value=100.0, key=f"tasa_inflacion_{key}")
    edad_matriculacion = st.number_input("Edad al matricularse", min_value=15, max_value=100, key=f"edad_matriculacion_{key}")
    rendimiento_sem1 = pedir_rendimiento_con_modal(key, periodo="del primer semestre")

    # Botón para realizar la predicción
    if st.button("Predecir", key=f"boton_predecir_{key}"):
        # Convertir las descripciones a sus correspondientes números
        curso_num = list(dic_curso.keys())[list(dic_curso.values()).index(curso)]
        matricula_al_dia_num = 1 if matricula_al_dia == "Sí" else 0

        # Crear un objeto PrediccionInput con los datos del formulario
        datos = PrediccionInput(
            rendimiento_sem1=rendimiento_sem1,
            evaluaciones_sem1=evaluaciones_sem1,
            materias_matriculadas_sem2=materias_matriculadas_sem2,
            curso=curso_num,
            matricula_al_dia=matricula_al_dia_num,
            tasa_inflacion=tasa_inflacion,
            edad_matriculacion=edad_matriculacion
        )

        # Realizar la predicción
        with st.spinner('Realizando predicción...'):
            resultado = predecir_cluster(datos) * 100

        # Mostrar el resultado de la predicción
        st.write(f"Se estima que el estudiante tendrá un rendimiento del **{resultado:.2f}%** en el segundo semestre.")
