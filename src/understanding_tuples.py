# Tuples
"""
    Las tuplas son listas de elementos que no
    cambian de tamaño. Las tuples son INMUTABLES.

    Se utilizan los () para definir una tupla.
"""

Rectangle_measurements = (200, 50) # (largo, ancho)
print(Rectangle[0])
print(Rectangle[1])


for measure in Rectangle_measurements:
    print(measure)

print(dir(Rectangle_measurements)) # built-in dir

# Regresando tantito a las listas
cars = ["bwm", "porche", 'masda']
print(cars)
cars[0]="bmw"
cars[1]="porshe"
cars[2]="mazda"
print(cars)

Rectangle_measurements = (200, 50) # (largo, ancho)
print(Rectangle[0])=300 # NO SE PUEDE
print(Rectangle[1])=100 # NO SE PUEDE
Rectangle_measurements = (300,50)

"""
    Nopodemos modificar una tupla directamente,
    lo que si podemos es cambiar la asignacion
    a una variable que almacena una tupla.
"""

