from collections import namedtuple
from typing import NamedTuple


class DescripcionCluster(NamedTuple):
    nombre: str
    perfil: str
    descripcion: str

clusters_3 = [
    DescripcionCluster(
        "Grupo 1",
        "Jóvenes, rendimiento-alto, regularidad",
        "Este grupo está compuesto por estudiantes jóvenes que tienden a tener un buen rendimiento académico y mantienen su matrícula al día. Su perfil sugiere un grupo con incentivos académicos o apoyos institucionales que contribuyen a su éxito."
    ),
    DescripcionCluster(
        "Grupo 2",
        "Adultos, bajo-rendimiento, desplazados",
        "Estudiantes de mayor edad, con un rendimiento académico bajo y con una alta proporción de personas desplazadas. Su perfil refleja posibles dificultades económicas o sociales que afectan su desempeño académico."
    ),
    DescripcionCluster(
        "Grupo 3",
        "Mayores, rendimiento-moderado, matrícula",
        "Incluye estudiantes mayores con un rendimiento moderado que, aunque presentan algunos retos académicos, logran mantenerse al día con los requisitos administrativos como la matrícula."
    )
]

clusters_7 = [
    DescripcionCluster(
        "Grupo 1",
        "Jóvenes, alto-rendimiento, becados",
        "Un grupo destacado por su juventud y buen rendimiento, con una proporción relativamente alta de becas que probablemente apoyan su desempeño."
    ),
    DescripcionCluster(
        "Grupo 2",
        "Adultos, bajo-rendimiento, asistencia-baja",
        "Estudiantes adultos que enfrentan problemas de bajo rendimiento y tienen dificultades para mantener una asistencia regular, lo que podría ser un indicador de desmotivación o complicaciones externas."
    ),
    DescripcionCluster(
        "Grupo 3",
        "Mayores, rendimiento-moderado, matrícula-al-día",
        "Similar al **Grupo 2** del **modelo de 3 grupos**, pero con mayor segmentación, mostrando estudiantes mayores que logran mantenerse al día administrativamente aunque su rendimiento sea intermedio."
    ),
    DescripcionCluster(
        "Grupo 4",
        "Edad-intermedia, regularidad, asistencia",
        "Estudiantes de edad intermedia que mantienen asistencia constante y cumplen regularmente con los requisitos administrativos, aunque su rendimiento no destaque particularmente."
    ),
    DescripcionCluster(
        "Grupo 5",
        "Jóvenes, asistencia-alta, rendimiento-variado",
        "Un grupo compuesto mayoritariamente por estudiantes jóvenes con asistencia alta, pero con un rendimiento académico variable."
    ),
    DescripcionCluster(
        "Grupo 6",
        "Desplazados, asistencia-baja, riesgo-alto",
        "Incluye estudiantes desplazados con bajos niveles de asistencia y alto riesgo de abandono, probablemente debido a limitaciones sociales o económicas significativas."
    ),
    DescripcionCluster(
        "Grupo 7",
        "Comprometidos, matrícula-al-día, bajo-apoyo",
        "Estudiantes comprometidos que mantienen su matrícula actualizada pero carecen de apoyo financiero o académico, lo que afecta negativamente su rendimiento."
    )
]
