# =====================================================================
# REPASO 6.2 - Menú del café (diccionarios en un caso real)
# Archivo original: clase1/6_2_menu.py
# =====================================================================
#
# CONCEPTOS
# ---------
# - Un diccionario es ideal como "tabla de precios": producto -> precio.
# - Buscar el MÁXIMO a mano: guardás "el mejor hasta ahora" y lo
#   comparás con cada elemento. Es un algoritmo clásico que conviene
#   saber escribir, aunque Python ya traiga max().
# - max(diccionario, key=diccionario.get) devuelve la CLAVE cuyo valor
#   es el más alto. key= le dice a max() "compará usando esto".
#
# ERRORES Y MEJORAS RESPECTO A LA VERSIÓN DE CLASE
# ------------------------------------------------
# 1. "defecto": 0 ESTÁ EN EL MENÚ: se usó como truco para arrancar la
#    búsqueda del más caro, pero se le imprime al cliente como si fuera
#    un producto ("- defecto.....ARS $ 0") y se puede pedir. Los datos
#    del negocio no se mezclan con valores auxiliares del algoritmo.
#    Para arrancar la búsqueda usamos None o el primer producto.
# 2. COMILLAS ANIDADAS EN EL f-string:
#        f"... {menu.get(producto_elegido, "defecto")}."
#    Usar " adentro de un f"..." solo funciona desde Python 3.12. En 3.11
#    o anterior da SyntaxError. Para que funcione en cualquier versión,
#    adentro usá comillas simples: f"... {menu.get(x, 'defecto')}".
# 3. menu.get(producto_elegido, "defecto") ya está dentro de un
#    "if producto_elegido in menu", así que el defecto nunca se usa, y si
#    se usara mezclaría un texto donde se espera un precio. Alcanza con
#    menu[producto_elegido].
# 4. producto_mas_barato se crea y nunca se calcula.
# 5. Si escriben "Cafe" o " cafe " no lo encuentra. Normalizamos con
#    .strip().lower().
# 6. El té de hibiscus a $32.000 seguro es un error de tipeo (¿3200?).
#    En datos reales, un valor raro merece una pregunta antes de
#    publicarse.
# =====================================================================

menu = {
    "cafe": 1200,
    "medialuna": 600,
    "tostado": 2500,
    "jugo": 1800,
    "te_de_hibiscus": 3200,
}

# --- 1. Imprimir la carta ---------------------------------------------
print("Bienvenidos al Café de SiMi - Backend con Python")
print("El menú es el siguiente:")
for producto, precio in menu.items():
    print(f"- {producto:.<20} ARS $ {precio}.-")
# {producto:.<20} = alineá a la izquierda en 20 caracteres y rellená
# con puntos. Así los precios quedan en columna.

# --- 2. Más caro y más barato A MANO (el algoritmo) --------------------
producto_mas_caro = None
producto_mas_barato = None
for producto, precio in menu.items():
    # La primera vuelta no hay con quién comparar: tomamos el primero.
    if producto_mas_caro is None or precio > menu[producto_mas_caro]:
        producto_mas_caro = producto
    if producto_mas_barato is None or precio < menu[producto_mas_barato]:
        producto_mas_barato = producto

# --- 2b. Lo mismo con funciones de Python (una línea cada uno) ---------
assert producto_mas_caro == max(menu, key=menu.get)
assert producto_mas_barato == min(menu, key=menu.get)
# assert verifica que algo sea True; si no, corta el programa con error.
# Sirve para comprobar que dos formas de calcular dan lo mismo.

# --- 3. Pedido del cliente --------------------------------------------
print()
print("Escribí el nombre de un producto, o:")
print("  'mas_caro'   para ver el producto más caro")
print("  'mas_barato' para ver el más barato")

producto_elegido = input("¿Qué querés? ").strip().lower()

if producto_elegido in menu:
    print(f"{producto_elegido} cuesta ARS $ {menu[producto_elegido]}.")
elif producto_elegido == "mas_caro":
    print(f"El más caro es {producto_mas_caro}: ARS $ {menu[producto_mas_caro]}")
elif producto_elegido == "mas_barato":
    print(f"El más barato es {producto_mas_barato}: ARS $ {menu[producto_mas_barato]}")
else:
    print("Ese producto no está en la carta.")

# =====================================================================
# PARA PRACTICAR
# ---------------
# 1. Convertilo en un pedido: con while True, el cliente agrega productos
#    hasta escribir "listo", y al final mostrás el detalle y el total.
#    Guardá el pedido en un diccionario {producto: cantidad}.
# 2. Agregá un descuento del 10% si el total supera ARS $ 5000.
# 3. Mostrá la carta ordenada por precio, de menor a mayor. Pista:
#        for producto in sorted(menu, key=menu.get):
# =====================================================================
