def convertir_entero_a_bits(numero):
    """
    Convierte un número entero a su representación binaria en formato de 32 bits.
    """
    if not (-2**31 <= numero < 2**31):
        return "El número debe estar en el rango de un entero de 32 bits (-2^31 a 2^31-1)."

    # Si el número es negativo, calcular el complemento a dos
    if numero < 0:
        numero = (1 << 32) + numero

    # Convertir el número a binario y rellenar con ceros a la izquierda para tener 32 bits
    bits = format(numero, '032b')
    return bits

# Solicitar número entero al usuario
try:
    numero = int(input("Ingresa un número entero (rango de 32 bits): "))
    resultado = convertir_entero_a_bits(numero)
    print(f"La representación en 32 bits es: {resultado}")
except ValueError:
    print("Por favor, ingresa un número válido.")


