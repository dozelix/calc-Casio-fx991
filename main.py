from functools import reduce
import math
numeros:float = []

def suma(numeros):
    return sum(numeros)

def resta(numeros):
    return reduce(lambda x, y: x - y, numeros)

def multiplicacion(numeros):
    return math.prod(numeros)

def division(numeros):
    return [x / 2 for x in numeros]
    

while True:    
        num = input("Ingrese un número (o 'salir' para terminar): ").lower()
        if num.isdigit():
            numeros.append(float(num))
        if num == "salir":
            break
        elif not num.strip() or num.isalpha():
            print("La respuesta no puede estar en blanco o contener letras. Por favor, ingrese un número válido.")


while True:
        operation = input("Ingrese la operación que desea realizar (suma, resta, multiplicacion, division): ").lower().strip()
        if operation not in ["suma", "resta", "multiplicacion", "division"]:
            print("Operación no válida. Por favor, ingrese una operación válida.")
            continue
        elif operation == "suma":
            result = suma(numeros)
        elif operation == "resta":
            result = resta(numeros)
        elif operation == "multiplicacion":
            result = multiplicacion(numeros)
        elif operation == "division":
            result = division(numeros)
        break

    

print(f"El resultado de la {operation} es: {result}")
    

    
    

