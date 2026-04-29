from punto import Punto

class Linea:
    """
    Clase que representa una línea recta en el plano cartesiano.
    
    Una línea se define por dos objetos de la clase Punto.
    """

    def __init__(self, p1: Punto, p2: Punto) -> None:
        """
        Inicializa una línea con dos puntos.

        Parámetros:
            p1 (Punto): El primer punto de la línea.
            p2 (Punto): El segundo punto de la línea.
        """
        self.p1 = p1
        self.p2 = p2

    def pendiente(self) -> float:
        """
        Calcula y devuelve la pendiente de la recta.

        Retorna:
            float: La pendiente de la recta.
            None: Si la recta es vertical (pendiente indefinida).
        """
        dx = self.p2.get_x() - self.p1.get_x()
        dy = self.p2.get_y() - self.p1.get_y()
        if dx == 0:
            return None  # Pendiente indefinida (línea vertical)
        return dy / dx

    def ordenada_al_origen(self) -> float:
        """
        Calcula la ordenada al origen (b) de la recta.

        Retorna:
            float: La ordenada al origen.
            None: Si la recta es vertical.
        """
        m = self.pendiente()
        if m is None:
            return None
        # y = mx + b => b = y - mx
        return self.p1.get_y() - (m * self.p1.get_x())

    def ecuacion(self) -> str:
        """
        Determina la ecuación de la recta que pasa por los dos puntos.

        Retorna:
            str: Ecuación de la recta en formato cadena.
        """
        m = self.pendiente()
        if m is None:
            return f"x = {self.p1.get_x()}"
        b = self.ordenada_al_origen()
        signo = "+" if b >= 0 else "-"
        return f"y = {m}x {signo} {abs(b)}"

    def pertenece(self, punto: Punto) -> bool:
        """
        Determina si un punto dado pertenece a la recta.

        Parámetros:
            punto (Punto): El punto a evaluar.

        Retorna:
            bool: True si el punto pertenece a la recta, False en caso contrario.
        """
        m = self.pendiente()
        if m is None:
            return punto.get_x() == self.p1.get_x()
        
        # Comprobamos si satisface y = mx + b con una pequeña tolerancia para flotantes
        y_calculada = m * punto.get_x() + self.ordenada_al_origen()
        return abs(punto.get_y() - y_calculada) < 1e-9

    def son_paralelas(self, otra_linea: "Linea") -> bool:
        """
        Determina si esta línea es paralela a otra.

        Parámetros:
            otra_linea (Linea): La línea con la que se va a comparar.

        Retorna:
            bool: True si son paralelas, False en caso contrario.
        """
        return self.pendiente() == otra_linea.pendiente()

    def son_perpendiculares(self, otra_linea: "Linea") -> bool:
        """
        Determina si esta línea es perpendicular a otra.

        Parámetros:
            otra_linea (Linea): La línea con la que se va a comparar.

        Retorna:
            bool: True si son perpendiculares, False en caso contrario.
        """
        m1 = self.pendiente()
        m2 = otra_linea.pendiente()
        
        # Manejo de líneas verticales y horizontales
        if (m1 is None and m2 == 0) or (m2 is None and m1 == 0):
            return True
        if m1 is None or m2 is None:
            return False
            
        return abs((m1 * m2) - (-1)) < 1e-9

    def punto_interseccion(self, otra_linea: "Linea") -> Punto:
        """
        Regresa el punto de intersección entre dos líneas.

        Parámetros:
            otra_linea (Linea): La línea con la que se busca la intersección.

        Retorna:
            Punto: Objeto Punto donde se intersectan, o None si son paralelas.
        """
        if self.son_paralelas(otra_linea):
            return None

        m1 = self.pendiente()
        b1 = self.ordenada_al_origen()
        m2 = otra_linea.pendiente()
        b2 = otra_linea.ordenada_al_origen()

        # Si la primera línea es vertical
        if m1 is None:
            x = self.p1.get_x()
            y = m2 * x + b2
            return Punto(x, y)
        
        # Si la segunda línea es vertical
        if m2 is None:
            x = otra_linea.p1.get_x()
            y = m1 * x + b1
            return Punto(x, y)

        # m1*x + b1 = m2*x + b2  =>  x(m1 - m2) = b2 - b1
        x = (b2 - b1) / (m1 - m2)
        y = m1 * x + b1
        return Punto(x, y)

    def __eq__(self, otra_linea: object) -> bool:
        """
        Saber si dos rectas son iguales (se ubican en los mismos puntos).

        Parámetros:
            otra_linea (object): Objeto a comparar.

        Retorna:
            bool: True si se definen por los mismos puntos, False de lo contrario.
        """
        if not isinstance(otra_linea, Linea):
            return False
        
        # Pueden estar definidos en el mismo orden o invertidos
        mismos_orden = self.p1 == otra_linea.p1 and self.p2 == otra_linea.p2
        orden_inverso = self.p1 == otra_linea.p2 and self.p2 == otra_linea.p1
        return mismos_orden or orden_inverso

    def __str__(self) -> str:
        """
        Devuelve la representación en cadena de la línea.
        """
        return f"Línea definida por {self.p1} y {self.p2}"

# --- Bloque de Pruebas ---
if __name__ == "__main__":
    p1 = Punto(1, 2)
    p2 = Punto(3, 6)
    linea1 = Linea(p1, p2)
    
    print("--- Pruebas de la clase Linea ---")
    print(f"Str: {linea1}")
    print(f"Ecuación: {linea1.ecuacion()}")
    print(f"Pendiente: {linea1.pendiente()}")
    print(f"Ordenada al origen: {linea1.ordenada_al_origen()}")
    
    p_test = Punto(2, 4)
    print(f"¿El punto {p_test} pertenece a la línea?: {linea1.pertenece(p_test)}")

    p3 = Punto(1, 3)
    p4 = Punto(3, 7)
    linea_paralela = Linea(p3, p4)
    print(f"¿Son paralelas linea1 y linea_paralela?: {linea1.son_paralelas(linea_paralela)}")

    p5 = Punto(0, 0)
    p6 = Punto(-4, 2)
    linea_perp = Linea(p5, p6)
    print(f"¿Son perpendiculares linea1 y linea_perp?: {linea1.son_perpendiculares(linea_perp)}")

    interseccion = linea1.punto_interseccion(linea_perp)
    if interseccion:
        print(f"Punto de intersección: {interseccion}")

    linea_igual = Linea(p2, p1)
    print(f"¿linea1 es igual a linea_igual? (mismos puntos): {linea1 == linea_igual}")