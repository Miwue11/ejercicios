class Personaje:
    def __init__(self,nombre,fuerza,velocidad):
        self.nombre=nombre
        self.velocidad=velocidad
        self.fuerza=fuerza
        
    def __repr__ (self):
        return f"{self.nombre} (fuerza: {self.fuerza}, Velocidad: {self.velocidad})"
     
    def __add__(self,otro_pj):
        nuevo_nombre=self.nombre + otro_pj.nombre
        nueva_fuerza=round(((self.fuerza + otro_pj.fuerza)/2)**2) 
        nueva_velocidad=round(((self.velocidad + otro_pj.velocidad)/2)**2 )       
        return Personaje(nuevo_nombre,nueva_fuerza,nueva_velocidad)
goku=Personaje("Goku",100,100)
buu=Personaje("Buu",300,10)
vegeta=Personaje("Vegetta",99,99)
gobuu= goku + buu
gogeta=goku+vegeta

print(gobuu)
print(gogeta)