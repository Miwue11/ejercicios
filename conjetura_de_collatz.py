


def conjetura_de_collatz(c0):
    if c0 <= 0:
        print("El número debe ser un entero positivo.")
        return
#cc
    pasos = 0

    while c0 != 1:
        print(c0, end=" -> ")
        if c0 % 2 == 0:
            c0 //= 2
        else:
            c0 = 3 * c0 + 1
        pasos += 1

    print(1)
    print(f"Se alcanzó 1 en {pasos} pasos.")

# Leer número del usuario
try:
    c0 = int(input("Ingresa un número natural: "))
    conjetura_de_collatz(c0)
except ValueError:
    print("Por favor, ingresa un número válido.")
