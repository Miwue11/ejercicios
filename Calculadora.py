class Calculadora():

    pregunta=input("""que quieres hacer:
    sumar(+)
    restar(-)
    dividir(/)
    multiplicar(*)
    >:""")

    def sumar_dos():
    

        while True:

            a=float(input("hola dime un numero: "))
            b=float(input("buenas, ahora el segundo numero: "))

            try:
                resultado= (a+b)
    
            except ValueError:
                print("No he podido hacer la operacion, introduce solo numeros.")
            else:
                break
        print(resultado)


    def multiplicar_dos():
    

        while True:

            try:
                a=input("hola dime un numero: ")
                b=input("buenas, ahora el segundo numero: ")
                resultado= float(a)*float(b)
            except ValueError:
                print("No he podido hacer la operacion, introduce solo numeros.")
            else:
                break
        print (resultado)
        

        
    def dividir_dos():
        

        while True:

            try:
                a=input("hola dime un numero: ")
                b=input("buenas, ahora el segundo numero: ")
                resultado= float(a)/float(b)
            except ValueError:
                    print("No he podido hacer la operacion, introduce solo numeros.")
            else:
                    break
        print (resultado)
        
    def restar_dos():
        

        while True:

            try:
                a=input("hola dime un numero: ")
                b=input("buenas, ahora el segundo numero: ")
                resultado= float(a)-float(b)
            except ValueError:
                    print("No he podido hacer la operacion, introduce solo numeros.")
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
print("¡Hasta la proxima!")