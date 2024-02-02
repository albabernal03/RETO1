# RETO1

El cifrado afín es un tipo de cifrado que usa el mismo alfabeto para el texto plano que para el texto cifrado que utiliza una expresión matemática para determinar la posición en el alfabeto (según el orden normal) del carácter del texto cifrado asociado.
En este cifrado la clave viene definida por dos valores numéricos a y b. Sea m el tamaño de alfabeto del texto plano. Para definir qué carácter del alfabeto sustituye a cada carácter se aplica la fórmula:
**C(x) = (ax + b) \mod m**
donde x es la posición del carácter al que le estamos buscando sustituto. El resultado se usa como índice en el orden predefinido del alfabeto.
***
Fórmula de descifrado:
D(y) = a^{-1} \cdot (y - b) \mod m


