# RETO

El cifrado afín es un tipo de cifrado que usa el mismo alfabeto para el texto plano que para el texto cifrado que utiliza una expresión matemática para determinar la posición en el alfabeto (según el orden normal) del carácter del texto cifrado asociado. En este cifrado la clave viene definida por dos valores numéricos a y b. Sea m el tamaño de alfabeto del texto plano. Para definir qué carácter del alfabeto sustituye a cada carácter se aplica la fórmula:


**C(x) = (ax + b) \mod m**


donde x es la posición del carácter al que le estamos buscando sustituto. El resultado se usa como índice en el orden predefinido del alfabeto.

***

El cifrado de Atbash es un cifrado simple donde cada letra del alfabeto se sustituye por su opuesta en el extremo opuesto del mismo alfabeto. En el caso del alfabeto latino, la letra A se sustituye por la Z, la B por la Y, y así sucesivamente.

Dado que el cifrado de Atbash no utiliza una clave como el cifrado afín, no hay valores específicos de a y b para definir. Simplemente, se invierte el orden de las letras.


En el cifrado de Atbash, la transformación se realiza mediante una función de mapeo que invierte el orden de las letras en el alfabeto. Matemáticamente, esta función puede expresarse de la siguiente manera:

Dado un alfabeto A de longitud m, y una letra original x en el alfabeto, la letra cifrada y en el cifrado de Atbash puede expresarse mediante la siguiente función:

**y = m - (x - 1)**

Aquí, x es la posición original de la letra en el alfabeto (por ejemplo, A=1, B=2, ..., Z=26), y y es la posición de la letra cifrada en el alfabeto invertido.
