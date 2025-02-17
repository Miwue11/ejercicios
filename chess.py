import re

# Definición de las piezas de ajedrez
PEON_BLANCO, TORRE_BLANCA, CABALLO_BLANCO, ALFIL_BLANCO, REINA_BLANCA, REY_BLANCO = "♙", "♖", "♘", "♗", "♕", "♔"
PEON_NEGRO, TORRE_NEGRA, CABALLO_NEGRO, ALFIL_NEGRO, REINA_NEGRA, REY_NEGRO = "♟", "♜", "♞", "♝", "♛", "♚"
VACIO = "."

# Creación del tablero inicial
TABLERO = [
    [TORRE_NEGRA, CABALLO_NEGRO, ALFIL_NEGRO, REINA_NEGRA, REY_NEGRO, ALFIL_NEGRO, CABALLO_NEGRO, TORRE_NEGRA],
    [PEON_NEGRO] * 8,
    [VACIO] * 8,
    [VACIO] * 8,
    [VACIO] * 8,
    [VACIO] * 8,
    [PEON_BLANCO] * 8,
    [TORRE_BLANCA, CABALLO_BLANCO, ALFIL_BLANCO, REINA_BLANCA, REY_BLANCO, ALFIL_BLANCO, CABALLO_BLANCO, TORRE_BLANCA]
]

def imprimir_tablero():
    print("  a b c d e f g h")
    print("  ----------------")
    for i, fila in enumerate(TABLERO):
        print(f"{8 - i} {' '.join(fila)} {8 - i}")
    print("  ----------------")
    print("  a b c d e f g h")

def notacion_a_indice(movimiento):
    coincidencia = re.match(r"([a-h])([1-8])", movimiento)
    if coincidencia:
        columna, fila = coincidencia.groups()
        return 8 - int(fila), ord(columna) - ord("a")
    return None

def mover_pieza(origen, destino):
    pos_origen = notacion_a_indice(origen)
    pos_destino = notacion_a_indice(destino)
    
    if not pos_origen or not pos_destino:
        print("Movimiento inválido. Usa notación como 'e2 e4'.")
        return False
    
    pieza = TABLERO[pos_origen[0]][pos_origen[1]]
    if pieza == VACIO:
        print("No hay pieza en la posición seleccionada.")
        return False
    
    # Movimiento básico (sin validaciones específicas)
    TABLERO[pos_destino[0]][pos_destino[1]] = pieza
    TABLERO[pos_origen[0]][pos_origen[1]] = VACIO
    return True

def jugar():
    turno = "blanco"
    while True:
        imprimir_tablero()
        movimiento = input(f"Turno de {turno} (ejemplo 'e2 e4'): ").strip().lower()
        if movimiento == "salir":
            break
        try:
            origen, destino = movimiento.split()
            if mover_pieza(origen, destino):
                turno = "negro" if turno == "blanco" else "blanco"
        except ValueError:
            print("Formato incorrecto. Introduce un movimiento válido.")

if __name__ == "__main__":
    jugar()