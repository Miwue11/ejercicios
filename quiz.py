with open("palabras_validas.txt", "r", encoding="utf-8") as archivo:
    palabras_unicas = sorted(set(palabra.strip() for palabra in archivo))

with open("palabras_no_repes.txt", "w", encoding="utf-8") as salida:
    salida.write("\n".join(palabras_unicas))
