"""
    Vamos a realizar un rpograma que defina un PIN
    para dar acceso a un usuario.

    El usuario va a tener un maximo de intentos para 
    colocar bien el pin

    Si el usuario sobrepasa este maximo  de intentos
    se le va bloquear la cuenta y el acceso
"""

CORRECT_PIN = "1234"
MAX_ATTEMPTS = 3
attempt = 0

while attempt < MAX_ATTEMPTS:

    user_input = input("Ingresa tu PIN: ")

    if user_input == CORRECT_PIN:
        print("Acceso concedido")
        break
    else:
        attempt+=1
        reamaining_attempts = MAX_ATTEMPTS - attempt
        if reamaining_attempts > 0:
            print("Ingresa  un pin valido")
            print(f"Te quedan {reamaining_attempts} intentos")
        else:
            print("Cuenta bloqueada.")