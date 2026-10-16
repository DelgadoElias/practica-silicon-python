edad = int(input("Ingresá tu edad: "))

if edad < 18:
    raise ValueError("Tenés que ser mayor de 18 años.")

print("Podés ingresar.")