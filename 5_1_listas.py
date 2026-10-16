# edades_compuestas = [1,1.2,'12'] # Le es indistinto el tipo de dato correlacionado con el anterior

 
edades = [1,13,24,32,12,2,2,2,4]
alumnos = ['Elias','Lautaro','Alejandro','Pablo','Paula','Martina']



#print(alumnos[2])   # Alejandro contando desde el INICIO
#print(alumnos[-4])  # Alejandro contando desde el FINAL

# print(edades_compuestas)
# print(type(edades_compuestas))


# Slicing
nueva_lista_alumnos = alumnos[2:5] # El 5 queda excluido del procedimiento

#print(alumnos[1:5])
#print(nueva_lista_alumnos)
#print(edades[::-1])

# print(alumnos[15]) # -----> Index Error

print(alumnos)

print(len(alumnos)) # 6


alumnos.append('Santiago')

alumnos.insert(0,'Pepito')

alumnos.insert(3,'Nicolas')

print(len(alumnos)) # 9

print(alumnos)

alumnos[3] = 'NUEVO_NOMBRE'

print(alumnos)

alumnos.pop(3)

print(alumnos)

print('-------- POP sin posicion')

ultimo_alumno = alumnos.pop()

print(alumnos)

print(ultimo_alumno)

print('------ remove edades')

edades.remove(1)

print(edades)

edades.remove(2) # Borra la primer ocurrencia con el valor nro 2

print(edades)

print('///////// alumnos')

print(alumnos)

alumnos.sort()

print(alumnos)


print('Mandarina' in alumnos)