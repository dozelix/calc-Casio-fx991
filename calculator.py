import math

class Calculator:
    """Calculator encapsula la pila LIFO y las operaciones (binarias y n-arias)."""
    def __init__(self):
        self.stack = []

    def push(self, value):
        # Acepta float o str convertible
        self.stack.append(float(value))

    def pop(self):
        if not self.stack:
            raise IndexError("Pila vacía")
        return self.stack.pop()

    def clear(self):
        self.stack.clear()

    def get_stack(self):
        return list(self.stack)

    # Operación binaria LIFO: consume dos últimos elementos (a, b) y devuelve resultado
    def binary(self, op):
        b = self.pop()
        a = self.pop()

        if op in ('+', 'suma'):
            return a + b
        if op in ('-', 'resta'):
            return a - b
        if op in ('*', 'multiplicacion'):
            return a * b
        if op in ('/', 'division'):
            if b == 0:
                # restaurar estado por consenso: push a y b de nuevo
                self.push(a)
                self.push(b)
                raise ZeroDivisionError('División por cero')
            return a / b

        # comando no reconocido: restaurar operandos y elevar
        self.push(a)
        self.push(b)
        raise ValueError(f"Operación binaria desconocida: {op}")

    # Operación n-aria: aplica sobre todos los elementos de la pila
    def nary(self, op):
        if not self.stack:
            raise IndexError('Pila vacía')

        values = self.stack.copy()

        if op in ('suma_todos', 'sumar_todos', 'suma_all', 'sumar'):
            res = math.fsum(values)
        elif op in ('multiplicacion_todos', 'producto_todos', 'producto'):
            res = math.prod(values)
        elif op in ('resta_todos', 'restar_todos'):
            res = values[0]
            for v in values[1:]:
                res -= v
        elif op in ('division_todos', 'dividir_todos'):
            res = values[0]
            for v in values[1:]:
                if v == 0:
                    raise ZeroDivisionError('División por cero en elementos de la pila')
                res /= v
        else:
            raise ValueError(f"Operación n-aria desconocida: {op}")

        # Reemplazar pila por el resultado único
        self.clear()
        self.push(res)
        return res
