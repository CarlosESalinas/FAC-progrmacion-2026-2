"""Modelo de preguntas del sistema: clase abstracta + herencia.

Este módulo define la jerarquía de preguntas, que es el núcleo del diseño
orientado a objetos del proyecto:

  * ``Pregunta`` es una clase ABSTRACTA (hereda de ``abc.ABC``). Define el
    contrato común que toda pregunta debe cumplir, pero NO puede instanciarse
    por sí sola.
  * ``PreguntaOpcionMultiple`` y ``PreguntaSeleccionMultiple`` son subclases
    concretas que implementan ese contrato con reglas de calificación distintas.

Usamos una clase abstracta porque "una pregunta" en general no tiene una forma
única de calificarse: depende de su tipo. La clase base obliga a cada subclase a
implementar ``calificar``, garantizando que el resto del sistema pueda tratar a
todas las preguntas de manera uniforme (POLIMORFISMO) sin conocer su tipo
concreto: el intento simplemente llama ``pregunta.realizar(...)``.
"""

from __future__ import annotations

import random
from abc import ABC, abstractmethod

from excepciones import ArchivoPreguntasError, RespuestaInvalidaError

# Letras usadas para etiquetar las opciones al mostrarlas en consola.
_ETIQUETAS = "ABCD"


class Pregunta(ABC):
    """Clase base abstracta para cualquier tipo de pregunta.

    Attributes:
        enunciado (str): Texto de la pregunta.
        opciones (list[str]): Posibles respuestas.
        correctas (set[str]): TEXTO de las opciones correctas.

    Guardamos las respuestas correctas como el *texto* de la opción (no como su
    posición A/B/C/D) por una razón concreta: al mostrar la pregunta barajamos
    las opciones para que el alumno no pueda memorizar posiciones. Si
    guardáramos la posición, esta dejaría de ser válida tras barajar; guardando
    el texto, la comparación sigue siendo correcta sin importar el orden.
    """

    def __init__(self, enunciado: str, opciones, correctas) -> None:
        self.enunciado = enunciado
        self.opciones = list(opciones)
        self.correctas = set(correctas)

    # --- Contrato abstracto: cada subclase DEBE implementarlo --------------
    @property
    @abstractmethod
    def tipo(self) -> str:
        """Identificador corto del tipo de pregunta ('OM' u 'SM')."""

    @property
    @abstractmethod
    def instruccion(self) -> str:
        """Texto que indica al usuario cómo debe responder."""

    @abstractmethod
    def _max_selecciones(self) -> int:
        """Cantidad máxima de letras que el usuario puede escribir."""

    @abstractmethod
    def calificar(self, seleccionadas: set) -> float:
        """Calcula el puntaje (0 a 1) dado el conjunto de opciones elegidas."""

    # --- Comportamiento compartido por todas las preguntas -----------------
    def realizar(self, numero: int) -> float:
        """Muestra la pregunta, captura una respuesta válida y la califica.

        Repite la captura hasta que el usuario escriba una entrada válida
        (capturando ``RespuestaInvalidaError``), de modo que un error de tecleo
        no interrumpa el examen.

        Args:
            numero: Posición de la pregunta dentro del intento (para mostrarla).

        Returns:
            El puntaje obtenido en esta pregunta (entre 0 y 1).
        """
        print(f"\nPregunta {numero}: {self.enunciado}")
        mapeo = self._mostrar_opciones()
        print(f"   ({self.instruccion})")
        while True:
            entrada = input("   Tu respuesta: ")
            try:
                seleccionadas = self._parsear_respuesta(entrada, mapeo)
                return self.calificar(seleccionadas)
            except RespuestaInvalidaError as error:
                print(f"   [!] {error} Intenta de nuevo.")

    def _mostrar_opciones(self) -> dict:
        """Baraja las opciones, las imprime con etiquetas y devuelve el mapeo.

        Returns:
            Un diccionario ``{etiqueta: texto_opcion}`` para traducir después
            las letras que escriba el usuario al texto real de cada opción.
        """
        opciones_barajadas = self.opciones[:]
        random.shuffle(opciones_barajadas)
        mapeo = {}
        for etiqueta, texto in zip(_ETIQUETAS, opciones_barajadas):
            mapeo[etiqueta] = texto
            print(f"   {etiqueta}) {texto}")
        return mapeo

    def _parsear_respuesta(self, entrada: str, mapeo: dict) -> set:
        """Convierte la cadena del usuario en un conjunto de textos de opción.

        Acepta separadores por coma o espacio (p. ej. ``A``, ``A,C`` o ``a c``).

        Args:
            entrada: Lo que escribió el usuario.
            mapeo: Diccionario ``{etiqueta: texto}`` de ``_mostrar_opciones``.

        Returns:
            Conjunto con el TEXTO de las opciones elegidas.

        Raises:
            RespuestaInvalidaError: si no escribió nada, repitió una letra,
                excedió el máximo permitido o usó una letra inexistente.
        """
        letras = [c.strip().upper() for c in entrada.replace(",", " ").split()]
        if not letras:
            raise RespuestaInvalidaError("No escribiste ninguna opción.")
        if len(letras) > self._max_selecciones():
            raise RespuestaInvalidaError(
                f"Solo puedes elegir hasta {self._max_selecciones()} opción(es)."
            )
        if len(set(letras)) != len(letras):
            raise RespuestaInvalidaError("Repetiste una opción.")
        seleccionadas = set()
        for letra in letras:
            if letra not in mapeo:
                raise RespuestaInvalidaError(f"La opción '{letra}' no existe.")
            seleccionadas.add(mapeo[letra])
        return seleccionadas


class PreguntaOpcionMultiple(Pregunta):
    """Pregunta con 3 opciones y exactamente 1 respuesta correcta.

    Rúbrica:
        * 1 punto si la opción elegida es la correcta.
        * 0 puntos en cualquier otro caso.
    """

    @property
    def tipo(self) -> str:
        return "OM"

    @property
    def instruccion(self) -> str:
        return "elige una sola opción, por ejemplo: A"

    def _max_selecciones(self) -> int:
        return 1

    def calificar(self, seleccionadas: set) -> float:
        """Devuelve 1.0 si la única opción elegida es la correcta; si no, 0.0."""
        return 1.0 if seleccionadas == self.correctas else 0.0


class PreguntaSeleccionMultiple(Pregunta):
    """Pregunta con 4 opciones y exactamente 2 respuestas correctas.

    Rúbrica (según las reglas del proyecto):
        * 1 punto   : elige exactamente las 2 correctas.
        * 0.5 puntos: elige solo 1 opción y esa es correcta.
        * 0 puntos  : elige alguna opción incorrecta.
        * 0 puntos  : elige 3 o 4 opciones.
    """

    @property
    def tipo(self) -> str:
        return "SM"

    @property
    def instruccion(self) -> str:
        return "elige una o dos opciones separadas por coma, por ejemplo: A,C"

    def _max_selecciones(self) -> int:
        # Permitimos teclear hasta 4 porque el alumno PUEDE elegir 3 o 4; eso no
        # es un error de captura, sino un caso que la rúbrica penaliza con 0.
        return len(self.opciones)

    def calificar(self, seleccionadas: set) -> float:
        """Aplica la rúbrica de selección múltiple y devuelve el puntaje.

        El orden de las comprobaciones importa: primero descartamos los casos
        que valen 0 (3+ opciones, o alguna incorrecta) y solo entonces
        distinguimos entre 2 aciertos (1 punto) y 1 acierto (0.5 puntos).
        """
        cantidad = len(seleccionadas)
        # Regla explícita: elegir 3 o 4 opciones anula la pregunta.
        if cantidad >= 3:
            return 0.0
        # Si eligió al menos una opción incorrecta, no hay puntos.
        if seleccionadas - self.correctas:
            return 0.0
        # A partir de aquí, TODAS las elegidas son correctas.
        if cantidad == 2:
            return 1.0
        if cantidad == 1:
            return 0.5
        return 0.0  # cantidad == 0 (no debería ocurrir, pero es defensivo)


def crear_pregunta(tipo: str, enunciado: str, opciones, correctas) -> Pregunta:
    """Fábrica que construye la subclase de ``Pregunta`` según el tipo.

    Centralizar la creación (patrón *factory*) evita que el resto del código
    tenga que decidir qué clase instanciar; solo conoce los tipos 'OM' y 'SM'.

    Raises:
        ArchivoPreguntasError: si el tipo no se reconoce.
    """
    tipo = tipo.strip().upper()
    if tipo == "OM":
        return PreguntaOpcionMultiple(enunciado, opciones, correctas)
    if tipo == "SM":
        return PreguntaSeleccionMultiple(enunciado, opciones, correctas)
    raise ArchivoPreguntasError(f"Tipo de pregunta desconocido: '{tipo}'.")
