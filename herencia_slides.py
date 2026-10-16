# =============================================================================
# CLASE 11 · HERENCIA Y POLIMORFISMO
# "Moldes a partir de otros moldes"
#
# Este archivo sigue la PPT slide por slide, pero con más ejemplos y detalles.
# Cada bloque es una función: al final del archivo podés comentar/descomentar
# cuál querés correr. Correlo con:  python herencia_slides.py
# =============================================================================


def titulo(texto):
    print()
    print("=" * 70)
    print(texto)
    print("=" * 70)


# =============================================================================
# SLIDE 3 · REPASO (17:30 → 17:45)
# =============================================================================

def repaso():
    titulo("REPASO · class, __init__, self, métodos")

    # --- Pregunta 1: ¿Qué imprime? ------------------------------------------
    class Contador:
        def __init__(self):
            self.n = 0

        def sumar(self):
            self.n += 1

    a = Contador()
    b = Contador()
    a.sumar()
    a.sumar()
    print("Pregunta 1 ->", a.n, b.n)  # 2 0
    # Cada objeto tiene SU PROPIO self.n. Sumar en 'a' no toca a 'b'.

    # --- Pregunta 2: ¿Qué es self? -------------------------------------------
    class Alumna:
        def __init__(self, nombre):
            self.nombre = nombre

        def saludar(self):
            return self.nombre

    sofi = Alumna("Sofi")
    print("Pregunta 2 ->", sofi.saludar())
    # Python traduce sofi.saludar() a Alumna.saludar(sofi).
    # self ES el objeto que está antes del punto. Por eso no lo pasamos a mano.
    print("Lo mismo, a mano ->", Alumna.saludar(sofi))

    # --- Pregunta 3: Perro y Gato repiten código -----------------------------
    # La respondemos en el bloque siguiente. Es el tema de hoy.


# =============================================================================
# SLIDE 4 · POR QUÉ HERENCIA (17:45 → 18:05)
# =============================================================================

def sin_herencia():
    titulo("SIN HERENCIA · copiar y pegar")

    class Perro:
        def __init__(self, nombre, edad):
            self.nombre = nombre
            self.edad = edad

        def dormir(self):
            return f"{self.nombre} duerme"

    class Gato:  # todo igual que Perro
        def __init__(self, nombre, edad):
            self.nombre = nombre
            self.edad = edad

        def dormir(self):
            return f"{self.nombre} duerme"

    print(Perro("Firu", 3).dormir())
    print(Gato("Misi", 2).dormir())
    # Problema: si mañana dormir() tiene que decir "duerme la siesta",
    # hay que cambiarlo en 2 lugares. Si agregamos Loro, en 3. Y siempre
    # uno se olvida de alguno -> bugs.


# El "padre" lo dejamos afuera de las funciones porque lo vamos a reusar
# en varios bloques de la clase.
class Animal:  # CLASE PADRE (o clase BASE)
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def dormir(self):
        return f"{self.nombre} duerme"

    def hablar(self):
        return f"{self.nombre} hace un sonido"


def con_herencia():
    titulo("CON HERENCIA · lo común, una sola vez")

    class Perro(Animal):  # HIJA: hereda todo de Animal
        pass  # por ahora no agrega nada

    class Gato(Animal):
        pass

    firu = Perro("Firu", 3)
    print(firu.dormir())  # Firu duerme
    print(firu.nombre, firu.edad)  # Firu 3
    # Perro no escribió __init__ ni dormir()... y los tiene. Los heredó.

    # ¿Cómo lo encuentra Python? Busca el método en la clase del objeto;
    # si no está, sube al padre; si no está, al abuelo... hasta 'object'.
    # Ese camino se llama MRO (Method Resolution Order):
    print("Camino de búsqueda de Perro:", [c.__name__ for c in Perro.__mro__])
    # ['Perro', 'Animal', 'object']  -> 'object' es el padre de TODAS las clases

    # Herramientas para preguntar sobre la familia:
    print("¿firu es un Perro?  ", isinstance(firu, Perro))   # True
    print("¿firu es un Animal? ", isinstance(firu, Animal))  # True: un hijo ES un padre
    print("¿firu es un Gato?   ", isinstance(firu, Gato))    # False: hermanos no
    print("¿Perro hereda de Animal?", issubclass(Perro, Animal))  # True
    print("¿Animal hereda de Perro?", issubclass(Animal, Perro))  # False: no al revés


# =============================================================================
# SLIDE 5 · PENSALO ASÍ: los hijos heredan rasgos pero tienen los suyos
# =============================================================================
#
#                  Animal  (nombre · edad · dormir())
#                 /      \
#     Perro(Animal)       Gato(Animal)
#     + raza              + color
#     + ladrar()          + maullar()
#
# Lo del padre viene "gratis". Lo propio de cada hija lo agregamos ahora.


# =============================================================================
# SLIDE 6 · super() (18:05 → 18:25)
# =============================================================================

class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)  # (1) el padre arma lo que sabe armar
        self.raza = raza                # (2) la hija agrega lo propio

    def ladrar(self):  # método propio: Animal no lo tiene
        return f"{self.nombre}: ¡Guau!"


class Gato(Animal):
    def __init__(self, nombre, edad, color):
        super().__init__(nombre, edad)
        self.color = color

    def maullar(self):
        return f"{self.nombre}: Miau"


def demo_super():
    titulo("super() · la hija suma lo suyo")

    firu = Perro("Firu", 3, "caniche")
    print(firu.nombre, firu.raza)  # Firu caniche
    print(firu.dormir())           # heredado
    print(firu.ladrar())           # propio

    misi = Gato("Misi", 2, "naranja")
    print(misi.maullar(), "| color:", misi.color)

    # Lo propio de una hija NO lo tiene la otra hija ni el padre:
    print("¿Gato tiene ladrar?  ", hasattr(misi, "ladrar"))           # False
    print("¿Animal tiene ladrar?", hasattr(Animal("X", 1), "ladrar"))  # False

    # vars() muestra los atributos del objeto: los del padre y los de la hija
    print("Atributos de firu:", vars(firu))
    # {'nombre': 'Firu', 'edad': 3, 'raza': 'caniche'}


def error_tipico_sin_super():
    titulo("ERROR TÍPICO · olvidar super().__init__")

    class PerroRoto(Animal):
        def __init__(self, nombre, edad, raza):
            # ¡Falta super().__init__(nombre, edad)!
            self.raza = raza

    roto = PerroRoto("Firu", 3, "caniche")
    print("Atributos de roto:", vars(roto))  # solo {'raza': 'caniche'}

    try:
        print(roto.dormir())  # dormir usa self.nombre... que nunca se creó
    except AttributeError as e:
        print("AttributeError ->", e)
    # Pista: cuando escribís __init__ en la hija, REEMPLAZÁS el del padre.
    # Si no llamás a super().__init__, el del padre nunca corre.
    # Regla: primero super().__init__(...), después lo tuyo.


def super_sin_init_en_la_hija():
    titulo("DETALLE · si la hija no escribe __init__, usa el del padre")

    class Loro(Animal):
        def repetir(self, frase):
            return f"{self.nombre} repite: {frase}"

    pepe = Loro("Pepe", 1)  # usa Animal.__init__ directamente
    print(pepe.repetir("hola"))
    # Solo hace falta escribir __init__ en la hija cuando AGREGA atributos.


# =============================================================================
# SLIDE 7 · MINI-EJERCICIO: Vehiculo -> Auto y Moto (resuelto)
# =============================================================================

class Vehiculo:
    def __init__(self, marca, anio):
        self.marca = marca
        self.anio = anio

    def describir(self):
        return f"{self.marca} ({self.anio})"


class Auto(Vehiculo):
    def __init__(self, marca, anio, puertas):
        super().__init__(marca, anio)
        self.puertas = puertas

    def abrir_puertas(self):  # yapa
        return f"Se abren {self.puertas} puertas"


class Moto(Vehiculo):
    def __init__(self, marca, anio, cilindrada):
        super().__init__(marca, anio)
        self.cilindrada = cilindrada


def ejercicio_vehiculos():
    titulo("MINI-EJERCICIO · Vehiculo -> Auto y Moto")

    auto = Auto("Toyota", 2020, 4)
    moto = Moto("Honda", 2018, 150)

    print(auto.describir())      # Toyota (2020)
    print(moto.describir())      # Honda (2018)
    print(auto.abrir_puertas())  # Se abren 4 puertas
    # describir() está escrito UNA sola vez, en Vehiculo. Las dos hijas lo tienen.


# =============================================================================
# SLIDE 9 · SOBREESCRITURA (18:35 → 18:55)
# =============================================================================

def demo_sobreescritura():
    titulo("SOBREESCRITURA · la hija lo hace a su manera")

    class PerroQueHabla(Animal):
        def hablar(self):  # mismo nombre que en Animal -> gana este
            return f"{self.nombre}: ¡Guau!"

    class GatoQueHabla(Animal):
        def hablar(self):
            return f"{self.nombre}: Miau"

    class Loro(Animal):
        pass  # no lo escribe -> usa el del padre

    print(PerroQueHabla("Firu", 3).hablar())  # Firu: ¡Guau!
    print(GatoQueHabla("Misi", 2).hablar())   # Misi: Miau
    print(Loro("Pepe", 1).hablar())           # Pepe hace un sonido

    # Sobreescribir NO cambia al padre: un Animal sigue hablando como Animal
    print(Animal("Genérico", 0).hablar())     # Genérico hace un sonido

    # Las 3 reglas:
    # 1. Mismo nombre y mismos parámetros que en el padre.
    # 2. La versión de la hija reemplaza a la del padre PARA ESE OBJETO.
    # 3. Si la hija no lo escribe, usa la del padre tal cual.


def demo_super_en_metodo():
    titulo("super() EN UN MÉTODO · agregar en vez de reemplazar")

    class GatoDormilon(Animal):
        def dormir(self):
            original = super().dormir()  # "Misi duerme"
            return original + " en el sillón"

    print(GatoDormilon("Misi", 2).dormir())  # Misi duerme en el sillón

    # Comparación: reemplazar del todo vs extender
    class GatoQueReemplaza(Animal):
        def dormir(self):
            return "zzz"  # se perdió el nombre: no reusa nada del padre

    print(GatoQueReemplaza("Misi", 2).dormir())  # zzz


def parametros_distintos_rompen():
    titulo("CUIDADO · si cambiás los parámetros, rompés a quien te usa")

    class PerroMal(Animal):
        def hablar(self, volumen):  # el padre no pedía 'volumen'
            return f"{self.nombre}: ¡GUAU!" * volumen

    try:
        print(PerroMal("Firu", 3).hablar())  # se llama igual que a cualquier Animal...
    except TypeError as e:
        print("TypeError ->", e)
    # ...y explota. Por eso la regla 1: mismos parámetros que el padre.
    # Si necesitás algo extra, dale un valor por defecto: def hablar(self, volumen=1)


# =============================================================================
# SLIDE 10 · MINI-EJERCICIO: cada animal a su manera (resuelto)
# =============================================================================

class PerroEj(Animal):
    def hablar(self):
        return f"{self.nombre}: ¡Guau!"

    def presentarse(self):
        # reusamos self.hablar() en vez de copiar el texto
        sonido = self.hablar().split(": ")[1]
        return f"Soy {self.nombre} y digo {sonido}"


class GatoEj(Animal):
    def hablar(self):
        return f"{self.nombre}: Miau"

    def dormir(self):
        return super().dormir() + " en el sillón"


class LoroEj(Animal):
    pass


class Vaca(Animal):
    def hablar(self):
        return f"{self.nombre}: Muuu"


def ejercicio_animales():
    titulo("MINI-EJERCICIO · cada animal a su manera")

    print(Vaca("Lola", 5).hablar())          # Lola: Muuu
    print(GatoEj("Misi", 2).dormir())        # Misi duerme en el sillón
    print(PerroEj("Firu", 3).presentarse())  # Soy Firu y digo ¡Guau!

    # Yapa: Vaca no sobreescribió dormir() -> usa el de Animal
    print(Vaca("Lola", 5).dormir())          # Lola duerme

    # Dos usos de super():
    #   - en __init__ para no repetir la carga de atributos
    #   - en un método para agregarle algo al original


# =============================================================================
# SLIDE 11 · POLIMORFISMO (18:55 → 19:10)
# =============================================================================

def demo_polimorfismo():
    titulo("POLIMORFISMO · mismo pedido, cada uno responde a su manera")

    animales = [
        PerroEj("Firu", 3),
        GatoEj("Misi", 2),
        LoroEj("Pepe", 1),
        Vaca("Lola", 5),
    ]

    for a in animales:
        print(a.hablar())  # el MISMO pedido
    # Firu: ¡Guau!
    # Misi: Miau
    # Pepe hace un sonido
    # Lola: Muuu

    # El for no sabe ni le importa qué animal es. Mañana agregás Pato:
    class Pato(Animal):
        def hablar(self):
            return f"{self.nombre}: Cuac"

    animales.append(Pato("Donald", 4))
    print("--- agregamos un Pato, el for no cambió ni una letra ---")
    for a in animales:
        print(a.hablar())

    # Sin polimorfismo tendríamos que preguntar el tipo a cada rato:
    print("--- versión SIN polimorfismo (no lo hagan así) ---")
    for a in animales:
        if isinstance(a, PerroEj):
            print(f"{a.nombre}: ¡Guau!")
        elif isinstance(a, GatoEj):
            print(f"{a.nombre}: Miau")
        elif isinstance(a, Vaca):
            print(f"{a.nombre}: Muuu")
        else:
            print(f"{a.nombre} hace un sonido")
    # ¿Viste? El Pato quedó "hace un sonido": cada animal nuevo obliga a
    # tocar el if. Con polimorfismo, el conocimiento vive en cada clase.


def polimorfismo_en_funciones():
    titulo("POLIMORFISMO · también funciona con funciones")

    def concierto(lista):
        # Esta función recibe "algo que sepa hablar()". No pide un tipo exacto.
        return " / ".join(a.hablar() for a in lista)

    print(concierto([PerroEj("Firu", 3), Vaca("Lola", 5)]))

    # Analogía de la slide: el botón ▶ play del control remoto.
    class Tele:
        def play(self):
            return "Tele: arranca la serie"

    class Parlante:
        def play(self):
            return "Parlante: suena música"

    class Consola:
        def play(self):
            return "Consola: empieza el juego"

    for aparato in [Tele(), Parlante(), Consola()]:
        print(aparato.play())
    # Ojo: Tele, Parlante y Consola NO heredan de nadie. En Python alcanza
    # con que tengan el mismo método ("duck typing": si camina como pato y
    # hace cuac como pato, es un pato). La herencia ayuda a garantizarlo.


# =============================================================================
# SLIDE 12 · CRITERIO: ¿cuándo heredar? "ES UN" vs "TIENE UN"
# =============================================================================

class Motor:
    def __init__(self, caballos):
        self.caballos = caballos

    def arrancar(self):
        return f"Motor de {self.caballos} HP: brrrm"


class AutoConMotor(Vehiculo):  # un Auto ES UN Vehículo -> hereda
    def __init__(self, marca, anio, caballos):
        super().__init__(marca, anio)
        self.motor = Motor(caballos)  # un Auto TIENE UN Motor -> atributo

    def arrancar(self):
        return f"{self.describir()} -> {self.motor.arrancar()}"


def criterio_es_un_tiene_un():
    titulo("CRITERIO · 'ES UN' -> heredá · 'TIENE UN' -> atributo")

    auto = AutoConMotor("Ford", 2015, 110)
    print(auto.arrancar())

    print("¿El auto es un Vehiculo?", isinstance(auto, Vehiculo))  # True
    print("¿El auto es un Motor?   ", isinstance(auto, Motor))     # False: lo TIENE
    print("Su motor:", auto.motor.caballos, "HP")

    # Otro ejemplo de "TIENE UN": una Biblioteca tiene libros (una lista).
    class Biblioteca:
        def __init__(self, nombre):
            self.nombre = nombre
            self.libros = []  # TIENE libros, no ES un libro

        def agregar(self, titulo_libro):
            self.libros.append(titulo_libro)

    bib = Biblioteca("Popular de Posadas")
    bib.agregar("Rayuela")
    bib.agregar("Ficciones")
    print(f"{bib.nombre} tiene {len(bib.libros)} libros: {bib.libros}")

    # La herencia se abusa. Si dudás, no heredes: un atributo siempre es
    # más simple de entender y de cambiar.


# =============================================================================
# SLIDE 13 · EJERCICIO INTEGRADOR: CuentaAhorro y CuentaCorriente (resuelto)
# =============================================================================

# Base de la Clase 10 (si la tuya es distinta, usá la tuya).
class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, monto):
        if monto <= 0:
            raise ValueError("El depósito tiene que ser mayor a 0")
        self.saldo += monto

    def retirar(self, monto):
        if monto > self.saldo:
            raise ValueError("Saldo insuficiente")
        self.saldo -= monto

    def mostrar_saldo(self):
        return f"{self.titular}: ${self.saldo:.2f}"


class CuentaAhorro(CuentaBancaria):
    def __init__(self, titular, saldo, tasa):
        super().__init__(titular, saldo)
        self.tasa = tasa

    def aplicar_interes(self):
        self.saldo += self.saldo * self.tasa

    def mostrar_saldo(self):  # bonus: extiende al del padre
        return super().mostrar_saldo() + f" (tasa {self.tasa:.0%})"


class CuentaCorriente(CuentaBancaria):
    def __init__(self, titular, saldo, limite_sobregiro):
        super().__init__(titular, saldo)
        self.limite_sobregiro = limite_sobregiro

    def retirar(self, monto):  # sobreescrito: permite quedar en negativo
        if self.saldo - monto < -self.limite_sobregiro:
            raise ValueError(
                f"Supera el sobregiro: el mínimo es -{self.limite_sobregiro}"
            )
        self.saldo -= monto


def ejercicio_integrador():
    titulo("INTEGRADOR · CuentaAhorro y CuentaCorriente")

    # --- Probalo así (de la slide) --------------------------------------------
    cc = CuentaCorriente("Tomi", 100, 500)
    cc.retirar(400)
    print("Después de retirar 400:", cc.mostrar_saldo())  # -300
    try:
        cc.retirar(300)  # quedaría en -600, pasa el límite de -500
    except ValueError as e:
        print("ValueError ->", e)

    ca = CuentaAhorro("Sofi", 1000, 0.05)
    ca.aplicar_interes()
    print("Con interés:", ca.mostrar_saldo())  # 1050 (tasa 5%)

    # La cuenta común sigue sin permitir sobregiro (el padre no cambió):
    comun = CuentaBancaria("Juan", 50)
    try:
        comun.retirar(100)
    except ValueError as e:
        print("Cuenta común ->", e)

    # --- Polimorfismo: un solo for para las tres -------------------------------
    print("--- depositamos 100 en cada una ---")
    cuentas = [
        CuentaBancaria("Juan", 50),
        CuentaAhorro("Sofi", 1000, 0.05),
        CuentaCorriente("Tomi", -200, 500),
    ]
    for cuenta in cuentas:
        cuenta.depositar(100)
        print(cuenta.mostrar_saldo())  # cada una lo muestra a su manera

    # Checklist para darlo por completo:
    # [x] Las dos hijas usan super().__init__.
    # [x] CuentaCorriente permite sobregiro dentro del límite y falla fuera.
    # [x] La lista mixta funciona con un solo for.


# =============================================================================
# SLIDE 14 · EXTRA (resueltos)
# =============================================================================

# --- Opción A · figuras ---------------------------------------------------------

class Figura:
    def area(self):
        return 0


class Circulo(Figura):
    def __init__(self, radio):
        super().__init__()  # Figura no tiene __init__ propio: usa el de object
        self.radio = radio

    def area(self):
        return 3.1416 * self.radio ** 2


class Rectangulo(Figura):
    def __init__(self, base, altura):
        super().__init__()
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura


class Cuadrado(Rectangulo):  # un Cuadrado ES UN Rectángulo con lados iguales
    def __init__(self, lado):
        super().__init__(lado, lado)  # reusa todo lo de Rectangulo
    # no hace falta sobreescribir area(): base * altura ya sirve


def extra_figuras():
    titulo("EXTRA A · Figura -> Circulo, Rectangulo, Cuadrado")

    figuras = [Circulo(1), Rectangulo(2, 3), Cuadrado(4)]
    total = 0
    for f in figuras:
        print(f"{type(f).__name__:<10} área = {f.area():.2f}")
        total += f.area()
    print(f"Total: {total:.2f}")

    # Herencia de 3 niveles: Cuadrado -> Rectangulo -> Figura -> object
    print("MRO de Cuadrado:", [c.__name__ for c in Cuadrado.__mro__])


# --- Opción B · empleados -------------------------------------------------------

class Empleado:
    def __init__(self, nombre, sueldo_base):
        self.nombre = nombre
        self.sueldo_base = sueldo_base

    def sueldo(self):
        return self.sueldo_base


class Gerente(Empleado):
    def __init__(self, nombre, sueldo_base, bono):
        super().__init__(nombre, sueldo_base)
        self.bono = bono

    def sueldo(self):
        return super().sueldo() + self.bono


class Desarrollador(Empleado):
    def __init__(self, nombre, sueldo_base, horas_extra, valor_hora):
        super().__init__(nombre, sueldo_base)
        self.horas_extra = horas_extra
        self.valor_hora = valor_hora

    def sueldo(self):
        return super().sueldo() + self.horas_extra * self.valor_hora


def extra_empleados():
    titulo("EXTRA B · Empleado -> Gerente, Desarrollador")

    equipo = [
        Empleado("Ana", 800_000),
        Gerente("Beto", 1_200_000, 300_000),
        Desarrollador("Cami", 1_000_000, 10, 15_000),
    ]
    for e in equipo:
        print(f"{e.nombre:<5} ${e.sueldo():>12,}")

    # Bonus: super().sueldo() + ... evita repetir "self.sueldo_base".
    # Si mañana el sueldo base suma antigüedad, se cambia en Empleado y
    # Gerente y Desarrollador lo heredan sin tocarlos.


# =============================================================================
# SLIDE 15 · CIERRE
# =============================================================================
#
# [x] Herencia: class Hija(Padre). La hija tiene todo lo del padre sin escribirlo.
# [x] super().__init__(...): el padre arma lo suyo; después la hija suma lo propio.
# [x] Sobreescribir: mismo nombre de método -> la versión de la hija gana.
# [x] Polimorfismo: mismo pedido, cada objeto responde a su manera. El for no cambia.
# [x] Criterio: "ES UN" -> heredá. "TIENE UN" -> atributo.
#
# Próxima clase (12): introducción práctica a la IA.


if __name__ == "__main__":
    repaso()
    sin_herencia()
    con_herencia()
    demo_super()
    error_tipico_sin_super()
    super_sin_init_en_la_hija()
    ejercicio_vehiculos()
    demo_sobreescritura()
    demo_super_en_metodo()
    parametros_distintos_rompen()
    ejercicio_animales()
    demo_polimorfismo()
    polimorfismo_en_funciones()
    criterio_es_un_tiene_un()
    ejercicio_integrador()
    extra_figuras()
    extra_empleados()
