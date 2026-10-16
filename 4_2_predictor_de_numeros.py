

# print("Juego - Detector de la mufa")
#
# for i in range(20):
#    if i % 3 == 0:
#         # Significa que es multiplo de 3
#         print(f" ----- El numero {i} es multiplo de 3 ----- Salteando.....")
#         continue
#    if i == 13:
#         print("Numero de la mufa! Me voy!")
#         break
#    print(f"El numero es: {i}")
#
# print(" ----- ----- ")
# print("Se termino el juego....")

while True:
    edad = int(input("Ingresa tu edad: "))
    if edad <= 0 or edad >= 120:
        print("Dato invalido")
        continue # HASTA ACA LLEGO ESTA VUELTA - VAMOS A LA SIGUIENTE VUELTA
    print("Edad registrada")

