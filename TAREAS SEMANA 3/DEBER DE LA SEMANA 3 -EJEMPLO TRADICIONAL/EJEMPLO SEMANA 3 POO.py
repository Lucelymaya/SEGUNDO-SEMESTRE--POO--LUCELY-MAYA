class Clima:
    def __init__(self):
        self.temperaturas = []

    def ingresar_temperatura(self, temperatura):
        """
        Método para ingresar una temperatura diaria.
        """
        self.temperaturas.append(temperatura)

    def calcular_promedio_semanal(self):
        """
        Método para calcular el promedio semanal de las temperaturas ingresadas.
        """
        if len(self.temperaturas) == 0:
            return 0
        return sum(self.temperaturas) / len(self.temperaturas)


def main():
    print("Programa para calcular el promedio semanal de temperaturas usando POO\n")

    clima = Clima()  # Creamos una instancia de la clase Clima

    # Ingreso de temperaturas diarias
    dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
    for dia in dias_semana:
        while True:
            try:
                temperatura = float(input(f"Ingrese la temperatura para el día {dia}: "))
                clima.ingresar_temperatura(temperatura)
                break
            except ValueError:
                print("Por favor, ingrese un número válido.")

    # Cálculo del promedio semanal
    promedio = clima.calcular_promedio_semanal()

    print("\nEl promedio semanal de temperaturas es: {:.2f}".format(promedio))


if __name__ == "__main__":
    main()
