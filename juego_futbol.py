class Personaje:
    def __init__(self,nombre,tiro,regate,fuerza,velocidad):
        self.nombre=nombre
        self.velocidad=velocidad
        self.fuerza=fuerza
        self.regate=regate
        self.tiro=tiro
        
    def __repr__ (self):
        return f"{self.nombre} (tiro: {self.tiro}, regate: {self.regate}, fuerza: {self.fuerza}, Velocidad: {self.velocidad})"
     
    def __add__(self,otro_pj):
        nuevo_nombre=self.nombre + otro_pj.nombre
        nueva_fuerza=round(((self.fuerza + otro_pj.fuerza)/2)**1.1) 
        nueva_velocidad=round(((self.velocidad + otro_pj.velocidad)/2)**1.1)
        nuevo_regate=round(((self.regate + otro_pj.regate)/2)**1.1) 
        nuevo_tiro=round(((self.tiro + otro_pj.tiro)/2)**1.1)        
        return Personaje(nuevo_nombre,nuevo_tiro,nuevo_regate,nueva_fuerza,nueva_velocidad)

def mostrar_personajes(futbolistas):
    if not futbolistas:
        print("No hay ningun personaje creado.")
    else:
        print("Personaje disponibles: ")
        for i, jugador in enumerate(futbolistas):
            print(F"{i+1}, {jugador}")
            
def crear_personaje():
    nombre=input("Ingrese el nombre del futbolistas: ")
    tiro=float(input("Ingrese el tiro del futbolista: "))
    regate=float(input("Ingrese el regate del futbolista: "))
    fuerza=float(input("Ingrese la fuerza del futbolista: "))
    velocidad=float(input("Ingrese la velocidad del futbolista: "))
    
    
    return Personaje(nombre,tiro,regate,fuerza,velocidad)

futbolistas=[]

while True:
    print("\n1. Crear personaje")
    print("2. Fusionar Personajes")
    print("3. Mostrar Personajes")
    print("4. Salir")
    opcion=input("Seleccione una opcion (1, 2, 3, o 4): ")
    
    if opcion=="1":
        personaje_nuevo=crear_personaje()
        futbolistas.append(personaje_nuevo)
        print("Personaje creado con éxito!")
        
    elif opcion=="2":
        if len(futbolistas)<2:
            print("Primero debes crear al menos dos personajes!.")
        else:
           mostrar_personajes(futbolistas)
           numpj1=int(input("Ingrese el numero del primer personaje: "))
           numpj2=int(input("Ingrese el numero del segundo personaje: "))
        
           if 1<= numpj1 <= len(futbolistas) and 1 <= numpj2 <= len(futbolistas) and numpj1 != numpj2:
               personaje1=futbolistas[numpj1-1]
               personaje2=futbolistas[numpj2-1]
               personaje_fusionado=personaje1 + personaje2
               futbolistas.append(personaje_fusionado)
               print(f"Fusión exitosa! El nuevo personaje es {personaje_fusionado}")
           else:
               print("Selección invalida. Asegúrate de elegir personajes válidos")

    elif opcion=="3":
        mostrar_personajes(futbolistas)  
    elif opcion=="4":
        break   
    else:
        print("Opcion invalida. Por favor, seleccione una opción válida.")
             
while True:
    print("Juego terminado")
    
    
