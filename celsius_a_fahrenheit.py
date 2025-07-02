# Convierte grados Celsius a Fahrenheit y muestra el resultado

def celsius_a_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


def main():
    try:
        celsius = float(input("Introduce la temperatura en grados Celsius: "))
    except ValueError:
        print("Por favor, introduce un número válido.")
        return
    fahrenheit = celsius_a_fahrenheit(celsius)
    print(f"{celsius} °C equivalen a {fahrenheit} °F")


if __name__ == "__main__":
    main()
