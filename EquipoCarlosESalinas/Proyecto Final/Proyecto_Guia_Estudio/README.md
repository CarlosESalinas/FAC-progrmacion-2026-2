# Sistema de Guía de Estudio Interactiva

Proyecto Final de la materia **Programación** — Facultad de Ciencias, UNAM
(Semestre 2026-2). Aplicación de consola en Python que permite resolver una
guía de estudio interactiva de autoevaluación. La materia configurada es
**Probabilidad**.

**Autor:** Carlos Eduardo Salinas Díaz · Modalidad: individual.

---

## Descripción

El programa solicita el nombre del estudiante y la materia, presenta **10
preguntas aleatorias** (sin repetición dentro de un intento) tomadas de un banco
de al menos 30, las califica de forma automática y permite **hasta 3 intentos**,
conservando la mejor calificación. Los resultados se guardan en un archivo CSV,
y un segundo script genera estadísticas a partir de ese archivo.

Soporta dos tipos de pregunta:

- **Opción múltiple:** 3 opciones, 1 correcta. Acierto = 1 punto.
- **Selección múltiple:** 4 opciones, 2 correctas.
  - Ambas correctas = 1 punto.
  - Una correcta y ninguna incorrecta = 0.5 puntos.
  - Alguna incorrecta, o elegir 3 o 4 opciones = 0 puntos.

Cada intento vale como máximo **10 puntos** (10 preguntas × 1 punto).

---

## Requisitos

- **Python 3.10 o superior.**
- No requiere bibliotecas externas: usa solo la biblioteca estándar
  (`csv`, `random`, `abc`, `datetime`, `pathlib`, `collections`).

Para verificar tu versión de Python:

```bash
python --version
```

---

## Estructura del repositorio

```
Proyecto_Guia_Estudio
|
|-- src/
|   |-- main.py            # Punto de entrada del programa principal
|   |-- sistema.py         # Orquestador (SistemaGuia)
|   |-- preguntas.py       # Clase abstracta Pregunta y sus subclases
|   |-- banco.py           # Carga del banco de preguntas (CSV)
|   |-- intento.py         # Clase Intento
|   |-- estudiante.py      # Clase Estudiante
|   |-- almacenamiento.py  # Persistencia de resultados (GestorResultados)
|   |-- excepciones.py     # Excepciones personalizadas
|   |-- reportes.py        # Segundo script: reportes estadísticos
|
|-- datos/
|   |-- preguntas.csv      # Banco de 30 preguntas
|   |-- resultados.csv     # Resultados acumulados
|
|-- diagramas/
|   |-- diagrama_clases.png
|
|-- documentos/
|   |-- propuesta_economica.pdf
|
|-- README.md
|-- .gitignore
```

---

## Cómo ejecutar

Desde la **raíz del proyecto** (la carpeta `Proyecto_Guia_Estudio`):

### 1. Programa principal (resolver la guía)

```bash
cd src
python main.py
```

El programa te pedirá tu nombre, la materia, y luego responderás las preguntas
escribiendo la letra de la opción (por ejemplo `A`). En las preguntas de
selección múltiple puedes elegir una o dos letras separadas por coma
(por ejemplo `A,C`). Al terminar, mostrará el reporte final y guardará tu
resultado en `datos/resultados.csv`.

> Las rutas a los archivos CSV se calculan a partir de la ubicación de los
> scripts, así que el programa funciona aunque lo ejecutes desde otra carpeta.

### 2. Reporte estadístico

```bash
cd src
python reportes.py
```

Lee `datos/resultados.csv` y muestra: promedio general, promedio por materia,
promedio por fecha, mejor estudiante registrado y total de estudiantes
evaluados.

---

## Cómo agregar más preguntas

Edita `datos/preguntas.csv`. Cada fila tiene estas columnas:

| Columna     | Significado                                                        |
|-------------|--------------------------------------------------------------------|
| `materia`   | Nombre de la materia.                                              |
| `tipo`      | `OM` (opción múltiple) o `SM` (selección múltiple).               |
| `enunciado` | Texto de la pregunta.                                             |
| `opcion_a`..`opcion_d` | Opciones (deja `opcion_d` vacía en las de tipo `OM`).  |
| `correctas` | Letra(s) correcta(s); para `SM` van dos separadas por `;` (`A;B`).|

---

## Requisitos técnicos cubiertos

- Programación Orientada a Objetos (clases y objetos).
- **Herencia:** `Pregunta` → `PreguntaOpcionMultiple`, `PreguntaSeleccionMultiple`;
  y la jerarquía de excepciones.
- **Composición:** `SistemaGuia` contiene un banco y un estudiante; `Intento` y
  `BancoDePreguntas` contienen preguntas.
- **Agregación:** `Estudiante` agrega intentos; `SistemaGuia` usa un gestor.
- **Clases abstractas:** `Pregunta` (con `abc.ABC`).
- **Manejo de excepciones** y **excepciones personalizadas** (`excepciones.py`).
- **Lectura y escritura de archivos CSV.**
- **Docstrings** en todas las clases y métodos.
- Buenas prácticas siguiendo **PEP 8**.
