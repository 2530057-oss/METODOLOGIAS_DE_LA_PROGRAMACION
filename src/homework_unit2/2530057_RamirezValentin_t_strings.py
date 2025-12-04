
# Alejandro Valentin Ramirez Gonzalez
# 2530057
# 1-3

# Resumen ejecutivo

# Un string en Python es un tipo de dato de texto e inmutable, lo que significa que no puede modificarse una vez creado.
# Permite operaciones como concatenar, medir longitud con len(), extraer subcadenas con slicing y buscar o reemplazar texto con métodos como find(), in, replace().
# Normalizar (lower(), strip(), etc.) es clave para comparar datos correctamente y evitar errores al validar entradas como nombres, correos o contraseñas.
# La validación de texto garantiza que los datos sean coherentes, seguros y útiles antes de procesarlos.
# El documento cubrirá la descripción de cada problema, los formatos de entrada y salida esperados y las validaciones necesarias.
# También incluirá el uso de métodos de string, ejemplos prácticos, casos de prueba y el código usado en cada sección.

# Problem 1: Full name formatter (name + initials)
"""
Description:
Given a person s full name in a single string (for example: “juan carlos tovar”), the program must:

1. Normalize the text (strip, remove extra spaces, fix upper/lowercase).
2. Display the name in Title Case and show the initials (for example: J.C.T.).

Inputs
* full_name (string)

Outputs:
* “Formatted name: …”
* “Initials: …”

Validations:
* The string must not be empty after strip().
* It must contain at least two words.

Test cases

Normal:
Input: Juan Perez Lopez
Output: Formatted name: Juan Perez Lopez | Initials: J.P.L

Border:
Input: maRiA de la cruz
Output: Formatted name: Maria De La Cruz | Initials: M.D.L.C

Error:
Input: (empty)
Output: Formatted name:  | Initials: (no data)
"""


full_name = input(f"tell me your full name: ")

normalized_name = " ".join(full_name.strip().lower().split())

title_name = normalized_name.title()

parts = normalized_name.split()

initials = ".".join([p[0].upper() for p in parts])
print("Formatted name:", title_name)
print("Initials:", initials)





# Problem 2: Simple email validator (structure + domain)
"""
Description:
Validate whether an email address has a correct basic format:

* It contains exactly one '@'.
* After the '@' there must be at least one '.'.
* It has no whitespace characters.
  If the email is valid, also display the domain (everything after '@').

Inputs:
* email_text (string)

Outputs:
* “Valid email: true/false”
* If valid: “Domain: …”

Validations:
* Not empty
* Exactly one '@'
* No spaces
* At least one '.' in the domain

Test cases

Normal:
Input: [user@example.com](mailto:user@example.com)
Output: Valid email. Domain: example.com

Border:
Input: [user@mail.co](mailto:user@mail.co)
Output: Valid email. Domain: mail.co

Error:
Input: user@@mail.com
Output: Invalid email: must contain exactly one '@'.
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




# Problem 3: Palindrome checker (ignoring spaces and case)
"""
Description:
Determine whether a phrase is a palindrome, meaning it reads the same forward and backward while ignoring spaces and letter case.

Inputs:
* phrase (string)

Outputs:
* “Is palindrome: true/false”

Validations:
* Not empty after strip()
* Minimum length of 3 after cleaning

Normal:
Input: ana
Output: ana | true

Border:
Input: a n a
Output: ana | true

Error:
Input: a
Output: Error: too short
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






# Problem 4: Sentence word stats (lengths and first/last word)
"""
Description:
Given a sentence, the program must:

1. Normalize spaces (remove leading/trailing spaces).
2. Split the sentence into words.
3. Output:

* Total word count
* First word
* Last word
* Shortest word (by length)
* Longest word (by length)

Inputs:
* sentence (string)

Outputs:
* Word count
* First word
* Last word
* Shortest word
* Longest word

Validations:
* Not empty
* At least one valid word

Normal:
Input: hola mundo desde python
Output: 4 | hola | python | hola | python

Border:
Input: uno dos tres
Output: 3 | uno | tres | uno | tres

Error:
Input: (empty)
Output: Error: sentence cannot be empty.
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






# Problem 5: Password strength classifier
"""
Description:
Classify a password as **weak**, **medium**, or **strong** according to minimal rules.

Rules:

* **weak**: length < 8
* **medium**: length ≥ 8 and partial mix
* **strong**: length ≥ 8 and contains uppercase, lowercase, digit, and symbol

Inputs:
* password_input (string)

Outputs:
* Password strength: weak/medium/strong

Validations:
* Not empty

Normal:
Input: Abc123!@
Output: strong

Border:
Input: abcdefg1
Output: medium

Error:
Input: (empty)
Output: weak
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



# Problem 6: Product label formatter (fixed-width text)
"""
Description:
Generate a **30-character label** in the format:
`Product: <NAME> | Price: $<PRICE>`

If the result is shorter than 30 characters → **pad with spaces**.
If longer than 30 → **truncate**.

Inputs:

* product_name (string)
* price_value (num/string)

Outputs:

* Label: "<30 chars>"

Validations:

* Name not empty
* Price must be convertible to a positive number

Normal:
Input: name=Pan price=12.5
Output: Label: "Product: Pan | Price: $12.5 "

Border:
Input: name=SuperProductoLargo price=9
Output: Label: "Product: SuperProductoLargo |"

Error:
Input: name=Pan price=abc
Output: Error: price must be a valid number.
"""


product_name = input("Enter product name: ").strip()
price_value = input("Enter price: ")

if not product_name:
    print("Error: product name cannot be empty.")
else:
    try:
        price_num = float(price_value)
        if price_num <= 0:
            print("Error: price must be a positive number.")
        else:
            price_str = f"{price_num}"

            base_label = f"Product: {product_name} | Price: ${price_str}"

            if len(base_label) < 30:
                final_label = base_label + (" " * (30 - len(base_label)))
            else:
                final_label = base_label[:30]

            print(f'Label: "{final_label}"')
    except ValueError:
        print("Error: price must be a valid number.")


# CONCLUSIONES

# Trabajar con strings es clave porque casi todo lo que escribe el usuario llega como texto y hay que limpiarlo.
# Usar funciones como lower(), strip(), split() o join() ayuda a que el texto quede ordenado y fácil de procesar.
# Normalizar antes de comparar evita errores por espacios de más o diferencias de mayúsculas.
# Las validaciones son importantes para evitar que entren datos basura al programa.
# Aprendí que los strings son inmutables y que para cambiarlos usamos slices o generamos uno nuevo.
# En general, dominar el manejo de texto hace que el código sea más claro y confiable.


# References:
# 1) Python documentation – Built-in Types: Text Sequence Type — str
# 2) Python Tutorial – Strings (docs.python.org)
# 3) “Automate the Boring Stuff with Python” – A. Sweigart (capítulos de manejo de texto)
# 4) Real Python – Articles on input validation and string handling
# 5) Apuntes de Algoritmos y Programación Básica – Sección de cadenas y validación

# REPOSITORIO DE GITHUB
https://github.com/2530057-oss/METODOLOGIAS_DE_LA_PROGRAMACION/blob/main/src/homework_unit2/2530057_RamirezValentin_t_strings.py