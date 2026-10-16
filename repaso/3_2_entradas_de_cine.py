# =====================================================================
# REPASO 3.2 - Entradas de cine (condicionales anidados y operadores lógicos)
# Archivo original: clase1/3_2_entradas_de_cine.py
# =====================================================================
#
# CONCEPTOS
# ---------
# - CONDICIONALES ANIDADOS: un if dentro de otro if. Útiles, pero más de
#   2 niveles se vuelve difícil de leer.
# - OPERADORES LÓGICOS (tablas de verdad):
#
#     and                       or                        not
#     True  and True  -> True   True  or True  -> True    not True  -> False
#     True  and False -> False  True  or False -> True    not False -> True
#     False and False -> False  False or False -> False
#
#   (En el original la tabla del "or" decía "True and True": es un error
#   de tipeo, son "or".)
#
# - El operador "in" con una tupla reemplaza varios "or":
#     pelicula == 1 or pelicula == 2   ->   pelicula in (1, 2)
#
# - ORDEN EN UNA CADENA if/elif: se evalúan de arriba hacia abajo y entra
#   en la PRIMERA que sea True. Por eso los rangos de edad se ordenan de
#   menor a mayor usando "<".
#
# ERRORES QUE ENCONTRAMOS EN LA VERSIÓN DE CLASE
# ----------------------------------------------
# 1. LÍMITE MAL PUESTO (error "off-by-one"):
#      if edad_usuario <= EDAD_MINIMA_PARA_PELICULAS_ADULTOS:   # 18
#    Con <=, alguien de 18 años (que ya es mayor) tiene que pedir
#    autorización. Debe ser  < 18.
# 2. LOS 59 AÑOS PAGAN COMO JUBILADO:
#      elif edad_usuario < BOLETO_GENERAL_EDAD:   # 59
#    Una persona de 59 no entra en "< 59" y cae en el else (jubilados),
#    aunque la constante dice que jubilado es desde los 60. El límite
#    correcto es  < BOLETO_JUBILADOS_EDAD  (60). Tener DOS constantes para
#    el mismo límite (59 y 60) es justamente lo que produjo el error:
#    mejor una sola.
# 3. La edad negativa se valida DESPUÉS de preguntar por la autorización:
#    alguien con edad -5 pasa por el control de mayores. Las validaciones
#    van PRIMERO.
# 4. No se valida el número de película: si escriben 7, el programa sigue
#    como si nada. Hay que rechazarlo.
# 5. La variable pelicula_tiene_condicion_a_mayores se asigna pero nunca
#    se usa: sobra o hay que usarla.
# 6. exit(1) funciona en la consola pero no siempre en otros entornos. La
#    forma correcta en un script es  import sys  y  sys.exit(1).
#    El 1 indica "terminó con error"; 0 es "terminó bien".
# 7. Las películas para mayores se repiten como números sueltos (1 y 2).
#    Guardarlas en una constante deja la regla en un solo lugar.
# =====================================================================

import sys

# --- Constantes: precios y límites de edad ----------------------------
# Cada rango se define por su edad TOPE (sin incluirla).
EDAD_TOPE_GRATUITO = 3      # 0 a 2 años
EDAD_TOPE_INFANTIL = 12     # 3 a 11 años
EDAD_JUBILADOS = 60         # 60 o más

PRECIO_GRATUITO = 0
PRECIO_INFANTIL = 2000
PRECIO_GENERAL = 5000
PRECIO_JUBILADOS = 2500

EDAD_MINIMA_PELICULAS_ADULTOS = 18
PELICULAS_PARA_MAYORES = (1, 2)   # tupla: una lista que no se modifica

# --- Entrada ----------------------------------------------------------
print("Seleccioná tu película:")
print("1. The Amazing Spider-Man   (+18)")
print("2. Spider-Man: No Way Home  (+18)")
print("3. Terminator")

nombre = input("¿Cuál es tu nombre? ")
edad_usuario = int(input(f"{nombre}, ¿cuál es tu edad? "))

# Validación 1: edad posible. Va ANTES de cualquier otra lógica.
if edad_usuario < 0 or edad_usuario > 120:
    print("Por favor, ingresá una edad válida.")
    sys.exit(1)

pelicula_a_mirar = int(input("¿Qué película querés mirar? Enviá el número: "))

# Validación 2: película existente.
if pelicula_a_mirar not in (1, 2, 3):
    print("Esa película no está en cartelera.")
    sys.exit(1)

# --- Proceso: control de edad para películas +18 ----------------------
es_para_mayores = pelicula_a_mirar in PELICULAS_PARA_MAYORES
es_menor = edad_usuario < EDAD_MINIMA_PELICULAS_ADULTOS   # < y no <=

if es_para_mayores and es_menor:
    print("Esta película es para mayores de 18.")
    respuesta = input("¿Tenés autorización o venís con tus padres? (s/n) ")
    # .strip() saca espacios y .lower() pasa a minúsculas:
    # así "S", " s " y "s" valen lo mismo.
    if respuesta.strip().lower() != "s":
        print("La película no es apta para vos. Elegí otra.")
        sys.exit(1)
    print("Perfecto, calculando precio...")

# --- Proceso: precio según edad ---------------------------------------
# Ordenado de menor a mayor: cada elif solo se evalúa si el anterior
# fue False, por eso no hace falta repetir el límite inferior.
if edad_usuario < EDAD_TOPE_GRATUITO:
    precio = PRECIO_GRATUITO
elif edad_usuario < EDAD_TOPE_INFANTIL:
    precio = PRECIO_INFANTIL
elif edad_usuario < EDAD_JUBILADOS:
    precio = PRECIO_GENERAL
else:
    precio = PRECIO_JUBILADOS

# --- Salida -----------------------------------------------------------
# Calculamos el precio en los if y lo imprimimos UNA vez: si cambia el
# mensaje, se cambia en un solo lugar.
print(f"{nombre}, el precio de tu entrada es: ${precio}")

# --- not: repaso rápido -----------------------------------------------
# valor = True
# not valor        -> False
# not not valor    -> True
# not edad > 15    -> se evalúa como not (edad > 15)

# =====================================================================
# PARA PRACTICAR
# ---------------
# 1. Agregá un "día del espectador" (miércoles): todas las entradas al
#    50%. Preguntá si hoy es miércoles (s/n).
# 2. Probá el programa con estas edades y verificá cada precio:
#    0, 2, 3, 11, 12, 17, 18, 59, 60. ¿Coincide con lo que esperabas?
#    (Probar justo los LÍMITES es la forma de encontrar errores como los
#    de la versión original.)
# 3. Permití comprar varias entradas y mostrá el total.
# =====================================================================
