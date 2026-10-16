# =====================================================================
# REPASO 9.1 - Manejo de errores: try / except / else / finally
# Archivo original: clase1/9_1_tryexcept.py
# =====================================================================
#
# CONCEPTOS
# ---------
# Cuando algo sale mal, Python lanza una EXCEPCIÓN y, si nadie la
# atrapa, el programa se corta y muestra el "Traceback" (el mensaje
# rojo). try/except permite ATRAPARLA y decidir qué hacer.
#
#     try:
#         # código que PUEDE fallar
#     except TipoDeError:
#         # qué hacer si falla con ese error
#     else:
#         # se ejecuta solo si NO hubo error
#     finally:
#         # se ejecuta SIEMPRE, haya error o no (cerrar archivos,
#         # conexiones a la base de datos, etc.)
#
# EXCEPCIONES QUE YA VIMOS EN EL CURSO
#   ValueError         int("hola")              valor con formato inválido
#   ZeroDivisionError  10 / 0                   (repaso 5.3)
#   IndexError         lista[99]                (repaso 5.1)
#   KeyError           diccionario["no_existe"] (repaso 6.1)
#   TypeError          "3" + 4                  (repaso 2.1)
#   NameError          usar una variable que no existe
#   RecursionError     recursión sin fin        (repaso 8.2)
#
# BUENAS PRÁCTICAS
# ----------------
# 1. Atrapá el error ESPECÍFICO (except ValueError), no cualquier cosa.
#    Un "except:" solo o "except Exception:" esconde errores que no
#    esperabas (un error de tipeo, por ejemplo) y te deja sin pistas.
# 2. Dentro del try poné SOLO la línea que puede fallar. Lo que depende
#    de que haya salido bien va en el else.
# 3. Si atrapás un error, hacé algo útil: avisar, reintentar, usar un
#    valor por defecto. Un except que solo hace "pass" esconde el
#    problema.
#
# MEJORAS RESPECTO A LA VERSIÓN DE CLASE
# --------------------------------------
# - Los dos ejemplos están bien. Lo que les falta es lo que pasa DESPUÉS
#   del error: el programa avisa y termina, pero sigue sin tener el
#   número. Lo habitual es REINTENTAR con un while True (abajo).
# - Sumamos finally, "except ... as error" y varios except.
# =====================================================================

# --- 1. try / except básico --------------------------------------------
try:
    numero = int(input("Ingresá un número: "))
    print("El número es:", numero)
except ValueError:
    print("Tenés que ingresar un número.")

# --- 2. try / except / else --------------------------------------------
# En el try queda SOLO lo que puede fallar.
try:
    numero = int(input("Ingresá otro número: "))
except ValueError:
    print("Tenés que ingresar un número.")
else:
    print("Perfecto, ingresaste:", numero)

# --- 3. Reintentar hasta que el dato sea válido ------------------------
# Es el patrón del repaso 4.2, ahora sin que letras rompan el programa.
while True:
    try:
        edad = int(input("Ingresá tu edad: "))
    except ValueError:
        print("  Eso no es un número entero, probá de nuevo.")
        continue
    if edad < 0:
        print("  La edad no puede ser negativa.")
        continue
    break
print(f"Edad registrada: {edad}")

# --- 4. Varios except y "as error" -------------------------------------
# "as error" guarda la excepción en una variable para ver su mensaje.
try:
    dividendo = int(input("Dividendo: "))
    divisor = int(input("Divisor: "))
    resultado = dividendo / divisor
except ValueError as error:
    print(f"  Dato inválido: {error}")
except ZeroDivisionError:
    print("  No se puede dividir por cero.")
else:
    print(f"  Resultado: {resultado}")
finally:
    print("  (esto se imprime siempre: fin de la división)")

# --- 5. Una función reutilizable -----------------------------------------
def pedir_entero(mensaje, minimo=None, maximo=None):
    """Pide un entero hasta que sea válido y esté dentro del rango."""
    while True:
        try:
            valor = int(input(mensaje))
        except ValueError:
            print("  Tiene que ser un número entero.")
            continue
        if minimo is not None and valor < minimo:
            print(f"  Tiene que ser {minimo} o más.")
            continue
        if maximo is not None and valor > maximo:
            print(f"  Tiene que ser {maximo} o menos.")
            continue
        return valor        # return también corta el while

nota = pedir_entero("Ingresá una nota del 1 al 10: ", minimo=1, maximo=10)
print(f"Nota cargada: {nota}")

# =====================================================================
# PARA PRACTICAR
# ---------------
# 1. Usá pedir_entero() para arreglar el int(input()) de los repasos
#    2.2, 3.2 y 5.3.
# 2. Pedí un índice y mostrá ese elemento de una lista; atrapá
#    IndexError y ValueError por separado.
# 3. Pedí un producto del menú del repaso 6.2 con  menu[producto]  y
#    atrapá KeyError para decir "no está en la carta".
# =====================================================================
