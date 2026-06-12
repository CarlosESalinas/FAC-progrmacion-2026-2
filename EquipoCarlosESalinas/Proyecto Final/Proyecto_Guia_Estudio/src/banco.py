"""Carga y administración del banco de preguntas.

``BancoDePreguntas`` es un ejemplo de COMPOSICIÓN: se construye a partir de
muchos objetos ``Pregunta`` y no tiene sentido sin ellos (si el banco
desaparece, sus preguntas desaparecen con él). El banco es responsable de:

  * leer el archivo ``preguntas.csv`` y filtrar por materia,
  * convertir cada fila en el objeto ``Pregunta`` adecuado, y
  * entregar una muestra aleatoria sin repeticiones para cada intento.
"""

from __future__ import annotations

import csv
import random
from pathlib import Path

from excepciones import (
    ArchivoPreguntasError,
    BancoInsuficienteError,
    MateriaNoDisponibleError,
)
from preguntas import Pregunta, crear_pregunta

_ETIQUETAS = "ABCD"
_COLUMNAS_OPCIONES = ("opcion_a", "opcion_b", "opcion_c", "opcion_d")


class BancoDePreguntas:
    """Contiene todas las preguntas de una materia y entrega muestras al azar."""

    #: Cantidad de preguntas que se presentan en cada intento.
    PREGUNTAS_POR_INTENTO = 10

    def __init__(self, materia: str, preguntas) -> None:
        self.materia = materia
        self._preguntas: list[Pregunta] = list(preguntas)

    @classmethod
    def desde_csv(cls, ruta_csv, materia: str) -> "BancoDePreguntas":
        """Construye un banco leyendo las preguntas de ``materia`` desde el CSV.

        Se usa un *classmethod* como constructor alternativo: deja claro que la
        forma habitual de crear un banco es "desde un CSV", sin obligar al
        ``__init__`` a saber nada de archivos.

        Args:
            ruta_csv: Ruta al archivo ``preguntas.csv``.
            materia: Nombre de la materia a filtrar.

        Raises:
            ArchivoPreguntasError: si el archivo no existe o está mal formado.
            MateriaNoDisponibleError: si no hay preguntas de esa materia.
        """
        ruta = Path(ruta_csv)
        if not ruta.exists():
            raise ArchivoPreguntasError(
                f"No se encontró el archivo de preguntas: {ruta}"
            )
        preguntas: list[Pregunta] = []
        try:
            with ruta.open(encoding="utf-8", newline="") as archivo:
                lector = csv.DictReader(archivo)
                for fila in lector:
                    if fila["materia"].strip().lower() != materia.strip().lower():
                        continue
                    preguntas.append(cls._fila_a_pregunta(fila))
        except (KeyError, ValueError, IndexError, OSError) as error:
            # Cualquier problema de formato (columna faltante, letra correcta
            # fuera de rango, etc.) se traduce a un error claro del dominio.
            raise ArchivoPreguntasError(
                f"El archivo de preguntas está mal formado: {error}"
            ) from error
        if not preguntas:
            raise MateriaNoDisponibleError(
                f"No hay preguntas registradas para la materia '{materia}'."
            )
        return cls(materia, preguntas)

    @staticmethod
    def _fila_a_pregunta(fila: dict) -> Pregunta:
        """Convierte una fila del CSV en el objeto ``Pregunta`` correspondiente.

        Las columnas de opción vacías se ignoran (las preguntas de opción
        múltiple solo usan tres). La columna ``correctas`` viene como letras
        separadas por ``;`` (p. ej. ``A;C``) que se traducen al texto real de
        cada opción correcta.
        """
        opciones = [
            fila[col].strip()
            for col in _COLUMNAS_OPCIONES
            if fila.get(col, "").strip()
        ]
        letras_correctas = [
            c.strip().upper() for c in fila["correctas"].split(";") if c.strip()
        ]
        textos_correctos = [
            opciones[_ETIQUETAS.index(letra)] for letra in letras_correctas
        ]
        return crear_pregunta(
            fila["tipo"], fila["enunciado"].strip(), opciones, textos_correctos
        )

    def total(self) -> int:
        """Número de preguntas disponibles en el banco."""
        return len(self._preguntas)

    def muestra_aleatoria(self) -> list:
        """Devuelve 10 preguntas distintas elegidas al azar.

        Usa ``random.sample``, que toma elementos *sin reemplazo*, garantizando
        que ninguna pregunta se repita dentro del mismo intento.

        Raises:
            BancoInsuficienteError: si hay menos de ``PREGUNTAS_POR_INTENTO``.
        """
        if self.total() < self.PREGUNTAS_POR_INTENTO:
            raise BancoInsuficienteError(
                f"Se requieren al menos {self.PREGUNTAS_POR_INTENTO} preguntas, "
                f"pero la materia '{self.materia}' solo tiene {self.total()}."
            )
        return random.sample(self._preguntas, self.PREGUNTAS_POR_INTENTO)
