print('*** Ciclo for ***')

print('Recorremos los caracteres de una cadena')
cadena = 'Hola Mundo'
# iteramos los caracteres
for index, letra in enumerate(cadena):
    print(f'Index: {index}', f'Letra: {letra}', end='\n')

print('\n\nRecorremos la lista de frutas:')
frutas = ['Plátano', 'Fresa', 'Mango']
for fruta in frutas:
    print(fruta, end=' ')