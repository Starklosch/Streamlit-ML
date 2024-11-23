import streamlit as st

from seccion_clasificacion import seccion_clasificacion
from seccion_clusters import seccion_clusters
from seccion_prediccion import seccion_prediccion


st.title("Estudio sobre la Deserción Estudiantil")
st.markdown("""
Este proyecto analiza las causas detrás de la deserción estudiantil y utiliza algoritmos avanzados de aprendizaje automático para predecir qué estudiantes tienen mayor probabilidad de abandonar sus estudios.
Basándonos en un análisis detallado de variables académicas, económicas y sociales, ofrecemos una herramienta poderosa para identificar patrones y tomar decisiones informadas para reducir la deserción.
""")


# opcion = st.radio("Selecciona una pestaña", ("Sección 1", "Sección 2", "Sección 3"))
clusters, prediccion, clasificacion, conclusiones, referencias = st.tabs(["Clusters", "Predicción", "Clasificación", "Conclusiones", "Referencias"])
with clusters:
    seccion_clusters(1)
with clasificacion:
    seccion_clasificacion(2)
with prediccion:
    seccion_prediccion(3)

with conclusiones:
    # Conclusión detallada
    st.markdown("""
    ### Conclusiones del Estudio

    **Factores Clave de Deserción:**
    Nuestro análisis revela que ciertas variables, como la edad al momento de matricularse, la regularidad en la asistencia y el rendimiento académico, son factores críticos que determinan las tasas de deserción estudiantil. Estas características permiten identificar patrones recurrentes entre los estudiantes con mayor riesgo de abandono.

    **Importancia del Apoyo Financiero:**
    Aunque los estudiantes con becas muestran un rendimiento ligeramente mejor en promedio, el acceso a este tipo de apoyo financiero sigue siendo limitado. Esto sugiere que ampliar la disponibilidad de becas podría tener un impacto positivo en la retención de los estudiantes, especialmente en aquellos provenientes de entornos socioeconómicos desfavorecidos.

    **Segmentación de Estudiantes:**
    A través de técnicas avanzadas de clustering, se lograron identificar grupos con características comunes que ofrecen una visión más clara sobre los perfiles de riesgo. Esta segmentación es clave para entender mejor las necesidades específicas de cada grupo y diseñar intervenciones más efectivas.

    **Estrategias de Mejora:**
    El modelo sugiere que políticas que fortalezcan el apoyo institucional, como programas de asesoramiento académico, tutorías o financiamiento adicional, podrían ser especialmente beneficiosas para los estudiantes en situación de riesgo. Fomentar una mayor regularidad en la asistencia y un enfoque personalizado podría reducir significativamente las tasas de deserción.

    **Impacto Potencial:**
    La implementación de este análisis en entornos académicos tiene el potencial de transformar la manera en que se enfrentan los problemas de deserción. Al permitir estrategias más personalizadas y basadas en datos, las instituciones educativas pueden mejorar no solo sus tasas de retención, sino también el éxito general de sus estudiantes.
    """)

with referencias:
    st.markdown("""
    - *Higher Education Predictors of Student Retention*, disponible en [Kaggle](https://www.kaggle.com/datasets/thedevastator/higher-education-predictors-of-student-retention/). Este dataset proporciona una visión detallada de los factores que afectan la retención estudiantil.

    - *Predicting Student Retention in Higher Education: A Survey and Future Directions* (MDPI). Disponible en [MDPI](https://www.mdpi.com/2306-5729/7/11/146). Este artículo ofrece una revisión de los enfoques utilizados para predecir la retención estudiantil y proporciona contextos metodológicos aplicables a nuestro análisis.
    """)
