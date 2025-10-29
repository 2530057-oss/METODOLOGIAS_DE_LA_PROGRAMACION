"""
strings variables es de manera sencilla una serie 
de caracteres. En python, todo lo que se encuentre
 dentro de comillas simples (' ') o (" ")
 sera considerado un stranding.

 Ejemplos:
    "Esto es un string"
    'Esto tambien es un string' 

' le dije a un amigo que "python es mi lenguaje favorito" '
" El lenguaje 'pytho' lleva el nombre por monty python, no por la serpiente "
"""
name = "clase de programacion"
print(name)

# title 
print(name.title())

print(name)
"""
    Un metodo es una accion que python
 puede realizar en un fractmento de datos 
 o sobre una variable.

    El punto despues de una variable 
seguido del metodo title dice que 
se puede ejecutar el metodo title () 
de una variable name.  

    Todos los metodos van seguidos de parentesis 
por que en ocasiones necesita informacion adicional
para funcionar, la cual iria dentro de los parentesis.
En esta ocasion, el metodo title() no requiere informacion
adicional para funcionar.
"""

print("Metodo upper: ", name.upper())
print("Metodo lower: ", name.lower())



# Concatenacion de STRINGS
first_name = "charly"
last_name = "mercury"
full_name = first_name + " " + last_name
print(full_name)
print(full_name.title())