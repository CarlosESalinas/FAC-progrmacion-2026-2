class NumeroComplejo:
    """
    Clase que representa un número complejo.
    
    Formado por una parte real y una parte imaginaria.
    """

    def __init__(self, real: float, imaginaria: float) -> None:
        """
        Inicializa la parte real y la parte imaginaria.

        Parámetros:
            real (float): Parte real del número complejo.
            imaginaria (float): Parte imaginaria del número complejo.
        """
        self.real = real
        self.imaginaria = imaginaria

    def sumar(self, otro: "NumeroComplejo") -> "NumeroComplejo":
        """Suma dos números complejos."""
        return NumeroComplejo(self.real + otro.real, self.imaginaria + otro.imaginaria)

    def restar(self, otro: "NumeroComplejo") -> "NumeroComplejo":
        """Resta dos números complejos."""
        return NumeroComplejo(self.real - otro.real, self.imaginaria - otro.imaginaria)

    def multiplicar(self, otro: "NumeroComplejo") -> "NumeroComplejo":
        """Multiplica dos números complejos."""
        real = (self.real * otro.real) - (self.imaginaria * otro.imaginaria)
        imaginaria = (self.real * otro.imaginaria) + (self.imaginaria * otro.real)
        return NumeroComplejo(real, imaginaria)

    def dividir(self, otro: "NumeroComplejo") -> "NumeroComplejo":
        """Divide dos números complejos."""
        denominador = (otro.real ** 2) + (otro.imaginaria ** 2)
        if denominador == 0:
            raise ValueError("No se puede dividir entre cero.")
        
        real = ((self.real * otro.real) + (self.imaginaria * otro.imaginaria)) / denominador
        imaginaria = ((self.imaginaria * otro.real) - (self.real * otro.imaginaria)) / denominador
        return NumeroComplejo(real, imaginaria)

    def __eq__(self, otro: object) -> bool:
        """Saber si dos números complejos son iguales."""
        if not isinstance(otro, NumeroComplejo):
            return False
        return self.real == otro.real and self.imaginaria == otro.imaginaria

    def __str__(self) -> str:
        """Representación en cadena del número complejo."""
        signo = "+" if self.imaginaria >= 0 else "-"
        return f"{self.real} {signo} {abs(self.imaginaria)}i"

# --- Menú Interactivo ---
def menu():
    while True:
        print("\n--- Calculadora de Números Complejos ---")
        print("[1] Sumar dos números complejos")
        print("[2] Restar dos números complejos")
        print("[3] Multiplicar dos números complejos")
        print("[4] Dividir dos números complejos")
        print("[5] Comparar si dos números complejos son iguales")
        print("[0] Salir del programa")
        
        opcion = input("Elige una opción: ")

        if opcion == '0':
            print("Saliendo del programa...")
            break
            
        if opcion in ['1', '2', '3', '4', '5']:
            try:
                print("-> Primer número complejo:")
                r1 = float(input("Parte real: "))
                i1 = float(input("Parte imaginaria: "))
                num1 = NumeroComplejo(r1, i1)

                print("-> Segundo número complejo:")
                r2 = float(input("Parte real: "))
                i2 = float(input("Parte imaginaria: "))
                num2 = NumeroComplejo(r2, i2)

                if opcion == '1':
                    print(f"Resultado Suma: {num1.sumar(num2)}")
                elif opcion == '2':
                    print(f"Resultado Resta: {num1.restar(num2)}")
                elif opcion == '3':
                    print(f"Resultado Multiplicación: {num1.multiplicar(num2)}")
                elif opcion == '4':
                    print(f"Resultado División: {num1.dividir(num2)}")
                elif opcion == '5':
                    if num1 == num2:
                        print("Los números complejos SON iguales.")
                    else:
                        print("Los números complejos NO son iguales.")
            except ValueError as e:
                print(f"Error en la entrada o cálculo: {e}. Por favor, ingresa solo números.")
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()