# =====================================================================
# REPASO 9.2 - Lanzar errores con raise
# Archivo original: clase1/9_2_raise.py
# =====================================================================
#
# CONCEPTOS
# ---------
# try/except ATRAPA errores. raise los LANZA.
#     raise ValueError("mensaje explicando qué salió mal")
#
# ¿Para qué lanzar un error a propósito?
#   Cuando una función recibe algo que no tiene sentido, no debería
#   seguir como si nada ni devolver un valor raro (como el "Hola" de
#   calcular_iva en la clase 7). Lanza un error y quien la llamó decide
#   qué hacer: mostrar un mensaje, reintentar, devolver un 400 en una API...
#
# SEPARAR RESPONSABILIDADES
#   - La FUNCIÓN valida y lanza el error (no sabe si hay una persona
#     mirando una consola, una página web o una app).
#   - Quien LLAMA a la función atrapa el error y decide cómo mostrarlo.
#   Esto es exactamente cómo funciona un backend: la lógica de negocio
#   lanza errores y la capa de la API los convierte en respuestas HTTP.
#
# ¿QUÉ TIPO DE ERROR LANZAR?
#   ValueError -> el tipo es correcto pero el valor no sirve (edad = -5)
#   TypeError  -> el tipo es incorrecto (edad = "veinte")
#   Una excepción PROPIA -> para errores del negocio (ver abajo)
#
# NOTAS / MEJORAS RESPECTO A LA VERSIÓN DE CLASE
# ----------------------------------------------
# 1. El raise está bien, pero nadie lo atrapa: la persona menor de 18 ve
#    un Traceback rojo en vez de un mensaje amable. raise tiene sentido
#    junto con un try/except en el lugar donde se llama.
# 2. ValueError ya lo usa int() cuando escriben letras. En el original no
#    hay forma de distinguir "escribiste letras" de "sos menor". Con una
#    excepción propia (MenorDeEdadError) quedan separados.
# 3. El 18 es un número mágico: EDAD_MINIMA = 18.
# 4. No se valida que la edad sea positiva.
# =====================================================================

EDAD_MINIMA = 18

# --- 1. Una excepción propia --------------------------------------------
# Se crea con una clase que hereda de Exception (clases: clase 10).
# El "pass" significa "no agrego nada": hereda todo de Exception.
class MenorDeEdadError(Exception):
    pass


# --- 2. La función VALIDA y LANZA -----------------------------------------
def validar_edad(edad):
    if edad < 0:
        raise ValueError("La edad no puede ser negativa.")
    if edad < EDAD_MINIMA:
        raise MenorDeEdadError(f"Tenés que tener {EDAD_MINIMA} años o más.")
    return edad


# --- 3. Quien LLAMA, ATRAPA y decide qué mostrar -------------------------
try:
    edad = int(input("Ingresá tu edad: "))     # ValueError si son letras
    validar_edad(edad)                          # puede lanzar los dos errores
except MenorDeEdadError as error:
    print(f"No podés ingresar: {error}")
except ValueError as error:
    print(f"Dato inválido: {error}")
else:
    print("Podés ingresar.")

# Ojo con el orden de los except: Python usa el PRIMERO que coincida.
# Como MenorDeEdadError NO hereda de ValueError, acá el orden da igual;
# pero si una excepción heredara de otra, la más específica va primero.


# --- 4. Ejemplo de backend: validar los datos de un pago ----------------
def validar_pago(pago):
    """pago es un diccionario como el que llegaría en un JSON."""
    if "monto" not in pago:
        raise KeyError("Falta el campo 'monto'.")
    if not isinstance(pago["monto"], (int, float)):
        raise TypeError("El monto tiene que ser un número.")
    if pago["monto"] <= 0:
        raise ValueError("El monto tiene que ser mayor a cero.")
    return True

pagos_de_prueba = [
    {"monto": 1500},
    {"monto": -20},
    {"monto": "mil"},
    {"moneda": "ARS"},
]

for pago in pagos_de_prueba:
    try:
        validar_pago(pago)
    except (KeyError, TypeError, ValueError) as error:   # varios en una tupla
        print(f"  {pago} -> RECHAZADO: {error}")
    else:
        print(f"  {pago} -> OK")
# Detalle: el mensaje de un KeyError se imprime entre comillas
# ("Falta el campo 'monto'."). Es una particularidad de KeyError; por eso
# muchos prefieren lanzar ValueError también para campos faltantes.

# =====================================================================
# PARA PRACTICAR
# ---------------
# 1. Escribí retirar(saldo, monto) que lance ValueError si el monto es
#    negativo y una excepción propia SaldoInsuficienteError si el monto
#    supera el saldo. Probala con try/except.
# 2. Combiná con el repaso 9.1: pedí la edad hasta que sea válida, pero
#    si es menor de 18, terminá el programa con un mensaje (sin
#    Traceback).
# =====================================================================
