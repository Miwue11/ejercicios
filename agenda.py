agenda= {}

def mostrar_contactos():
    print("\nNombre".ljust(20)+"Numero de Contacto")
    print("-" * 35)
    for nombre, numero in agenda.items():
        print(f"{nombre.ljust(20)}{numero}")



while True:
    print(f"\nOPCIONES: ")
    print("1. Añadir nuevo contacto")
    print("2. Buscar contacto")
    print("3. Mostrar todos los contacto")
    print("4. eliminar contacto")
    print("5. Salir")
    
    opcion=(input("Introduce tu opcion: "))
    
    if opcion == "1":
        nombre= input("Nombre de contacto: ")
        numero= input("Numero de contacto: ")
        agenda[nombre]=numero
        print("El contacto ha sido añadido.")
    
    elif opcion=="2":
        nombre_buscar=input("Nombre del contacto a buscar: ")
        
        if nombre_buscar in agenda:
            print(f"su numero es {agenda[nombre_buscar]}")
        else:
            print("No se ha encontrado el contacto.")
    
    elif opcion=="3":
        if not agenda:
            print("La agenda esta vacía")
        else:
            mostrar_contactos()
    
    elif opcion=="4":
        nombre_eliminar=input("Nombre del contacto a eliminar: ")
        if nombre_eliminar in agenda:
            agenda.pop(nombre_eliminar)
            print("El contacto ha sido eliminado.")
        else:
            print("No se encontró el contacto a eliminar.")
            
    
    elif opcion=="5":
        print("Hasta pronto")
        break
    
    else:
        print("Opcion no válida")
        
if __name__=="__main__":
    mostrar_contactos()