def es_palindromo(texto):
    # Paso 1: Filtrar el texto para conservar solo caracteres alfanuméricos
    texto_filtrado = ''.join(caracter for caracter in texto if caracter.isalnum())
    
    # Paso 2: Sustituir los caracteres acentuados por su equivalente sin acento
    texto_filtrado = texto_filtrado.lower()  # Convertir a minúsculas para tratar acentos
    
    # Paso 3: Convertir todas las letras a minúsculas
    texto_filtrado = texto_filtrado.replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u')
    
    # Paso 4: Verificar si el texto filtrado es igual a su imagen reflejada
    return texto_filtrado == texto_filtrado[::-1]

# Pedir al usuario que ingrese la frase
frase = input("Ingresa una frase para verificar si es un palíndromo: ")

# Verificar si es un palíndromo
if es_palindromo(frase):
    print(f'"{frase}" es un palíndromo.')
else:
    print(f'"{frase}" no es un palíndromo.')
