class ClimaDiario:
    def __init__(self):
        self.temperaturas = []

    def ingresar_temperaturas(self):
        for dia in range(7):
            temperatura = float(input(f"Ingrese la temperatura del día {dia + 1}: "))
            self.temperaturas.append(temperatura)

    def calcular_promedio_semanal(self):
        suma_temperaturas = sum(self.temperaturas)
        promedio = suma_temperaturas / len(self.temperaturas)
        return promedio

def main():
    clima = ClimaDiario()
    print("Entrada de temperaturas diarias:")
    clima.ingresar_temperaturas()
    promedio = clima.calcular_promedio_semanal()
    print(f"El promedio semanal de temperaturas es: {promedio:.2f}°C")

if __name__ == "__main__":
    main()