canciones = ['De Musica Ligera','Ciudad', 'Nunca quise']

canciones.append('Persiana')
canciones.insert(0,'Cae el Sol')

print('Estado inicial')
print(canciones)

canciones.pop(0)

print('Pop en 0')
print(canciones)

canciones.sort() # Ordenamiento de la lista

print(canciones)

print(f"La lista de canciones tiene una longitud de: {len(canciones)}")
print(f"La cancion Cae el Sol esta en la lista?: {'Cae el Sol' in canciones}")

for cancion in canciones: #  ['De Musica Ligera','Ciudad', 'Nunca quise']
    print(cancion)

for posicion, cancion in enumerate(canciones):
    print(f"{posicion} ----- {cancion}")