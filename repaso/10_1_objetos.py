# =====================================================================
# REPASO 10.1 - Objetos en la práctica: cuenta bancaria y carrito
# Archivo original: clase1/10_1_objetos.py (estaba vacío)
# =====================================================================
#
# OBJETIVO
# --------
# Practicar clases con ejemplos cercanos a un backend real:
#   1. CuentaBancaria: un objeto que PROTEGE sus datos (encapsulamiento)
#      y valida con raise (clase 9).
#   2. Producto + Carrito: objetos que CONTIENEN otros objetos.
#   3. Herencia: una clase que extiende a otra.
#
# CONCEPTOS NUEVOS
# ----------------
# ENCAPSULAMIENTO: el objeto controla cómo se modifican sus datos.
#   Nadie debería hacer  cuenta.saldo = 1000000  desde afuera; se usan
#   métodos (depositar, retirar) que validan.
#   En Python, un atributo que empieza con _ (self._saldo) es una
#   CONVENCIÓN que significa "privado, no lo toques desde afuera".
#   Python no lo impide: es un acuerdo, como las constantes en mayúscula.
#
# HERENCIA: class CajaDeAhorro(CuentaBancaria)
#   La clase hija recibe todos los atributos y métodos de la madre y
#   puede agregar nuevos o cambiar (sobrescribir) los existentes.
#   super() llama al método de la clase madre.
#
# __repr__: como __str__, pero pensado para programadores (debug). Es
#   lo que se ve cuando el objeto está dentro de una lista que se imprime.
# =====================================================================


# =====================================================================
# 1. CuentaBancaria
# =====================================================================
class SaldoInsuficienteError(Exception):
    pass


class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        if saldo_inicial < 0:
            raise ValueError("El saldo inicial no puede ser negativo.")
        self.titular = titular
        self._saldo = saldo_inicial      # _ = "privado por convención"
        self.movimientos = []            # historial

    @property
    def saldo(self):
        # Solo lectura: se puede LEER cuenta.saldo, pero no asignarlo.
        return self._saldo

    def depositar(self, monto):
        if monto <= 0:
            raise ValueError("El depósito tiene que ser mayor a cero.")
        self._saldo += monto
        self.movimientos.append(("depósito", monto))

    def retirar(self, monto):
        if monto <= 0:
            raise ValueError("El retiro tiene que ser mayor a cero.")
        if monto > self._saldo:
            raise SaldoInsuficienteError(
                f"Saldo insuficiente: tenés ${self._saldo} y querés retirar ${monto}."
            )
        self._saldo -= monto
        self.movimientos.append(("retiro", monto))

    def transferir(self, destino, monto):
        # Reutilizamos los métodos: si retirar() falla, depositar() no se
        # ejecuta y no se "crea" plata de la nada.
        self.retirar(monto)
        destino.depositar(monto)

    def __str__(self):
        return f"Cuenta de {self.titular}: ${self._saldo}"


print("--- Cuenta bancaria ---")
cuenta_elias = CuentaBancaria("Elias", 10000)
cuenta_paula = CuentaBancaria("Paula")

cuenta_elias.depositar(5000)
cuenta_elias.retirar(2000)
cuenta_elias.transferir(cuenta_paula, 3000)
print(cuenta_elias)          # $10000
print(cuenta_paula)          # $3000

try:
    cuenta_paula.retirar(50000)
except SaldoInsuficienteError as error:
    print(f"Operación rechazada: {error}")

try:
    cuenta_elias.saldo = 999999      # @property sin setter: no se puede
except AttributeError:
    print("No se puede modificar el saldo directamente.")

print("Movimientos de Elias:")
for tipo, monto in cuenta_elias.movimientos:
    print(f"  {tipo:<10} ${monto}")


# =====================================================================
# 2. Producto y Carrito (objetos que contienen objetos)
# =====================================================================
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __repr__(self):
        return f"Producto({self.nombre!r}, {self.precio})"
        # !r muestra el valor con comillas: Producto('cafe', 1200)


class Carrito:
    def __init__(self):
        self.items = {}              # {nombre_producto: [producto, cantidad]}

    def agregar(self, producto, cantidad=1):
        if producto.nombre in self.items:
            self.items[producto.nombre][1] += cantidad
        else:
            self.items[producto.nombre] = [producto, cantidad]

    def quitar(self, nombre_producto):
        self.items.pop(nombre_producto, None)

    def total(self):
        return sum(producto.precio * cantidad for producto, cantidad in self.items.values())

    def mostrar(self):
        for producto, cantidad in self.items.values():
            subtotal = producto.precio * cantidad
            print(f"  {cantidad} x {producto.nombre:<12} ${subtotal}")
        print(f"  TOTAL: ${self.total()}")


print()
print("--- Carrito ---")
cafe = Producto("cafe", 1200)
medialuna = Producto("medialuna", 600)
tostado = Producto("tostado", 2500)

carrito = Carrito()
carrito.agregar(cafe, 2)
carrito.agregar(medialuna, 3)
carrito.agregar(tostado)
carrito.agregar(cafe)            # ya estaba: suma cantidad
carrito.mostrar()
print([cafe, medialuna])         # usa __repr__


# =====================================================================
# 3. Herencia: CajaDeAhorro es una CuentaBancaria con límite de retiros
# =====================================================================
class CajaDeAhorro(CuentaBancaria):
    LIMITE_RETIROS = 3               # atributo de CLASE: compartido por todas

    def __init__(self, titular, saldo_inicial=0):
        super().__init__(titular, saldo_inicial)   # reutiliza el __init__ de la madre
        self.retiros_realizados = 0

    def retirar(self, monto):        # SOBRESCRIBE el retirar de la madre
        if self.retiros_realizados >= self.LIMITE_RETIROS:
            raise ValueError("Llegaste al límite de retiros del mes.")
        super().retirar(monto)       # las validaciones de la madre siguen valiendo
        self.retiros_realizados += 1


print()
print("--- Herencia ---")
caja = CajaDeAhorro("Martina", 10000)
for intento in range(1, 5):
    try:
        caja.retirar(1000)
        print(f"  Retiro {intento} OK - {caja}")
    except ValueError as error:
        print(f"  Retiro {intento} rechazado: {error}")

print(isinstance(caja, CajaDeAhorro))     # True
print(isinstance(caja, CuentaBancaria))   # True: una caja de ahorro ES una cuenta

# =====================================================================
# PARA PRACTICAR
# ---------------
# 1. Agregá a Carrito un método aplicar_descuento(porcentaje) y validá
#    con raise que el porcentaje esté entre 0 y 100.
# 2. Creá una clase Alumno con nombre y una lista de notas, con métodos
#    agregar_nota(nota) (que valide 1 a 10), promedio() y aprobo().
#    Reutilizá lo que aprendiste en el repaso 5.3 (¡cuidado con la lista
#    vacía!).
# 3. Creá CuentaCorriente(CuentaBancaria) que permita quedar en negativo
#    hasta un "descubierto" de $5000. Pista: sobrescribí retirar().
# =====================================================================
