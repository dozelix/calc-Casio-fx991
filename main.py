import math

# Implementación con pila LIFO (stack)
stack = []

def push(value):
    stack.append(value)

def pop_value():
    if not stack:
        raise IndexError("Pila vacía")
    return stack.pop()

def do_binary(op):
    try:
        b = pop_value()
        a = pop_value()
    except IndexError:
        print("Error: no hay suficientes operandos en la pila.")
        return

    try:
        if op in ('+', 'suma'):
            res = a + b
        elif op in ('-', 'resta'):
            res = a - b
        elif op in ('*', 'multiplicacion'):
            res = a * b
        elif op in ('/', 'division'):
            if b == 0:
                print("Error: división por cero no permitida.")
                # devolver operandos a la pila en su orden original
                push(a)
                push(b)
                return
            res = a / b
        else:
            print(f"Operación '{op}' no reconocida.")
            push(a)
            push(b)
            return
    except Exception as e:
        print(f"Error al realizar la operación: {e}")
        push(a)
        push(b)
        return

    push(res)
    print(f"Resultado: {res}. Pila actual: {stack}")


def show_help():
    print("""
Modo de uso (LIFO stack):
- Ingresar números (ej: 3, 4.2) para apilarlos.
- Ingresar operador (+, -, *, /) o palabras (suma, resta, multiplicacion, division) para aplicar la operación a los dos últimos elementos de la pila.
- Comandos: 'pila' para mostrar la pila, 'limpiar' para vaciarla, 'ayuda' para este mensaje, 'salir' para terminar.
""")


def main():
    print("Calculadora usando pila LIFO (RPN-like). Escriba 'ayuda' para más información.")
    show_help()

    while True:
        entrada = input("Entrada: ").strip().lower()
        if not entrada:
            continue

        if entrada == 'salir':
            print("¡Gracias por usar la calculadora! Hasta luego.")
            break
        elif entrada in ('pila', 'stack'):
            print(f"Pila: {stack}")
            continue
        elif entrada in ('limpiar', 'clear'):
            stack.clear()
            print("Pila vaciada.")
            continue
        elif entrada in ('ayuda', 'help'):
            show_help()
            continue
        elif entrada in ('+', '-', '*', '/', 'suma', 'resta', 'multiplicacion', 'division'):
            do_binary(entrada)
            continue

        # intentar convertir a número
        try:
            numero = float(entrada)
            push(numero)
            print(f"Número apilado. Pila: {stack}")
        except ValueError:
            print("Entrada inválida. Escriba 'ayuda' para información de uso.")


if __name__ == '__main__':
    main()
