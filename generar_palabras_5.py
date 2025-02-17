# Filtrar palabras de 5 letras desde un archivo
def generar_lista_palabras():
    with open("diccionario.txt", "r", encoding="utf-8") as archivo:
        palabras = [palabra.strip().upper() for palabra in archivo if len(palabra.strip()) == 5]
    with open("palabras_validas.txt", "w", encoding="utf-8") as salida:
        salida.write("\\n".join(palabras))
    print(f"Se generó una lista con {len(palabras)} palabras de 5 letras.")
generar_lista_palabras()