cadena = "Hola Mundo"
vocales = ['a', 'e', 'i', 'o', 'u']
contador = 0

for letter in cadena:
    if letter.lower() in vocales:
        contador += 1

print(contador)