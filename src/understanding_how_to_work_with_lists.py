# Trabajando con listas
"""
    Recorrer una lista sin importar la cantidad
    de elementos que tenga.
"""

magicians = ["ron", "hermione", "harry", "hagrid," "cedrik"] 


for magician in magicians:
    print(magician)
    print(magician.upper())
    print(f"{magician.title()} ese fue un gran echizo.")
    print(f"\t {magician.lower()}No podemos esperar para ver tu siguiente echizo")
    
print("Gracias a todos, fue un gran espectaculo")

"""
    identacion:

    python utiliza la identacion para determinar
    cuando una linea de codigo esta conectado a 
    la linea de codigo anterior.

    Basicamente, se utilizan 4 espacios en blanco 
    para obligarnos a escribir codigo ordenado y
    estructurado.
"""

# No olvidemos identar
magicians = ["alice", "david", "carolina"]
for magician in magicians:
    print(magician)

"""
    Identacion Error:
"""


#Error de logica 
magicians = ["alice", "david", "carolina"]
for magician in magicians:
    print(magician)
print(f"I can't wait to see your next trick, {magician.title()}")
 

# Identacion innecesaria
message = "hola python"
    print(message)
