# =====================================================================
# REPASO 6.1 - Diccionarios
# Archivo original: clase1/6_1_diccionarios.py
# =====================================================================
#
# CONCEPTOS
# ---------
# Un DICCIONARIO guarda pares CLAVE: VALOR.
#     persona = {"nombre": "Elias", "edad": 25}
# - En una lista accedés por POSICIÓN (lista[0]); en un diccionario
#   accedés por CLAVE (persona["nombre"]).
# - Las claves no se repiten: si asignás una clave que ya existe, se PISA
#   el valor anterior.
# - Las claves suelen ser strings; los valores pueden ser cualquier cosa
#   (números, listas, otros diccionarios...).
# - Es el formato más parecido a JSON, el que vas a usar TODO EL TIEMPO
#   en backend: lo que recibe y devuelve una API casi siempre se
#   convierte en un diccionario de Python.
#
# OPERACIONES
#   d["clave"]              lee el valor (KeyError si la clave no existe)
#   d.get("clave")          lee el valor o devuelve None si no existe
#   d.get("clave", defecto) lee el valor o devuelve "defecto"
#   d["clave"] = valor      agrega la clave o pisa su valor
#   del d["clave"]          borra (KeyError si no existe)
#   d.pop("clave", None)    borra y devuelve el valor; con un segundo
#                           argumento no falla si la clave no está
#   "clave" in d            ¿existe la CLAVE? (no busca en los valores)
#   d.keys()   d.values()   d.items()
#   len(d)                  cantidad de pares
#
# NOTAS / ERRORES DE LA VERSIÓN DE CLASE
# --------------------------------------
# 1. El mensaje dice "¿Existe un nombre en mi persona?" pero el código
#    pregunta por "apellido". Mensaje y código tienen que coincidir.
# 2. mi_persona.get('nombre', 'Lautaro') devuelve "Elias", porque la clave
#    existe. El valor por defecto solo aparece cuando la clave NO existe.
#    Abajo hay un ejemplo que muestra la diferencia.
# 3. pop("documento", None) es la forma segura de borrar una clave que
#    tal vez no existe; del rompe. Buen ejemplo, lo dejamos.
# =====================================================================

mi_persona = {
    "nombre": "Elias",
    "edad": 25,
    "listado": ["Programador", "DevOps", "FinOps"],   # un valor puede ser una lista
}
# La coma después del último elemento es válida y recomendada: al
# agregar una línea nueva no te olvidás la coma.

print("--- Agregar, modificar y borrar ---")
mi_persona["direccion"] = "Avenida Las Pruebas 1212"   # clave nueva: agrega
mi_persona["edad"] = 24                                # clave existente: pisa
del mi_persona["listado"]                              # borra (rompe si no existe)
mi_persona.pop("documento", None)                      # borra sin romper
print(mi_persona)

print("--- Preguntar si existe una clave ---")
print(f'¿Existe "apellido" en mi_persona? {"apellido" in mi_persona}')   # False
print(f'¿Existe "nombre" en mi_persona? {"nombre" in mi_persona}')       # True
# "in" busca en las CLAVES, no en los valores:
print(f'¿"Elias" está como clave? {"Elias" in mi_persona}')               # False
print(f'¿"Elias" está como valor? {"Elias" in mi_persona.values()}')      # True

print("--- [] vs .get() ---")
print(mi_persona["nombre"])                         # Elias
print(mi_persona.get("nombre", "Sin nombre"))       # Elias (existe, ignora el defecto)
print(mi_persona.get("apellido", "Sin apellido"))   # Sin apellido (no existe)
print(mi_persona.get("apellido"))                   # None
# print(mi_persona["apellido"])                     # KeyError: descomentá y probá

print("--- keys, values, items ---")
print(mi_persona.keys())
print(mi_persona.values())
print(mi_persona.items())    # lista de tuplas (clave, valor)

print("--- Recorridos ---")
print("Solo las claves:")
for clave in mi_persona:                     # igual que mi_persona.keys()
    print(f"  {clave}")

print("Clave y valor:")
for clave, valor in mi_persona.items():      # desempaquetado de la tupla
    print(f"  {clave}: {valor}")

print("Solo los valores:")
for valor in mi_persona.values():
    print(f"  {valor}")

print("--- Lista de diccionarios (lo que devuelve una API) ---")
# Una lista donde cada elemento es un diccionario con la misma forma.
alumnos = [
    {"nombre": "Lautaro", "edad": 20, "aprobado": True},
    {"nombre": "Paula", "edad": 22, "aprobado": False},
    {"nombre": "Martina", "edad": 19, "aprobado": True},
]
for alumno in alumnos:
    estado = "aprobó" if alumno["aprobado"] else "no aprobó"
    print(f"{alumno['nombre']} ({alumno['edad']}) {estado}")
# Nota: adentro de un f"..." con comillas dobles usamos comillas simples
# para la clave: f"{alumno['nombre']}". (Ver nota en el repaso 6.2.)

print("--- Diccionario anidado ---")
mi_persona["contacto"] = {"email": "elias@ejemplo.com", "telefono": "376-000000"}
print(mi_persona["contacto"]["email"])

# =====================================================================
# PARA PRACTICAR
# ---------------
# 1. Armá un diccionario con 5 países y su capital. Pedí un país y mostrá
#    su capital, o "No la conozco" si no está (usá .get()).
# 2. CONTAR PALABRAS: dado un texto, armá un diccionario
#    {palabra: cantidad_de_veces}. Pista:
#        conteo[palabra] = conteo.get(palabra, 0) + 1
# 3. Con la lista "alumnos" de arriba, calculá el promedio de edad y la
#    cantidad de aprobados.
# =====================================================================
