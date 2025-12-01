#lists
"""
    las listas son elementos mmutables que pueden cambiar o variar

    Las listas nos permiten almacenar informacion
    en un lugar, la cantidad que tenga: ya sean 
    poco elementos o millones de elementos.

    Se recomienda nombrar una variable de tipo lista
    en plural.
    
    En python los corchetes [] definen una lista,
    sus elementos van separados por comas.
    Ejemplos:
"""
bicycles=['trek', 'canondale', 'redline', 'specialized', 'giant']
print(bicycles)

print(bicycles[0].title())

# Los indices comienzan en 0 y terminan en n-1 , donde n es el numero de elementos 
print(bicycles[4].title())

# Accediendo al ultimo elementos 
print(bicycles[-1].title()) #Ultimo elemento 
print(bicycles[-2].title())
print(bicycles[-5].title()) #Primer elemento 

# Utilizando valores de la lista 
message = "mi primer bicicleta fue una " + bicycles[4].title() 
print(message)

message_f = f"mi primer bicicleta fue una {bicycles[4].title()}."
print(message_f)

## Agregar elementos a una lista 
print("\n")
print("Agregar elementos a una lista.")
print(bicycles)
print("Metodos de las listas para agregar elementos: list_name.append(elements)")
bicycles.append("ducatti")
print(bicycles)

"""
    #Lista A-105
    Agrega elementos a una lista 
        -append(): Agrega un elemento al final de una lista 
"""

print ("\n--- Agregar elementos a una lista metodo append() ---")
motorcycles = ['honda', 'yamaha', 'susuki']
print(motorcycles) # Salida: ['honda', 'yamaha', 'susuki']
motorcycles.append('ducati')
print(motorcycles) # Salida: ['honda', 'yamaha', 'susuki', 'ducati']



"""
    Agregar elementos a una lista en una pocision especifica
        - insert(): Inserta un elemento en una pocision especifica 
"""
print ("\n--- Agregar elementos a una lista metodo insert() ---")
motorcycles = ['honda', 'yamaha', 'susuki']
print(motorcycles) # Salida: ['honda', 'yamaha', 'susuki']
motorcycles.insert(1, 'ducati')
print(motorcycles) # Salida: ['honda', 'yamaha', 'susuki', 'ducati']



"""
Eliminar elementos de una lista (del)

"""
print("\n--- Eliminar elementos de una lista (del) ---")
motorcycles = ['honda', 'yamaha', 'suzuki'] 
print(motorcycles) #Salida: ['honda', 'yamaha', 'suzuki']
del motorcycles[0]
print(motorcycles) #Salida: ['yamaha', 'suzuki']



"""
Eliminar elementos de una lista (pop)
"""
print("\n--- Eliminar elementos de una lista (pop) ---")
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles) #Salida: ['honda', 'yamaha', 'suzuki']
popped_motorcycle = motorcycles.pop()
print(motorcycles) #Salida: ['honda', 'yamaha']
print(f'La motocicleta que borraste fue {popped_motorcycle.title()}.')



"""
Eliminar un elemento de una lista por valor (pop)

"""
print("\n--- Eliminar un elemento de una lista por valor (pop) ---")
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles) #Salida: ['honda', 'yamaha', 'suzuki']
popped_motorcycle = motorcycles.pop(1)
print(motorcycles) #Salida: ['honda', 'yamaha']
print(f'La motocicleta que borraste fue {popped_motorcycle.title()}.')



"""
Eliminar un elemento de una lista por valor (remove)

"""
print("\n--- Eliminar un elemento de una lista por valor (remove) ---")
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducatti']
print(motorcycles) #Salida: ['honda', 'yamaha', 'suzuki', 'ducatti']
motorcycles.remove('ducatti')
print(motorcycles) #Salida: ['honda', 'yamaha', 'suzuki']
print("\n")



"""
organizar una lista permanente con sort()
"""
print("\n--- organizar una lista permanente con sort() ---")
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars) #Salida: ['bmw', 'audi', 'toyota', 'subaru']
cars.sort() 
print(cars) #Salida: ['audi', 'bmw', 'subaru', 'toyota']



"""
    Ejemplo:
"""
students = ["jesus", "joshue", "ana", "mike", "africa", "gerardo"]
print(students)
desired_student = input("¿que estudiante deseas borrar de la lista?")
students.remove(desired_student.strip().lower())
print(students)
print("tu has eliminado:", desired_student)
students.reverse()
print(students)

print(len(students))



cars = ["kia", "ford", "tesla", "volvo", "chevrolet" ]
print(cars)
print(sorted(cars))
sorted_list = sorted(cars)
print("lista original: ", cars)
