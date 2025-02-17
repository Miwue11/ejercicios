class Pokemon:
    def __init__(self,nombre,tipo1,tipo2,vida,ataque,ataque_especial,defensa,defensa_especial,velocidad):
        self.nombre=nombre
        self.tipo1=tipo1
        self.tipo2=tipo2
        self.velocidad=velocidad
        self.vida=vida
        self.ataque=ataque
        self.ataque_especial=ataque_especial
        self.defensa=defensa
        self.defensa_especial=defensa_especial
        
    def __repr__ (self):
        return f"{self.nombre} (Tipos: {self.tipo1}, {self.tipo2}  Vida: {self.vida}, Ataque: {self.ataque}, Ataque Especial: {self.ataque_especial}, Defensa: {self.defensa}, Defensa Especial: {self.defensa_especial} Velocidad: {self.velocidad})"

    def __add__(self,otro_pj):
        nuevo_nombre=self.nombre + otro_pj.nombre
        nuevo_tipo1= self.tipo1
        nuevo_tipo2=otro_pj.tipo2
        nueva_vida=round(((self.vida + otro_pj.vida)/2)**1.18) 
        nuevo_ataque=round(((self.ataque + otro_pj.ataque)/2)**1.18) 
        nuevo_ataque_especial=round(((self.ataque_especial + otro_pj.ataque_especial)/2)**1.18) 
        nueva_velocidad=round(((self.velocidad + otro_pj.velocidad)/2)**1.18)
        nueva_defensa=round(((self.defensa + otro_pj.defensa)/2)**1.18) 
        nueva_defensa_especial=round(((self.defensa_especial + otro_pj.defensa_especial)/2)**1.18)        
        return Pokemon(nuevo_nombre,nuevo_tipo1,nuevo_tipo2,nueva_vida,nuevo_ataque,nuevo_ataque_especial,nueva_defensa,nueva_defensa_especial,nueva_velocidad)

def mostrar_personajes(pokemon):
    if not pokemon:
        print("No hay ningun Pokémon creado.")
    else:
        print("Pokémon disponibles: ")
        for i, poke in enumerate(pokemon):
            print(F"{i+1}, {poke}")
            
def crear_personaje():
    nombre=input("Ingrese el nombre del Pokémon: ")
    tipo1= input("Ingrese el primer tipo del Pokémon: ")
    tipo2=input("Ingrese el segundo tipo del Pokémon: ")
    vida=float(input("Ingrese la vida del Pokémon: "))
    ataque=float(input("Ingrese el ataque del Pokémon: "))
    ataque_especial=float(input("Ingrese el ataque especial del Pokémon: "))
    defensa=float(input("Ingrese la defensa del pokemon: "))
    defensa_especial=float(input("Ingrese la defensa especial del Pokémon: "))
    velocidad=float(input("Ingrese la velocidad del Pokémon: "))
    return Pokemon(nombre,tipo1,tipo2,vida,ataque,ataque_especial,defensa,defensa_especial,velocidad)

pokemon=[]

while True:
    print("\n1. Crear Pokémon")
    print("2. Fusionar Pokémon")
    print("3. Mostrar Pokémon")
    print("4. Salir")
    opcion=input("Seleccione una opcion (1, 2, 3, o 4): ")
    
    if opcion=="1":
        personaje_nuevo=crear_personaje()
        pokemon.append(personaje_nuevo)
        print("Pokémon creado con éxito!")
        
    elif opcion=="2":
        if len(pokemon)<2:
            print("Primero debes crear al menos dos Pokémon!.")
        else:
           mostrar_personajes(pokemon)
           try:
              numpj1 = int(input("Ingrese el número del primer Pokémon: "))
              numpj2 = int(input("Ingrese el número del segundo Pokémon: "))
              if 1<= numpj1 <= len(pokemon) and 1 <= numpj2 <= len(pokemon) and numpj1 != numpj2:
               personaje1=pokemon[numpj1-1]
               personaje2=pokemon[numpj2-1]
               personaje_fusionado=personaje1 + personaje2
               pokemon.append(personaje_fusionado)
               print(f"Fusión exitosa! El nuevo personaje es {personaje_fusionado}")
              else:
                print("Selección invalida. Asegúrate de elegir personajes válidos")
           except ValueError:
               print("Entrada invalida. Intente nuevamente.")

    elif opcion=="3":
        mostrar_personajes(pokemon)  
    elif opcion=="4":
        break   
    else:
        print("Opcion invalida. Por favor, seleccione una opción válida.")
             
