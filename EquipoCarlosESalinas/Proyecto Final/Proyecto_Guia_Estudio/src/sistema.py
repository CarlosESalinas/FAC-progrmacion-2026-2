"""Orquestador principal del Sistema de Guía de Estudio Interactiva.

``SistemaGuia`` es el corazón de la COMPOSICIÓN del sistema: contiene (compone)
un ``BancoDePreguntas`` y un ``Estudiante``, y USA (agrega) un
``GestorResultados`` para la persistencia. Concentra el flujo de control: pedir
datos, ejecutar hasta tres intentos, mostrar el reporte y guardar.
"""

from __future__ import annotations

from datetime import date

from almacenamiento import GestorResultados
from banco import BancoDePreguntas
from estudiante import Estudiante
from intento import Intento

#: Materias para las que existen preguntas. Centralizar la lista facilita
#: ampliar el sistema más adelante sin tocar la lógica del menú.
MATERIAS_DISPONIBLES = ["Probabilidad"]

#: Número máximo de intentos permitidos por el proyecto.
MAX_INTENTOS = 3


class SistemaGuia:
    """Coordina todo el flujo: datos del alumno, intentos, reporte y guardado."""

    def __init__(self, ruta_preguntas, ruta_resultados) -> None:
        self.ruta_preguntas = ruta_preguntas
        self.gestor = GestorResultados(ruta_resultados)
        self.estudiante: Estudiante | None = None
        self.banco: BancoDePreguntas | None = None

    # --- Utilidades de entrada -------------------------------------------
    @staticmethod
    def _pedir_texto(mensaje: str) -> str:
        """Pide texto no vacío al usuario, repitiendo hasta obtenerlo."""
        while True:
            valor = input(mensaje).strip()
            if valor:
                return valor
            print("   [!] El campo no puede estar vacío.")

    def _elegir_materia(self) -> str:
        """Muestra el menú de materias y devuelve la elegida."""
        print("\nMaterias disponibles:")
        for indice, materia in enumerate(MATERIAS_DISPONIBLES, start=1):
            print(f"   {indice}) {materia}")
        while True:
            opcion = input("Elige el número de la materia: ").strip()
            if opcion.isdigit() and 1 <= int(opcion) <= len(MATERIAS_DISPONIBLES):
                return MATERIAS_DISPONIBLES[int(opcion) - 1]
            print("   [!] Opción no válida.")

    @staticmethod
    def _desea_reintentar() -> bool:
        """Pregunta al usuario si desea realizar otro intento."""
        while True:
            respuesta = input("\n¿Deseas intentar de nuevo? (s/n): ").strip().lower()
            if respuesta in ("s", "si", "sí"):
                return True
            if respuesta in ("n", "no"):
                return False
            print("   [!] Responde 's' o 'n'.")

    # --- Flujo principal --------------------------------------------------
    def iniciar(self) -> None:
        """Ejecuta el ciclo completo del programa."""
        print("=" * 52)
        print(" SISTEMA DE GUÍA DE ESTUDIO INTERACTIVA")
        print("=" * 52)
        nombre = self._pedir_texto("\nNombre completo del estudiante: ")
        self.estudiante = Estudiante(nombre)
        materia = self._elegir_materia()
        # Construcción del banco: puede lanzar errores del dominio, que se
        # capturan en main.py (punto único de manejo de errores de arranque).
        self.banco = BancoDePreguntas.desde_csv(self.ruta_preguntas, materia)

        self._ciclo_de_intentos()
        self._mostrar_reporte(materia)
        self._guardar(materia)

    def _ciclo_de_intentos(self) -> None:
        """Realiza hasta ``MAX_INTENTOS`` intentos preguntando si desea seguir.

        Cada iteración genera una NUEVA muestra aleatoria de preguntas, tal como
        exige el proyecto: cada intento es distinto.
        """
        for numero in range(1, MAX_INTENTOS + 1):
            preguntas = self.banco.muestra_aleatoria()
            intento = Intento(numero, preguntas)
            intento.ejecutar()
            self.estudiante.agregar_intento(intento)
            # Tras el último intento ya no tiene sentido preguntar.
            if numero < MAX_INTENTOS and not self._desea_reintentar():
                break

    def _mostrar_reporte(self, materia: str) -> None:
        """Imprime el reporte final en consola."""
        est = self.estudiante
        print("\n" + "=" * 52)
        print(" REPORTE FINAL")
        print("=" * 52)
        print(f"Estudiante:          {est.nombre}")
        print(f"Materia:             {materia}")
        print(f"Intentos realizados: {est.numero_de_intentos}")
        for intento in est.intentos:
            print(f"   - Intento {intento.numero}: {intento.calificacion}")
        print(f"Calificación final (mejor intento): {est.calificacion_final}")
        print("=" * 52)

    def _guardar(self, materia: str) -> None:
        """Construye el registro y lo persiste en el CSV de resultados.

        Los intentos no realizados se guardan como cadena vacía, conservando las
        tres columnas Intento1..Intento3 que exige el formato.
        """
        calificaciones = ["", "", ""]
        for intento in self.estudiante.intentos:
            calificaciones[intento.numero - 1] = intento.calificacion
        registro = {
            "Nombre completo": self.estudiante.nombre,
            "Materia": materia,
            "Intento1": calificaciones[0],
            "Intento2": calificaciones[1],
            "Intento3": calificaciones[2],
            "Calificacion final": self.estudiante.calificacion_final,
            "Fecha": date.today().isoformat(),
        }
        self.gestor.guardar(registro)
        print("\n[OK] Resultados guardados correctamente.")
