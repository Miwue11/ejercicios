
def ahorcado():
    palabra_secreta= input("dime la palabra secreta: ").lower()
    letras_adivinadas=["_"]*len(palabra_secreta)
    letras_usadas=[]
    intentos_restantes=6
    while "_" in letras_adivinadas and intentos_restantes > 0:
        print("\npalabra: "," ".join(letras_adivinadas))
        print("intentos restantes: ", intentos_restantes)
        print("letras usadas: ",letras_usadas)
        letra=input("Adivina una letra: ").lower()
        if len(letra) != 1 or not letra.isalpha():
            print("Por favor, introduce una letra válida.")
            continue
        if letra in letras_usadas:
            print("ya usaste esa letra")
            continue
        letras_usadas.append(letra)
        if letra in palabra_secreta:
            print("CORRECTO")
            
            for i,l in enumerate(palabra_secreta):
                if l == letra:
                    letras_adivinadas[i]=letra
        else:
            print("INCORRECTO")
            intentos_restantes-=1
        if letra in palabra_secreta:
            intentos_restantes+=1
            print("Ganaste una vida!.")
            if intentos_restantes>6:
                print("Oh no... tienes las vidas al maximo, no subiras mas vidas...")
        if intentos_restantes>6:
                    intentos_restantes-=1
        if letra not in palabra_secreta:
            print("Perdiste una vida!.")
    if "_" not in letras_adivinadas:
        print("\n FELICIDADES, ADIVINASTE LA PALABRA: ",palabra_secreta)
    else:
        print("\n te quedaste sin intentos...")
if __name__=="__main__":
    ahorcado()