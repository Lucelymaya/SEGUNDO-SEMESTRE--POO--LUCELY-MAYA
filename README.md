# Función para ingresar las temperaturas diarias
def ingresar_temperaturas():
    temperaturas = []
    for i in range(7):  # 7 días de la semana
        temp = float(input(f"Ingrese la temperatura del día {i+1}: "))
        temperaturas.append(temp)
    return temperaturas

# Función para calcular el promedio semanal de las temperaturas
def calcular_promedio(temperaturas):
    return sum(temperaturas) / len(temperaturas)

# Función principal
def main():
    print("Programa para calcular el promedio semanal del clima")
    temperaturas = ingresar_temperaturas()
    promedio = calcular_promedio(temperaturas)
    print(f"El promedio semanal de las temperaturas es: {promedio:.2f}°C")

if __name__ == "__main__":
    main()