
def mostrar_saldo(saldo):
    print(f"tu saldo actual es: {saldo:.2f}€")
def depositar():
    dinero= float(input("Introduce la cantidad de dinero a depositar: "))
    if dinero <0:
        print("La cantidad introducida no es valida.")
        return 0 
    else: 
        return dinero
    
def retirar_dinero(saldo):
    dinero= float(input("Introduce la cantidad de dinero a retirar: "))
    if dinero > saldo:
        print("No puedes retirar tanto dinero.")
        return 0
    elif dinero<0:
        print("La cantidad debe ser mayor de cero")
        return 0 
    else:
        return dinero
def menu_principal():
    saldo=0
    en_ejecucion=True
    
    while en_ejecucion:
        print("\nPROGRAMA BANCARIO")
        print("1. Mostrar saldo.")
        print("2. Depositar.")
        print("3. Retirar.")
        print("4. Salir.")
        opcion=input("Elige una opcion: ")
        
        if opcion=="1":
            mostrar_saldo(saldo)
        elif opcion=="2":
            saldo+=depositar()
        elif opcion=="3":
            saldo-=retirar_dinero(saldo)
        elif opcion=="4":
            en_ejecucion=False
            print("Buen dia")
        else:
            print("Eleccion no valida")
            return menu_principal()
if __name__=="__main__":
    menu_principal()