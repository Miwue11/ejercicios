print("BIENVENIDOS AL CUESTIONARIO POKEMON!!!!!!")
pregunta=input("""
    quieres jugar...?
    a ver si te atreves...: 
""")
class Quiz():
    while True:  
        def quizPKM1():
            print("Serás capaz de acertar la pregunta mas facil del Quiz...?")
            try:
                pregunta1=input("¿Cómo se llama el Pokémon inicial de tipo fuego de la región de Kanto?: ").capitalize()
                if pregunta1=="Charmander":
                            print("CORRECTO")
                elif pregunta1 != "Charmander":
                                print("ERROR")
                                return Quiz.quizPKM1()
            except ValueError:
                    print("Error..., la respuesta era: Charmander ")
        break    

    while True:
        def quizPKM2():
            print("Vamos con otra pregunta facilita...")
            try:
                pregunta2=input("¿De qué tipo es Pikachu?: ").capitalize()
                if pregunta2=="Eléctrico":
                    print("CORRECTO")
                elif pregunta2 != "Eléctrico":
                    print("ERROR")
                    print("recuerda que debes poner acentos... jiji")
                    return Quiz.quizPKM2()
            except ValueError:
                print("Error..., la respuesta era: Eléctrico ")
        break

    while True:        
        def quizPKM3():
            print("En esta pregunta ya necesitas ser un buen amante de Pokémon...")
            try:
                pregunta3=(input("¿En qué generación se introdujo el tipo Hada?: "))
                if pregunta3=="6":
                    print("CORRECTO")
                elif pregunta3!= "6":
                                print("Error..., recuerda q solo debes poner numeros enteros.")
                                return Quiz.quizPKM3()
            except ValueError:
                print("Error..., recuerda q solo debes poner numeros enteros. ")
        break

    while True:       
        def quizPKM4():
            print("Esto se esta volviendo modo Tryhard...")
            try:
                pregunta4=input("¿Qué Pokémon tuvo la primera forma regional introducida en la serie principal?: ").capitalize()
                if pregunta4=="Rattata":
                    print("CORRECTO")
                elif pregunta4 != "Rattata":
                                print("Recuerda que debes poner mayusculas y acentos... jiji")
                                return Quiz.quizPKM4()
            except ValueError:
                print("recuerda que debes poner mayusculas y acentos... jiji ")
        break

    while True:        
        def quizPKM5():
            print("Has llegado a la ultima, si aciertas esta, tienes mis respetos...")
            try:
                pregunta5=(input("¿Cuántos puntos tiene la estadística mas alta de Shuckle?: "))
                if pregunta5=="230":
                    print("CORRECTO")
                elif pregunta5 != "230":
                                print("Error..., recuerda q solo puedes poner numeros enteros ")
                                return Quiz.quizPKM5()
            except ValueError:
                print("Error..., recuerda q solo puedes poner numeros enteros ")
        
        break

if pregunta!="no":
    Quiz.quizPKM1()
    Quiz.quizPKM2()
    Quiz.quizPKM3()
    Quiz.quizPKM4()
    Quiz.quizPKM5()
    print("ENHORABUENA, GANASTE EL QUIZ!, IMPRESIONANTE!")
else: 
    print("cagón/a...")

if __name__=="__main__":
    Quiz()


