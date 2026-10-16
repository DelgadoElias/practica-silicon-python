#  Bucles en Python


# while CONDICION:
# while True:
    # TODO LO QUE ESTA ADENTRO TIENE UNA IDENTACION
#    comando = input("Coloca tu comando >>> ")
#    if comando == "input":
#        print("Decifrando mensaje en consola: input")
#    print(f"Tu comando es: {comando}")

# print("")

# i ----> iteration o iteracion

# print(type(range(5)))


# for <<var>> in <<valor_a_condicionar>>
# for iteration in range(5): # range ----> 0 1 2 3 4
#    print(f"La vuelta es el numero: {iteration}")

# For - Voy a ingresar un numero y luego de eso voy a hacer un print de la cantidad de vueltas que voy y saludar por cada print

numero = int(input("Ingresa un numero:  "))
vueltas_por_cada_numero = int(input("Ingresa la cantidad de vueltas por cada numero:  "))


# 12 - int 12
# range(12) - 0 1 2 3 4 5 6 7 8 9 10 11

print("----- ----- ----- FOR CON CONTINUE ----- ----- -----")

for vuelta in range(numero):
   if vuelta == 3:
        continue
   print(f"CONTINUE - La vuelta es la numero: {vuelta}")
   for subvuelta in range(vueltas_por_cada_numero):
        print(f"CONTINUE - Subvuelta : {subvuelta} de la rama de vueltas: {vuelta}")


print("----- ----- ----- FOR CON BREAK ----- ----- -----")

for vuelta in range(numero):
   if vuelta == 3:
        break
   print(f"BREAK - La vuelta es la numero: {vuelta}")
   for subvuelta in range(vueltas_por_cada_numero):
        print(f"BREAK - Subvuelta : {subvuelta} de la rama de vueltas: {vuelta}")



print("Termino el ciclo")
