# =====================================================================
# REPASO 6.3 - Sets (conjuntos)
# Archivo original: clase1/6_3_sets.py
# =====================================================================
#
# CONCEPTOS
# ---------
# Un SET es una colección:
#   - SIN ELEMENTOS REPETIDOS (si agregás un duplicado, se ignora).
#   - SIN ORDEN: no tiene índices, set[0] da error.
#   - Muy rápido para preguntar "¿está x?" con in, aunque tenga millones
#     de elementos (en una lista, Python revisa uno por uno).
#
# CÓMO SE CREA
#   colores = {"rojo", "verde"}      con llaves y valores sueltos
#   set(["a", "b", "a"])             a partir de una lista -> {"a", "b"}
#   vacio = set()                    ¡OJO! {} crea un DICCIONARIO vacío
#
# OPERACIONES DE CONJUNTOS (como en matemática)
#   a | b   unión              todo lo que está en a o en b
#   a & b   intersección       lo que está en los dos
#   a - b   diferencia         lo que está en a pero no en b
#   a ^ b   diferencia simétrica: lo que está en uno solo
#
# MÉTODOS
#   .add(x)       agrega uno
#   .remove(x)    borra (KeyError si no está)
#   .discard(x)   borra sin fallar si no está
#
# CUÁNDO USARLO EN BACKEND
#   - Sacar duplicados de una lista: list(set(lista))
#   - Comparar permisos/roles: ¿qué permisos tiene el usuario que el
#     endpoint exige?
#   - Llevar registro de IDs ya procesados para no procesarlos dos veces.
#
# NOTAS SOBRE LA VERSIÓN DE CLASE
# -------------------------------
# 1. set(['Holamundo', 'holamundo']) tiene DOS elementos, no uno: para
#    Python son textos distintos porque las mayúsculas cuentan. Si la idea
#    era mostrar que "son la misma palabra escrita distinto", hay que
#    normalizar antes con .lower().
# 2. Se creó la variable formas_de_escribir_holamundo y después se volvió
#    a escribir el mismo set adentro del print. Usá la variable.
# 3. Falta un espacio después del = (estilo PEP 8): x = set(...)
# =====================================================================

formas_de_escribir_holamundo = set(['Holamundo', 'holamundo'])
print(formas_de_escribir_holamundo)        # 2 elementos: distinguen mayúsculas
print(len(formas_de_escribir_holamundo))   # 2

# Normalizando primero, quedan como la misma palabra:
normalizadas = {palabra.lower() for palabra in ['Holamundo', 'holamundo', 'HOLAMUNDO']}
print(normalizadas)                        # {'holamundo'}
# La línea de arriba es una "set comprehension": como una list
# comprehension pero con llaves.

print("--- Sacar duplicados ---")
votos = ["azul", "rojo", "azul", "verde", "rojo", "azul"]
opciones_votadas = set(votos)
print(opciones_votadas)                    # sin repetidos (el orden puede variar)
print(f"Se votaron {len(opciones_votadas)} opciones distintas")

print("--- Agregar y borrar ---")
opciones_votadas.add("amarillo")
opciones_votadas.add("azul")               # ya estaba: no pasa nada
opciones_votadas.discard("violeta")        # no está: discard no falla
print(opciones_votadas)

print("--- Operaciones de conjuntos ---")
alumnos_python = {"Elias", "Lautaro", "Paula", "Martina"}
alumnos_javascript = {"Paula", "Pablo", "Martina", "Santiago"}

print(f"Cursan alguna:        {alumnos_python | alumnos_javascript}")
print(f"Cursan las dos:       {alumnos_python & alumnos_javascript}")
print(f"Solo Python:          {alumnos_python - alumnos_javascript}")
print(f"Solo una de las dos:  {alumnos_python ^ alumnos_javascript}")

print("--- Ejemplo backend: permisos ---")
permisos_del_usuario = {"leer", "escribir"}
permisos_requeridos = {"leer", "borrar"}
faltantes = permisos_requeridos - permisos_del_usuario
if faltantes:                              # un set vacío vale False
    print(f"Acceso denegado. Faltan permisos: {faltantes}")
else:
    print("Acceso permitido")

# =====================================================================
# PARA PRACTICAR
# ---------------
# 1. Pedí 10 números al usuario y decí cuántos DISTINTOS ingresó.
# 2. Dadas dos listas de invitados (de la novia y del novio), mostrá
#    quiénes están invitados por los dos lados.
# 3. Dado un texto, mostrá qué letras del abecedario NO aparecen.
#    Pista: set("abcdefghijklmnñopqrstuvwxyz") - set(texto.lower())
# =====================================================================
