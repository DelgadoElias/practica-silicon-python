# =====================================================================
# REPASO 7 - Funciones y alcance de variables (scope)
# Archivo original: clase1/7_funciones.py
# =====================================================================
#
# CONCEPTOS
# ---------
# Una FUNCIÓN es un bloque de código con nombre que se escribe UNA vez
# y se usa (se "invoca" o "llama") todas las veces que haga falta.
#
#     def nombre_de_la_funcion(parametro1, parametro2):
#         # cuerpo con sangría
#         return resultado
#
# - def solo DEFINE la función: no ejecuta nada. Se ejecuta cuando la
#   llamás: nombre_de_la_funcion(3, 4)
# - PARÁMETRO: el nombre en la definición (precio).
#   ARGUMENTO: el valor real que pasás al llamarla (15000).
# - ARGUMENTOS POSICIONALES: se asignan por orden  f("Elias", "Delgado")
#   ARGUMENTOS POR NOMBRE (keyword): f(apellido="Delgado", nombre="Elias")
#   -> con nombre, el orden no importa y se lee mejor.
#
# return vs print
#   - print() MUESTRA algo en pantalla y la función devuelve None.
#   - return DEVUELVE un valor a quien llamó la función, que lo puede
#     guardar en una variable, usar en una cuenta, etc.
#   - Una función de cálculo debería hacer return, no print: así sirve
#     para mostrar, guardar en una base de datos o mandar en una API.
#   - return TERMINA la función: lo que está debajo no se ejecuta.
#
# ALCANCE (SCOPE)
#   - GLOBAL: variables creadas fuera de cualquier función.
#   - LOCAL: variables creadas DENTRO de una función. Nacen cuando la
#     función se ejecuta y desaparecen cuando termina.
#   - Si dentro de una función asignás una variable con el mismo nombre
#     que una global, se crea una LOCAL nueva que "tapa" a la global.
#     La global NO cambia.
#   - La palabra clave global permite modificar la global desde adentro,
#     pero se evita: hace que el código sea difícil de seguir. Mejor
#     pasar valores por parámetro y devolverlos con return.
#
# ERRORES QUE ENCONTRAMOS EN LA VERSIÓN DE CLASE
# ----------------------------------------------
# 1. calcular_iva() devuelve "Hola" (un str) si el precio supera 15000, y
#    un número si no. Una función debería devolver SIEMPRE EL MISMO TIPO:
#    quien la usa va a hacer cuentas con el resultado y "Hola" * 2 no es
#    lo que espera. Si un caso es inválido, se lanza un error (clase 9).
# 2. El 1.21 es un número mágico: va en una constante IVA = 0.21.
# 3. saludar_a_una_persona() recibe apellido y documento y no los usa, y
#    crea "nombre" sin usarlo. Los parámetros que no se usan confunden.
# 4. El segundo print dice "La temperatura en celsius es 100" pero le pasa
#    30. Otra vez: mensaje y código tienen que coincidir. Usar la misma
#    variable en el texto y en la llamada lo evita.
# 5. Farenheit se escribe Fahrenheit.
# 6. LA PREGUNTA DE LA CLASE: "¿este print da 200 o 300?". Da 200: el
#    "entero = 50" de adentro crea una variable LOCAL. La global entero
#    sigue valiendo 200. (300 era entero_dos, que es local y devuelta.)
# =====================================================================

# --- Constantes -------------------------------------------------------
IVA = 0.21

# --- Funciones bien definidas -----------------------------------------
def calcular_precio_con_iva(precio):
    """Devuelve el precio con IVA incluido."""
    # Lo de arriba entre triple comilla es un DOCSTRING: la documentación
    # de la función. Se ve con help(calcular_precio_con_iva).
    return round(precio * (1 + IVA), 2)


def saludar():
    print("Hola mundo")      # esta función solo muestra: no devuelve nada


def armar_saludo(nombre, apellido):
    """Devuelve el saludo como texto; quien llama decide qué hacer."""
    return f"Hola, {nombre} {apellido}"


def celsius_a_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


# --- Uso ---------------------------------------------------------------
saludar()

print(calcular_precio_con_iva(1000))     # 1210.0
print(calcular_precio_con_iva(20000))    # 24200.0 (mismo tipo SIEMPRE)

# Argumentos posicionales y por nombre:
print(armar_saludo("Elias", "Delgado"))
print(armar_saludo(apellido="Delgado", nombre="Elias"))   # mismo resultado

# Mensaje y llamada usan la MISMA variable: no pueden contradecirse.
for temperatura in (0, 30, 100):
    print(f"{temperatura} °C son {celsius_a_fahrenheit(temperatura)} °F")

# --- return vs print -----------------------------------------------------
resultado = saludar()            # imprime, pero...
print(f"saludar() devolvió: {resultado}")    # None: no tiene return

texto = armar_saludo("Paula", "Gómez")       # no imprime nada todavía
print(texto.upper())                         # podemos usar el valor devuelto

# --- Scope: la pregunta de la clase ----------------------------------
entero = 200                     # GLOBAL

def sumar_entero():
    entero_dos = 300             # LOCAL
    entero = 50                  # LOCAL nueva: tapa a la global, no la cambia
    entero += 100                # la local pasa a 150
    print(f"  adentro: entero = {entero}, entero_dos = {entero_dos}")
    return entero_dos

entero_salido_de_la_funcion = sumar_entero()
print(f"afuera: entero = {entero}")          # 200: la global no cambió
print(f"afuera: devuelto = {entero_salido_de_la_funcion}")   # 300
# print(entero_dos)   # NameError: entero_dos solo existe dentro de la función

# Si REALMENTE hay que cambiar la global (evitarlo cuando se pueda):
contador = 0

def incrementar_contador():
    global contador
    contador += 1

incrementar_contador()
incrementar_contador()
print(f"contador global = {contador}")      # 2

# La forma recomendada: entra por parámetro, sale por return.
def incrementar(valor):
    return valor + 1

contador = incrementar(contador)
print(f"contador = {contador}")             # 3

# Error típico: leer una global y DESPUÉS asignarla en la misma función.
#     def romper():
#         print(contador)   # UnboundLocalError
#         contador = 10     # esta asignación hace que contador sea LOCAL
#                           # en TODA la función, incluso en la línea de arriba

# =====================================================================
# PARA PRACTICAR -> ver 7_1_ejercicios.py (con soluciones)
# =====================================================================
