v 0.0.0
# calc-Casio-fx991
para comenzar, intentare diseñar una calculadora de escritorio pasando por las 3 fases de arquitectura de software

--

empezare diseñando la estructura de este proyecto en arquitectura de 1 solo modulo.
He de dejar claro que será la evolucion hacia una arquitectura de capas, utilizare python que es el lenguaje que domino con naturalidad, sin embargo como desafio personal utilizare mis conocimientos para realizar una arquitectura en c++ o java, son lenguajes desafiantes para mi persona. en medida de lo posible realizare una programacion de la misma sin el uso de IA para desarrollar mis habilidades de programacion
lo maximo posible.

para comenzar con una documentacion formal (redaccion antes de programar)
el objetivo actual es la redaccion de logica de programacion de funciones y llamado a la funcion
suma, resta, division, multiplicacion. no se tomara en cuenta el problema de punto flotante (por el momento)

--

v0.0.1
tengo un problema respecto a la division,no la puedo implementar de momento de forma compleja, sin embargo se puede ingresar una cantidad de digitos en la lista que se dividira por 2
mi solucion es que si se pide una division se solicite el numero divisor tras la eleccion.

en segundo caso, mi otra solucion era que se implementara una consulta de dos inputs en un bucle, el cual seria consultar el numero y siguiente a ello el operador. se como hacerlo, pero no recuerdo como hacerlo.

en tercer caso, se me ideó la idea de implementar un unico input qur reciba un string de numeros y operadores, el cual "creo" que se deberia sumar con librerias nativas, y con ello el sumar operadores de resta a un numero deberia de formar una operacion de resta o de multiplicacion, ya que como definicion la resta como tal es una suma, pero... no se como manejar una division en este string, la division es una MIERDAA FUCCCK.

realmente no se como solucionar lo de la division, considero que la solucion sea una mezcla entre la solicitud con inputs y la cadena,¿por qué? porque detras, la calculadora ira haciendo los calculos, y trabajaria sobre un string que va cambiando respuesta a respuesta hasta que el usuario solicite el resultado.
15-16/04/2026 escrito a las 00:07


cuarto caso, considere que primero deberia ir la eleccion de operador, luego se deberian insertar los numeros, con ello el usuario sabe de primera instancia lo que hara y como insertar los datos, ademas de que si escoge division la implementacion de solicitud del dividendo sería en teoria mas facil de realizar.

todas estas opciones las pondria en un analisis de requisitos, con ia claramente o con un ser humano de confianza pensante. 00.22 16/04/2026

quinto caso, diseñar la clase calculadora con las funciones como metodos (esto mas a futuro)

sexto caso; todos estos problemas se me reducirian si simplemente opto por un diseño grafico, honestamente si tengo una GUI es claro que se seguiria mas o menos un string o var que se iria modificando con cada boton pulsado o numero insertado.


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

