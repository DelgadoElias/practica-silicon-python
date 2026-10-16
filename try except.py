# try except.py
# Clase 9 - Manejo de errores + Cierre del Módulo 1
# Contenido: try/except, errores específicos, else, finally, raise,
# input blindado y gestor de tareas en consola.


# ============================================================
# 1. TRY / EXCEPT BÁSICO
# ============================================================
class DemoTryExcept:
    """Ejemplos de try/except: qué pasa sin y con manejo de errores."""

    @staticmethod
    def sin_try():
        # Si el usuario escribe "hola", el programa muere con ValueError
        edad = int(input("Tu edad (sin try): "))
        print(f"Tenés {edad}")

    @staticmethod
    def con_try():
        while True:
            try:
                edad = int(input("Tu edad (con try): "))
                break  # salió bien -> salgo del bucle
            except ValueError:
                print("Eso no es un número, probá de nuevo")
        print(f"Tenés {edad}")  # el programa sigue vivo


# ============================================================
# 2. ERRORES ESPECÍFICOS
# ============================================================
class Calculadora:
    """Divide dos números atrapando cada error por separado."""

    @staticmethod
    def dividir_interactivo():
        try:
            a = int(input("Número: "))
            b = int(input("Dividir por: "))
            print(a / b)
        except ValueError:
            print("Tenés que escribir números enteros")
        except ZeroDivisionError:
            print("No se puede dividir por cero")
        except Exception as e:  # solo si necesitás el detalle del error
            print(f"Algo salió mal: {e}")


# ============================================================
# 3. ELSE Y FINALLY
# ============================================================
class CargaNotas:
    """Flujo completo: try / except / else / finally."""

    @staticmethod
    def cargar_nota():
        try:
            nota = int(input("Nota: "))
        except ValueError:
            print("Nota inválida")
        else:  # solo si NO falló
            print("Aprobado" if nota >= 6 else "Desaprobado")
        finally:  # SIEMPRE
            print("Fin de la carga")


# ============================================================
# 4. RAISE: LANZAR TU PROPIO ERROR
# ============================================================
class Validador:
    """Validaciones propias con raise."""

    @staticmethod
    def validar_edad(edad):
        if edad < 0:
            raise ValueError("Edad negativa")
        if edad > 120:
            raise ValueError("Más de 120 años")
        return edad

    @staticmethod
    def demo_raise():
        try:
            Validador.validar_edad(-5)
        except ValueError as err:
            print(err)  # Edad negativa


# ============================================================
# 5. MINI-EJERCICIO: INPUT BLINDADO
# ============================================================
class InputBlindado:
    """Pide datos hasta que sean válidos."""

    @staticmethod
    def pedir_entero(mensaje):
        while True:
            try:
                return int(input(mensaje))
            except ValueError:
                print("Eso no es un número entero, probá de nuevo")

    @staticmethod
    def pedir_entero_entre(mensaje, minimo, maximo):
        while True:
            try:
                valor = InputBlindado.pedir_entero(mensaje)
                if valor < minimo or valor > maximo:
                    raise ValueError(f"Tiene que estar entre {minimo} y {maximo}")
                return valor
            except ValueError as err:
                print(err)

    @staticmethod
    def demo_edad():
        try:
            edad = InputBlindado.pedir_entero_entre("Edad: ", 0, 120)
            print(f"Listo: {edad}")
        finally:
            print("gracias")


# ============================================================
# 6. GESTOR DE TAREAS EN CONSOLA (proyecto del módulo)
# ============================================================
class GestorTareas:
    """Gestor de tareas: menú, agregar, ver, marcar, eliminar."""

    def __init__(self):
        self.tareas = []  # lista de diccionarios {"texto": ..., "hecha": ...}

    # --- Paso 1: menú ---
    def mostrar_menu(self):
        print("\n=== MIS TAREAS ===")
        print("1. Agregar tarea")
        print("2. Ver tareas")
        print("3. Marcar como hecha")
        print("4. Eliminar tarea")
        print("5. Salir")

    # --- Paso 2: agregar ---
    def agregar_tarea(self):
        texto = input("Tarea: ").strip()
        if texto == "":
            print("No puede estar vacía")
            return
        self.tareas.append({"texto": texto, "hecha": False})
        print("Agregada ✓")

    # --- Paso 3: ver ---
    def ver_tareas(self):
        if len(self.tareas) == 0:
            print("No hay tareas todavía")
            return
        for i, t in enumerate(self.tareas, 1):
            marca = "✓" if t["hecha"] else "○"
            print(f"{i}. {marca} {t['texto']}")

    # --- Paso 4 y 5: validación compartida ---
    def pedir_numero_tarea(self):
        self.ver_tareas()
        try:
            n = int(input("Número de tarea: "))
            if 1 <= n <= len(self.tareas):
                return n - 1  # el usuario ve desde 1
            print("Ese número no existe")
        except ValueError:
            print("Tenés que escribir un número")
        return None

    def marcar_hecha(self):
        i = self.pedir_numero_tarea()
        if i is not None:
            self.tareas[i]["hecha"] = True
            print("¡Hecha! ✓")

    def eliminar_tarea(self):
        i = self.pedir_numero_tarea()
        if i is not None:
            borrada = self.tareas.pop(i)
            print(f"Eliminada: {borrada['texto']}")

    # --- Paso 6: menú blindado ---
    def ejecutar(self):
        while True:
            self.mostrar_menu()
            try:
                opcion = int(input("Opción: "))
            except ValueError:
                print("Escribí un número del 1 al 5")
                continue  # de vuelta al menú

            if opcion == 1:
                self.agregar_tarea()
            elif opcion == 2:
                self.ver_tareas()
            elif opcion == 3:
                self.marcar_hecha()
            elif opcion == 4:
                self.eliminar_tarea()
            elif opcion == 5:
                print("¡Chau!")
                break
            else:
                print("Esa opción no existe")


# ============================================================
# PROGRAMA PRINCIPAL
# ============================================================
def menu_principal():
    opciones = {
        "1": ("try/except básico", DemoTryExcept.con_try),
        "2": ("Errores específicos (división)", Calculadora.dividir_interactivo),
        "3": ("else y finally (notas)", CargaNotas.cargar_nota),
        "4": ("raise (validar edad)", Validador.demo_raise),
        "5": ("Input blindado (edad 0-120)", InputBlindado.demo_edad),
        "6": ("Gestor de tareas", lambda: GestorTareas().ejecutar()),
        "0": ("Salir", None),
    }
    while True:
        print("\n=== CLASE 9: TRY / EXCEPT ===")
        for clave, (nombre, _) in opciones.items():
            print(f"{clave}. {nombre}")
        eleccion = input("Elegí una demo: ").strip()
        if eleccion == "0":
            print("¡Chau!")
            break
        if eleccion in opciones:
            try:
                opciones[eleccion][1]()
            except KeyboardInterrupt:
                print("\nCortado por el usuario")
        else:
            print("Esa opción no existe")


if __name__ == "__main__":
    menu_principal()
