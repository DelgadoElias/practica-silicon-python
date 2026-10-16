# Calculadora de propina
# El usuario debera de ingresar el numero y con esto se debera de calcular la propina
# La propina se definira siendo el 10% del valor total que ingrese el usuario

nombre = input("¿Cual es tu nombre? ")
numero_de_mesa = int(input("¿Cual es tu numero de mesa? "))
total_a_pagar = int(input(f"{nombre} - ¿Cual es el total a pagar de su mesa?"))
propina_calculada = int(total_a_pagar * 0.10) # 0.10 Es equivalente al 10% del monto

print(f"{nombre} - Tu mesa es la numero {numero_de_mesa} y el total a pagar es de:  ARS ${total_a_pagar}")
print(f"{nombre} - Por recomendaciones, le sugerimos que la propina sea de: {propina_calculada}")