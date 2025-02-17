def convertir_bits_a_entero(bits):
    """
    Convierte una secuencia de bits (0s y 1s) en un entero considerando 32 bits.
    """
    if len(bits) != 32:
        return "La secuencia debe tener exactamente 32 bits."

    try:
        # Verificar que solo contenga '0' y '1'
        if not all(bit in ('0', '1') for bit in bits):
            return "La secuencia solo debe contener los caracteres '0' y '1'."

        # Verificar si es negativo (complemento a dos)
        if bits[0] == '1':
            # Convertir a entero negativo usando complemento a dos
            numero = -((1 << 32) - int(bits, 2))
        else:
            # Convertir a entero positivo
            numero = int(bits, 2)

        return numero
    except ValueError:
        return "Error en la conversión, verifica la secuencia de bits."

# Solicitar secuencia de bits al usuario
bits = input("Ingresa una secuencia de 32 bits (0 y 1): ")
resultado = convertir_bits_a_entero(bits)
print(f"El número entero correspondiente es: {resultado}")