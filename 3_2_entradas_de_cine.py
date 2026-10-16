
BOLETO_GRATUITO_EDAD = 3
BOLETO_GRATUITO_PRECIO = 0

BOLETO_INFANTIL_EDAD = 12
BOLETO_INFANTIL_PRECIO = 2000

BOLETO_GENERAL_EDAD = 59
BOLETO_GENERAL_PRECIO = 5000

BOLETO_JUBILADOS_EDAD = 60
BOLETO_JUBILADOS_PRECIO = 2500

EDAD_MINIMA_PARA_PELICULAS_ADULTOS = 18

pelicula_tiene_condicion_a_mayores = False

print("Selecciona tu pelicula: ")
print("1. The amazing spiderman") # Para mayores
print("2. Spiderman No way Home") # Para mayores
print("3. Terminator")

nombre = input("Cual es tu nombre")
edad_usuario = int(input(f"{nombre} Cual es tu edad "))
pelicula_a_mirar = int(input("Que pelicula queres mirar, envia el numero: "))


if pelicula_a_mirar == 1 or pelicula_a_mirar == 2:
    pelicula_tiene_condicion_a_mayores = True
    print("Esta pelicula es para mayores")
    if edad_usuario <= EDAD_MINIMA_PARA_PELICULAS_ADULTOS:
        respuesta = int(input("Tenes autorizacion o venis con tus padres? Responde 1 si es correcto, cualquier otro numero es incorrecto  "))
        if respuesta == 1:
            print("Perfecto, calculando precio")
        else: 
            print("La pelicula no es apta para vos elegi otra pelicula")
            exit(1)

if edad_usuario < 0:
    print("Por favor, ingresa una edad valida")
elif edad_usuario < BOLETO_GRATUITO_EDAD:
    print(f"El precio de tu entrada es de: ${BOLETO_GRATUITO_PRECIO}")
elif edad_usuario < BOLETO_INFANTIL_EDAD:
    print(f"El precio de tu entrada es de: ${BOLETO_INFANTIL_PRECIO}")
elif edad_usuario < BOLETO_GENERAL_EDAD:
    print(f"El precio de tu entrada es de: ${BOLETO_GENERAL_PRECIO}")
else:
    print(f"El precio de tu entrada es de: ${BOLETO_JUBILADOS_PRECIO}")


# and
# True and True     -----> True
# True and False    -----> False
# False and False   -----> False

# or
# True and True     -----> True
# True and False    -----> True
# False and False   -----> False


# valor = True
# not valor         ------> False
# not not valor     ------> True

# edad = 18
# edad > 15         ------> Es una condicion true
# not edad > 15     ------> Arrojara False
