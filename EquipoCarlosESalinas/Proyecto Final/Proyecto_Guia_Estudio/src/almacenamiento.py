"""Persistencia de resultados en archivo CSV.

``GestorResultados`` aísla todo lo relacionado con leer y escribir el archivo de
resultados. Separar la persistencia en su propia clase sigue el principio de
RESPONSABILIDAD ÚNICA: el resto del sistema no necesita saber cómo ni dónde se
guardan los datos, solo pide "guarda este resultado". El ``SistemaGuia`` USA un
``GestorResultados`` (relación de agregación: el gestor es reutilizable y podría
sustituirse, por ejemplo, por uno que escriba en base de datos).
"""

from __future__ import annotations

import csv
from pathlib import Path


class GestorResultados:
    """Lee y escribe el archivo CSV de resultados."""

    #: Orden exacto de columnas exigido por el proyecto.
    ENCABEZADOS = [
        "Nombre completo",
        "Materia",
        "Intento1",
        "Intento2",
        "Intento3",
        "Calificacion final",
        "Fecha",
    ]

    def __init__(self, ruta_csv) -> None:
        self.ruta = Path(ruta_csv)

    def guardar(self, registro: dict) -> None:
        """Agrega un registro al CSV, escribiendo los encabezados si es nuevo.

        Se abre en modo ``"a"`` (append) para no sobrescribir resultados
        previos. Si el archivo aún no existe, se crea la carpeta contenedora y
        se escribe primero la fila de encabezados.

        Args:
            registro: Diccionario cuyas claves coinciden con ``ENCABEZADOS``.
        """
        es_nuevo = not self.ruta.exists()
        self.ruta.parent.mkdir(parents=True, exist_ok=True)
        with self.ruta.open("a", encoding="utf-8", newline="") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=self.ENCABEZADOS)
            if es_nuevo:
                escritor.writeheader()
            escritor.writerow(registro)
