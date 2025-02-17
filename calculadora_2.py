class Calculadora():

    pregunta=input("""que quieres hacer:
    sumar
    restar
    dividir
    multiplicar
    >:""")

    def sumar_dos():
    
    #iniciando un bucle while
        while True:
        #pidiendo numeros
            a=int(input("hola dime un numero: "))
            b=int(input("buenas, ahora el segundo numero: "))
        #intentando convertirlos a enteros y sumandolos
            try:
                resultado= (a+b)
        #excepciones    
            except ValueError:
                print("introduce un numero entero")
            else:
                break
        print(resultado)


    def multiplicar_dos():
    
    #iniciando un bucle while
        while True:
        #pidiendo numeros
            try:
                a=input("hola dime un numero: ")
                b=input("buenas, ahora el segundo numero: ")
                resultado= int(a)*int(b)
            except ValueError:
                print("introduce numeros")
            else:
                break
        print (resultado)
        
    #mostrando el resultado
        
    def dividir_dos():
        
        #iniciando un bucle while
        while True:
            #pidiendo numeros
            try:
                a=input("hola dime un numero: ")
                b=input("buenas, ahora el segundo numero: ")
                resultado= int(a)/int(b)
            except ValueError:
                    print("introduce numeros")
            else:
                    break
        print (resultado)
        
    def restar_dos():
        
        #iniciando un bucle while
        while True:
            #pidiendo numeros
            try:
                a=input("hola dime un numero: ")
                b=input("buenas, ahora el segundo numero: ")
                resultado= int(a)-int(b)
            except ValueError:
                    print("introduce numeros")
            else:
                    break
        print (resultado)

    if pregunta=="sumar":
        print("vamos a sumar...")
        sumar_dos()
        
    elif pregunta=="multiplicar":
        print("vamos a multiplicar...")
        multiplicar_dos()

    elif pregunta=="dividir":
        print("vamos a dividir...")
        dividir_dos()
    else:
        print("vamos a restar...")
        restar_dos()
        
Calculadora()