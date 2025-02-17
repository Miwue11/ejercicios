
class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre=nombre
        self.edad=edad
        self.grado=grado
    
    def estudiar(self):
        print("estudiando...")

nombre= input("dime tu nombre: ")
edad=input("dime tu edad: ")
grado=input("dime tu grado: ")


estudiante= Estudiante(nombre,edad,grado)

print(f"""
el estudiante se llama: {estudiante.nombre} \n
el estudiante tiene {estudiante.edad}\n
el estudiante cursa un {estudiante.grado} \n 
""")

while True:
    estudiar= input("que vas a hacer: ")
    if (estudiar.lower()=="estudiar"):
        estudiante.estudiar()
    