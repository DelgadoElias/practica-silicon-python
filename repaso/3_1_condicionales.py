# =====================================================================
# REPASO 3.1 - Condicionales: if / elif / else
# Archivo original: clase1/3_1_condicionales.py
# =====================================================================
#
# CONCEPTOS
# ---------
# Un condicional ejecuta un bloque de código SOLO si una condición es
# verdadera (True).
#
#     if CONDICION:
#         # bloque verdadero (con sangría de 4 espacios)
#     elif OTRA_CONDICION:
#         # se evalúa solo si la anterior fue False
#     else:
#         # se ejecuta si ninguna anterior fue True
#     # código normal: se ejecuta siempre
#
# - Los dos puntos (:) al final del if son obligatorios.
# - La SANGRÍA (indentación) es lo que le dice a Python qué líneas están
#   "adentro" del if. En otros lenguajes se usan llaves { }; en Python
#   se usan espacios. El estándar es 4 espacios.
# - Solo se ejecuta UNO de los bloques de una cadena if/elif/else: el
#   primero cuya condición sea True.
#
# EL OPERADOR % (resto) PARA PARES E IMPARES
#   n % 2 == 0  -> par    (dividir por 2 no deja resto)
#   n % 2 == 1  -> impar
#
# NOTAS / MEJORAS
# ---------------
# 1. Guardar la condición en una variable con nombre claro
#    (el_numero_es_par) es una muy buena práctica: el if se lee como una
#    oración en castellano. Lo mantenemos.
# 2. Nombres muy largos como numero_seleccionado_por_el_usuario cansan
#    al leer. "numero" alcanza cuando el contexto es claro.
# 3. En el código comentado del ejemplo de votar, el print("Podes votar")
#    quedó sin sangría: si se descomenta así, da IndentationError.
#    Cuidado al comentar/descomentar bloques.
# =====================================================================

numero = int(input("Elegí un número: "))

el_numero_es_par = numero % 2 == 0
print(f"el_numero_es_par es de tipo {type(el_numero_es_par)} y vale {el_numero_es_par}")

if el_numero_es_par:          # no hace falta escribir "== True"
    print("El número es par... ¡Yupi!")
else:
    print("El número es impar... Qué lástima")

# --- if / elif / else: varias opciones excluyentes --------------------
if numero > 0:
    print("Es positivo")
elif numero < 0:
    print("Es negativo")
else:
    print("Es cero")

# --- Condiciones combinadas -------------------------------------------
# and -> las dos tienen que ser True
# or  -> alcanza con que una sea True
# not -> invierte: not True -> False
if numero > 0 and el_numero_es_par:
    print("Es positivo Y par")

# Python permite encadenar comparaciones (otros lenguajes no):
if 1 <= numero <= 10:          # equivale a: numero >= 1 and numero <= 10
    print("Está entre 1 y 10")

# --- Operador ternario: un if/else en una sola línea -------------------
# valor_si_true if condicion else valor_si_false
paridad = "par" if el_numero_es_par else "impar"
print(f"Resumen: {numero} es {paridad}")

# --- Ejemplo de la clase: votar (arreglado y descomentado) ------------
EDAD_MINIMA_PARA_VOTAR = 16   # en Argentina se vota desde los 16

edad = int(input("¿Qué edad tenés? "))
if edad >= EDAD_MINIMA_PARA_VOTAR:
    print("Podés votar")
else:
    print("Todavía no podés votar")
print("Proceso finalizado.")   # BLOQUE NORMAL: se ejecuta siempre

# =====================================================================
# PARA PRACTICAR
# ---------------
# 1. Pedí una nota del 1 al 10 y mostrá: "Desaprobado" (1-5),
#    "Aprobado" (6-7), "Muy bien" (8-9), "Excelente" (10). Si está fuera
#    de rango, mostrá "Nota inválida".
# 2. Pedí un año y decí si es bisiesto: es divisible por 4 y no por 100,
#    o es divisible por 400.
# 3. Pedí tres números y mostrá el mayor (sin usar max()).
# =====================================================================
