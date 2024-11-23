from calendar import c
import streamlit as st

# Función para calcular el rendimiento anual
def calcular_rendimiento(promedio_anual, calificacion_maxima, materias_aprobadas, materias_inscritas):
    return (promedio_anual / calificacion_maxima) * (materias_aprobadas / materias_inscritas)

def pedir_promedio(key=None, periodo="anual"):
    calificacion_maxima = st.number_input(
        "Calificación máxima (por ejemplo, 100)",
        min_value=1.0,
        max_value=1000.0,
        value=100.0,
        step=1.0,
        key=f"calificacion_maxima_{key}"
    )
    promedio_anual = st.number_input(
        f"Promedio {periodo}",
        min_value=0.0,
        max_value=calificacion_maxima,
        value=50.0,
        step=1.0,
        help="Como máximo debe ser igual a la calificación máxima.",
        key=f"promedio_{key}"
    )
    return promedio_anual, calificacion_maxima

def pedir_rendimiento(key=None, periodo="anual"):
    # Pregunta si quiere calcular el rendimiento anual o ingresarlo directamente
    with st.container(border=True):
        calcular_rendimiento_manual = st.checkbox(
            "No cuento con el rendimiento " + periodo,
            help="Selecciona esta opción para calcularlo en base a la cantidad de materias inscritas, aprobadas, calificación promedio y calificación máxima posible.",
            key=f"calcular_rendimiento_manual_{key}"
        )

        promedio_anual = None
        calificacion_maxima = None
        if calcular_rendimiento_manual:
            st.write(f"Indica los siguientes valores para calcular el rendimiento {periodo}:")

            # Ingresar los valores necesarios para calcular el rendimiento anual
            promedio_anual, calificacion_maxima = pedir_promedio(key, periodo)
            materias_inscritas = st.number_input(
                "Número de materias inscritas",
                min_value=0,
                value=6,
                key=f"materias_inscritas_{key}"
            )
            materias_aprobadas = st.number_input(
                "Número de materias aprobadas",
                min_value=0,
                max_value=materias_inscritas,
                value=5,
                help="Como máximo debe ser igual al número de materias inscritas.",
                key=f"materias_aprobadas_{key}"
            )

            # Cálculo del rendimiento anual
            rendimiento = calcular_rendimiento(promedio_anual, calificacion_maxima, materias_aprobadas, materias_inscritas)
            st.write(f"El rendimiento {periodo} calculado es: {rendimiento * 100:.2f}%")
        else:
            # Si no se desea calcular el rendimiento manual, se usa el valor ingresado por el slider
            rendimiento = st.slider(
                f"Rendimiento {periodo} (0-100%)",
                min_value=0,
                max_value=100,
                value=70,
                key=f"rendimiento_slider_{key}"
            ) / 100.0

    return rendimiento, calcular_rendimiento_manual, promedio_anual, calificacion_maxima




@st.dialog("Calcular Rendimiento Anual")
def modal(key = "", periodo = "anual", *, promedio = None, calificacion_maxima = None, materias_aprobadas = None, materias_inscritas = None):
    st.write(f"Indica los siguientes valores para calcular el rendimiento {periodo}:")

    if calificacion_maxima is None:
        calificacion_maxima = st.number_input(
            "Calificación máxima (por ejemplo, 100)",
            min_value=1.0,
            max_value=1000.0,
            value=100.0,
            step=1.0,
            key=f"calificacion_maxima_{key}"
        )
    if promedio is None:
        promedio = st.number_input(
            f"Promedio {periodo}",
            min_value=0.0,
            max_value=calificacion_maxima,
            value=50.0,
            step=1.0,
            help="Como máximo debe ser igual a la calificación máxima.",
            key=f"promedio_{key}"
        )
    if materias_inscritas is None:
        materias_inscritas = st.number_input(
            "Número de materias inscritas",
            min_value=0,
            value=6,
            key=f"materias_inscritas_{key}"
        )
    if materias_aprobadas is None:
        materias_aprobadas = st.number_input(
            "Número de materias aprobadas",
            min_value=0,
            max_value=materias_inscritas,
            value=5,
            help="Como máximo debe ser igual al número de materias inscritas.",
            key=f"materias_aprobadas_{key}"
        )

    # Cálculo del rendimiento anual
    rendimiento = calcular_rendimiento(promedio, calificacion_maxima, materias_aprobadas, materias_inscritas)
    st.write(f"El rendimiento {periodo} calculado es: **{rendimiento * 100:.2f}%**")

    if st.button("Confirmar"):
        st.session_state.rendimiento_calculado = rendimiento
        st.rerun()

def pedir_rendimiento_con_modal(key=None, periodo="anual", **kwargs):

    valor_inicial = 70.0
    if "rendimiento_calculado" in st.session_state:
        valor_inicial = st.session_state.rendimiento_calculado * 100

    sliderKey = f"rendimiento_slider_{key}"
    sliderTextKey = f"rendimiento_text_{key}"

    def update_slider():
        st.session_state[sliderKey] = st.session_state[sliderTextKey]

    col1, col2 = st.columns([4, 1])

    with col1:
        rendimiento = st.slider(
            f"Rendimiento {periodo} (0-100%)",
            min_value=0,
            max_value=100,
            step=1,
            value=int(valor_inicial),
            key=sliderKey
        )

    with col2:
        rendimiento_text = st.number_input(
            "",
            key=sliderTextKey,
            value=rendimiento,
            on_change=update_slider
        )

    if st.button(f"No cuento con el rendimiento {periodo}", key=f"abrir_modal_{key}", help="Presiona este botón para calcularlo.",):
        modal(**kwargs)

    return rendimiento / 100.0
