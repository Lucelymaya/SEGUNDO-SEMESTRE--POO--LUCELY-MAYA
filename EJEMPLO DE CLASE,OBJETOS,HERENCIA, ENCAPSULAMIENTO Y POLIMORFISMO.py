# Este programa gestiona información de vehículos utilizando conceptos de POO:
# Definición de Clase, Definición de Objeto, Herencia, Encapsulación y Polimorfismo.

class Vehiculo:
    """
    Clase base para representar un vehículo.
    """

    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def descripcion(self):
        """
        Método que retorna la descripción del vehículo.
        """
        return f"{self.marca} {self.modelo} del año {self.año}"

    def arrancar(self):
        """
        Método que simula el arranque del vehículo.
        """
        return f"El {self.marca} {self.modelo} está funcionando perfectamente y es muy comodo."


class Coche(Vehiculo):
    """
    Clase derivada que representa un coche, hereda de Vehiculo.
    """

    def __init__(self, marca, modelo, año, puertas):
        # Llamar al constructor de la clase base
        super().__init__(marca, modelo, año)
        # Atributo encapsulado
        self.__puertas = puertas

    def descripcion(self):
        """
        Método sobrescrito que incluye el número de puertas en la descripción.
        """
        return f"{self.marca} {self.modelo} del año {self.año} con {self.__puertas} puertas"

    def obtener_puertas(self):
        """
        Método getter para acceder al atributo encapsulado __puertas.
        """
        return self.__puertas

    def arrancar(self):
        """
        Método sobrescrito para incluir un mensaje específico para coches.
        """
        return f"El coche {self.marca} {self.modelo} está funcionando perfectamente."


def main():
    # Crear una instancia de Vehiculo
    vehiculo = Vehiculo("Toyota", "Jeep BJ", 1951)
    print(vehiculo.descripcion())
    print(vehiculo.arrancar())

    # Crear una instancia de Coche
    coche = Coche("Ford", "Mustang", 2021, 4)
    print(coche.descripcion())
    print(coche.arrancar())
    print(f"El coche tiene {coche.obtener_puertas()} puertas.")


# Ejecutar la función principal
if __name__ == "__main__":
    main()

