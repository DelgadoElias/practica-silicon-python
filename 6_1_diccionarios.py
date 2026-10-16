

mi_persona = {
    "nombre": "Elias",
    "edad": 25,
    "listado": ["Programador", "DevOps", "finOps"]
}


mi_persona["direccion"] = "Avenida las pruebas 121212"
mi_persona["edad"] = 24

del mi_persona["listado"]

mi_persona.pop("documento",None)

print(f'Existe un nombre en mi persona? {"apellido" in mi_persona}')

print(mi_persona["nombre"])

# Diccionarios

print(mi_persona.keys())
print(mi_persona.values())
print(mi_persona.items())
print(mi_persona.get('nombre','Lautaro'))

print('Recorrido de Diccionario /////////////////////////////')

print("Solo las claves:")

for clave in mi_persona:
    print(clave)

print("Los items completos:")

for clave, valor in mi_persona.items():
    print(f"clave: {clave} valor: {valor}")

print("Solo los valores:")

for valor in mi_persona.values():
    print(valor)