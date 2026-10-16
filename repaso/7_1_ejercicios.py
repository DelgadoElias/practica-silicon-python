# =====================================================================
# REPASO 7.1 - Ejercicios de funciones (con soluciones)
# Archivo original: clase1/7_1_ejercicios.py (estaba vacío)
# =====================================================================
#
# CÓMO USAR ESTE ARCHIVO
# ----------------------
# 1. Leé el enunciado de cada ejercicio.
# 2. Intentá resolverlo SIN mirar la solución (tapala o escribilo en otro
#    archivo).
# 3. Ejecutá este archivo: al final, cada solución se prueba con assert.
#    Si cambiás una solución y rompés algo, el assert te avisa con
#    AssertionError en qué línea.
#
# RECORDATORIO: la receta para escribir una función
# -------------------------------------------------
#   a) ¿Qué RECIBE?  -> parámetros
#   b) ¿Qué DEVUELVE? -> return (y de qué tipo, siempre el mismo)
#   c) Un ejemplo concreto: es_par(4) -> True
#   d) Recién ahí, escribir el cuerpo.
# =====================================================================


# ---------------------------------------------------------------------
# EJERCICIO 1 - es_par
# Escribí una función que reciba un número entero y devuelva True si es
# par y False si es impar.
# ---------------------------------------------------------------------
def es_par(numero):
    return numero % 2 == 0
    # No hace falta un if/else: la comparación ya ES un bool.
    # Evitar:  if numero % 2 == 0: return True  else: return False


# ---------------------------------------------------------------------
# EJERCICIO 2 - mayor_de_tres
# Devolvé el mayor de tres números SIN usar max().
# ---------------------------------------------------------------------
def mayor_de_tres(a, b, c):
    mayor = a
    if b > mayor:
        mayor = b
    if c > mayor:
        mayor = c
    return mayor


# ---------------------------------------------------------------------
# EJERCICIO 3 - calcular_descuento
# Recibe un precio y un porcentaje de descuento (0 a 100) y devuelve el
# precio final redondeado a 2 decimales.
# ---------------------------------------------------------------------
def calcular_descuento(precio, porcentaje):
    return round(precio * (1 - porcentaje / 100), 2)


# ---------------------------------------------------------------------
# EJERCICIO 4 - contar_vocales
# Recibe un texto y devuelve cuántas vocales tiene (con o sin tilde,
# mayúsculas o minúsculas).
# ---------------------------------------------------------------------
def contar_vocales(texto):
    vocales = "aeiouáéíóú"
    cantidad = 0
    for letra in texto.lower():
        if letra in vocales:       # "in" también funciona con strings
            cantidad += 1
    return cantidad


# ---------------------------------------------------------------------
# EJERCICIO 5 - promedio
# Recibe una lista de números y devuelve el promedio. Si la lista está
# vacía, devuelve 0 (no tiene que romperse). Ver el error de la clase 5.3.
# ---------------------------------------------------------------------
def promedio(numeros):
    if not numeros:                # lista vacía -> False
        return 0
    return sum(numeros) / len(numeros)


# ---------------------------------------------------------------------
# EJERCICIO 6 - es_palindromo
# Devuelve True si el texto se lee igual al derecho y al revés,
# ignorando espacios y mayúsculas. "Neuquén" no (por la tilde),
# "Anita lava la tina" sí.
# ---------------------------------------------------------------------
def es_palindromo(texto):
    limpio = texto.replace(" ", "").lower()
    return limpio == limpio[::-1]   # [::-1] da vuelta el string


# ---------------------------------------------------------------------
# EJERCICIO 7 - filtrar_aprobados
# Recibe un diccionario {nombre: nota} y devuelve una LISTA con los
# nombres de quienes tienen 6 o más.
# ---------------------------------------------------------------------
NOTA_PARA_APROBAR = 6

def filtrar_aprobados(notas_por_alumno):
    aprobados = []
    for nombre, nota in notas_por_alumno.items():
        if nota >= NOTA_PARA_APROBAR:
            aprobados.append(nombre)
    return aprobados


# ---------------------------------------------------------------------
# EJERCICIO 8 - funciones que usan otras funciones
# Escribí precio_final(precio, porcentaje_descuento) que aplique el
# descuento (ejercicio 3) y DESPUÉS el IVA del 21%. Reutilizá la
# función del ejercicio 3: no copies el cálculo.
# ---------------------------------------------------------------------
IVA = 0.21

def precio_final(precio, porcentaje_descuento):
    con_descuento = calcular_descuento(precio, porcentaje_descuento)
    return round(con_descuento * (1 + IVA), 2)


# =====================================================================
# PRUEBAS - si todo está bien, al ejecutar se imprime solo el mensaje
# final. assert condicion  ->  si la condición es False, corta con error.
# Esto es la idea básica de los TESTS automáticos (más adelante: pytest).
# =====================================================================
assert es_par(4) is True
assert es_par(7) is False
assert es_par(0) is True

assert mayor_de_tres(1, 2, 3) == 3
assert mayor_de_tres(3, 2, 1) == 3
assert mayor_de_tres(-1, -5, -3) == -1
assert mayor_de_tres(2, 2, 1) == 2

assert calcular_descuento(1000, 10) == 900
assert calcular_descuento(1000, 0) == 1000
assert calcular_descuento(999.99, 15) == 849.99

assert contar_vocales("Hola Mundo") == 4
assert contar_vocales("Posadas, Misiones") == 7
assert contar_vocales("") == 0

assert promedio([6, 7, 8]) == 7
assert promedio([9, 10]) == 9.5
assert promedio([]) == 0

assert es_palindromo("Anita lava la tina") is True
assert es_palindromo("Python") is False

assert filtrar_aprobados({"Ana": 8, "Juan": 5, "Sol": 6}) == ["Ana", "Sol"]
assert filtrar_aprobados({}) == []

assert precio_final(1000, 10) == 1089.0

print("Todas las pruebas pasaron.")

# =====================================================================
# DESAFÍOS EXTRA (sin solución)
# ------------------------------
# 1. fizzbuzz(n): devuelve "Fizz" si n es múltiplo de 3, "Buzz" si es
#    de 5, "FizzBuzz" si es de ambos, y el número como str si no.
# 2. es_primo(n): True si n es primo. Escribí sus propios assert.
# 3. invertir_diccionario(d): {"a": 1, "b": 2} -> {1: "a", 2: "b"}
# =====================================================================
