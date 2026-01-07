"""
===========================================================
SCRIPT DE ESTUDIO: ENCAPSULACIÓN Y @property EN PYTHON
===========================================================

Este archivo explica y demuestra:

1. Qué es encapsulación
2. Qué son atributos privados (__)
3. Qué es @property
4. Qué es un setter (@propiedad.setter)
5. Qué es una property de solo lectura
6. Qué es una property calculada
7. Cómo interactúa raise con @property
8. Flujo real de ejecución

Lee este archivo de arriba hacia abajo.
===========================================================
"""


class CuentaSinEncapsulacion:
    def __init__(self, saldo):
        # El saldo es público → cualquiera puede modificarlo
        self.saldo = saldo


# Esto es peligroso:
cuenta_mala = CuentaSinEncapsulacion(1000)
cuenta_mala.saldo = -5000  # Python lo permite 😬


# =========================================================
# 2. ATRIBUTOS PRIVADOS (__)
# =========================================================

class CuentaBase:
    def __init__(self, saldo):
        # __saldo es un atributo privado (name mangling)
        self.__saldo = saldo


# Desde afuera NO se puede acceder directamente:
cuenta_base = CuentaBase(1000)
# cuenta_base.__saldo  ❌ AttributeError


# =========================================================
# 3. @property → LECTURA CONTROLADA
# =========================================================

class CuentaLectura:
    def __init__(self, saldo):
        self.__saldo = saldo

    @property
    def saldo(self):
        """
        Este método se comporta como un atributo.

        Cuando alguien escribe:
            cuenta.saldo

        Python ejecuta internamente:
            cuenta.saldo()
        """
        return self.__saldo


cuenta = CuentaLectura(1000)
print("Saldo (solo lectura):", cuenta.saldo)

# cuenta.saldo = 500  ❌ No existe setter → AttributeError


# =========================================================
# 4. @property + @setter → ESCRITURA CONTROLADA
# =========================================================

class CuentaSegura:
    def __init__(self, saldo):
        self.__saldo = saldo

    @property
    def saldo(self):
        """
        Getter:
        Permite consultar el saldo.
        """
        return self.__saldo

    @saldo.setter
    def saldo(self, valor):
        """
        Setter:
        Se ejecuta cuando alguien hace:
            cuenta.saldo = valor

        Aquí se validan reglas de negocio.
        """
        if valor < 0:
            # raise detiene la ejecución inmediatamente
            raise ValueError("El saldo no puede ser negativo")

        self.__saldo = valor


cuenta = CuentaSegura(1000)
cuenta.saldo = 1500        # OK
print("Saldo actualizado:", cuenta.saldo)

# cuenta.saldo = -200      # 💥 ValueError


# =========================================================
# 5. raise Y FLUJO DE EJECUCIÓN
# =========================================================

def ejemplo_raise(valor):
    print("Inicio de la función")

    if valor < 0:
        raise ValueError("Valor inválido")

    print("Esto SOLO se ejecuta si no hay error")


# ejemplo_raise(-1)  # La función se corta antes del último print


# =========================================================
# 6. MÉTODOS PRIVADOS + @property (DISEÑO REAL)
# =========================================================

class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular          # público
        self.__saldo = saldo_inicial    # privado
        self.__activa = True            # privado

    @property
    def saldo(self):
        """
        Property de solo lectura.
        El saldo NO se modifica directamente.
        """
        return self.__saldo

    def depositar(self, monto):
        """
        Método público que define el flujo:
        1. Validar cuenta
        2. Validar monto
        3. Modificar estado
        """
        self.__validar_cuenta_activa()
        self.__validar_monto(monto)

        self.__saldo += monto

    def retirar(self, monto):
        self.__validar_cuenta_activa()
        self.__validar_monto(monto)

        if monto > self.__saldo:
            raise ValueError("Fondos insuficientes")

        self.__saldo -= monto

    # ---------------------------
    # MÉTODOS PRIVADOS
    # ---------------------------

    def __validar_monto(self, monto):
        """
        Método privado:
        No puede llamarse desde afuera.
        """
        if monto <= 0:
            raise ValueError("El monto debe ser mayor a cero")

    def __validar_cuenta_activa(self):
        if not self.__activa:
            raise RuntimeError("La cuenta está inactiva")


# =========================================================
# 7. USO REAL DE LA CLASE
# =========================================================

cuenta = CuentaBancaria("Juan", 1000)

print("Saldo inicial:", cuenta.saldo)

cuenta.depositar(500)
print("Saldo tras depósito:", cuenta.saldo)

cuenta.retirar(300)
print("Saldo tras retiro:", cuenta.saldo)

# cuenta.depositar(-100)  # 💥 Error controlado
# cuenta.retirar(5000)    # 💥 Fondos insuficientes


# =========================================================
# 8. PROPERTY CALCULADA
# =========================================================

class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    @property
    def area(self):
        """
        No existe self.area.
        Se calcula cada vez que se consulta.
        """
        return self.ancho * self.alto


r = Rectangulo(4, 5)
print("Área del rectángulo:", r.area)


# =========================================================
# 9. RESUMEN FINAL (MENTAL)
# =========================================================
"""
- __atributo     → protege el estado
- @property      → lectura segura
- @setter        → escritura validada
- raise          → corta ejecución si una regla falla
- Métodos públicos → definen el flujo
- Métodos privados → aplican reglas internas

Esto es encapsulación real en Python.
"""
