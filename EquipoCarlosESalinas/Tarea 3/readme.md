# Tarea 3 de la clase de Programación de la Facultad de Ciencias 
## Semestre 2026-2

**Intengrante**: 
- Carlos Eduardo Salinas Díaz

### Resumen

La presente entrega corresponde a la tarea número 3 de la clase de Programación. Se incluyen las soluciones a los siguientes ejercicios:
1. Crear un programa que permite la representación de líneas basandose en la clase Punto, el cual está formado por dos puntos en el plano Cartesiano, mediante una clases llamada ´Linea´, la cual deberá incluir los siguiente métodos:
    * Que determine la ecuación de la recta que pase por dos puntos dados y que devuelva en formato cadenda (
Se incluye el bloque de pruebas al final del programa para validar el correcto funcionamiento de cada uno de los métodos. La solución de este ejercicio se encuentra en el script *linea.py*.
´__str__´) la ecuación de la recta. 
    * Que devuelva la pendiente de la curva (´pendiente´).
    * Que devuelva la ordenada al origen (´ordenada_al_origen´).
    * Que determine si un punto, pasado como parámetro, pertenece o no a la recta (´pertenece´).
    * Que determine si dos líneas son paralelas (´son_paralelas´).
    * Que determine si dos líneas son perpendiculares (´son_perpendiculares´).
    * Que regrese el punto de intersección entre dos líneas (´punto_interseccion´).
    * Implementa el método ´__eq__´ para saber si dos rectas son iguales (si se ubican en los mismos puntos).

Se incluye el bloque de pruebas al final del programa para validar el correcto funcionamiento de cada uno de los métodos. La solución de este ejercicio se encuentra en el script *linea.py*.

2. Desarrollar un programa que permita representar números complejos. El nombre de la clase será ´NumeroComplejo´, misma que deberá estar conformada por los siguiente métodos: 

    * Un método constructor ´__init__´ que inicialice las partes real e imaginaria.
    * Métodos que permitan sumar, restar, multiplicar y dividir dos números complejos.
    * Un método ´__eq__´, que permita comparar la igualdad entre dos números complejos.
    * Un método ´__str__´ que permita la representación textual del número.


Se incluye el bloque de pruebas al final del programa para validar el correcto funcionamiento de cada uno de los métodos implementados. La solución de este ejercicio se encuentra en el script *calculadora_de_complejos.py*.

Ambos programas están documentados con docstring y siguen las convenciones PEP 8 y PEP 257.

--- 

## Respuetas a los ejericios

### Ejericio 1

**¿Dónde se usa la abstracción en este ejercicio?**
La abstracción se utiliza al modelar el concepto matemático de una "Línea Recta" a través de una clase en Python. Ocultamos la complejidad de las fórmulas matemáticas (como calcular pendientes, ordenadas y ecuaciones) y exponemos únicamente métodos simples que el usuario puede llamar, como linea.pendiente() o linea.ecuacion().

**¿Dónde se usa la encapsulación en este ejercicio?** 
La encapsulación se observa al agrupar los datos que definen a la línea (los atributos self.p1 y self.p2) junto con los métodos que operan sobre ellos (como calcular si son paralelas o perpendiculares) dentro de la misma clase

### Ejercicio 2
**¿Dónde se usa la abstracción en este ejercicio?**
La abstracción se aplica al crear un tipo de dato NumeroComplejo que el usuario puede manejar conceptualmente como una sola entidad matemática, sin necesidad de preocuparse por cómo se implementan internamente las operaciones de multiplicación o división (las cuales requieren el uso de conjugados y denominadores matemáticos).


**¿Dónde se usa la encapsulación en este ejercicio?** Se usa al empaquetar las variables de estado (la parte real y la parte imaginaria) dentro de la clase NumeroComplejo , restringiendo las operaciones que se pueden hacer sobre ellas estrictamente a los métodos definidos en la clase (sumar, restar, etc.).

--- 

### Configuración básica para la ejecución de los programas

Crear un ambiente virtual de python con el siguiente comando:
- Para windows:
comandos para crear el ambiente virtual:
    - py -m venv .venv
    - .venv\Scripts\activate
- Para linux:
comandos para crear el ambiente virtual:
    - python3 -m venv .venv
    - source .venv/bin/activate
- Ejecutar el programa de linea.py:
    - python linea.py
- Ejecutar el programa de calculadora_de_complejos.py:
    - python calculadora_de_complejos.py

