

def calcular_base_exponencial(numero_base, exponente=2):
    return numero_base ** exponente

print(calcular_base_exponencial(10))
print(calcular_base_exponencial(8))

def pedir_pizza(gusto = "Muzzarella", tamanio = "mediana", cantidad = 1):
    plural = lambda palabra, cantidad:  palabra + "s" if cantidad > 1 else palabra
    suma_multiplicacion = lambda valor, valor2, comando: valor + valor if comando == "sumar" else valor * valor2 
    if cantidad > 1:
        palabra = "pizzas"

    return f"{cantidad} {palabra} {tamanio} de {gusto}"


print(pedir_pizza("Muzzarella", "medianas", 4))

#########print(pedir_pizza())


# *args


def sumatoria(*numeros):
    x = 0
    print(f"Tupla :{numeros}")
    for num in numeros:
        x += num
    return x

print(sumatoria())
print(sumatoria(2,3,4,7,12,48))

def crear_perfil(**datos):
    print(datos)
    for campo, valor in datos.items():
        print(f"Campo: {campo} ------ Valor: {valor}")

plural = lambda x: x
plural(10)


calcular_base_exponencial = lambda x: x ** 2 

calcular_base_exponencial(10)

suma_multiplicacion = lambda valor, valor2, comando: valor + valor if comando == "sumar" else valor * valor2
plural = lambda palabra, cantidad: palabra + "s" if cantidad > 1 else palabra
 
crear_perfil(nombre="Elias",apellido="Delgado")
