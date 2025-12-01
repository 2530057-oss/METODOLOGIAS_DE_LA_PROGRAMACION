"""
Alejandro Valentin Ramirez Gonzalez
2530057
1-3
"""



# Dado el nombre completo de una persona en una sola cadena (por ejemplo: "juan carlos tovar"), el programa debe:
# 1) Normalizar el texto (strip, espacios extra, mayúsculas/minúsculas).
# 2) Mostrar el nombre formateado en Title Case y las iniciales (por ejemplo: J.C.T.).

"""
full_name = input(f"tell me your full name: ")

normalized_name = " ".join(full_name.strip().lower().split())

title_name = normalized_name.title()

parts = normalized_name.split()

initials = ".".join([p[0].upper() for p in parts])
print("Formatted name:", title_name)
print("Initials:", initials)
"""

# Valida si una dirección de correo tiene un formato básico correcto:
# - Contiene exactamente un '@'.
# - Después del '@' debe haber al menos un '.'.
# - No contiene espacios en blanco.
# Si el correo es válido, también muestra el dominio (la parte después de '@').
"""
email = input("Enter an email address: ")

if " " in email:
    print("Invalid email: contains spaces.")
elif email.count("@") != 1:
    print("Invalid email: must contain exactly one '@'.")
else:
    username, domain = email.split("@")

    if "." not in domain:
        print("Invalid email: domain must contain at least one '.'.")
    else:
        print("Valid email.")
        print("Domain:", domain)
"""

#Determina si una frase es un palíndromo, es decir, se lee igual de izquierda a derecha y de derecha a izquierda, ignorando espacios y mayúsculas/minúsculas.

"""
phrase = input("Enter a phrase: ")

clean_input = phrase.strip()

if not clean_input:
    print("Error: phrase cannot be empty.")
else:
    normalized = clean_input.lower().replace(" ", "")

    if len(normalized) < 3:
        print("Error: phrase too short after cleaning (minimum 3 characters).")
    else:
        is_palindrome = normalized == normalized[::-1]

        print("Normalized phrase:", normalized)
        print("Is palindrome:", "true" if is_palindrome else "false")

"""

# Dada una oración, el programa debe:
# 1) Normalizar espacios (quitar espacios al principio y al final).
# 2) Separar las palabras por espacios.
# 3) Mostrar:
#   - Número total de palabras.
#   - Primera palabra.
#   - Última palabra.
#   - Palabra más corta y más larga (por longitud).


"""
sentence = input("Enter a sentence: ")

clean = sentence.strip()

if not clean:
    print("Error: sentence cannot be empty.")
else:
    words = clean.split()

    if len(words) == 0:
        print("Error: no valid words found.")
    else:
        count = len(words)

        first_word = words[0]
        last_word = words[-1]

        shortest = min(words, key=len)
        longest = max(words, key=len)

        print("Word count:", count)
        print("First word:", first_word)
        print("Last word:", last_word)
        print("Shortest word:", shortest)
        print("Longest word:", longest)


"""

# Descripción:
# Clasifica una contraseña como "weak", "medium" o "strong" según reglas 
# mínimas (puedes afinarlas, pero documéntalas en los comentarios).

"""
password_input = input("Enter a password: ")

if not password_input:
    print("Password strength: weak")
else:
    has_upper = False
    has_lower = False
    has_digit = False
    has_symbol = False

    for ch in password_input:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True
        elif not ch.isalnum():
            has_symbol = True

    length = len(password_input)

    if length >= 8 and has_upper and has_lower and has_digit and has_symbol:
        print("Password strength: strong")
    elif length >= 8 and (
        (has_upper and has_lower) or
        (has_lower and has_digit) or
        (has_upper and has_digit)
    ):
        print("Password strength: medium")
    else:
        print("Password strength: weak")

""""
