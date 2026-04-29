import math


class Punto:
    """
    Clase que representa un punto en el plano cartesiano.

    Un punto se define como una pareja ordenada de números (x, y).
    Puede crearse, desplazarse, sumarse con otro punto, restarse,
    calcular la distancia respecto a otro punto, determinar si está
    alineado con otros dos puntos, verificar si es igual a otro punto
    e imprimirse como una pareja ordenada.
    """

    def __init__(self, x: float = 1, y: float = 1) -> None:
        """
        Inicializa un punto con coordenadas x e y.

        Parámetros:
            x (float): Coordenada en el eje X.
            y (float): Coordenada en el eje Y.
        """
        self.x = x
        self.y = y

    def get_x(self) -> float:
        """
        Devuelve la coordenada x del punto.

        Retorna:
            float: Valor de x.
        """
        return self.x

    def get_y(self) -> float:
        """
        Devuelve la coordenada y del punto.

        Retorna:
            float: Valor de y.
        """
        return self.y

    def desplazamiento(self, dx: float, dy: float) -> "Punto":
        """
        Desplaza el punto en los ejes X e Y.

        Parámetros:
            dx (float): Desplazamiento en el eje X.
            dy (float): Desplazamiento en el eje Y.

        Retorna:
            Punto: El mismo punto ya desplazado.
        """
        self.x += dx
        self.y += dy
        return self

    def suma(self, otro_punto: "Punto") -> "Punto":
        """
        Suma este punto con otro punto.

        Parámetros:
            otro_punto (Punto): Punto que se desea sumar.

        Retorna:
            Punto: Nuevo punto con la suma de las coordenadas.
        """
        return Punto(self.x + otro_punto.x, self.y + otro_punto.y)

    def resta(self, otro_punto: "Punto") -> "Punto":
        """
        Resta otro punto a este punto.

        Parámetros:
            otro_punto (Punto): Punto que se desea restar.

        Retorna:
            Punto: Nuevo punto con la resta de las coordenadas.
        """
        return Punto(self.x - otro_punto.x, self.y - otro_punto.y)

    def distancia(self, otro_punto: "Punto") -> float:
        """
        Calcula la distancia euclidiana entre este punto y otro punto.

        Parámetros:
            otro_punto (Punto): Punto con el que se calculará la distancia.

        Retorna:
            float: Distancia entre ambos puntos.
        """
        return math.sqrt((self.x - otro_punto.x) ** 2 + (self.y - otro_punto.y) ** 2)

    def esta_alineado(self, punto_1: "Punto", punto_2: "Punto") -> bool:
        """
        Determina si este punto está alineado con otros dos puntos.

        Parámetros:
            punto_1 (Punto): Primer punto.
            punto_2 (Punto): Segundo punto.

        Retorna:
            bool: True si los tres puntos están alineados, False en caso contrario.
        """
        return (punto_1.x - self.x) * (punto_2.y - self.y) == \
               (punto_2.x - self.x) * (punto_1.y - self.y)

    def es_igual(self, otro_punto: object) -> bool:
        """
        Determina si este punto es igual a otro punto.

        Parámetros:
            otro_punto (object): Objeto que se desea comparar.

        Retorna:
            bool: True si ambos puntos tienen las mismas coordenadas,
                  False en caso contrario.
        """
        if not isinstance(otro_punto, Punto):
            return False

        return self.x == otro_punto.x and self.y == otro_punto.y

    def __eq__(self, otro_punto: object) -> bool:
        """
        Compara este punto con otro usando el operador ==.

        Parámetros:
            otro_punto (object): Objeto que se desea comparar.

        Retorna:
            bool: True si ambos puntos son iguales, False en caso contrario.
        """
        return self.es_igual(otro_punto)

    def __str__(self) -> str:
        """
        Devuelve la representación en cadena del punto.

        Retorna:
            str: Punto en formato (x, y).
        """
        return f"({self.x}, {self.y})"


if __name__ == "__main__":
    punto1 = Punto(2, 2)
    punto2 = Punto(1, 1)
    punto3 = punto1.suma(punto2)
    
    punto4 = Punto()
    

    print("x", punto3.get_x())
    print("y", punto3.get_y())

    print(punto3)

    while True:
        print("\n[0] SALIR")
        print("[1] Suma")
        print("[2] Resta")
        print("[3] Desplazamiento")
        print("[4] Distancia")
        print("Elige una opción: ")
        opcion = int(input())

        if opcion == 0:
            print("Se terminó el programa")
            break

        elif opcion == 1:
            print("SUMA...")
            x1 = int(input("Escribe la coordenada x del primer punto: "))
            y1 = int(input("Escribe la coordenada y del primer punto: "))

            x2 = int(input("Escribe la coordenada x del segundo punto: "))
            y2 = int(input("Escribe la coordenada y del segundo punto: "))

            punto1 = Punto(x1, y1)
            punto2 = Punto(x2, y2)

            print(punto1.suma(punto2))

        elif opcion == 2:
            print("RESTA...")
            x1 = int(input("Escribe la coordenada x del primer punto: "))
            y1 = int(input("Escribe la coordenada y del primer punto: "))

            x2 = int(input("Escribe la coordenada x del segundo punto: "))
            y2 = int(input("Escribe la coordenada y del segundo punto: "))

            punto1 = Punto(x1, y1)
            punto2 = Punto(x2, y2)

            print(punto1.resta(punto2))

        elif opcion == 3:
            print("DESPLAZAMIENTO...")
            x1 = int(input("Escribe la coordenada x del punto: "))
            y1 = int(input("Escribe la coordenada y del punto: "))

            punto1 = Punto(x1, y1)
            print("Punto original:", punto1)

            incremento_x = int(input("Escribe el incremento en x: "))
            incremento_y = int(input("Escribe el incremento en y: "))

            valor = punto1.desplazamiento(incremento_x, incremento_y)
            print("Resultado del desplazamiento:", valor)
            print("Punto desplazado:", punto1)

        elif opcion == 4:
            print("DISTANCIA...")
            x1 = int(input("Escribe la coordenada x del primer punto: "))
            y1 = int(input("Escribe la coordenada y del primer punto: "))
            x2 = int(input("Escribe la coordenada x del segundo punto: "))
            y2 = int(input("Escribe la coordenada y del segundo punto: "))

            punto1 = Punto(x1, y1)
            punto2 = Punto(x2, y2)

            punto3 = punto1.distancia(punto2)

            print("Distancia:", punto1.distancia(punto2))
            print(punto3)

        else:
            print("Opción no válida")