v0.0.2 - Documentación nueva: Cambio a pila LIFO y operaciones n-arias

Resumen de cambios:
- main.py ahora usa una pila LIFO (stack) para almacenar operandos en lugar de un array global acumulativo.
- Soporte para operaciones binarias RPN-like (consumen los 2 últimos elementos): +, -, *, / (también aceptan nombres en español: suma, resta, multiplicacion, division).
- Soporte para operaciones n-arias que actúan sobre toda la pila y dejan el resultado como único elemento: suma_todos, resta_todos, multiplicacion_todos, division_todos.

Cómo usar (ejemplos):
- Apilar números: escribir 3<enter>, 4<enter>
- Operación binaria: escribir +  (suma 4 y 3 => apila 7)
- Operación n-aria: apilar 1, 2, 3 y escribir suma_todos => deja [6]
- Ver la pila: escribir pila
- Vaciar la pila: escribir limpiar

Consideraciones de diseño y próximas mejoras (según feedback del autor):
- Refactorizar operadores para seguir principios SRP/DRY/POO y facilitar porte a móvil.
- Separar lógica de UI (entrada/salida) de la lógica de cálculo en módulos/clases.
- Añadir tests unitarios para operaciones binarias y n-arias.

Notas técnicas:
- Las operaciones n-arias respetan el orden de apilado para las operaciones no conmutativas (resta y división). Por ejemplo, con pila [a, b, c] (a fue apilado antes que b y c), resta_todos resulta en a - b - c.
- En caso de división por cero durante una operación n-aria, se aborta y la pila no se modifica.

Archivo añadido por automatización; no modifica README.md existente.
