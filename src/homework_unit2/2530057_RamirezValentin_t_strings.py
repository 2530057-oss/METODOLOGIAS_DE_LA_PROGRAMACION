"""
Alejandro Valentin Ramirez Gonzalez
2530057
1-3
"""
# Resumen ejecutivo

# Un string en Python es un tipo de dato de texto e inmutable, lo que significa que no puede modificarse una vez creado.
# Permite operaciones como concatenar, medir longitud con len(), extraer subcadenas con slicing y buscar o reemplazar texto con métodos como find(), in, replace().
# Normalizar (lower(), strip(), etc.) es clave para comparar datos correctamente y evitar errores al validar entradas como nombres, correos o contraseñas.
# La validación de texto garantiza que los datos sean coherentes, seguros y útiles antes de procesarlos.
# El documento cubrirá la descripción de cada problema, los formatos de entrada y salida esperados y las validaciones necesarias.
# También incluirá el uso de métodos de string, ejemplos prácticos, casos de prueba y el código usado en cada sección.

# BUENAS PRÁCTICAS

# - Los strings son inmutables: cada cambio crea una nueva cadena.
# - Usar strip() y lower() para normalizar entrada antes de validar.
# - Evitar números mágicos; documentar el significado de cada slice.
# - Usar métodos nativos como replace(), split(), join().
# - Primero validar que no esté vacío; luego el formato.
# - Escribir variables con nombres claros y mensajes simples.




# Problem 1: Full name formatter (name + initials)

# Descripción:
# Dado el nombre completo de una persona en una sola cadena (por ejemplo: "juan carlos tovar"), el programa debe:
# 1) Normalizar el texto (strip, espacios extra, mayúsculas/minúsculas).
# 2) Mostrar el nombre formateado en Title Case y las iniciales (por ejemplo: J.C.T.).

# Entradas:
# - full_name (string)

# Salidas:
# - "Formatted name: ..."
# - "Initials: ..."

# Validaciones:
# - No vacío tras strip()
# - Debe contener al menos 2 palabras

# Casos de prueba:
# Normal:
# Entrada: Juan Perez Lopez
# Salida: Formatted name: Juan Perez Lopez | Initials: J.P.L

# Border:
# Entrada: maRiA de la cruz
# Salida: Formatted name: Maria De La Cruz | Initials: M.D.L.C

# Error:
# Entrada: (vacío)
# Salida: Formatted name: | Initials: (no hay datos)

"""
full_name = input(f"tell me your full name: ")

normalized_name = " ".join(full_name.strip().lower().split())

title_name = normalized_name.title()

parts = normalized_name.split()

initials = ".".join([p[0].upper() for p in parts])
print("Formatted name:", title_name)
print("Initials:", initials)
"""




# Problem 2: Simple email validator (structure + domain)

# Descripción:
# Valida si una dirección de correo tiene un formato básico correcto:
# - Contiene exactamente un '@'.
# - Después del '@' debe haber al menos un '.'.
# - No contiene espacios en blanco.
# Si el correo es válido, también muestra el dominio (la parte después de '@').

# Entradas:
# - email_text (string)

# Salidas:
# - "Valid email: true/false"
# - Si es válido: "Domain: ..."

# Validaciones:
# - No vacío
# - Un solo '@'
# - No espacios
# - Al menos un '.' en el dominio

# Casos de prueba:
# Normal:
# Entrada: user@example.com
# Salida: Valid email. Domain: example.com

# Border:
# Entrada: user@mail.co
# Salida: Valid email. Domain: mail.co

# Error:
# Entrada: user@@mail.com
# Salida: Invalid email: must contain exactly one '@'.

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




# Problem 3: Palindrome checker (ignoring spaces and case)

# Descripcion:
#Determina si una frase es un palíndromo, es decir, se lee igual de izquierda a derecha
# y de derecha a izquierda, ignorando espacios y mayúsculas/minúsculas.

# Entradas:
# - phrase (string)

# Salidas:
# - "Is palindrome: true/false"

# Validaciones:
# - No vacío tras strip()
# - Longitud mínima de 3 tras limpiar

# Normal:
# Entrada: ana
# Salida: ana | true

# Border:
# Entrada: a n a
# Salida: ana | true

# Error:
# Entrada: a
# Salida: Error: too short

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




# Problem 4: Sentence word stats (lengths and first/last word)

#Descripcion:
# Dada una oración, el programa debe:
# 1) Normalizar espacios (quitar espacios al principio y al final).
# 2) Separar las palabras por espacios.
# 3) Mostrar:
#   - Número total de palabras.
#   - Primera palabra.
#   - Última palabra.
#   - Palabra más corta y más larga (por longitud).

# Entradas:
# - sentence (string)

# Salidas:
# - Word count
# - First word
# - Last word
# - Shortest word
# - Longest word

# Validaciones:
# - No vacío
# - Al menos una palabra válida

# Normal:
# Entrada: hola mundo desde python
# Salida: 4 | hola | python | hola | python

# Border:
# Entrada: uno dos tres
# Salida: 3 | uno | tres | uno | tres

# Error:
# Entrada: (vacío)
# Salida: Error: sentence cannot be empty.

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





# Problem 5: Password strength classifier

# Descripción:
# Clasifica una contraseña como "weak", "medium" o "strong" según reglas 
# mínimas (puedes afinarlas, pero documéntalas en los comentarios).

# Reglas usadas:
# - weak: longitud < 8
# - medium: longitud >= 8 y mezcla parcial
# - strong: >= 8 y contiene mayúscula, minúscula, dígito y símbolo

# Entradas:
# - password_input (string)

# Salidas:
# - "Password strength: weak/medium/strong"

# Validaciones:
# - No vacía

# Normal:
# Entrada: Abc123!@
# Salida: strong

# Border:
# Entrada: abcdefg1
# Salida: medium

# Error:
# Entrada: (vacío)
# Salida: weak

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
"""


# Problem 6: Product label formatter (fixed-width text)

# Descripción:
# Genera una etiqueta de 30 caracteres:
# "Product: <NAME> | Price: $<PRICE>"

# Si es más corta, rellena con espacios.
# Si es más larga, recorta.

# Entradas:
# - product_name (string)
# - price_value (num/string)

# Salidas:
# - "Label: '<30 chars>'"

# Validaciones:
# - Nombre no vacío
# - Precio convertible a número positivo

# Normal:
# Entrada: nombre=Pan price=12.5
# Salida: Label: "Product: Pan | Price: $12.5 "

# Border:
# Entrada: nombre=SuperProductoLargo price=9
# Salida: Label: "Product: SuperProductoLargo |"

# Error:
# Entrada: nombre= Pan price=abc
# Salida: Error: price must be a valid number.


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
"""

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
