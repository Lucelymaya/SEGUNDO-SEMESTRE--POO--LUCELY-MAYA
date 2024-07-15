# Definición de Clase y Herencia
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def mostrar_identificacion(self):
        return f"Vehículo de marca {self.marca}, modelo {self.modelo}"

class Coche(Vehiculo):
    def __init__(self, marca, modelo, numero_de_puertas):
        super().__init__(marca, modelo)
        self.numero_de_puertas = numero_de_puertas

    def mostrar_detalles(self):
        informacion_base = super().mostrar_identificacion()
        return f"{informacion_base}, con {self.numero_de_puertas} puertas"

# Creando un objeto de la clase Vehiculo
mi_vehiculo = Vehiculo("Toyota", "Corolla")
print(mi_vehiculo.mostrar_identificacion())

# Creando un objeto de la clase Coche
mi_coche = Coche("Honda", "Civic", 4)
print(mi_coche.mostrar_detalles())

# Definición de Clase y Encapsulación
class CuentaBancaria:
    def __init__(self, saldo_inicial):
        self.__saldo = saldo_inicial  # Atributo privado

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Depositado: {cantidad}. Nuevo saldo: {self.__saldo}")
        else:
            print("Cantidad a depositar debe ser positiva.")

    def retirar(self, cantidad):
        if cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print(f"Retirado: {cantidad}. Nuevo saldo: {self.__saldo}")
        else:
            print("Fondos insuficientes para el retiro.")

    def obtener_saldo(self):  # Método 'getter' para el saldo
        return self.__saldo

# Creando un objeto de la clase CuentaBancaria
mi_cuenta = CuentaBancaria(1000)

# Utilizando los métodos de la clase
print(f"Saldo inicial: {mi_cuenta.obtener_saldo()}")
mi_cuenta.depositar(500)
mi_cuenta.retirar(200)
print(f"Saldo final: {mi_cuenta.obtener_saldo()}")

# Polimorfismo
class DispositivoElectronico:
    def encender(self, modo='normal'):
        if modo == 'normal':
            return "Dispositivo electrónico encendido en modo normal"
        elif modo == 'eco':
            return "Dispositivo electrónico encendido en modo ecológico"
        else:
            return "Modo no reconocido, dispositivo electrónico encendido en modo normal"

# Creando un objeto de la clase DispositivoElectronico
mi_dispositivo = DispositivoElectronico()

# Utilizando el método con diferentes argumentos
print(mi_dispositivo.encender())  # Sin especificar modo
print(mi_dispositivo.encender('eco'))  # Modo ecológico
print(mi_dispositivo.encender('rápido'))  # Modo no reconocido

# Explicación del código:
#
# 1. Clase Vehiculo:
#    - Definición de la clase base Vehiculo con un constructor que inicializa los atributos 'marca' y 'modelo'.
#    - Método mostrar_identificacion para devolver la información del vehículo.
# 2. Clase Coche:
#    - Herencia de la clase Vehiculo.
#    - Constructor que llama al constructor de la clase base con super() y añade el atributo 'numero_de_puertas'.
#    - Método mostrar_detalles que amplía el comportamiento de mostrar_identificacion.
# 3. Clase CuentaBancaria:
#    - Definición de la clase con un atributo privado '__saldo'.
#    - Métodos depositar y retirar para modificar el saldo con validaciones.
#    - Método obtener_saldo como 'getter' para el saldo.
# 4. Clase DispositivoElectronico:
#    - Método encender que utiliza polimorfismo para cambiar el comportamiento según el argumento 'modo'.
# 5. Creación y uso de objetos:
#    - Se crean instancias de cada clase y se utilizan sus métodos para demostrar encapsulación, herencia y polimorfismo.
