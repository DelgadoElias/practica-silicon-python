# =====================================================================
# REPASO 10 - Programación Orientada a Objetos (POO): clases y objetos
# Archivo original: clase1/10_poo.py
# =====================================================================
#
# CONCEPTOS
# ---------
# CLASE: el MOLDE o plano. Define qué DATOS tiene algo (atributos) y qué
#        puede HACER (métodos).        -> class Persona:
# OBJETO (o instancia): una cosa concreta hecha con ese molde.
#                                      -> elias = Persona("Elias", 25, "Posadas")
#   Una clase, muchos objetos: cada uno con SUS propios datos.
#
# __init__ (el CONSTRUCTOR): se ejecuta automáticamente al crear el
#   objeto. Ahí se cargan los atributos iniciales.
#
# self: es "el objeto mismo". Dentro de la clase, self.nombre significa
#   "el nombre de ESTE objeto". Python lo pasa solo: al llamar
#   elias.cumpleanios() no se escribe el self.
#
# ATRIBUTO: una variable que pertenece al objeto  (self.edad)
# MÉTODO:   una función que pertenece al objeto   (def cumpleanios(self))
#
# Nombres: las clases van en PascalCase (Persona, CuentaBancaria); los
# atributos y métodos en snake_case.
#
# ERRORES QUE ENCONTRAMOS EN LA VERSIÓN DE CLASE
# ----------------------------------------------
# 1. es_mayor SE CALCULA ANTES DE SUMAR EL AÑO:
#        def cumpleanios(self):
#            self.es_mayor = self.edad > 18   # con la edad VIEJA
#            self.edad += 1
#    Alguien de 18 que cumple 19 queda con es_mayor = False. El orden de
#    las líneas importa: primero sumar, después recalcular.
# 2. DATO DUPLICADO QUE SE DESINCRONIZA: guardar es_mayor como atributo
#    obliga a recalcularlo cada vez que cambia la edad. En el original,
#    elias.edad = 23 cambia la edad y es_mayor queda viejo. Mejor
#    calcularlo cuando se pide, con un método o con @property (abajo).
# 3. > 18 deja afuera a quien tiene exactamente 18. La mayoría de edad
#    es >= 18.
# 4. El comentario pide que la edad sea mayor a 0 pero no se valida. Con
#    lo de la clase 9, lanzamos ValueError en __init__.
# 5. amigos se crea y no se usa. Le agregamos un método.
# 6. print(type(elias)) muestra <class '__main__.Persona'>; y print(elias)
#    muestra algo como <__main__.Persona object at 0x...>. Con __str__
#    definimos cómo se ve un objeto al imprimirlo.
# 7. En el primer print se mezclan datos de elias y de martin
#    ({elias.nombre} {elias.edad} {martin.ciudad}). Seguramente era
#    elias.ciudad.
# 8. Se escribe "cumpleaños"; en código usamos "cumpleanios" para evitar
#    la ñ. Python acepta ñ en nombres, pero mucha gente evita caracteres
#    no ingleses en el código.
# =====================================================================

EDAD_MAYORIA = 18


class Persona:
    def __init__(self, nombre, edad, ciudad):
        if edad < 0:
            raise ValueError("La edad no puede ser negativa.")
        self.nombre = nombre
        self.edad = edad
        self.ciudad = ciudad
        self.amigos = []            # una lista de otras Persona

    # @property: se usa como un ATRIBUTO (sin paréntesis) pero se CALCULA
    # cada vez que se lee. Así nunca queda desactualizado.
    @property
    def es_mayor(self):
        return self.edad >= EDAD_MAYORIA

    def cumpleanios(self):
        self.edad += 1
        print(f"¡Feliz cumpleaños, {self.nombre}! Ahora tenés {self.edad}.")

    def agregar_amigo(self, otra_persona):
        if otra_persona not in self.amigos:
            self.amigos.append(otra_persona)

    def presentarse(self):
        return f"Hola, soy {self.nombre}, tengo {self.edad} años y vivo en {self.ciudad}."

    # __str__: lo que se muestra con print(objeto) o en un f-string.
    def __str__(self):
        return f"{self.nombre} ({self.edad}, {self.ciudad})"


# --- Crear objetos ------------------------------------------------------
elias = Persona("Elias", 25, "Posadas")
martin = Persona("Martin", 25, "San Vicente")

print(elias)                    # usa __str__
print(type(elias))              # <class '__main__.Persona'>
print(elias.presentarse())

# --- Modificar atributos y llamar métodos --------------------------------
elias.edad = 23                 # se puede cambiar un atributo directamente
elias.cumpleanios()             # 24
martin.cumpleanios()            # 26
print(f"Edades: {elias.edad} {martin.edad}")

# --- es_mayor nunca queda desactualizado -------------------------------
lucia = Persona("Lucía", 17, "Oberá")
print(f"{lucia.nombre} es mayor: {lucia.es_mayor}")    # False
lucia.cumpleanios()                                    # 18
print(f"{lucia.nombre} es mayor: {lucia.es_mayor}")    # True (en el original daba False)

# --- Objetos que se relacionan con otros objetos --------------------------
elias.agregar_amigo(martin)
elias.agregar_amigo(lucia)
elias.agregar_amigo(martin)      # repetido: no se agrega
print(f"Amigos de {elias.nombre}: {len(elias.amigos)}")
for amigo in elias.amigos:
    print(f"  - {amigo}")

# --- Cada objeto tiene sus propios datos --------------------------------
print(f"Amigos de {martin.nombre}: {len(martin.amigos)}")   # 0: lista propia

# --- La validación del constructor -------------------------------------
try:
    fantasma = Persona("Fantasma", -3, "Ninguna")
except ValueError as error:
    print(f"No se pudo crear la persona: {error}")

# =====================================================================
# PARA PRACTICAR -> ver 10_1_objetos.py
# =====================================================================
