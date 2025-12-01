# 

try:
    age = int(input("Escribe tu edad: "))
except:
    age = -1
    print("Error, ingresaste un cararcter no valido")


if age >= 100:
    print("Tienes mas de un siglo")
elif age >= 18 and age < 100:
    print("Eres mayor de edad")
elif age >= 0 and age < 18:
    print("eres menor de edad")
else:
    print("Tuviste un error")


print("Holi charly")

"""
    Hacer un programa que pregunte la edad de una persona
    y responde lo siguiente:
        - Si la edad es menor o igual a 4, entonces la entrada
          es gratuita
        -Si la edad es menor a 18, pero mayor que 4
        entonces la entrada cuesta $200
         -Si la edad es mayor o igual que 18, entonces la entrada 
         cuesta $400.
"""

try:
    age = int(input("Escribe tu edad: "))
except:
    age = -1
    print("Error, ingresaste un cararcter no valido")

if age > 0 and age <= 4:
    print("tu entrada es gratuita")
elif age < 18 and age > 4:
    print("la entrada cuesta $200")
if age >= 18:
    print("La entrada cuesta $400")

# Multiple if 
guisos = ["desebrada", 'asado', "salsa verde", "pozole"]
if "asado" in guisos:
    print("Si hay asado")
else:
    print("No hay asado")
if "tamales" in guisos:
    print("hay tamales")
else:
    print("No hay tamales")
if "Salsa verde" in guisos:
    print("Si hay salsa verde")
else:
    print("No hay salsa verde")

# lista vacia
guisos = [5]
if guisos:
    print("hay guisos")

# utilizando varias listas
guisos_diponibles = ["salsa verde", "deshebrada", "mole"]
guisos_a_ordenar = ["deshebrada", "caldo de iguana"]

print("¿Que guiso desea ordenar?")
for guiso in guisos_a_ordenar:
    print(f"Deseo {guiso}")
    if guiso in guisos_diponibles:
        print(f"Si tenemos {guiso}")
    else:
        print("No tenemos ese guiso")
print("Realizado pedido...")

