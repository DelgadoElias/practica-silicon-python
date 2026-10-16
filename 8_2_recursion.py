def cuenta_regresiva(numero):
    if numero == 0:
        print("Despegue")
    else:
        print(numero)
        cuenta_regresiva(numero - 1)

cuenta_regresiva(-10)
