def ingresar_temperaturas():
    temperaturas = []
    dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']

    for dia in dias_semana:
        temperatura = float(input(f"Ingrese la temperatura para el día {dia}: "))
        temperaturas.append(temperatura)

    return temperaturas


def calcular_promedio_semanal(temperaturas):
    suma_temperaturas = sum(temperaturas)
    promedio = suma_temperaturas / len(temperaturas)
    return promedio


def main():
    print("Programa para calcular el promedio semanal de temperaturas\n")

    temperaturas = ingresar_temperaturas()
    promedio = calcular_promedio_semanal(temperaturas)

    print("\nLas temperaturas ingresadas fueron:", temperaturas)
    print(f"El promedio semanal de temperaturas es: {promedio:.2f}")


if __name__ == "__main__":
    main()