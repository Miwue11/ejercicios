
#ejercicio2
#crear un sistema para una escuela. en este sistema, 
#vamos a tener dos clases principales,
#Persona y #Estudiante. La clase Persona, tendra (nombre y edad) y 
# la de Estudiante tendra (grado), ambas clases tendran un metodo
#que imprima sus acciones.

#debera utilizarse el super() en el metodo de iniciacion (init) para 
#reutilizar el codigo de la clase padre (Persona). luego crear 
#una instancia de la clase Estudiante e imprimir sus atributos y 
#utilizar metodos para asegurarte de q funciona correctamente.

class Persona:
    def __init__(self,nombre,edad):
      self.nombre=nombre
      self.edad=edad
       
class Estudiante(Persona):
    def __init__(self, nombre, edad,grado):
       Persona.__init__(self,nombre, edad)
       self.grado=grado
    def hablar_grado(self):
        print(f"hola soy {self.nombre}, tengo {self.edad} años y estoy cursando {self.grado}")
        

Miguel= Estudiante("Miguel",26,"2º Grado" ) 
Lidia= Estudiante("Lidia",27,"Universidad") 

Miguel.hablar_grado()
Lidia.hablar_grado()


herencia= issubclass(Estudiante,Persona)
print(herencia)


#ejercicio2.2
#imagina que estas modelando animales en un Zoo. Crea tres clases
#de "Animal", "Mamifero", y "Ave". la clase "Animal" debe tener un metodo llamado "comer".
#la clase "Mamifero" debe tener "Amamantar" y la clase "Ave" uno llamado "volar"

#ahora crea una clase "Murcielago" que herede de "Mamifero" y de "Ave", en ese orden, 
#y por lo tanto debe ser capaz de "amamantar" y "volar" ademas de "comer" 

#finalmente juega con el orden de hernecia "Murcielago" y observa como cambia el MRO
#y el comportamiento de los metodos al usar super()


class Animal:
    def __init__(self,comer):
      self.comer=comer

class Mamifero():
    def __init__(self, comer,amamantar):
       Animal.__init__(self,comer)
       self.amamantar=amamantar

class Ave():
     def __init__(self, comer,volar):
       Animal.__init__(self,comer)
       self.volar=volar

class Murcielago(Animal,Mamifero,Ave):
    def __init__(self,comer, amamantar, volar):
       Animal.__init__(self,comer)
       Mamifero.__init__(self,comer,amamantar)
       Ave.__init__(self,comer,volar)
      
    def accion(self):  
       print(f"el Murcielago puede {self.comer}, {self.amamantar} y ademas puede {self.volar}")
        

murcielago=Murcielago('comer','amamantar','volar')

murcielago.accion()
print(Murcielago.mro())