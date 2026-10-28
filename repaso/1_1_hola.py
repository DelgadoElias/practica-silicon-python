# BBBBBBBESTOY TRABAJANDO EN UNA NUEVA FUNCIONALIDAD =====================================================================
# REPASO 1.1 - Mi primer archivo de Python
# Archivo original: clase1/1_1_hola.py
# =====================================================================
#
# CONCEPTOSwefwefwffwewefwef
# ---------
# - Un programa de Python es un archivo de texto con extensión .py.
#   Python lo lee de ARRIBA hacia ABAJO, una línea por vez.
# - Para ejecutarlo, desde la terminal y parados en la carpeta del archivo:
#       python 1_1_hola.py
# - print() es una FUNCIÓN: recibe algo entre paréntesis y lo muestra en
#   la consola. Lo que va entre comillas es un "string" (texto).
# - Todo lo que está después de un # es un COMENTARIO: Python lo ignora.
#   Sirve para explicar el código a otras personas (y a vos en 3 meses).
#
# NOTAS
# -----
# - Las comillas pueden ser simples 'hola' o dobles "hola": son lo mismo.
#   Elegí una y usala siempre igual en todo el archivo.
# - Python distingue mayúsculas: print() funciona, Print() da error.
# - Si te olvidás de cerrar una comilla o un paréntesis vas a ver un
#   SyntaxError. Leé el número de línea que te indica el error.
#
# MEJORAS
# -------
# - El original funciona perfecto. Acá sumamos algunas variantes de print()
#   que vamos a usar todo el curso.
# =====================================================================

print("Hola mundo")
print("Este es mi primer archivo de Python")

# print() puede recibir VARIOS valores separados por coma.
# Por defecto los separa con un espacio.
print("Hola", "mundo", "desde", "Python")

# El parámetro sep cambia el separador.
print("2026", "10", "07", sep="-")        # 2026-10-07

# El parámetro end cambia lo que se imprime al final (por defecto es un
# salto de línea "\n"). Así dos print() quedan en la misma línea:
print("Cargando", end="...")
print(" listo!")

# Caracteres especiales dentro de un string:
#   \n -> salto de línea      \t -> tabulación
print("Línea 1\nLínea 2")
print("Nombre:\tElias")

# Texto de varias líneas con triple comilla:
print("""
Bienvenido al curso de Backend con Python
-----------------------------------------
Clase 1
""")

# =====================================================================
# PARA PRACTICAR
# ---------------
# 1. Imprimí tu nombre, tu ciudad y tu comida favorita en tres líneas
#    distintas usando UN SOLO print() (pista: \n).
# 2. Imprimí la fecha de hoy con el formato 07/10/2026 usando sep.
# 3. Dibujá un rectángulo de asteriscos de 5x3 con print().
#    Pista: "*" * 5 da "*****".
# =====================================================================
