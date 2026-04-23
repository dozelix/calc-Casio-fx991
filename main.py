from calculator import Calculator


def show_help():
    print("""
Modo de uso (CLI -> lógica en Calculator):
- Ingresar números (ej: 3, 4.2) para apilarlos.
- Operadores binarios (consumen 2 elementos): +, -, *, / (o suma, resta, multiplicacion, division).
- Operaciones n-arias (actúan sobre toda la pila): suma_todos, resta_todos, multiplicacion_todos, division_todos.
- Comandos: 'pila' para mostrar la pila, 'limpiar' para vaciarla, 'ayuda' para este mensaje, 'salir' para terminar.
""")


def main():
    calc = Calculator()
    print("Calculadora usando clase Calculator (pila LIFO). Escriba 'ayuda' para más información.")
    show_help()

    while True:
        entrada = input("Entrada: ").strip()
        if not entrada:
            continue

        cmd = entrada.lower()
        if cmd == 'salir':
            print("¡Gracias por usar la calculadora! Hasta luego.")
            break
        if cmd in ('pila', 'stack'):
            print(f"Pila: {calc.get_stack()}")
            continue
        if cmd in ('limpiar', 'clear'):
            calc.clear()
            print("Pila vaciada.")
            continue
        if cmd in ('ayuda', 'help'):
            show_help()
            continue

        # binarios
        if cmd in ('+', '-', '*', '/', 'suma', 'resta', 'multiplicacion', 'division'):
            try:
                res = calc.binary(cmd)
                # después de calcular, el método binary no re-apila el resultado; lo hacemos aquí
                calc.push(res)
                print(f"Resultado: {res}. Pila: {calc.get_stack()}")
            except IndexError:
                print("Error: no hay suficientes operandos en la pila.")
            except ZeroDivisionError:
                print("Error: División por cero no permitida.")
            except Exception as e:
                print(f"Error: {e}")
            continue

        # n-arias
        if cmd in ('suma_todos', 'sumar_todos', 'suma_all', 'sumar',
                   'resta_todos', 'restar_todos',
                   'multiplicacion_todos', 'producto_todos', 'producto',
                   'division_todos', 'dividir_todos'):
            try:
                res = calc.nary(cmd)
                print(f"Resultado n-ario: {res}. Pila: {calc.get_stack()}")
            except IndexError:
                print("Error: pila vacía.")
            except ZeroDivisionError:
                print("Error: división por cero en los elementos de la pila.")
            except Exception as e:
                print(f"Error: {e}")
            continue

        # intentar número
        try:
            num = float(entrada)
            calc.push(num)
            print(f"Número apilado. Pila: {calc.get_stack()}")
        except ValueError:
            print("Entrada inválida. Escriba 'ayuda' para información de uso.")


if __name__ == '__main__':
    main()
