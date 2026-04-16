def suma(num, num2):
    return num + num2
def resta(num, num2):
    return num - num2
def multiplicacion(num, num2):
    return num * num2
def division(num, num2):
    if num2 != 0:
        return num / num2
    else:
        return "Error: No se puede dividir por cero"
num = int(input("ingresar numero: "))
num2 = int(input("ingresar numero: "))
operation = input("Ingrese la operación que desea realizar (suma, resta, multiplicacion, division): ").lower()
if operation == "suma":
    result = suma(num, num2)
elif operation == "resta":
    result = resta(num, num2)
elif operation == "multiplicacion":
    result = multiplicacion(num, num2)
elif operation == "division":
    result = division(num, num2)
else:    result = "Operación no válida"

print(f"El resultado de la {operation} es: {result}")