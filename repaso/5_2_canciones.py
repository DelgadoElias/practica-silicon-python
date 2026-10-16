# =====================================================================
# REPASO 5.2 - Playlist de canciones (recorrer listas con for y enumerate)
# Archivo original: clase1/5_2_canciones.py
# =====================================================================
#
# CONCEPTOS
# ---------
# RECORRER UNA LISTA
#     for cancion in canciones:        -> te da cada ELEMENTO
#         print(cancion)
#
# enumerate(): te da la POSICIÓN y el ELEMENTO al mismo tiempo
#     for posicion, cancion in enumerate(canciones):
#         ...
#   enumerate(lista, start=1) empieza a contar desde 1, ideal para
#   mostrar listas numeradas a personas (nadie dice "canción número 0").
#
# DESEMPAQUETADO: "posicion, cancion" recibe los dos valores que da
# enumerate en cada vuelta. Funciona igual que  a, b = 1, 2
#
# NOTAS / MEJORAS RESPECTO A LA VERSIÓN DE CLASE
# ----------------------------------------------
# 1. Se pregunta si 'Cae el Sol' está en la lista DESPUÉS de haberla
#    sacado con pop(0): la respuesta es False y es correcto, pero vale la
#    pena notarlo: pop(0) sacó justamente esa canción porque insert(0, ...)
#    la había puesto primera.
# 2. Guardar lo que devuelve pop() permite avisar QUÉ se sacó.
# 3. El comentario del for muestra la lista inicial, pero en ese momento
#    la lista ya está ordenada y tiene 'Persiana'. Los comentarios
#    desactualizados confunden más que no tener comentarios.
# 4. Numerar desde 1 con enumerate(..., start=1).
# =====================================================================

canciones = ['De Música Ligera', 'Ciudad', 'Nunca quise']

canciones.append('Persiana')         # al final
canciones.insert(0, 'Cae el Sol')    # al principio

print('Estado inicial')
print(canciones)

sacada = canciones.pop(0)            # pop devuelve lo que saca
print(f"Saqué de la lista: {sacada}")
print(canciones)

canciones.sort()                     # orden alfabético
print('Ordenada:')
print(canciones)

print(f"La playlist tiene {len(canciones)} canciones")
print(f"¿'Cae el Sol' está en la lista? {'Cae el Sol' in canciones}")

print("--- Recorrido simple ---")
for cancion in canciones:
    print(cancion)

print("--- Recorrido numerado (desde 1) ---")
for numero, cancion in enumerate(canciones, start=1):
    print(f"{numero}. {cancion}")

print("--- Buscar una canción ---")
buscada = input("¿Qué canción buscás? ")
if buscada in canciones:
    # .index() devuelve la posición (desde 0), sumamos 1 para mostrarla
    print(f"Está en el puesto {canciones.index(buscada) + 1}")
else:
    print("No está en la playlist")

# Ojo: "in" distingue mayúsculas. "ciudad" no encuentra "Ciudad".
# Una búsqueda que no distingue mayúsculas:
coincidencias = [c for c in canciones if buscada.lower() in c.lower()]
print(f"Coincidencias (sin importar mayúsculas): {coincidencias}")
# La línea de arriba es una LIST COMPREHENSION: una forma corta de armar
# una lista filtrando otra. Equivale a:
#     coincidencias = []
#     for c in canciones:
#         if buscada.lower() in c.lower():
#             coincidencias.append(c)

# =====================================================================
# PARA PRACTICAR
# ---------------
# 1. Armá un menú con while True: 1) agregar canción, 2) borrar canción,
#    3) ver playlist, 4) salir.
# 2. Evitá que se agregue una canción repetida.
# 3. Guardá también la duración en minutos en otra lista y mostrá la
#    duración total de la playlist. (En la clase 6 vemos que esto queda
#    mejor con un diccionario.)
# =====================================================================
