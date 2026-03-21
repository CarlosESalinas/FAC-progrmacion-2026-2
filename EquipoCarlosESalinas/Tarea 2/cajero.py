# ------------------------------------------------------------
# CAJERO AUTOMATICO BASICO
# Permite: consultar saldo, depositar, retirar y salir.
# No acepta cantidades negativas ni retiros mayores al saldo.
# ------------------------------------------------------------

def mostrar_menu():
    """Imprime las opciones disponibles del cajero."""
    print("1. Consultar saldo")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Salir")

def consultar_saldo(saldo):
    """Muestra el saldo actual al usuario."""
    print(f"\n  Tu saldo actual es: ${saldo:.2f}")

def depositar(saldo):
    """
    Pide una cantidad al usuario y la suma al saldo.
    No acepta cantidades menores o iguales a cero.
    Retorna el nuevo saldo.
    """
    cantidad = float(input("\n  ¿Cuanto deseas depositar? $"))

    if cantidad <= 0:
        # No aceptamos numeros negativos ni cero
        print("  Error: la cantidad debe ser mayor a cero.")
    else:
        saldo = saldo + cantidad
        print(f"  Deposito exitoso. Nuevo saldo: ${saldo:.2f}")

    return saldo  # Regresamos el saldo (modificado o igual)

def retirar(saldo):
    """
    Pide una cantidad al usuario y la resta del saldo.
    No acepta: cantidades negativas ni retiros mayores al saldo.
    Retorna el nuevo saldo.
    """
    cantidad = float(input("\n  ¿Cuanto deseas retirar? $"))

    if cantidad <= 0:
        # No aceptamos negativos ni cero
        print("  Error: la cantidad debe ser mayor a cero.")
    elif cantidad > saldo:
        # No se puede retirar mas de lo que hay
        print(f"  Error: saldo insuficiente. Tu saldo es ${saldo:.2f}")
    else:
        saldo = saldo - cantidad
        print(f"  Retiro exitoso. Nuevo saldo: ${saldo:.2f}")

    return saldo  # Regresamos el saldo (modificado o igual)

def main():
    """
    Funcion principal del cajero.
    El while mantiene el menu activo hasta que el usuario elija salir.
    """
    # Saldo inicial de la cuenta
    saldo = 1000.00
    print("\nBienvenido al cajero automatico.")

    # El while mantiene el programa corriendo
    while True:
        mostrar_menu()
        opcion = input("  Elige una opcion (1-4): ").strip()

        if opcion == "1":
            # Opcion 1: solo mostrar saldo
            consultar_saldo(saldo)

        elif opcion == "2":
            # Opcion 2: depositar y actualizar saldo
            saldo = depositar(saldo)

        elif opcion == "3":
            # Opcion 3: retirar y actualizar saldo
            saldo = retirar(saldo)

        elif opcion == "4":
            # Opcion 4: salir del programa
            print("\n  Gracias por usar el cajero. ¡Hasta luego!")
            break  # Termina el while

        else:
            # Cualquier otra entrada no es valida
            print("  Opcion no valida. Por favor elige entre 1 y 4.")

# Punto de entrada
if __name__ == "__main__":
    main()