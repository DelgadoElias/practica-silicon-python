class Persona:
    def __init__(self, nombre, edad, ciudad):
        self.nombre = nombre
        self.edad = edad # Que la edad tenga que ser mayor a 0 por que sino no existe
        self.ciudad = ciudad
        self.amigos = 0
        self.es_mayor = edad > 18
    def cumpleanios(self):
        self.es_mayor = self.edad > 18
        self.edad += 1

elias = Persona("Elias", 25, "Posadas")
martin = Persona("Martin",25, "San Vicente")

print(f"{elias.nombre} {elias.edad} {martin.ciudad}")

elias.edad = 23
elias.cumpleanios()
martin.cumpleanios()

print(type(elias))

print(f"{elias.nombre} {elias.edad} {martin.ciudad}")

print("Edades")
print(f"{elias.edad} {martin.edad}")
