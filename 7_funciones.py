# Funciones

numero = 2 # Contexto GLOBAL


def calcular_iva(precio):
    if precio > 15000:
        return "Hola"
    else:
        return precio * 1.21

# Definir una funcion y lo que hace EN EL CASO DE QUE LA INVOQUE
def saludar():
    # EN LA IDENTACION, VOY A ESCRIBIR TODO EL CODIGO DE LA FUNCION
    print("Hola mundo")


def saludar_a_una_persona(nombre_de_la_persona, apellido, documento):
    nombre = nombre_de_la_persona # Contexto LOCAL / De funcion
    print("Iniciando protocolo de saludo:")
    print(f"Hola, {nombre_de_la_persona}")
    print("Fin de protocolo de saludo:")


# Como invoco una funcion?
# saludar_a_una_persona(nombre_de_la_persona="Delgado", documento="00-00000000-0", apellido="Delgado")

# saludar_a_una_persona("Elias","Delgado","documento")

def celsius_a_farenheit(temperatura_en_celsius):
    return temperatura_en_celsius * 9 / 5 + 32

print(f"La temperatura en celsius es 100. En Farenheit es: {celsius_a_farenheit(100)}")
print(f"La temperatura en celsius es 100. En Farenheit es: {celsius_a_farenheit(30)}")


entero = 200

def sumar_entero():
    entero_dos = 300
    entero = 50 
    print(f"Sumar entero es: {entero_dos}")
    print(f"Sumar entero es: {entero}")
    entero += 100
    print(f"Sumar entero es: {entero}")
    return entero_dos

entero_salido_de_la_funcion = sumar_entero()
print(f"Sumar entero es: {entero}") # Este print, segun el contexto, da 200 o 300?
 
