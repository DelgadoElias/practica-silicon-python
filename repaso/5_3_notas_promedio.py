# =====================================================================
# REPASO 5.3 - Cargar notas y calcular el promedio
# Archivo original: clase1/5_3_notas_promedio.py
# =====================================================================
#
# CONCEPTOS
# ---------
# - VALOR CENTINELA: un valor especial que significa "terminé"
#   (acá, -1). Es la forma clásica de cargar una cantidad desconocida
#   de datos con while True + break.
# - ACUMULADOR: una variable que arranca en 0 y va sumando en cada vuelta
#   (suma += nota). CONTADOR: igual, pero suma de a 1.
# - Python ya trae funciones para esto: sum(lista), len(lista),
#   max(lista), min(lista).
#
# ERRORES QUE ENCONTRAMOS EN LA VERSIÓN DE CLASE
# ----------------------------------------------
# 1. EL PROMEDIO USA // (división entera):
#        nota_final = suma // len(notas)
#    // TRUNCA (corta los decimales), así que la nota informada es falsa:
#    con [9, 10] el promedio real es 9.5 y el programa dice 9; con
#    [6, 7, 7] es 6.67 y dice 6. (Como el umbral es un entero, quién
#    aprueba no cambia; pero si mañana se aprueba con 6.5, sí.)
#    Para promedios se usa /  y, para mostrarlo, {promedio:.2f}.
# 2. DIVISIÓN POR CERO: si la persona escribe -1 de entrada, notas queda
#    vacía, len(notas) es 0 y el programa se rompe con ZeroDivisionError.
#    Siempre hay que contemplar la lista vacía.
# 3. La variable "aprobados = 0" se crea y nunca se usa.
# 4. Si la nota está fuera de rango se hace continue sin avisar: la
#    persona no sabe por qué no se cargó. Hay que avisar.
# 5. El bloque final  "i = 0 / while i < 10"  no hace nada útil: era la
#    comparación con el for de C/Java  for(i = 0; i < 10; i++).
#    Lo dejamos abajo explicado.
# 6. El mensaje de instrucciones se imprime en CADA vuelta. Alcanza con
#    mostrarlo una vez, antes del bucle.
# =====================================================================

NOTA_MINIMA = 1
NOTA_MAXIMA = 10
NOTA_PARA_APROBAR = 6
FIN_DE_CARGA = -1         # valor centinela

nombre = input("Ingresá tu nombre: ")
notas = []

print(f"Cargá tus notas de {NOTA_MINIMA} a {NOTA_MAXIMA}. "
      f"Cuando termines, escribí {FIN_DE_CARGA}.")

while True:
    nota_cargada = int(input("Cargá tu nota: "))
    if nota_cargada == FIN_DE_CARGA:
        break
    if nota_cargada < NOTA_MINIMA or nota_cargada > NOTA_MAXIMA:
        print(f"  La nota tiene que estar entre {NOTA_MINIMA} y {NOTA_MAXIMA}. No se cargó.")
        continue
    notas.append(nota_cargada)

# --- Caso borde: no cargó ninguna nota --------------------------------
if len(notas) == 0:            # también se puede escribir: if not notas:
    print("No cargaste ninguna nota, no hay promedio para calcular.")
else:
    # --- Promedio parcial vuelta a vuelta (como en clase) -------------
    suma = 0
    for posicion, nota in enumerate(notas, start=1):
        suma += nota           # suma = suma + nota
        print(f"Procesando nota {nota} - promedio parcial: {suma / posicion:.2f}")

    # --- Resultado final: con / y no con // ---------------------------
    promedio = suma / len(notas)
    # Atajo equivalente con funciones de Python:
    # promedio = sum(notas) / len(notas)

    print(f"{nombre}, tus notas: {notas}")
    print(f"Promedio: {promedio:.2f}  |  Mejor: {max(notas)}  |  Peor: {min(notas)}")

    if promedio >= NOTA_PARA_APROBAR:
        print(f"¡Felicidades! Aprobaste con {promedio:.2f}")
    else:
        print(f"No pudiste aprobar, tu promedio es {promedio:.2f}")

# --- La comparación con otros lenguajes ------------------------------
# En C/Java/JavaScript:  for (i = 0; i < 10; i++) { ... }
# En Python, lo mismo es:
#     for i in range(10):
#         ...
# Y escrito con while (lo que había al final del archivo original):
#     i = 0
#     while i < 10:
#         ...           # bloque de código
#         i += 1
# El for con range es más corto y no permite olvidarse del i += 1.

# =====================================================================
# PARA PRACTICAR
# ---------------
# 1. Contá cuántas notas son de aprobación (>= 6) y cuántas no
#    (acá sí se usa una variable "aprobados").
# 2. Si la persona escribe letras, el int() se rompe. Protegelo con
#    try/except (clase 9) o con .isdigit() (ver repaso 4.2).
#    Ojo: "-1".isdigit() es False, así que el centinela hay que
#    revisarlo ANTES.
# 3. Calculá el promedio descartando la nota más baja.
# =====================================================================
