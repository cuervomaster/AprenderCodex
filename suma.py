"""Modulo de ejemplo que contiene una funcion para sumar dos numeros."""


def suma(a, b):
    """Devuelve la suma de dos numeros."""
    return a + b


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Uso: python suma.py num1 num2")
    else:
        numero1 = float(sys.argv[1])
        numero2 = float(sys.argv[2])
        print(suma(numero1, numero2))

