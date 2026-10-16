# =====================================================================
# REPASO 4.1 - Bucles: while, for, range, break y continue
# Archivo original: clase1/4_1_bucles_en_python.py
# =====================================================================
#
# CONCEPTOS
# ---------
# Un BUCLE repite un bloque de código. Cada repetición es una
# "vuelta" o ITERACIÓN.
#
# while CONDICION:
#     - Repite MIENTRAS la condición sea True.
#     - Se usa cuando NO sabemos de antemano cuántas vueltas hay
#       (ej: "pedí datos hasta que escriba salir").
#     - Si la condición nunca se vuelve False -> BUCLE INFINITO.
#
# for variable in secuencia:
#     - Recorre los elementos de una secuencia uno por uno.
#     - Se usa cuando SÍ sabemos cuántas vueltas hay, o queremos recorrer
#       una colección (lista, string, diccionario...).
#
# range(): genera una secuencia de números
#     range(5)         -> 0, 1, 2, 3, 4        (el 5 NO se incluye)
#     range(2, 6)      -> 2, 3, 4, 5           (desde, hasta sin incluir)
#     range(0, 10, 2)  -> 0, 2, 4, 6, 8        (desde, hasta, paso)
#     range(5, 0, -1)  -> 5, 4, 3, 2, 1        (paso negativo: cuenta atrás)
#
# break    -> CORTA el bucle por completo y sigue después de él.
# continue -> SALTA el resto de ESTA vuelta y pasa a la siguiente.
#
# Ojo: break y continue afectan solo al bucle MÁS CERCANO. En un for
# anidado, un break adentro corta el bucle de adentro, no el de afuera.
#
# NOTAS / MEJORAS RESPECTO A LA VERSIÓN DE CLASE
# ----------------------------------------------
# 1. SANGRÍA DE 3 ESPACIOS: el original mezcla 3 espacios (en el for) y
#    8 (en el if). Python lo acepta porque cada bloque es consistente
#    consigo mismo, pero el estándar (PEP 8) es SIEMPRE 4 espacios. La
#    mezcla es la causa número uno de IndentationError. Configurá el
#    editor para que la tecla Tab inserte 4 espacios.
# 2. Se escribe IDENTACIÓN, pero la palabra correcta en castellano es
#    "sangría" o "indentación".
# 3. Al número 3 que se saltea le conviene un nombre: VUELTA_A_SALTEAR.
# =====================================================================

VUELTA_A_SALTEAR = 3

numero = int(input("Ingresá un número: "))
vueltas_por_cada_numero = int(input("Ingresá la cantidad de subvueltas: "))

print("----- FOR CON CONTINUE -----")
# La vuelta 3 se saltea, pero el bucle SIGUE con la 4, 5, ...
for vuelta in range(numero):
    if vuelta == VUELTA_A_SALTEAR:
        continue
    print(f"CONTINUE - Vuelta {vuelta}")
    for subvuelta in range(vueltas_por_cada_numero):
        print(f"    subvuelta {subvuelta} de la vuelta {vuelta}")

print("----- FOR CON BREAK -----")
# Al llegar a la vuelta 3 el bucle se CORTA: no hay vuelta 3, 4, 5...
for vuelta in range(numero):
    if vuelta == VUELTA_A_SALTEAR:
        break
    print(f"BREAK - Vuelta {vuelta}")
    for subvuelta in range(vueltas_por_cada_numero):
        print(f"    subvuelta {subvuelta} de la vuelta {vuelta}")

print("----- WHILE CON CONTADOR -----")
# Equivale a  for i in range(3). Si te olvidás del  i += 1  es infinito.
i = 0
while i < 3:
    print(f"while - vuelta {i}")
    i += 1          # i = i + 1

print("----- WHILE TRUE CON SALIDA -----")
# El patrón de la clase (consola de comandos) con una salida explícita.
# while True es infinito A PROPÓSITO, y el break es la única salida.
while True:
    comando = input("Escribí un comando ('salir' para terminar) >>> ")
    if comando == "salir":
        break
    print(f"Tu comando es: {comando}")

print("----- for ... else -----")
# Poco conocido: el else de un for se ejecuta si el bucle terminó SIN
# break. Sirve para búsquedas: "recorrí todo y no lo encontré".
for vuelta in range(numero):
    if vuelta == 7:
        print("Encontré el 7, corto.")
        break
else:
    print("Recorrí todo el rango y nunca apareció el 7.")

print("Terminó el ciclo")

# =====================================================================
# PARA PRACTICAR
# ---------------
# 1. Imprimí la tabla de multiplicar de un número del 1 al 10.
# 2. Con for y range, imprimí los números pares del 0 al 20 de dos formas:
#    con range(0, 21, 2) y con un if + %.
# 3. Con dos for anidados, imprimí este triángulo:
#        *
#        **
#        ***
#        ****
# 4. Pedí números hasta que escriban 0 y mostrá la suma total.
# =====================================================================
