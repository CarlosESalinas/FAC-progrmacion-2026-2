"""Excepciones personalizadas del Sistema de Guía de Estudio Interactiva.

Definir una jerarquía propia de excepciones permite distinguir los errores
*esperados* del dominio del problema (entradas inválidas, archivos mal
formados, materias sin preguntas suficientes) de los errores genéricos de
Python. Así el código que orquesta el sistema puede:

  * capturar ``GuiaEstudioError`` para tratar cualquier fallo controlado, o
  * capturar una subclase específica cuando necesita una reacción particular.

Todas heredan de una clase base común, lo que cumple a la vez el requisito de
"excepciones personalizadas" y refuerza el uso de herencia en el proyecto.
"""


class GuiaEstudioError(Exception):
    """Clase base para todos los errores propios del sistema.

    Hereda de ``Exception`` y sirve como raíz de la jerarquía. Capturar esta
    clase atrapa cualquier error controlado del dominio sin enmascarar errores
    de programación ajenos (por ejemplo, un ``KeyError`` inesperado).
    """


class ArchivoPreguntasError(GuiaEstudioError):
    """Se lanza cuando el CSV de preguntas no existe o está mal formado."""


class ArchivoResultadosError(GuiaEstudioError):
    """Se lanza cuando el CSV de resultados no existe o está vacío."""


class MateriaNoDisponibleError(GuiaEstudioError):
    """Se lanza cuando la materia elegida no tiene preguntas registradas."""


class BancoInsuficienteError(GuiaEstudioError):
    """Se lanza cuando hay menos preguntas de las necesarias para un intento."""


class RespuestaInvalidaError(GuiaEstudioError):
    """Se lanza cuando la respuesta capturada por el usuario no es válida."""
