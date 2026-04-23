Backlog de tests unitarios (v0.0.3)

Objetivo: dejar una lista priorizada de tests unitarios y un conjunto básico de tests automatizados para la clase Calculator.

Prioridad alta (deben existir ya):
- test-push-pop: validar push(), pop() y get_stack() con floats y strings convertibles.
- test-binary-ops: validar operaciones binarias básicas (+, -, *, /) y que devuelven el resultado correcto.
- test-binary-insufficient-operands: validar que binary() lanza IndexError con menos de 2 operandos.
- test-binary-div-zero: validar que división por cero en binary() lanza ZeroDivisionError y restaura la pila.
- test-nary-ops: validar suma/producto/resta/división sobre toda la pila y que dejan el resultado como único elemento.
- test-nary-div-zero: validar que división por cero en n-ary no modifica la pila y lanza ZeroDivisionError.

Prioridad media:
- test-clear-and-state: validar clear() y que get_stack() devuelve copia y no referencia.
- test-sequence-operations: secuencia de operaciones mixtas (push, binario, n-ario) y validar estado final.

Prioridad baja / integraciones:
- test-cli-integration: ejecutar main.py en subprocess con entradas simuladas y validar salidas (smoke tests).
- test-edge-floats: casos con floats especiales (inf, nan) y comportamiento definido.

Notas:
- Implementar estos tests con pytest. Mantener tests determinísticos y aislados.
- Añadir CI (GitHub Actions) que ejecute pytest en cada PR.

Archivo generado automáticamente como backlog de tests unitarios para la v0.0.3.
