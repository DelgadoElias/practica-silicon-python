# =====================================================================
# REPASO 5.1 - Listas
# Archivo original: clase1/5_1_listas.py
# =====================================================================
#
# CONCEPTOS
# ---------
# Una LISTA guarda varios valores EN ORDEN dentro de una sola variable.
#     alumnos = ['Elias', 'Lautaro', 'Alejandro']
# - Se escribe con corchetes [] y los elementos se separan con coma.
# - Puede mezclar tipos ([1, 1.2, '12']), pero en la práctica conviene
#   que todos sean del mismo tipo: así se pueden tratar todos igual.
# - Es MUTABLE: se pueden agregar, cambiar y borrar elementos.
#
# ÍNDICES: la posición de cada elemento, EMPEZANDO EN 0
#     alumnos  = ['Elias', 'Lautaro', 'Alejandro', 'Pablo', 'Paula', 'Martina']
#     positivo:     0         1           2           3        4         5
#     negativo:    -6        -5          -4          -3       -2        -1
#   alumnos[0]  -> 'Elias'      (el primero)
#   alumnos[-1] -> 'Martina'    (el último, sin saber el largo)
#   alumnos[15] -> IndexError   (esa posición no existe)
#
# SLICING (rebanadas): lista[desde:hasta:paso]  ("hasta" NO se incluye)
#   alumnos[2:5]  -> posiciones 2, 3 y 4
#   alumnos[:3]   -> los 3 primeros
#   alumnos[3:]   -> desde la posición 3 hasta el final
#   alumnos[::-1] -> la lista dada vuelta
#   El slicing devuelve una lista NUEVA; la original no cambia.
#
# MÉTODOS MÁS USADOS
#   .append(x)      agrega x al FINAL
#   .insert(i, x)   agrega x en la posición i (corre el resto)
#   .pop()          saca y DEVUELVE el último
#   .pop(i)         saca y devuelve el de la posición i
#   .remove(x)      borra la PRIMERA aparición del VALOR x
#                   (ValueError si x no está)
#   .sort()         ordena la lista EN EL LUGAR (modifica la original)
#   .index(x)       devuelve la posición de x
#   .count(x)       cuántas veces aparece x
#   len(lista)      cantidad de elementos
#   x in lista      True/False: ¿x está en la lista?
#
# DIFERENCIAS QUE CONFUNDEN
#   pop(i) vs remove(x): pop usa la POSICIÓN; remove usa el VALOR.
#   lista.sort() vs sorted(lista): sort() modifica la lista y devuelve
#   None; sorted() devuelve una lista NUEVA ordenada y no toca la original.
#     ERROR CLÁSICO:  alumnos = alumnos.sort()   -> alumnos queda en None
#
# NOTAS / MEJORAS
# ---------------
# 1. sort() ordena por orden de caracteres: las MAYÚSCULAS van antes que
#    las minúsculas ('Zoe' < 'ana'). Para ordenar sin distinguir:
#    alumnos.sort(key=str.lower)
# 2. remove() con un valor que no está rompe el programa. Conviene
#    preguntar antes con "in".
# =====================================================================

edades = [1, 13, 24, 32, 12, 2, 2, 2, 4]
alumnos = ['Elias', 'Lautaro', 'Alejandro', 'Pablo', 'Paula', 'Martina']

print("--- Índices ---")
print(alumnos[2])    # Alejandro, contando desde el inicio
print(alumnos[-4])   # Alejandro, contando desde el final
print(alumnos[-1])   # Martina (el último)

print("--- Slicing ---")
print(alumnos[2:5])  # ['Alejandro', 'Pablo', 'Paula'] (el 5 queda afuera)
print(alumnos[:3])   # los 3 primeros
print(edades[::-1])  # dada vuelta

print("--- Agregar ---")
print(len(alumnos))            # 6
alumnos.append('Santiago')     # al final
alumnos.insert(0, 'Pepito')    # al principio
alumnos.insert(3, 'Nicolas')   # en la posición 3
print(len(alumnos))            # 9
print(alumnos)

print("--- Modificar por posición ---")
alumnos[3] = 'NUEVO_NOMBRE'
print(alumnos)

print("--- Borrar ---")
alumnos.pop(3)                 # por POSICIÓN
ultimo_alumno = alumnos.pop()  # sin posición: el último, y lo devuelve
print(f"Saqué a: {ultimo_alumno}")
print(alumnos)

edades.remove(1)               # por VALOR: borra el primer 1
edades.remove(2)               # borra solo el PRIMER 2, quedan los otros
print(edades)

# remove() de un valor que no existe -> ValueError. Preguntamos antes:
if 99 in edades:
    edades.remove(99)
else:
    print("El 99 no está, no lo borro.")

print("--- Ordenar ---")
ordenados = sorted(alumnos)    # lista NUEVA, la original no cambia
print(f"sorted(): {ordenados}")
print(f"original: {alumnos}")
alumnos.sort()                 # ahora sí modificamos la original
print(f"sort():   {alumnos}")
edades.sort(reverse=True)      # de mayor a menor
print(edades)

print("--- Buscar y contar ---")
print('Mandarina' in alumnos)          # False
print(edades.count(2))                 # cuántos 2 quedan
print(alumnos.index('Pablo'))          # en qué posición está
print(f"Mayor: {max(edades)}, menor: {min(edades)}, suma: {sum(edades)}")

print("--- Recorrer ---")
for alumno in alumnos:
    print(f"- {alumno}")

# =====================================================================
# PARA PRACTICAR
# ---------------
# 1. Dada  numeros = [5, 3, 8, 1, 9, 2], mostrá: el mayor, el menor, el
#    promedio y la lista ordenada SIN modificar la original.
# 2. Pedí 5 nombres con un for + input() y guardalos en una lista.
#    Después mostralos ordenados alfabéticamente.
# 3. ¿Qué imprime este código? Pensalo antes de ejecutarlo:
#        a = [1, 2, 3]
#        b = a
#        b.append(4)
#        print(a)
#    (Pista: b = a NO copia la lista, las dos variables apuntan a la
#    MISMA lista. Para copiar: b = a.copy() o b = a[:].)
# =====================================================================
