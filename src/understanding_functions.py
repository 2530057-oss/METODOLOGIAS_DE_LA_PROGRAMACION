### FUNCIONES
# Las funciones son bloques de codigo para realizar 
# Una tarea en especifico

# Cuando queremos realizar la terea que se ha definido 
# en la funcion, tenemos que llamar el nombre de la 
# funcion que realiza la accion.

"""
    Sintaxis de una funcion 

    def nombre_funcion():
        '''
            docstrings
        '''
        acciones

    Ejemplos: Vamos a definir una funcion que de un 
    saludo a cristopher

"""
"""
def gretting_cristopher():
    
        Funcion para saludar a una persona 
        llamada cristopher
    
    for i in range(0,5):
        print("Hello cristopher")

gretting_cristopher()
"""

# Ejemplo de una funcion que genere el nombre completo
# de una persona y lo regrese

def create_full_name(first_name, last_name, middle_name=""):
    full_name = f"{first_name} {middle_name} {last_name}".title()
    return full_name


first_name = input("Dame tu primer nombre: ")
middle_name = input("Dame tu segundo nombre: (sinoo tienees degundo nombre, da enter) ")
last_name = input("Dame tu apellido: ")

# parametros posicionales - positional arguments
generated_fullname = create_full_name(
    first_name.strip().lower() 
    last_name.strip().lower()
    middle_name.strip().lower())
print(generated_fullname)

# argumentos llaves - keyword arguments
generated_fullname_2 = create_full_name(
    middle_name = user_middle_name,
    first_name = user_first_name, 
    last_name = user_last_name
)
print(generated_fullname_2)
# args en funciones
# kwargs en funciones
# Manejo de datos (.txt, csv, json, excel, works, pdf)
# args via consola (sys)
# cli en python - comand line interference
# testing - casos prueba (borde, validos, invalidos)