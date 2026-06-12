"""Entidad que representa al estudiante que resuelve la guía.

``Estudiante`` es un ejemplo de AGREGACIÓN: acumula una lista de objetos
``Intento``, pero esos intentos podrían existir y razonarse de forma
independiente. La calificación final se *deriva* de los intentos (es la mejor).
"""

from __future__ import annotations


class Estudiante:
    """Representa a un estudiante con su nombre y los intentos que realiza.

    Attributes:
        nombre (str): Nombre completo del estudiante.
        intentos (list[Intento]): Intentos realizados, en orden.
    """

    def __init__(self, nombre: str) -> None:
        if not nombre or not nombre.strip():
            raise ValueError("El nombre del estudiante no puede estar vacío.")
        self.nombre = nombre.strip()
        self.intentos: list = []

    def agregar_intento(self, intento) -> None:
        """Registra un intento realizado por el estudiante."""
        self.intentos.append(intento)

    @property
    def calificacion_final(self) -> float:
        """La mejor calificación obtenida entre todos los intentos.

        Se calcula como propiedad (no se almacena) para que siempre refleje el
        estado actual de la lista de intentos sin riesgo de quedar desfasada.
        """
        if not self.intentos:
            return 0.0
        return max(intento.calificacion for intento in self.intentos)

    @property
    def numero_de_intentos(self) -> int:
        """Cantidad de intentos realizados."""
        return len(self.intentos)
