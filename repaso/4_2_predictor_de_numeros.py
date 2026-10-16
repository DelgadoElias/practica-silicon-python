# =====================================================================
# REPASO 4.2 - Validar datos con while True + continue/break
#              y el "Detector de la mufa"
# Archivo original: clase1/4_2_predictor_de_numeros.py
# =====================================================================
#
# CONCEPTOS
# ---------
# PATRÓN DE VALIDACIÓN DE ENTRADA (lo vas a usar todo el tiempo):
#
#     while True:
#         dato = input(...)
#         if dato_es_invalido:
#             print("error")
#             continue      # vuelve a preguntar
#         break             # dato válido: salimos del bucle
#
# - continue -> "esta vuelta no sirve, preguntá de nuevo".
# - break    -> "ya tengo lo que necesito, salgo".
#
# ERRORES QUE ENCONTRAMOS EN LA VERSIÓN DE CLASE
# ----------------------------------------------
# 1. BUCLE SIN SALIDA: después de "Edad registrada" no hay break, así que
#    el programa vuelve a preguntar la edad para siempre. La única forma
#    de salir es Ctrl+C. Todo while True necesita al menos un break.
# 2. LÍMITES: "edad <= 0" rechaza a un bebé de 0 años. Según el caso,
#    conviene "edad < 0". Pensá siempre qué pasa justo en el límite.
# 3. Si escriben letras, int() lanza ValueError y el programa se rompe.
#    Con lo de la clase 9 (try/except) lo resolvemos (ver abajo).
# 4. El nombre del archivo ("predictor de números") no coincide con lo
#    que hace (validar una edad). Los nombres deberían describir el
#    contenido.
# =====================================================================

EDAD_MINIMA = 0
EDAD_MAXIMA = 120

# --- Versión 1: validación con continue y break -----------------------
while True:
    edad = int(input("Ingresá tu edad: "))
    if edad < EDAD_MINIMA or edad > EDAD_MAXIMA:
        print(f"Dato inválido: tiene que estar entre {EDAD_MINIMA} y {EDAD_MAXIMA}.")
        continue      # vuelve al principio del while
    break             # llegamos acá solo si la edad es válida

print(f"Edad registrada: {edad}")

# --- Versión 2 (adelanto de la clase 9): también rechaza letras --------
# .isdigit() devuelve True si el texto son solo dígitos: "25" -> True,
# "veinte" -> False, "-3" -> False. Así evitamos que int() se rompa.
while True:
    texto = input("Ingresá tu edad otra vez (probá escribir letras): ")
    if not texto.isdigit():
        print("Tenés que escribir un número entero.")
        continue
    edad = int(texto)
    if edad > EDAD_MAXIMA:
        print("Esa edad no parece real.")
        continue
    break

print(f"Edad registrada: {edad}")

# --- El juego del "Detector de la mufa" (estaba comentado) -------------
# Combina for + continue + break en un solo ejemplo.
print("Juego - Detector de la mufa")
for i in range(20):
    if i % 3 == 0:                    # múltiplo de 3 -> lo salteamos
        print(f"  {i} es múltiplo de 3, salteando...")
        continue
    if i == 13:                       # número de la mufa -> cortamos todo
        print("¡Número de la mufa! Me voy.")
        break
    print(f"El número es: {i}")
print("Se terminó el juego.")

# Pregunta para pensar: ¿por qué el 12 nunca se imprime como
# "El número es: 12"? ¿Y por qué el 15 nunca aparece?

# =====================================================================
# PARA PRACTICAR
# ---------------
# 1. "Adiviná el número": guardá un número secreto (ej: 7) y pedí intentos
#    hasta que lo adivinen. Decí "más alto" o "más bajo" en cada intento.
#    Limitá a 5 intentos.
#    Extra: usá  import random  y  random.randint(1, 100)  para que el
#    número sea al azar. (Ese sí sería un "predictor de números".)
# 2. Pedí una contraseña hasta que tenga al menos 8 caracteres
#    (len(texto) >= 8).
# =====================================================================
