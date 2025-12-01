"""
    las listas tambien pueden almacenar
    numeros y de echo, son ideales para esto.
    python ofrece una gran cantidad de 
    herramientas que ayudan a trabajar
    eficiente listas de numeros.
"""

# Meetodo built - in range()
"""
    El meodo range() nos ayuda a crear facilmente
    series de numeros:

    Ejemplos:
"""

print("numeros del 0 al 9")
for value in range(10): # 10 numeros entre el 0-9
    print(value)

print("numeros del 1 al 9")
for value in range(1,10): # 10 numeros entre el 1-9
    print(value)

print("Numeros impares del 1 al 9")
for value in range(1,10,2): # 10 numeros entre el 1-9
    print(value)
odd_numbers = list(range(1,10,2))
print(odd_numbers)

print("Numeros pares del 1 al 9")
for value in range(0,10,2): # 10 numeros entre el 1-9
    print(value)
even_numbers = list(range(0,10,2))
print(even_numbers)

print("Tabla del 9")
for value in range(0,91,9): # 10 numeros entre el 1-9
    print(value)
tabla_del_9 = list(range(0,91,9))
print(tabla_del_9)


# Cuadrados de los  primeros 10 numeros
squares = []
for number in range(1,11):
    square = number**2
    squares.append(square)
print(squares)

## Mas metodos built-in
# Metodos min()
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits)) # Salida: 0

# Metodos max()
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(max(digits)) # Salida: 9

# Metodos sum()
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(sum(digits)) # Salida: 45

