# Concidicionales

# edad = int(input("¿Que edad tenes?"))
# print(f"Validemos la condicion. La condicion es {edad >= 19}")

# if CONDICION: 
# if edad >= 19:
    # BLOQUE VERDADERO - SOLAMENTE SE EJECUTA SI LA CONDICION ES VERDADERA
    # print("Sos mayor o tenes 19 años, podes pasar")

# BLOQUE NORMAL
# print("La ejecucion de siempre")


# edad_para_sufragio = int(input("Que edad tenes  "))

#if edad_para_sufragio >=18:
     # BLOQUE VERDADERO - SOLAMENTE SE EJECUTA SI LA CONDICION ES VERDADERA
#print("Podes votar")
#    nombre = input("Escribi tu nombre")
#else:
#    # BLOQUE FALSO - SOLAMENTE SE EJECUTA SI LA CONDICION ES FALSA - SI LA VERDADERA NO PASA, SIEMPRE VA A ENTRAR A ESTA PARTE
#    print("NO podes votar")
#    nombre_padre = input("Escribi los nombres de tus padres")

# BLOQUE NORMAL
# print("Proceso finalizado por favor continuar.....")
#print("Proceso finalizado por favor continuar.....")


numero_seleccionado_por_el_usuario = int(input("Selecciona un numero al azar:   "))

el_numero_es_par = numero_seleccionado_por_el_usuario % 2 == 0

print(f"La variable el_numero_es_par tiene un tipo de: {type(el_numero_es_par)} y tiene un valor de: {el_numero_es_par}")

if el_numero_es_par:
    print("El numero es par.... Yupi")
else:
    print("El numero es impar.... Que lastima")
