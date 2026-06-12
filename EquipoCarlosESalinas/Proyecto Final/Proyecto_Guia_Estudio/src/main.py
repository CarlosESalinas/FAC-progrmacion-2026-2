"""Punto de entrada del Sistema de Guía de Estudio Interactiva.

Ejecución:
    python main.py

Este archivo es deliberadamente delgado: su única tarea es construir el
``SistemaGuia`` con las rutas correctas y arrancarlo, dejando un único lugar
donde se capturan los errores controlados del dominio.
"""

from pathlib import Path

from excepciones import GuiaEstudioError
from sistema import SistemaGuia

# Las rutas se calculan a partir de la ubicación de ESTE archivo, no del
# directorio de trabajo. Así el programa encuentra siempre la carpeta `datos/`
# sin importar desde dónde se ejecute la consola (src/ o la raíz del proyecto).
RAIZ = Path(__file__).resolve().parent.parent
RUTA_PREGUNTAS = RAIZ / "datos" / "preguntas.csv"
RUTA_RESULTADOS = RAIZ / "datos" / "resultados.csv"


def main() -> None:
    """Crea el sistema y lo ejecuta, controlando los errores esperados."""
    sistema = SistemaGuia(RUTA_PREGUNTAS, RUTA_RESULTADOS)
    try:
        sistema.iniciar()
    except GuiaEstudioError as error:
        # Errores previstos del dominio (archivo faltante, materia sin
        # preguntas, banco insuficiente). Se muestran de forma amable.
        print(f"\n[ERROR] {error}")
    except KeyboardInterrupt:
        print("\n\nPrograma interrumpido por el usuario. ¡Hasta luego!")


if __name__ == "__main__":
    main()
