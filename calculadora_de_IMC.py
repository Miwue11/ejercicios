#Calculadora de IMC
#IMC= peso/ (altura**2)

#<19: delgadez

#entre 20 y 25: normal

#entre 26 y 30 : sobrepeso

#>30: obesidad

def calculadora_imc():
    
    try:
        nombre= input("hola crack, como te llamas: ")
        peso= float(input(f"hola {nombre}, cuanto pesas en kilos: "))
        altura=float(input("ahora, dime cuanto mides en metros: "))
        if altura >= 3:
                print("""bro, pon el punto que te estoy pidiendo metros, no centimetros.
                      Vamos a empezar de nuevo...: """)
                return calculadora_imc()
        imc= peso / (altura**2)
        print(f"hola {nombre}, tu IMC es {imc} ")
    except ValueError:
           print("no pongas letritas joder, ahora hay q empezar de nuevo...:")
           return calculadora_imc()

    
    if imc<20:
            print("pareces un puto spaghetti bro.")
    elif imc>=20 and imc<=25:
            print("tienes un cuerpo, normal, NORMAL.")
    elif imc>25 and imc<= 30:
            print("tienes sobrepeso, muevete un poco, yo confio en ti.")
    else:
            print("estas obeso puta foca.")
    

calculadora_imc()


