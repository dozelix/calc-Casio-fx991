from functools import reduce
import math
numeros = []


def suma(numeros):
    return math.fsum(numeros)

def resta(numeros):
    return reduce(lambda x, y: x - y, numeros)

def multiplicacion(numeros):
    return math.prod(numeros)

def division(numeros,divisor):
    return [x / divisor for x in numeros]

operaciones = {
    "suma": suma,
    "resta": resta,
    "multiplicacion": multiplicacion,
    "division": division
}

while True:
    while True:
        num = input(("Ingrese un número u operador (o 'salir' para terminar): ")).lower()
        if num.isdigit():
            numeros.append(float(num))
        elif num == "salir":
            break
        elif not num.strip() or num.isalpha():
            print("La respuesta no puede estar en blanco o contener letras. Por favor, ingrese un número válido.")

    while True:
        operation = input("Ingrese la operación que desea realizar (suma, resta, multiplicacion, division): ").lower().strip()
        if operation in operaciones:
            try:
                result = operaciones[operation](numeros)
            except ZeroDivisionError:
                result = None
                print("Error: División por cero no permitida.")
            except Exception as e:
                result = None
                print(f"Error al realizar la operación: {e}")
        else:
            print(f"Operación '{operation}' no válida.")
            result = None

            
        break
    print(f"El resultado de la {operation} es: {result}")

    again = input("¿Desea realizar otra operación? (s/n): ").lower().strip()
    if again == "s":
        numeros.clear()
        continue
    elif again == "n":
        print("¡Gracias por usar la calculadora! ¡Hasta luego!")
        exit()
    else:
        print("Respuesta no válida. Por favor, ingrese 's(sí)' o 'n(no)'.")