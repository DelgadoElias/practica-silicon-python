menu = {
    "cafe": 1200,
    "medialuna": 600,
    "tostado":2500,
    "jugo":1800,
    "te_de_hibiscus":32000,
    "defecto": 0
}

# 1. Imprimamos la carta

print("Bienvenidos al Cafe de SiMi Backend con Python")
print("El menu es el siguiente: ")

producto_mas_caro = "defecto"
producto_mas_barato = "defecto"

for producto, precio in menu.items():
    if menu.get(producto_mas_caro,0) < precio:
        producto_mas_caro = producto
    print(f"- {producto}..........ARS $ {precio}.-")

print("Elegi un producto:")
print("Escribi 'mas_caro' para saber cual es el producto mas caro de nuestra carta")

producto_elegido = input("Escribi el nombre del producto que queres: ")

if producto_elegido in menu:
    print(f"El producto como tal cuesta: ARS $ {menu.get(producto_elegido, "defecto")}.")
elif producto_elegido == 'mas_caro':
    print(f"El producto mas caro que tenemos es: {producto_mas_caro} con un precio de {menu.get(producto_mas_caro,0)}")
else:
    print("El producto no esta en la lista")