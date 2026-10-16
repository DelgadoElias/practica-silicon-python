# =====================================================================
# REPASO 8.2 - Recursión
# Archivo original: clase1/8_2_recursion.py
# =====================================================================
#
# CONCEPTOS
# ---------
# Una función RECURSIVA es una función que se llama a sí misma.
# Toda recursión necesita DOS partes:
#   1. CASO BASE: la condición en la que la función NO se vuelve a llamar
#      y termina. Sin caso base, se llama para siempre.
#   2. CASO RECURSIVO: se llama a sí misma con un problema MÁS CHICO,
#      que se ACERCA al caso base.
#
# Cada llamada queda "esperando" en la PILA DE LLAMADAS (call stack).
# Python limita esa pila a unas 1000 llamadas; si se pasa, lanza
# RecursionError: maximum recursion depth exceeded.
#
# ¿CUÁNDO USARLA?
#   - Problemas que tienen estructura de árbol o anidada: carpetas
#     dentro de carpetas, comentarios con respuestas, un JSON con
#     diccionarios dentro de diccionarios.
#   - Para contar o repetir algo simple, un for/while es más claro y no
#     tiene límite de profundidad.
#
# ERROR QUE ENCONTRAMOS EN LA VERSIÓN DE CLASE
# --------------------------------------------
# cuenta_regresiva(-10)  NUNCA LLEGA AL CASO BASE:
#   el caso base es  numero == 0, pero arrancando en -10 la función va a
#   -11, -12, -13... y nunca pasa por 0. Resultado: RecursionError
#   después de ~1000 llamadas.
#   Arreglo: usar  numero <= 0  como caso base, que cubre al 0 y a
#   cualquier negativo. Regla general: el caso base tiene que atrapar
#   TODOS los valores donde hay que parar, no uno solo.
# =====================================================================

def cuenta_regresiva(numero):
    if numero <= 0:                    # CASO BASE: <= y no ==
        print("¡Despegue!")
    else:                              # CASO RECURSIVO
        print(numero)
        cuenta_regresiva(numero - 1)   # problema más chico: se acerca a 0

cuenta_regresiva(5)
cuenta_regresiva(-10)                  # ahora termina enseguida

# La misma cuenta regresiva con un bucle (más simple para este caso):
for numero in range(5, 0, -1):
    print(numero)
print("¡Despegue!")


# --- Recursión que DEVUELVE un valor -----------------------------------
# Factorial: 5! = 5 * 4 * 3 * 2 * 1 = 120
#   factorial(5) = 5 * factorial(4)
#                    = 4 * factorial(3)
#                        = 3 * factorial(2)
#                            = 2 * factorial(1)
#                                = 1                  <- caso base
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(f"5! = {factorial(5)}")          # 120


# --- Sumar los dígitos de un número ------------------------------------
# 1234 -> 1 + 2 + 3 + 4 = 10
#   n % 10  da el último dígito  (1234 % 10 = 4)
#   n // 10 saca el último dígito (1234 // 10 = 123)
def sumar_digitos(n):
    if n < 10:
        return n
    return n % 10 + sumar_digitos(n // 10)

print(f"Suma de dígitos de 1234: {sumar_digitos(1234)}")   # 10


# --- Donde la recursión SÍ brilla: estructuras anidadas ----------------
# Contar cuántos archivos hay en una "carpeta" con subcarpetas. Las
# carpetas son diccionarios y los archivos, strings.
proyecto = {
    "main.py": "archivo",
    "README.md": "archivo",
    "app": {
        "rutas.py": "archivo",
        "modelos": {
            "usuario.py": "archivo",
            "pago.py": "archivo",
        },
    },
}

def contar_archivos(carpeta):
    total = 0
    for contenido in carpeta.values():
        if isinstance(contenido, dict):        # ¿es una subcarpeta?
            total += contar_archivos(contenido)   # recursión
        else:
            total += 1
    return total

print(f"Archivos en el proyecto: {contar_archivos(proyecto)}")   # 5
# Con un for común esto es difícil, porque no sabemos de antemano
# cuántos niveles de subcarpetas hay.

# =====================================================================
# PARA PRACTICAR
# ---------------
# 1. potencia(base, exp) recursiva: base ** exp = base * base ** (exp - 1)
# 2. invertir(texto) recursiva: "hola" -> "aloh"
#    Pista: texto[-1] + invertir(texto[:-1])
# 3. fibonacci(n): 0, 1, 1, 2, 3, 5, 8, 13...  fib(n) = fib(n-1) + fib(n-2)
#    Probá fibonacci(35): ¿por qué tarda tanto? (Se recalculan los mismos
#    valores miles de veces. Investigá "memoización".)
# =====================================================================
