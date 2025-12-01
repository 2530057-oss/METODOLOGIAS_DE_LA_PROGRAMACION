# While
"""
    el while es un ciclo controlado/comando
    por condicion.

    la estructura basica de un while es:

        while conditional:
            actions
"""
# while infinito 
"""
    programa si el usuario escribe un  numero
    entre 25 y 50, entonces esta dentro del rango
    y salirme del while,
    de otro modo pedirle otro numero.
"""

while True:
    try:
        number = int(input("ingresa un numero: "))

        if number >= 25 and number <= 50:
            print("Estas en el rango, lo hiciste bien")
            break
        else:
            print("Estas fuera del rango, intenta de nuevo")
    except ValueError:
        print("Se ha introducido una variable no salida.")
    except KeyboardInterrupt:
        print("\nPrograma terminado por el usuario.")
        break

print("Saliste del while")