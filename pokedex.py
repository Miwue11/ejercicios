pokedex= {}   

    
def mi_pokedex():
    print("\n----DATOS DEL POKEMON----")
    print("-"*35)
    for datos in pokedex.items():
        print(f"{datos}")

while True:
    print(f"\nOPCIONES: ")
    print("1. Añadir nuevo Pokemon")
    print("2. Buscar Pokemon")
    print("3. Mostrar todos los Pokemon")
    print("4. eliminar Pokemon")
    print("5. Salir")
    
    opcion=(input("Introduce tu opcion: "))
    
    if opcion == "1":
        try:
            nº=int(input("Dime el numero en el que registrarlo: "))
            nombre= input("Nombre del Pokemon: ")
            tipo1= input("Tipo principal y secundario del Pokemon: ")
            categoria= input("dime si es Común, Pseudolegendario, Legendario o Singular: ")
            pokedex[nombre]=[nº,tipo1,categoria,"Atrapado."]
            print("El Pokemon ha sido añadido.")
        except ValueError:
            print("\nIntroduce datos válidos.")
            mi_pokedex()
    
    elif opcion=="2":
        buscar=input("Nombre del Pokemon a buscar: ")
        
        if buscar in pokedex:
            print(f"su Pokemon es {pokedex[buscar]}")
        else:
            print("No se ha encontrado el Pokemon.")
    
    elif opcion=="3":
        if not pokedex:
            print("La Pokedex esta vacía")
        else:
            mi_pokedex()
    
    elif opcion=="4":
        nombre_eliminar=input("Nombre del Pokemon a eliminar: ")
        if nombre_eliminar in pokedex:
            pokedex.pop(nombre_eliminar)
            print("El Pokemon ha sido eliminado.")
        else:
            print("No se encontró el Pokemon a eliminar.")
            
    
    elif opcion=="5":
        print("Hasta pronto")
        break
    
    else:
        print("Opcion no válida")



if __name__=="__main__":
    mi_pokedex()