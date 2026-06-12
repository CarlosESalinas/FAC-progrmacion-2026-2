"""Segundo script: genera estadísticas a partir de ``resultados.csv``.

Ejecución:
    python reportes.py

El proyecto pide separar la captura de datos (programa principal) del análisis
(este script). ``ReporteEstadistico`` encapsula esa lógica de análisis en una
clase, lo que mantiene el código ordenado y fácil de extender con nuevas
métricas. Se usa solo la biblioteca estándar (``csv``, ``collections``) para que
no haga falta instalar dependencias.
"""

from __future__ import annotations

import csv
from collections import defaultdict
from pathlib import Path

from excepciones import ArchivoResultadosError


class ReporteEstadistico:
    """Lee el CSV de resultados y calcula estadísticas agregadas."""

    def __init__(self, ruta_csv) -> None:
        self.ruta = Path(ruta_csv)
        self.registros: list[dict] = []

    def cargar(self) -> None:
        """Carga los registros del CSV en memoria.

        Raises:
            ArchivoResultadosError: si el archivo no existe o está vacío.
        """
        if not self.ruta.exists():
            raise ArchivoResultadosError(
                f"No se encontró el archivo de resultados: {self.ruta}"
            )
        with self.ruta.open(encoding="utf-8", newline="") as archivo:
            self.registros = list(csv.DictReader(archivo))
        if not self.registros:
            raise ArchivoResultadosError("El archivo de resultados está vacío.")

    @staticmethod
    def _calificacion(registro: dict) -> float:
        """Extrae la calificación final de un registro como ``float``."""
        return float(registro["Calificacion final"])

    def promedio_general(self) -> float:
        """Promedio de las calificaciones finales de todos los registros."""
        total = sum(self._calificacion(r) for r in self.registros)
        return total / len(self.registros)

    def _promedio_agrupado(self, columna: str) -> dict:
        """Promedio de la calificación final agrupando por una columna dada.

        Se usa un ``defaultdict(list)`` para acumular las calificaciones de cada
        grupo y luego se promedia cada lista. Reutilizar este método privado
        evita duplicar la lógica para "por materia" y "por fecha".
        """
        acumulado: dict[str, list[float]] = defaultdict(list)
        for registro in self.registros:
            acumulado[registro[columna]].append(self._calificacion(registro))
        return {grupo: sum(v) / len(v) for grupo, v in acumulado.items()}

    def promedio_por_materia(self) -> dict:
        """Promedio de calificación final por materia."""
        return self._promedio_agrupado("Materia")

    def promedio_por_fecha(self) -> dict:
        """Promedio de calificación final por fecha."""
        return self._promedio_agrupado("Fecha")

    def mejor_estudiante(self) -> tuple:
        """Devuelve ``(nombre, calificación)`` del mejor resultado registrado."""
        mejor = max(self.registros, key=self._calificacion)
        return mejor["Nombre completo"], self._calificacion(mejor)

    def total_estudiantes(self) -> int:
        """Número total de evaluaciones (filas) registradas."""
        return len(self.registros)

    def imprimir(self) -> None:
        """Muestra el reporte estadístico completo en consola."""
        print("=" * 52)
        print(" REPORTE ESTADÍSTICO")
        print("=" * 52)
        print(f"Total de estudiantes evaluados: {self.total_estudiantes()}")
        print(f"Promedio general: {self.promedio_general():.2f}")

        print("\nPromedio por materia:")
        for materia, promedio in sorted(self.promedio_por_materia().items()):
            print(f"   - {materia}: {promedio:.2f}")

        print("\nPromedio por fecha:")
        for fecha, promedio in sorted(self.promedio_por_fecha().items()):
            print(f"   - {fecha}: {promedio:.2f}")

        nombre, calificacion = self.mejor_estudiante()
        print(f"\nMejor estudiante registrado: {nombre} ({calificacion})")
        print("=" * 52)


def main() -> None:
    """Carga los resultados y muestra el reporte estadístico."""
    raiz = Path(__file__).resolve().parent.parent
    ruta = raiz / "datos" / "resultados.csv"
    reporte = ReporteEstadistico(ruta)
    try:
        reporte.cargar()
        reporte.imprimir()
    except ArchivoResultadosError as error:
        print(f"[ERROR] {error}")


if __name__ == "__main__":
    main()
