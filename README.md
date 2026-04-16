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

tengo un problema respecto a la division,no la puedo implementar de momento de forma compleja, sin embargo se puede ingresar una cantidad de digitos en la lista que se dividira por 2
mi solucion es que si se pide una division se solicite el numero divisor tras la eleccion.

en segundo caso, mi otra solucion era que se implementara una consulta de dos inputs en un bucle, el cual seria consultar el numero y siguiente a ello el operador. se como hacerlo, pero no recuerdo como hacerlo.

en tercer caso, se me ideó la idea de implementar un unico input qur reciba un string de numeros y operadores, el cual "creo" que se deberia sumar con librerias nativas, y con ello el sumar operadores de resta a un numero deberia de formar una operacion de resta o de multiplicacion, ya que como definicion la resta como tal es una suma, pero... no se como manejar una division en este string, la division es una MIERDAA FUCCCK.

realmente no se como solucionar lo de la division, considero que la solucion sea una mezcla entre la solicitud con inputs y la cadena,¿por qué? porque detras, la calculadora ira haciendo los calculos, y trabajaria sobre un string que va cambiando respuesta a respuesta hasta que el usuario solicite el resultado.
15-16/04/2026 escrito a las 00:07


