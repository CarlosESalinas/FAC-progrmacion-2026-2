import random

# ------------------------------------------------------------
# JUEGO DE DADOS
# El usuario y la computadora lanzan dos dados cada uno.
# Gana quien cuyo PRODUCTO de sus dados sea multiplo de 2 o 5,
# pero NO de ambos a la vez (XOR).
# En empate se lanza un dado extra y gana el mayor.
# ------------------------------------------------------------

def lanzar_dado():
    """Devuelve un numero aleatorio entre 1 y 6 (un dado)."""
    return random.randint(1, 6)

def turno_usuario():
    """
    Pide al usuario que presione Enter para lanzar cada dado.
    Retorna los dos resultados y su producto.
    """
    print("\n-- Tu turno --")
    input("Presiona Enter para lanzar tu primer dado...")
    dado1 = lanzar_dado()
    print(f"  Dado 1: {dado1}")

    input("Presiona Enter para lanzar tu segundo dado...")
    dado2 = lanzar_dado()
    print(f"  Dado 2: {dado2}")

    producto = dado1 * dado2
    print(f"  Tu producto: {dado1} x {dado2} = {producto}")
    return dado1, dado2, producto

def turno_computadora():
    """
    La computadora lanza dos dados automaticamente.
    Retorna los dos resultados y su producto.
    """
    print("\n-- Turno de la computadora --")
    dado1 = lanzar_dado()
    print(f"  Dado 1: {dado1}")
    dado2 = lanzar_dado()
    print(f"  Dado 2: {dado2}")

    producto = dado1 * dado2
    print(f"  Producto de la computadora: {dado1} x {dado2} = {producto}")
    return dado1, dado2, producto

def es_multiplo_de_2_o_5_pero_no_ambos(numero):
    """
    Verifica si el numero es multiplo de 2 O de 5, pero NO de ambos.
    Multiplo de ambos seria multiplo de 10, eso no cuenta.
    Retorna True si cumple la condicion, False si no.
    """
    mult2 = (numero % 2 == 0)  # Es divisible entre 2?
    mult5 = (numero % 5 == 0)  # Es divisible entre 5?

    # XOR: uno o el otro, pero no los dos
    return mult2 != mult5

def desempate():
    """
    Cuando hay empate, cada jugador lanza UN dado extra.
    Gana el que saque el numero mayor. Retorna el resultado.
    """
    print("\n  ** EMPATE ** Cada jugador lanza un dado extra.")

    input("  Presiona Enter para lanzar tu dado extra...")
    dado_usuario = lanzar_dado()
    print(f"  Tu dado extra: {dado_usuario}")

    dado_cpu = lanzar_dado()
    print(f"  Dado extra de la computadora: {dado_cpu}")

    if dado_usuario > dado_cpu:
        return "usuario"
    elif dado_cpu > dado_usuario:
        return "computadora"
    else:
        return "empate"

def determinar_ganador(prod_usuario, prod_cpu):
    """
    Compara si cada producto cumple la condicion.
    Retorna: 'usuario', 'computadora', o 'empate'.
    """
    usuario_gana = es_multiplo_de_2_o_5_pero_no_ambos(prod_usuario)
    cpu_gana     = es_multiplo_de_2_o_5_pero_no_ambos(prod_cpu)

    print(f"\n  ¿Tu producto ({prod_usuario}) cumple la condicion? {usuario_gana}")
    print(f"  ¿Producto de la CPU ({prod_cpu}) cumple la condicion? {cpu_gana}")

    if usuario_gana and not cpu_gana:
        return "usuario"
    elif cpu_gana and not usuario_gana:
        return "computadora"
    else:
        # Ambos cumplen o ninguno cumple -> empate -> desempate
        return desempate()

def mostrar_resultado(ganador):
    """Muestra un mensaje dependiendo de quien gano."""
    if ganador == "usuario":
        print("  ¡GANASTE! Felicidades.")
    elif ganador == "computadora":
        print("  Gano la computadora. Mejor suerte la proxima.")
    else:
        print("  EMPATE TOTAL. Nadie gano.")

def jugar_ronda():
    """Ejecuta una ronda completa del juego."""
    _, _, prod_usuario = turno_usuario()
    _, _, prod_cpu     = turno_computadora()
    ganador = determinar_ganador(prod_usuario, prod_cpu)
    mostrar_resultado(ganador)

def main():

    # El while mantiene el juego activo
    while True:
        jugar_ronda()

        # Preguntar si quiere jugar otra vez
        respuesta = input("\n¿Quieres jugar otra vez? (s/n): ").strip().lower()
        if respuesta != "s":
            print("\nGracias por jugar. ¡Hasta luego!")
            break  # Sale del while

# Punto de entrada del programa
if __name__ == "__main__":
    main()
