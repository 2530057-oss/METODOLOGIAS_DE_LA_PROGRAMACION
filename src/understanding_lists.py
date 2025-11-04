#lists
"""
    las listas son elementos mmutables 

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
message = "mi primer bicicleta fue una " + bicycles[4].title() "."
print(message)

message_f = f"mi primer bicicleta fue una {bicycles[4].title()}."
print(message)