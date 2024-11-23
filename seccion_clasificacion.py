import streamlit as st
from comun import pedir_promedio, pedir_rendimiento_con_modal
from clasificacion import ClasificationInput, clasificar
from diccionarios import dic_estado_civil, dic_modo_postulacion, dic_curso, dic_nacionalidad, dic_ocupacion_madre_padre, dic_calificacion_madre_padre, dic_calificacion_previa

def seccion_clasificacion(key):
    # Cabecera
    st.header("Ingresa datos del estudiante")
    st.markdown("Introduce datos del estudiante para obtener una predicción sobre su continuidad en la carrera.")

    # Edad al matricularse
    edad_matriculacion = st.number_input("Edad al matricularse", min_value=15, max_value=100, key=f"edad_matriculacion_{key}")

    promedio_anual, calificacion_maxima = pedir_promedio(key)

    rendimiento_anual = pedir_rendimiento_con_modal(key)

    promedio_anual_normalizado = promedio_anual / calificacion_maxima

    # Otros datos del estudiante
    # Selección de opciones para el estudiante
    estado_civil_input = st.selectbox("Estado civil", options=list(dic_estado_civil.values()), key=f"estado_civil_{key}")
    modo_postulacion_input = st.selectbox("Modo de postulación", options=list(dic_modo_postulacion.values()), key=f"modo_postulacion_{key}")
    curso_input = st.selectbox("Curso", options=list(dic_curso.values()), key=f"curso_{key}")
    asistencia_dia_noche = st.radio("Asistencia", options=["Día", "Noche"], key=f"asistencia_dia_noche_{key}")

    calificacion_previa_input = st.selectbox("Calificación previa", options=list(dic_calificacion_previa.values()), key=f"calificacion_previa_{key}")
    nacionalidad_input = st.selectbox("Nacionalidad", options=list(dic_nacionalidad.values()), key=f"nacionalidad_{key}")
    calificacion_madre = st.number_input("Calificación promedio de la madre", min_value=0.0, max_value=100.0, key=f"calificacion_madre_{key}")
    calificacion_padre = st.number_input("Calificación promedio del padre", min_value=0.0, max_value=100.0, key=f"calificacion_padre_{key}")

    ocupacion_madre_input = st.selectbox("Ocupación de la madre", options=list(dic_ocupacion_madre_padre.values()), key=f"ocupacion_madre_{key}")
    ocupacion_padre_input = st.selectbox("Ocupación del padre", options=list(dic_ocupacion_madre_padre.values()), key=f"ocupacion_padre_{key}")

    desplazado = st.selectbox("¿Es desplazado?", options=["Sí", "No"], key=f"desplazado_{key}")
    necesidades_educativas_especiales = st.selectbox("¿Tiene necesidades educativas especiales?", options=["Sí", "No"], key=f"necesidades_educativas_especiales_{key}")
    deudor = st.selectbox("¿Es deudor?", options=["Sí", "No"], key=f"deudor_{key}")
    matricula_al_dia = st.selectbox("¿Tiene la matrícula al día?", options=["Sí", "No"], key=f"matricula_al_dia_{key}")

    genero = st.selectbox("Género", options=["Masculino", "Femenino", "Otro"], key=f"genero_{key}")
    beca = st.selectbox("¿Tiene beca?", options=["Sí", "No"], key=f"beca_{key}")

    materias_sin_evaluaciones = st.number_input("Materias sin evaluaciones", min_value=0, value=0, key=f"materias_sin_evaluaciones_{key}")
    tasa_desempleo = st.number_input("Tasa de desempleo (%)", min_value=0.0, max_value=100.0, key=f"tasa_desempleo_{key}")
    tasa_inflacion = st.number_input("Tasa de inflación (%)", min_value=0.0, max_value=100.0, key=f"tasa_inflacion_{key}")
    PIB = st.number_input("PIB (Producto Interno Bruto)", min_value=0.0, key=f"PIB_{key}")
    materias_matriculadas = st.number_input("Número de materias matriculadas", min_value=1, value=6, key=f"materias_matriculadas_{key}")
    materias_aprobadas = st.number_input("Número de materias aprobadas", min_value=0, max_value=materias_matriculadas, value=5, key=f"materias_aprobadas_{key}")

    # Clasificación al presionar el botón
    if st.button("Clasificar", key=f"boton_clasificar_{key}"):
        # Conversión de respuestas en valores numéricos
        estado_civil = dic_estado_civil.get(estado_civil_input, None)
        modo_postulacion = dic_modo_postulacion.get(modo_postulacion_input, None)
        curso = dic_curso.get(curso_input, None)
        asistencia_dia_noche = 1 if asistencia_dia_noche == "Día" else 0
        calificacion_previa = dic_calificacion_previa.get(calificacion_previa_input, None)
        nacionalidad = dic_nacionalidad.get(nacionalidad_input, None)

        calificacion_madre = dic_calificacion_madre_padre.get(calificacion_madre, None)
        calificacion_padre = dic_calificacion_madre_padre.get(calificacion_padre, None)
        ocupacion_madre = dic_ocupacion_madre_padre.get(ocupacion_madre_input, None)
        ocupacion_padre = dic_ocupacion_madre_padre.get(ocupacion_padre_input, None)

        desplazado = 1 if desplazado == "Sí" else 0
        necesidades_educativas_especiales = 1 if necesidades_educativas_especiales == "Sí" else 0
        deudor = 1 if deudor == "Sí" else 0
        matricula_al_dia = 1 if matricula_al_dia == "Sí" else 0
        genero = {"Masculino": 0, "Femenino": 1, "Otro": 2}.get(genero, None)
        beca = 1 if beca == "Sí" else 0

        # Preparación de los datos de entrada para el modelo de clasificación
        datos = ClasificationInput(
            estado_civil=estado_civil,
            modo_postulacion=modo_postulacion,
            curso=curso,
            asistencia_dia_noche=asistencia_dia_noche,
            calificacion_previa=calificacion_previa,
            nacionalidad=nacionalidad,
            calificacion_madre=calificacion_madre,
            calificacion_padre=calificacion_padre,
            ocupacion_madre=ocupacion_madre,
            ocupacion_padre=ocupacion_padre,
            desplazado=desplazado,
            necesidades_educativas_especiales=necesidades_educativas_especiales,
            deudor=deudor,
            matricula_al_dia=matricula_al_dia,
            genero=genero,
            beca=beca,
            edad_matriculacion=edad_matriculacion,
            materias_sin_evaluaciones=materias_sin_evaluaciones,
            tasa_desempleo=tasa_desempleo,
            tasa_inflacion=tasa_inflacion,
            PIB=PIB,
            materias_matriculadas=materias_matriculadas,
            materias_aprobadas=materias_aprobadas,
            rendimiento_anual=rendimiento_anual,
            promedio_anual_normalizado=promedio_anual_normalizado
        )

        # Clasificación
        with st.spinner('Clasificando...'):
            clasificacion = clasificar(datos)

        # Mostrar el resultado de la clasificación
        if clasificacion == "Graduate":
            st.write("Es probable que el estudiante se gradúe")
        else:
            st.write("Es probable que el estudiante abandone la carrera")
