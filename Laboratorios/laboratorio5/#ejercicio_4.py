#ejercicio_4
import math

def impedancia():
    print("Calculadora de Impedancia")
    try:
        r = input("Ingrese resistencia: ")
        x = input("Ingrese reactancia: ")

        r = float(r)
        x = float(x)

        zz = math.sqrt(r**2 + x**2)

    except ValueError:
        print("Error.")
    else:
        print(f"La magnitud de la impedancia es: {zz:.2f} Ohm.")

if __name__ == "__main__":
    impedancia()