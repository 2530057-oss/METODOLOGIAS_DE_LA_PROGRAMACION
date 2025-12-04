# Alejandro Valentin Ramirez Gonzalez
# 2530057
# 1-3

# RESUMEN EJECUTIVO
# Un bucle for en Python itera sobre una secuencia de elementos y se usa típicamente para recorrer listas, tuplas, cadenas o rangos.
# Un bucle while repite un bloque de código mientras se cumpla una condición, siendo útil cuando no se conoce de antemano cuántas veces se ejecutará.
# Un contador es una variable que incrementa o decrementa para llevar registro de iteraciones, mientras que un acumulador suma o combina valores durante el bucle.
# Definir correctamente la condición de salida es crucial para evitar ciclos infinitos que detengan o bloqueen el programa.
# Los bucles permiten automatizar tareas repetitivas, recorrer colecciones, mostrar menús o solicitar datos hasta que se cumplan criterios.
# El documento cubrirá la descripción de cada problema, entradas y salidas, validaciones aplicadas y ejemplos de uso de for y while en diferentes contextos.

# Problem 1: Sum of range with for
"""
Description:
Calculates the sum of all integers from 1 to n (inclusive). It also calculates the sum of only 
the even numbers in the same range using a for loop.

Inputs:
* n (int; upper limit of the range)

Outputs:
* Sum 1..n: <total_sum>
* Even sum 1..n: <even_sum>

Validations:
* Verify that n can be converted to int
* n >= 1; if not, output "Error: invalid input"

Test cases:
Normal:
Input: 5
Output: Sum 1..n: 15 | Even sum 1..n: 6

Border:
Input: 1
Output: Sum 1..n: 1 | Even sum 1..n: 0

Error:
Input: 0
Output: Error: invalid input
"""

try:
    n = int(input("Enter a positive integer n: ").strip())
except:
    print("Error: invalid input")
    exit()

if n < 1:
    print("Error: invalid input")
    exit()

total_sum = 0
even_sum = 0

for i in range(1, n + 1):
    total_sum += i
    if i % 2 == 0:
        even_sum += i

print("Sum 1..n:", total_sum)
print("Even sum 1..n:", even_sum)



# Problem 2: Multiplication table with for
"""
Description:
Generates and displays the multiplication table of a base number, from 1 up to a limit m. For example, 
if base = 5 and m = 4, the output is:
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20

Inputs:
* base (int)
* m (int; table limit)

Outputs:
* One line per multiplication:

  * "5 x 1 = 5"
  * "5 x 2 = 10"
  * etc.

Validations:
* base and m must be convertible to int
* m >= 1; if not, output "Error: invalid input"


Test cases:
Normal:
Input: base=3, m=5
Output:
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
3 x 4 = 12
3 x 5 = 15

Border:
Input: base=7, m=1
Output: 7 x 1 = 7

Error:
Input: base=5, m=0
Output: Error: invalid input
"""
try:
    base = int(input("Enter the base number: ").strip())
    m = int(input("Enter the limit of the table: ").strip())
except:
    print("Error: invalid input")
    exit()

if m < 1:
    print("Error: invalid input")
    exit()

for i in range(1, m + 1):
    print(f"{base} x {i} = {base * i}")



# Problem 3: Average of numbers with while and sentinel
"""
Description:
Reads numbers one by one until the user enters a sentinel value (e.g., -1). It calculates the average
of the valid numbers entered and the total count. If the user enters only the sentinel without any valid numbers, 
an error message is shown.

Inputs:
* number (float; read repeatedly)
* sentinel_value (fixed in the code, e.g., -1)

Outputs:
* Count: <count>
* Average: <average_value>
* If no valid numbers entered: Error: no data

Validations:
* Each input must be convertible to float
* Ignore the sentinel in calculations

Test cases:
Normal:
Input sequence: 5, 10, 15, -1
Output: Count: 3 | Average: 10.0

Border:
Input sequence: 7, -1
Output: Count: 1 | Average: 7.0

Error:
Input sequence: -1
Output: Error: no data
"""

sentinel_value = -1
count = 0
total = 0.0

while True:
    try:
        number = float(input("Enter a number (-1 to stop): ").strip())
    except:
        print("Error: invalid input")
        continue

    if number == sentinel_value:
        break

    total += number
    count += 1

if count == 0:
    print("Error: no data")
else:
    average = total / count
    print("Count:", count)
    print("Average:", average)



# Problem 4: Password attempts with while
"""
Description:
Implements a simple password attempt system. A correct password is defined in the code (e.g., "admin123").
 The user has a maximum of MAX_ATTEMPTS to enter it. If the user enters the correct password within the limit,
  a success message is shown. If the attempts are exhausted, a lock message is shown.

Inputs:
* user_password (string; entered on each attempt)

Outputs:
* If correct: Login success
* If all attempts fail: Account locked

Validations:
* MAX_ATTEMPTS > 0 (defined as a constant in the code, e.g., 3)
* Correctly count the number of attempts

Test cases:
Normal:
Input sequence: "pass1", "pass2", "admin123"
Output: Login success

Border:
Input sequence: "admin123"
Output: Login success

Error:
Input sequence: "pass1", "pass2", "pass3"
Output: Account locked
"""

CORRECT_PASSWORD = "admin123"
MAX_ATTEMPTS = 3
attempts = 0

while attempts < MAX_ATTEMPTS:
    user_password = input("Enter password: ").strip()
    attempts += 1

    if user_password == CORRECT_PASSWORD:
        print("Login success")
        break
else:
    print("Account locked")


# Problem 5: Simple menu with while
"""
Description:
Implements a text menu that repeats until the user selects the exit option. Example menu:

1. Show greeting
2. Show current counter value
3. Increment counter
4. Exit

The program executes the action corresponding to each option and redisplays the menu until 0 is chosen.

Inputs:
* option (string or int; user choice)

Outputs:
* Messages according to the option:

  * "Hello!" for greeting
  * "Counter:" <counter_value> to show the counter
  * "Counter incremented" when incrementing
  * "Bye!" on exit
* For invalid options: "Error: invalid option"

Validations:
* Normalize option (e.g., convert to int with error handling)
* Ensure only 0, 1, 2, 3 are accepted as valid options

Test cases:
Normal:
Input sequence: 1, 2, 3, 2, 0
Output:
Hello!
Counter: 0
Counter incremented
Counter: 1
Bye!

Border:
Input sequence: 0
Output: Bye!

Error:
Input sequence: 5
Output: Error: invalid option
"""

counter = 0

while True:
    print("\nMenu:")
    print("1) Show greeting")
    print("2) Show current counter value")
    print("3) Increment counter")
    print("0) Exit")
    
    option_text = input("Enter your option: ").strip()
    try:
        option = int(option_text)
    except:
        print("Error: invalid option")
        continue

    if option == 1:
        print("Hello!")
    elif option == 2:
        print("Counter:", counter)
    elif option == 3:
        counter += 1
        print("Counter incremented")
    elif option == 0:
        print("Bye!")
        break
    else:
        print("Error: invalid option")


# Problem 6: Pattern printing with nested loops
"""
Description:
Uses nested for loops to print a right-angled triangle pattern of asterisks. For example, for n = 4:
*
**
***
****

Optionally, it can print an inverted pattern (documented if implemented).

Inputs:

* n (int; number of rows in the pattern)

Outputs:

* Pattern line by line:

  * "*"
  * "**"
  * "***"
  * "****"
* Optional inverted pattern if implemented

Validations:

* n must be convertible to int
* n >= 1; if not, output "Error: invalid input"

Test cases:
Normal:
Input: n=4
Output:
*
**
***
****

Border:
Input: n=1
Output: *

Error:
Input: n=0
Output: Error: invalid input
"""
try:
    n = int(input("Enter the number of rows: ").strip())
except:
    print("Error: invalid input")
    exit()

if n < 1:
    print("Error: invalid input")
    exit()

# Right-angled triangle
for i in range(1, n + 1):
    print("*" * i)

# Optional inverted triangle
for i in range(n, 0, -1):
    print("*" * i)

# CONCLUSIONES
# Los bucles for son ideales para recorrer secuencias con un número conocido de elementos, mientras que los while se usan cuando la repetición depende de una condición.
# Los contadores y acumuladores ayudan a llevar control de iteraciones y a sumar o combinar valores dentro del bucle de forma eficiente.
# Un riesgo común con while es crear ciclos infinitos si la condición de salida no se actualiza correctamente.
# Los menús interactivos y los intentos de contraseña son ejemplos típicos donde while permite repetir acciones hasta que se cumpla un criterio.
# Los bucles anidados permiten generar patrones más complejos y procesar estructuras de datos multidimensionales.
# Aprendí que combinando for y while se pueden resolver problemas de manera flexible y clara, optimizando cálculos y recorridos.


# References:
# 1) Python documentation – for statements, while statements
# 2) Python Tutorial – Sección de bucles y estructuras de control
# 3) “Automate the Boring Stuff with Python” – Capítulos sobre loops y control de flujo
# 4) Artículos sobre patrones de diseño con bucles: contadores, acumuladores y menús (Real Python, GeeksforGeeks)
# 5) Apuntes de clase y recursos oficiales de programación básica sobre bucles for y while


# REPOSITORIO DE GITHUB
