
# OTRO CAMBIO
# while True:
#     try:
#         numero = int(input("Ingresá un número: "))
#     
#     except ValueError:
#         print("Tenés que ingresar un número.")

# try: # Deberia de ir SOLA Y UNICAMENTE, las lineas que pueden arrojar un error
#     numero_uno = int(input("Ingresá el primer numero: "))
#     numero_dos = int(input("Ingresá el segundo numero: "))
#
#     numero_final = numero_uno / numero_dos
# except ValueError:
#     print("Tenes que ingresar un numero")
# except ZeroDivisionError:
#     print("El programa no procesa divisiones por zero")
# except Exception as e:
#     print(e)
#     print("Ocurrio un error")
# else: # Solamente sucede si el try salio exitoso SIN LLAMADOS A EXCEPCIONES
#     print(f"Salio todo bien. Numero final: {numero_final}") 
# finally:
#     print("Finalmente llegue al final")


def input_blindado(mensaje = "El numero tiene que estar dentro del minimo y el maximo", minimo = 0, maximo = 100):
    while True:
        try:
            numero_blindado = int(input("Ingresa tu numero"))
            if numero_blindado < minimo or numero_blindado > maximo:
                raise ValueError(mensaje)
        except ValueError as e:
            # Trabajar en la implementacion para poder solucionar
            print(e)
        else:
            break
        finally:
            print("Okay")
    return numero_blindado


numero = input_blindado()
print(numero)


# def validar_mayoria_de_edad(edad):
#     try:
#         edad_validada = int(edad)
#         if edad_validada < 0:
#             raise ValueError("Ingrese una edad positiva")
#         if edad_validada > 100:
#             raise ValueError("La edad deberia de ser menor a 100")
#     except ValueError as e:
#         print(e)
#     else:
#         print(f"Tu edad es: {edad}")
#         return edad_validada > 18
#
#
#
# valor_booleano = validar_mayoria_de_edad(input("Ingresá un número: "))
# print(f"valor_booleano: {valor_booleano}")
# while True:
#
#     # Regla no escrita: El try deberia de ser lo mas sencillo posible, la menor cantidad de lineas
#     try:
#         numero = int(input("Ingresá un número: "))
#
#     except ValueError:
#         print("Tenés que ingresar un número.")
#     
#     else:
#         print("Perfecto, ingresaste el numero:", numero)
#         break
#
# print("Seguimos fuera del flujo del While infinito")


# # Try except else
#
# try:
#     numero = int(input("Ingresá un número: "))
#
# except ValueError:
#     print("Tenés que ingresar un número.")
#
# else:
#     print("Perfecto, ingresaste:", numero)


# Principio Zen de Python
