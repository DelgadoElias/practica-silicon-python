print("Hola mundo")


class Animal:
    def __init__(self, nombre, edad, peso):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso

    def dormir(self):
        return f"{self.nombre} - ZzZzZz"

    def pesaje(self):
        return f"{self.nombre} - Peso oficial: {self.peso}"

    def comunicarse(self):
        return f"{self.nombre} - Hola que tal"


class Perro(Animal):
    def __init__(self, nombre, edad, peso, vacunado):
        super().__init__(nombre, edad, peso)
        self.vacunado = vacunado

    def comunicarse(self):
        print(f"Interno: {super().comunicarse()}")
        return f"{self.nombre} - Guau!"


class Gato(Animal):
    def __init__(self, name, edad, peso, color):
        super().__init__(name, edad, peso)
        self.color = color

    def comunicarse(self):
            print(f"Interno: {super().comunicarse()}")
            return f"{self.nombre} - Miau!"

class Vaca(Animal):
    def __init__(self, nombre, edad, peso, granja, documentacion):
        super().__init__(nombre, edad, peso)
        self._granja = granja # Protegido
        # Privado - Le cambio el nombre por que es privada
        self.__documentacion = documentacion # _Vaca__documentacion

    # float 12.0
    # int 1200   Lo ultimos 2 digitos equivalen a una moneda

    @property # Getter
    def documentacion(self):
        # REGLAS DE NEGOCIO O VALIDACIONES PARA QUE SE LEA COMO TIENE QUE SER LA INFORMACION
        return self.__documentacion

    @documentacion.setter
    def documentacion(self, valor):
            # REGLAS DE NEGOCIO O VALIDACIONES 
            # PARA ESCRIBIR CON SEGURIDAD MI CODIGO
            return self.__documentacion
    

    def comunicarse(self):
            print(f"Interno: {super().comunicarse()}")
            return f"{self.nombre} - Muuu!"

    def ver_documentacion(self):
        print(self.__documentacion)

class Gallina(Animal):
    def __init__(self, nombre, edad, peso, huevos):
        super().__init__(nombre, edad, peso)
        self.huevos = huevos

    def comunicarse(self):
            print(f"Interno: {super().comunicarse()}")
            return f"{self.nombre} - Coco!"

class Caniche(Perro):
    def __init__(self, nombre, edad, peso, vacunado, velocidad):
        super().__init__(nombre, edad, peso, vacunado)
        self.velocidad = velocidad





# /api/sistema/iniciar-sesion

# nombre, password, numero_cuenta


class Sesion_Usuario:
    def __init__(self, usuario, password):
        self.usuario = usuario
        self.password = password # Normalmente va a estar encriptada

    def iniciar_sesion():
        # Valido los datos
        return "LLAVE_CRIPTOGRAFICA"

class Sesion_Usuario_Bancaria(Sesion_Usuario):
    def __init__(self, usuario, password, numero_cuenta):
        super().__init__(usuario, password)
        self.numero_cuenta = numero_cuenta

    def iniciar_sesion(self):
        llave_momentanea = super().iniciar_sesion()
        encriptacion_numero_cuenta = self.numero_cuenta # Encriptado
        if(llave_momentanea == encriptacion_numero_cuenta):
            return True
        return False

sub = Sesion_Usuario_Bancaria("user", "pass", "account")

print(isinstance(sub, Sesion_Usuario_Bancaria))
print(issubclass(Animal, Sesion_Usuario))

# nombre, password, cuit, clave_usuario

perro = Perro("Firulais", 3, 30, False)

firuar = Caniche("Firuar", 3, 30, vacunado=False, velocidad=20 )
vaca_lechera = Vaca("Lechera",1,300,"Las Marias", "Carpeta")

vaca_lechera._granja = "3 De Febrero"
vaca_lechera.titulacion = "Graduada"
vaca_lechera.__documentacion = "Nono"
print(vaca_lechera.__documentacion)
vaca_lechera.ver_documentacion()

gallinita_pintadita = Gallina("Pintadita",1,4,30)
gatito = Gato("Gato", 1, 13, "Negro")

perro.dormir()

listado_de_animales = [perro, firuar, vaca_lechera, gallinita_pintadita, gatito]

for animal in listado_de_animales:
    print(animal.comunicarse())