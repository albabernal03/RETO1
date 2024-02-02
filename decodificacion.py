def atbash_decodificar(texto):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    alfabeto_invertido = alfabeto[::-1]
    decodificado = ''
    for caracter in texto:
        if caracter.lower() in alfabeto:
            indice = alfabeto.index(caracter.lower())
            if caracter.isupper():
                decodificado += alfabeto_invertido[indice].upper()
            else:
                decodificado += alfabeto_invertido[indice]
        else:
            decodificado += caracter
    return decodificado.lower()

# Ejemplo de uso
mensaje_codificado = "GSVUOZTRHHZBDVZIVXIZAB"
mensaje_decodificado = atbash_decodificar(mensaje_codificado)
print("Mensaje decodificado:", mensaje_decodificado)