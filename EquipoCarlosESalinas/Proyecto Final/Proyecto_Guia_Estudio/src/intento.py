"""Representa un intento individual del examen.

``Intento`` es COMPOSICIÓN pura: se construye a partir de objetos ``Pregunta``
y no existe sin ellas. Su responsabilidad es presentar las preguntas en orden y
acumular el puntaje total del intento.
"""

from __future__ import annotations


class Intento:
    """Un intento contiene sus preguntas y sabe cómo aplicarlas y calificarse.

    Attributes:
        numero (int): Número de intento (1, 2 o 3).
        preguntas (list[Pregunta]): Preguntas que se presentarán.
        calificacion (float): Puntaje obtenido (0 a 10) una vez ejecutado.
    """

    def __init__(self, numero: int, preguntas) -> None:
        self.numero = numero
        self.preguntas = list(preguntas)
        self.calificacion = 0.0
        self._completado = False

    def ejecutar(self) -> float:
        """Presenta cada pregunta en consola y acumula el puntaje total.

        Aquí se aprecia el POLIMORFISMO: el intento llama a ``pregunta.realizar``
        sin preguntar ni saber si cada pregunta es de opción múltiple o de
        selección múltiple. Cada objeto responde según su propia clase.

        Returns:
            La calificación obtenida (de 0 a 10), redondeada a 2 decimales.
        """
        print(f"\n===== Intento {self.numero} =====")
        total = 0.0
        for indice, pregunta in enumerate(self.preguntas, start=1):
            total += pregunta.realizar(indice)
        self.calificacion = round(total, 2)
        self._completado = True
        print(f"\n>> Calificación del intento {self.numero}: {self.calificacion}")
        return self.calificacion
