def cifrado_atbash(texto):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    resultado = ""
    
    for char in texto:
        if char.isalpha():  # Solo procesa letras, ignora otros caracteres
            if char.islower():
                posicion_original = ord(char) - ord('a') + 1
                posicion_cifrada = 27 - posicion_original
                resultado += chr(posicion_cifrada - 1 + ord('a'))
            elif char.isupper():
                posicion_original = ord(char) - ord('A') + 1
                posicion_cifrada = 27 - posicion_original
                resultado += chr(posicion_cifrada - 1 + ord('A'))
        else:
            resultado += char  # Mantiene caracteres no alfabéticos sin cambios
    
    return resultado

def descifrado_atbash(texto_cifrado):
    return cifrado_atbash(texto_cifrado)

mensaje_codificado = "GSVUOZTRHHZBDVZIVXIZAB"
mensaje_decodificado = descifrado_atbash(mensaje_codificado)

print("Mensaje decodificado:", mensaje_decodificado)