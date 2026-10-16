# =====================================================================
# REPASO 8.1 - Funciones avanzadas: valores por defecto, *args, **kwargs
#              y lambda
# Archivo original: clase1/8_1_funciones_avanzadas.py
# =====================================================================
#
# CONCEPTOS
# ---------
# PARÁMETROS CON VALOR POR DEFECTO
#     def potencia(base, exponente=2):
#   Si no pasás el exponente, vale 2. Los parámetros con defecto van
#   SIEMPRE después de los que no tienen: def f(a=1, b) es SyntaxError.
#
# *args -> cantidad VARIABLE de argumentos POSICIONALES
#     def sumatoria(*numeros):   sumatoria(1, 2, 3)  -> numeros = (1, 2, 3)
#   Llegan como TUPLA. El nombre "args" es una convención; lo que importa
#   es el asterisco.
#
# **kwargs -> cantidad VARIABLE de argumentos POR NOMBRE
#     def crear_perfil(**datos):  crear_perfil(nombre="Elias")
#                                 -> datos = {"nombre": "Elias"}
#   Llegan como DICCIONARIO.
#
# ORDEN cuando se combinan:
#     def f(obligatorio, con_defecto=1, *args, **kwargs):
#
# LAMBDA -> función anónima de UNA sola expresión
#     cuadrado = lambda x: x ** 2      equivale a   def cuadrado(x):
#                                                       return x ** 2
#   Su lugar natural es pasarla como argumento a otra función, por
#   ejemplo key= en sorted() o max(). Para ponerle nombre, PEP 8
#   recomienda usar def (se lee mejor y el error muestra el nombre).
#
# ERRORES QUE ENCONTRAMOS EN LA VERSIÓN DE CLASE
# ----------------------------------------------
# 1. pedir_pizza() SE ROMPE CON 1 PIZZA:
#        if cantidad > 1:
#            palabra = "pizzas"
#        return f"{cantidad} {palabra} ..."
#    Si cantidad es 1, "palabra" nunca se crea y Python lanza
#    UnboundLocalError. Por eso  print(pedir_pizza())  estaba comentado.
#    Una variable tiene que tener valor en TODOS los caminos del código.
# 2. La lambda "plural" se define adentro de pedir_pizza pero no se usa:
#    era justo lo que resolvía el punto 1.
# 3. suma_multiplicacion hace  valor + valor  en vez de  valor + valor2:
#    sumar(3, 5) da 6 en vez de 8.
# 4. calcular_base_exponencial = lambda x: x ** 2  PISA la función que se
#    definió arriba con def: desde esa línea, la versión con exponente
#    deja de existir. En Python las funciones son valores y un nombre
#    puede reasignarse; por eso hay que tener cuidado al reutilizar
#    nombres.
# 5. Varias lambdas se calculan sin usar el resultado:
#    plural(10)  o  calcular_base_exponencial(10)  solos no muestran nada.
# 6. pedir_pizza("Muzzarella", "medianas", 4) pasa el plural ya hecho en
#    el tamaño. Si la función pluraliza, conviene pasar "mediana".
# 7. En sumatoria, "x" no dice qué guarda; "total" sí. Y Python ya trae
#    sum().
# =====================================================================

# --- Valores por defecto ----------------------------------------------
def calcular_potencia(base, exponente=2):
    return base ** exponente

print(calcular_potencia(10))          # 100  (usa exponente=2)
print(calcular_potencia(2, 10))       # 1024
print(calcular_potencia(exponente=3, base=2))   # 8, por nombre

# --- pedir_pizza arreglada --------------------------------------------
def pluralizar(palabra, cantidad):
    return palabra + "s" if cantidad > 1 else palabra

def pedir_pizza(gusto="muzzarella", tamanio="mediana", cantidad=1):
    # Las dos palabras se calculan SIEMPRE, no solo dentro de un if.
    pizza = pluralizar("pizza", cantidad)
    tamanio = pluralizar(tamanio, cantidad)
    return f"{cantidad} {pizza} {tamanio} de {gusto}"

print(pedir_pizza())                              # 1 pizza mediana de muzzarella
print(pedir_pizza("napolitana", "grande", 4))     # 4 pizzas grandes de napolitana
print(pedir_pizza(cantidad=2))                    # solo cambio la cantidad

# --- TRAMPA CLÁSICA: lista como valor por defecto --------------------
# El valor por defecto se crea UNA sola vez, al definir la función.
def agregar_mal(item, lista=[]):
    lista.append(item)
    return lista

print(agregar_mal("a"))    # ['a']
print(agregar_mal("b"))    # ['a', 'b']  <- ¡arrastra el valor anterior!

def agregar_bien(item, lista=None):
    if lista is None:      # creamos una lista nueva en cada llamada
        lista = []
    lista.append(item)
    return lista

print(agregar_bien("a"))   # ['a']
print(agregar_bien("b"))   # ['b']

# --- *args --------------------------------------------------------------
def sumatoria(*numeros):
    print(f"  llegó la tupla: {numeros}")
    total = 0
    for numero in numeros:
        total += numero
    return total               # equivalente a: return sum(numeros)

print(sumatoria())                       # 0
print(sumatoria(2, 3, 4, 7, 12, 48))     # 76

# El * también DESEMPAQUETA una lista al llamar:
valores = [1, 2, 3]
print(sumatoria(*valores))               # igual que sumatoria(1, 2, 3)

# --- **kwargs -------------------------------------------------------------
def crear_perfil(nombre, **datos_extra):
    perfil = {"nombre": nombre}
    perfil.update(datos_extra)   # agrega todos los pares del otro diccionario
    return perfil

print(crear_perfil("Elias", apellido="Delgado", ciudad="Posadas"))

for campo, valor in crear_perfil("Paula", edad=22).items():
    print(f"  {campo}: {valor}")

# El ** también desempaqueta un diccionario al llamar:
datos = {"apellido": "Gómez", "edad": 30}
print(crear_perfil("Martina", **datos))

# --- lambda: dónde SÍ tiene sentido -----------------------------------
productos = [("tostado", 2500), ("cafe", 1200), ("jugo", 1800)]

# Ordenar por precio: key recibe una función que dice "por qué ordenar".
print(sorted(productos, key=lambda producto: producto[1]))

# El más caro:
print(max(productos, key=lambda producto: producto[1]))

# suma_multiplicacion arreglada (valor + valor2):
def sumar_o_multiplicar(valor, valor2, comando):
    return valor + valor2 if comando == "sumar" else valor * valor2

print(sumar_o_multiplicar(3, 5, "sumar"))        # 8
print(sumar_o_multiplicar(3, 5, "multiplicar"))  # 15

# =====================================================================
# PARA PRACTICAR
# ---------------
# 1. promedio(*notas) que funcione con cualquier cantidad de notas y
#    devuelva 0 si no recibe ninguna.
# 2. armar_url(base, **parametros) que devuelva por ejemplo
#    "https://api.com/buscar?q=python&pagina=2"
#    Pista: "&".join(f"{k}={v}" for k, v in parametros.items())
# 3. Ordená la lista de alumnos del repaso 6.1 por edad usando sorted()
#    y una lambda.
# =====================================================================
