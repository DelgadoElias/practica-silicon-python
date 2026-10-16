# =====================================================================
# REPASO 2.1 - Variables, tipos de datos y operadores
# Archivo original: clase1/2_1_sobre-mi.py
# =====================================================================
#
# CONCEPTOS
# ---------
# VARIABLE: una "caja" con nombre donde guardamos un valor.
#     nombre_de_la_variable = valor
#   El = NO significa "igual" como en matemática: significa ASIGNAR
#   (guardá lo de la derecha en la caja de la izquierda).
#
# TIPOS DE DATOS BÁSICOS
#   str   -> texto            "Elias", 'Posadas', "25"
#   int   -> número entero     25, -3, 0
#   float -> número decimal    1.75, 3.0
#   bool  -> verdadero/falso   True, False   (con mayúscula inicial)
#   type(valor) nos dice de qué tipo es algo.
#
# CONVENCIONES DE NOMBRES (PEP 8, la guía de estilo oficial de Python)
#   snake_case       -> variables y funciones: mi_nombre, altura_de_casa
#   MAYUSCULAS       -> "constantes": valores que no deberían cambiar,
#                       por ejemplo MAX_INTENTOS = 3
#   Python no impide cambiar una constante: es un acuerdo entre personas.
#
# input() SIEMPRE DEVUELVE UN str
#   Aunque la persona escriba 25, input() devuelve "25" (texto).
#   Para hacer cuentas hay que CONVERTIR: int("25") -> 25, float("1.75")
#
# OPERADORES ARITMÉTICOS
#   +  suma          -  resta        *  multiplicación
#   /  división (siempre da float)   7 / 2  -> 3.5
#   // división entera (descarta decimales)   7 // 2 -> 3
#   %  resto (módulo)                 7 % 2  -> 1
#   ** potencia                       2 ** 3 -> 8
#
# OPERADORES DE COMPARACIÓN (siempre devuelven un bool)
#   ==  igual   !=  distinto   >  mayor   <  menor   >=  <=
#
# NOTAS / ERRORES DE LA VERSIÓN DE CLASE
# --------------------------------------
# 1. La línea  `mi_edad == 19`  sola no hace nada: compara y descarta el
#    resultado. Para ver el resultado hay que imprimirlo o guardarlo en
#    una variable.
# 2. El texto dice "es distinta al numero 19?" pero el código compara con
#    25. El mensaje y el código tienen que decir lo mismo; si no, el que
#    lee la salida se confunde. Usar una variable evita esto.
# 3. `mi_nombre = "Elias"` y en la línea siguiente `mi_nombre = input(...)`:
#    el primer valor se pisa. Sirve para mostrar que una variable puede
#    cambiar, pero en un programa real sobra.
# 4. Si en int(input(...)) la persona escribe "veinte" o deja vacío, el
#    programa se rompe con ValueError. Lo resolvemos en la clase 9
#    (try/except).
# 5. Al input() le conviene dejar un espacio al final del mensaje para que
#    lo que escribe el usuario no quede pegado a la pregunta.
# =====================================================================

# --- Constantes (arriba de todo, en MAYÚSCULAS) ----------------------
MAX_INTENTOS = 3
EDAD_A_COMPARAR = 19

# --- Entrada de datos -------------------------------------------------
mi_nombre = input("¿Cuál es tu nombre? ")            # str
mi_edad = int(input("¿Cuál es tu edad? "))           # str -> int
altura = float(input("¿Cuánto medís? (ej: 1.75) "))  # str -> float
le_gustan_las_motos = True                           # bool

# --- Proceso y salida -------------------------------------------------
print(f"Nombre: {mi_nombre}  -> tipo {type(mi_nombre)}")
print(f"Edad:   {mi_edad}  -> tipo {type(mi_edad)}")
print(f"Altura: {altura}  -> tipo {type(altura)}")
print(f"¿Le gustan las motos? {le_gustan_las_motos}  -> tipo {type(le_gustan_las_motos)}")

# f-strings: la f antes de las comillas permite meter variables entre {}.
# Es la forma recomendada. La alternativa vieja era concatenar con +, y
# ahí hay que convertir todo a str a mano:
print("Mi nombre es " + mi_nombre + " y tengo " + str(mi_edad) + " años")
print(f"Mi nombre es {mi_nombre} y tengo {mi_edad} años")   # más claro

# Dentro de las llaves podemos hacer cuentas y dar formato:
print(f"En días vividos (aprox): {mi_edad * 365}")
print(f"Altura con 1 decimal: {altura:.1f} m")

print("--- Operadores aritméticos ---")
print(7 / 2)    # 3.5  (división normal, siempre float)
print(7 // 2)   # 3    (división entera)
print(7 % 2)    # 1    (resto: muy útil para saber si un número es par)
print(2 ** 10)  # 1024 (potencia)

print("--- Comparaciones ---")
# Guardamos la comparación en una variable con nombre claro: así el
# mensaje y el código no se pueden contradecir.
es_igual = mi_edad == EDAD_A_COMPARAR
es_distinta = mi_edad != EDAD_A_COMPARAR
print(f"¿Tu edad es igual a {EDAD_A_COMPARAR}? {es_igual}")
print(f"¿Tu edad es distinta a {EDAD_A_COMPARAR}? {es_distinta}")

# Cuidado con mezclar tipos: "25" == 25 es False (texto vs número).
print(f'"25" == 25 -> {"25" == 25}')

# =====================================================================
# PARA PRACTICAR
# ---------------
# 1. Pedí el año de nacimiento y calculá la edad aproximada.
# 2. Pedí dos números decimales y mostrá suma, resta, producto y división
#    con 2 decimales ({valor:.2f}).
# 3. ¿Qué imprime print(10 % 3)? ¿Y print(type(10 / 2))? Pensalo antes de
#    ejecutarlo.
# 4. ¿Qué pasa si hacés "3" * 4? ¿Y "3" + 4? Probalo y explicá el error.
# =====================================================================
