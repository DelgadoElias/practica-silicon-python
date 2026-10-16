# =====================================================================
# REPASO 8.3 - Calculadora flexible
# Archivo original: clase1/8_3_calculadora_flexible.py (estaba vacío)
# =====================================================================
#
# OBJETIVO
# --------
# Integrar lo visto en la clase 8 en un solo programa:
#   - parámetros con valor por defecto
#   - *args (cualquier cantidad de números)
#   - **kwargs (opciones con nombre)
#   - lambdas guardadas en un DICCIONARIO de operaciones
#   - un menú con while True
#
# IDEA CLAVE: DICCIONARIO DE FUNCIONES
# ------------------------------------
# En Python las funciones son valores: se pueden guardar en variables,
# listas o diccionarios. En vez de un if/elif por operación:
#
#     if op == "+": ...
#     elif op == "-": ...
#     elif op == "*": ...
#
# guardamos  {"+": funcion_suma, "-": funcion_resta, ...}  y buscamos
# la función por su símbolo. Agregar una operación es agregar UNA línea
# al diccionario, sin tocar el resto del programa.
# =====================================================================

OPERACIONES = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b,
    "**": lambda a, b: a ** b,
    "%": lambda a, b: a % b,
}
# Acá la lambda SÍ tiene sentido: son funciones chiquitas que viven
# dentro de una estructura de datos, sin necesidad de un nombre propio.


def calcular(operador, *numeros, decimales=2):
    """Aplica el operador a todos los números, de izquierda a derecha.

    calcular("+", 1, 2, 3)  ->  (1 + 2) + 3  ->  6
    calcular("-", 10, 3, 2) ->  (10 - 3) - 2 ->  5

    decimales va DESPUÉS de *numeros, así que solo se puede pasar por
    nombre: calcular("/", 10, 3, decimales=4). Si fuera posicional, el
    4 se confundiría con un número más para operar.
    """
    if operador not in OPERACIONES:
        return None            # el operador no existe
    if len(numeros) == 0:
        return 0

    funcion = OPERACIONES[operador]
    resultado = numeros[0]
    for numero in numeros[1:]:             # del segundo en adelante
        if operador in ("/", "%") and numero == 0:
            return None                    # evitamos ZeroDivisionError
        resultado = funcion(resultado, numero)
    return round(resultado, decimales)


def mostrar(operador, *numeros, **opciones):
    """Imprime la cuenta completa. Las opciones con nombre (**opciones)
    se reenvían tal cual a calcular()."""
    resultado = calcular(operador, *numeros, **opciones)
    cuenta = f" {operador} ".join(str(n) for n in numeros)
    if resultado is None:
        print(f"{cuenta} = no se puede calcular")
    else:
        print(f"{cuenta} = {resultado}")


# --- Ejemplos -----------------------------------------------------------
mostrar("+", 1, 2, 3, 4)               # 1 + 2 + 3 + 4 = 10
mostrar("-", 100, 30, 20)              # 50
mostrar("*", 2, 3, 4)                  # 24
mostrar("/", 10, 3)                    # 3.33
mostrar("/", 10, 3, decimales=5)       # 3.33333
mostrar("/", 10, 0)                    # no se puede calcular
mostrar("**", 2, 10)                   # 1024
mostrar("?", 1, 2)                     # operador inexistente

# Las funciones del diccionario se pueden usar directamente:
print(OPERACIONES["*"](6, 7))          # 42


# --- Versión interactiva ----------------------------------------------
print()
print("CALCULADORA FLEXIBLE")
print(f"Operadores disponibles: {' '.join(OPERACIONES)}")
print("Escribí 'salir' para terminar.")

while True:
    operador = input("\nOperador: ").strip()
    if operador == "salir":
        break
    if operador not in OPERACIONES:
        print("Operador no válido.")
        continue

    texto = input("Números separados por espacio (ej: 10 5 2): ")
    # split() corta el texto por espacios: "10 5 2" -> ["10", "5", "2"]
    # Convertimos cada parte a float con una list comprehension.
    try:
        numeros = [float(parte) for parte in texto.split()]
    except ValueError:
        print("Tenés que escribir solo números.")
        continue
    # (try/except se ve en la clase 9: si float() falla, en vez de
    # romperse el programa, entra al except.)

    mostrar(operador, *numeros)        # el * desempaqueta la lista

print("¡Chau!")

# =====================================================================
# PARA PRACTICAR
# ---------------
# 1. Agregá la operación "//" (división entera) con una sola línea.
# 2. Agregá "promedio" como operación especial: no encaja en el
#    patrón (a, b), así que hay que resolverla aparte en calcular().
# 3. Guardá un historial de cuentas en una lista y mostrá las últimas 5
#    cuando la persona escriba "historial".
# =====================================================================
