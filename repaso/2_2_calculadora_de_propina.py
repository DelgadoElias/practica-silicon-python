# =====================================================================
# REPASO 2.2 - Calculadora de propina
# Archivo original: clase1/2_2_calculadora_de_propina.py
# =====================================================================
#
# CONCEPTOS
# ---------
# - Un programa casi siempre tiene 3 partes: ENTRADA (input), PROCESO
#   (cálculos) y SALIDA (print). Separarlas visualmente ayuda a leerlo.
# - Porcentajes: el 10% de un monto es  monto * 10 / 100  o  monto * 0.10
#
# NOTAS / MEJORAS RESPECTO A LA VERSIÓN DE CLASE
# ----------------------------------------------
# 1. NÚMEROS MÁGICOS: el 0.10 aparece "suelto" en el cálculo. Si mañana la
#    propina sugerida pasa al 15%, hay que buscarlo dentro del código.
#    Mejor ponerlo en una CONSTANTE arriba: PORCENTAJE_PROPINA = 10.
# 2. PLATA CON int(): con int(input(...)) un total de 12500.50 da error, y
#    con int(total * 0.10) se pierden los centavos (int() TRUNCA, no
#    redondea: int(9.99) -> 9). Para montos usamos float y round(x, 2).
#    (En sistemas de pagos reales se usa el módulo decimal, porque float
#    tiene errores chicos de precisión: 0.1 + 0.2 -> 0.30000000000000004.)
# 3. El total con propina no se mostraba: es lo que el cliente quiere
#    saber.
# 4. Formato de números: {valor:,.2f} muestra separador de miles y 2
#    decimales -> 12,500.50
# =====================================================================

# --- Constantes -------------------------------------------------------
PORCENTAJE_PROPINA = 10   # en %. Cambiar acá si cambia la política.

# --- Entrada ----------------------------------------------------------
nombre = input("¿Cuál es tu nombre? ")
numero_de_mesa = int(input("¿Cuál es tu número de mesa? "))
total_a_pagar = float(input(f"{nombre}, ¿cuál es el total de tu mesa? ARS $"))

# --- Proceso ----------------------------------------------------------
propina = round(total_a_pagar * PORCENTAJE_PROPINA / 100, 2)
total_con_propina = round(total_a_pagar + propina, 2)

# --- Salida -----------------------------------------------------------
print()
print(f"Mesa {numero_de_mesa} - {nombre}")
print(f"Consumo:                    ARS ${total_a_pagar:,.2f}")
print(f"Propina sugerida ({PORCENTAJE_PROPINA}%):     ARS ${propina:,.2f}")
print(f"Total con propina:          ARS ${total_con_propina:,.2f}")

# --- Para pensar: int() vs round() ------------------------------------
print()
print(f"int(9.99)      -> {int(9.99)}      (trunca: corta los decimales)")
print(f"round(9.99)    -> {round(9.99)}     (redondea al entero más cercano)")
print(f"round(9.987,2) -> {round(9.987, 2)}  (redondea a 2 decimales)")

# =====================================================================
# PARA PRACTICAR
# ---------------
# 1. Preguntá cuántas personas hay en la mesa y mostrá cuánto paga cada
#    una (total con propina dividido la cantidad de personas).
# 2. Ofrecé tres opciones de propina (10%, 15% y 20%) y mostrá las tres.
# 3. Después de ver condicionales (clase 3): si el total supera
#    ARS $50.000, sugerí 15% en vez de 10%.
# =====================================================================
