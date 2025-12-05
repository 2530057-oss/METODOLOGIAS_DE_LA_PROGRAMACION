# Alejandro Valentin Ramirez Gonzalez
# 2530057
# 1-3

# RESUMEN EJECUTIVO
# Una función en Python es un bloque de código reutilizable que ejecuta una tarea específica cuando se le llama.
# Los parámetros son las variables definidas en la creación de la función, mientras que los argumentos son los valores que se envían al llamarla.
# Separar la lógica en funciones permite organizar mejor el código, reutilizar procesos y evitar repeticiones innecesarias.
# Un valor de retorno es el resultado que la función entrega al finalizar, y es preferible devolverlo para poder usarlo en otros cálculos o decisiones.
# Esto es más flexible que solo imprimir, ya que permite integrar la función dentro de programas más grandes.
# El documento cubrirá la descripción de cada problema, el diseño de funciones, sus entradas y salidas, las validaciones necesarias y pruebas básicas para verificar su correcto funcionamiento.



# Problem 1: Rectangle area and perimeter (basic functions)
"""
Description:
Define two functions:
calculate_area(width, height): returns the area of a rectangle.
calculate_perimeter(width, height): returns the perimeter.
The main code must read (or define) the values, call the functions, and display the results.

Inputs:
width (float)
height (float)

Outputs:
Area: <area_value>
Perimeter: <perimeter_value>

Validations:
width > 0
height > 0
If any condition fails, display "Error: invalid input" and do not call the functions.

Test cases:

Normal
Input: width=5 height=3
Output:
Area: 15
Perimeter: 16

Border
Input: width=0.1 height=0.1
Output:
Area: 0.01
Perimeter: 0.4

Error
Input: width=-2 height=4
Output:
Error: invalid input
"""


print("Enter width:")
try:
    width = float(input().strip())
except:
    print("Error: invalid input")
    exit()

print("Enter height:")
try:
    height = float(input().strip())
except:
    print("Error: invalid input")
    exit()

if width <= 0 or height <= 0:
    print("Error: invalid input")
    exit()

def calculate_area(width, height):
    return width * height

def calculate_perimeter(width, height):
    return 2 * (width + height)

print("Calculating area...")
print("Area:", calculate_area(width, height))

print("Calculating perimeter...")
print("Perimeter:", calculate_perimeter(width, height))



# Problem 2: Grade classifier (function with return string)
"""
Description:
Define a function classify_grade(score) that receives a numeric grade (0–100) and returns a category:
A if score >= 90
B if 80 <= score < 90
C if 70 <= score < 80
D if 60 <= score < 70
F if score < 60
The main code must call the function and display the result.

Inputs:
score (float or int)

Outputs:
Score: <score>
Category: <grade_letter>

Validations:
0 <= score <= 100
If not satisfied, display "Error: invalid input" and do not classify.

Test cases:

Normal
Input: score=85
Output:
Score: 85
Category: B

Border
Input: score=90
Output:
Score: 90
Category: A

Error
Input: score=120
Output:
Error: invalid input
"""

print("Enter score:")
try:
    score = float(input().strip())
except:
    print("Error: invalid input")
    exit()

if score < 0 or score > 100:
    print("Error: invalid input")
    exit()

def classify_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

print("Classifying grade...")
print("Score:", score)
print("Category:", classify_grade(score))


# Problem 3: List statistics function (min, max, average)
"""
Description:
Define a function summarize_numbers(numbers_list) that receives a list of numbers and returns a dictionary with:
"min": minimum
"max": maximum
"average": average (float)
The main code must build the list (for example, from comma-separated text), call the function, and display the values.

Inputs:
numbers_text (string, e.g., "10,20,30")
Internally: numbers_list (list of float or int)

Outputs:
Min: <min_value>
Max: <max_value>
Average: <average_value>

Validations:
numbers_text not empty after strip().
List not empty after conversion.
All elements must be convertible to numbers; if any fails, show "Error: invalid input".

Test cases:

Normal
Input: "10,20,30"
Output:
Min: 10
Max: 30
Average: 20.0

Border
Input: "5"
Output:
Min: 5
Max: 5
Average: 5.0

Error
Input: "10,abc,30"
Output:
Error: invalid input
"""

print("Enter numbers separated by commas:")
numbers_text = input().strip()

if numbers_text == "":
    print("Error: invalid input")
    exit()

parts = numbers_text.split(",")
numbers_list = []

for p in parts:
    p = p.strip()
    if p == "":
        print("Error: invalid input")
        exit()
    try:
        num = float(p)
        numbers_list.append(num)
    except:
        print("Error: invalid input")
        exit()

if len(numbers_list) == 0:
    print("Error: invalid input")
    exit()

def summarize_numbers(numbers_list):
    result = {
        "min": min(numbers_list),
        "max": max(numbers_list),
        "average": sum(numbers_list) / len(numbers_list)
    }
    return result

summary = summarize_numbers(numbers_list)

print("Min:", summary["min"])
print("Max:", summary["max"])
print("Average:", summary["average"])


# Problem 4: Apply discount list (pure function)
"""
Description:
Define a function apply_discount(prices_list, discount_rate) that:

* receives a list of prices (float) and a discount rate (e.g., 0.10 for 10%)
* returns a new list with discounted prices (without modifying the original list).
  The main code must:
* Create a list of prices
* Call the function
* Show the original list and the discounted list

Inputs:
prices_text (string; e.g., "100,200,300")
discount_rate (float, between 0 and 1)

Outputs:
Original prices: <original_list>
Discounted prices: <discounted_list>

Validations:
prices_text not empty and resulting list not empty
All prices > 0
0 <= discount_rate <= 1; otherwise, "Error: invalid input"

Test cases:

Normal
Input: "100,200,300", discount_rate = 0.10
Output:
Original prices: [100.0, 200.0, 300.0]
Discounted prices: [90.0, 180.0, 270.0]

Border
Input: "50", discount_rate = 0
Output:
Original prices: [50.0]
Discounted prices: [50.0]

Error
Input: "100, -20, 300", discount_rate = 0.20
Output:
Error: invalid input
"""

print("Enter prices separated by commas:")
prices_text = input().strip()

if prices_text == "":
    print("Error: invalid input")
    exit()

parts = prices_text.split(",")
prices_list = []

for p in parts:
    p = p.strip()
    if p == "":
        print("Error: invalid input")
        exit()
    try:
        price = float(p)
        if price <= 0:
            print("Error: invalid input")
            exit()
        prices_list.append(price)
    except:
        print("Error: invalid input")
        exit()

print("Enter discount rate (0 to 1):")
try:
    discount_rate = float(input().strip())
except:
    print("Error: invalid input")
    exit()

if discount_rate < 0 or discount_rate > 1:
    print("Error: invalid input")
    exit()

def apply_discount(prices_list, discount_rate):
    discounted = []
    for price in prices_list:
        discounted.append(price * (1 - discount_rate))
    return discounted

discounted_list = apply_discount(prices_list, discount_rate)

print("Original prices:", prices_list)
print("Discounted prices:", discounted_list)


# Problem 5: Greeting function with default parameters
"""
Description:
Define a function greet(name, title="") that:

* Optionally concatenates the title before the name (e.g., "Dr. Alice", "Eng. Bob")
* Returns the message: "Hello, <full_name>!"
  If title is empty, use only the name. The main code must call the function using positional and named arguments.

Inputs:
name (string)
title (optional string)

Outputs:
Greeting: <greeting_message>

Validations:
name not empty after strip()
title may be empty, but if not, must also be stripped

Test cases:

Normal
Input: name="Alice", title="Dr."
Output:
Greeting: Hello, Dr. Alice!

Border
Input: name="Bob", title=""
Output:
Greeting: Hello, Bob!

Error
Input: name="   "
Output:
Error: invalid input
"""

print("Enter name:")
name = input().strip()

if name == "":
    print("Error: invalid input")
    exit()

print("Enter title (optional):")
title = input().strip()

def greet(name, title=""):
    if title != "":
        full_name = title + " " + name
    else:
        full_name = name
    return f"Hello, {full_name}!"

greeting_message = greet(name=name, title=title)

print("Greeting:", greeting_message)


# Problem 6: Factorial function (iterative or recursive)
"""
Description:
Define a function factorial(n) that returns n! (the factorial of n). You can implement it using a for-loop or recursion;
here we use the **iterative** version to avoid unnecessary recursion depth.

Inputs:
n (int)

Outputs:
n: <n>
Factorial: <factorial_value>

Validations:
n must be an integer
n ≥ 0

Test cases:

Normal
Input: n=5
Output:
n: 5
Factorial: 120

Border
Input: n=0
Output:
n: 0
Factorial: 1

Error
Input: n=-3
Output:
Error: invalid input
"""

n_text = input().strip()

try:
    n = int(n_text)
except:
    print("Error: invalid input")
    exit()

if n < 0 or n > 20:
    print("Error: invalid input")
    exit()

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

value = factorial(n)

print("n:", n)
print("Factorial:", value)


# CONCLUSIONES

# Las funciones ayudan a organizar el código dividiéndolo en partes claras y reutilizables, evitando repeticiones.
# Usar return es más útil que solo imprimir porque permite reutilizar los resultados en cálculos o decisiones posteriores.
# Los parámetros y los valores por defecto hacen el código más flexible y adaptable a distintas situaciones.
# Encapsular lógica en funciones resulta muy cómodo en tareas repetidas, como validaciones o cálculos frecuentes.
# También facilita mantener limpia la lógica principal, separando lo esencial de las funciones de apoyo.
# Aprendí que esta separación mejora la lectura, el mantenimiento y la escalabilidad de cualquier programa.

# References:
# 1) Python documentation – Defining Functions (def, return, parameters)
# 2) Python Tutorial – Sección de funciones y alcance de variables (scope)
# 3) “Automate the Boring Stuff with Python” – Capítulos sobre funciones y modularización
# 4) Artículos sobre diseño de funciones y buenas prácticas (Real Python, GeeksforGeeks)
# 5) Apuntes de clase y recursos oficiales de programación básica sobre definición y uso de funciones

# REPOSITORIO DE GITHUB
https://github.com/2530057-oss/METODOLOGIAS_DE_LA_PROGRAMACION/blob/main/src/homework_unit2/2530057_RamirezValentin_funciones_en_python.py