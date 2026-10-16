nombre = input("Ingresa tu nombre: ")
notas = []

while True:
    print("Necesito que cargues tus notas, si no tenes mas para cargar, escribi '-1'")
    nota_cargada = int(input("Carga tu nota: "))
    if nota_cargada == -1:
        break
    if nota_cargada < 1 or nota_cargada > 10:
        continue
    notas.append(nota_cargada)


suma = 0
aprobados = 0

for posicion, nota in enumerate(notas): # [8,3,1,4,7,7,7]
    suma += nota # suma = suma + nota
    print(f"Procesando nota: {nota} - Al momento el promedio es: {suma // (posicion + 1)}")

nota_final = suma // len(notas)

if nota_final >= 6:
    print(f"Felicidades! Aprobaste con: {nota_final}")
else:
    print(f"No pudiste aprobar, tu nota es: {nota_final}")


#    for(i = 0; i< 10; i++){}
#    for posicion, nota in enumerate(notas): 


i = 0

while i < 10:
    i = i+1
    # TODO BLOQUE DE CODIGO
