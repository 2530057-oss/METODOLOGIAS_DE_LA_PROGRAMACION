
# Alejandro Valentin Ramirez Gonzalez
# 2530057
# 1-3

# RESUMEN EJECUTIVO

# En Python, int representa números enteros sin decimales, mientras que float maneja números con punto decimal.
# Los float permiten valores más precisos o fraccionarios, pero pueden tener errores de redondeo por su naturaleza binaria.
# Un booleano (True/False) es un tipo lógico que resulta de comparaciones como ==, >, <, >=, <= o expresiones lógicas con and, or, not.
# Validar rangos es esencial para evitar datos fuera de límites y prevenir errores como divisiones entre cero.
# Esto garantiza que los cálculos numéricos sean seguros y que el programa no falle por valores inválidos.
# El documento incluirá la descripción de cada problema, entradas y salidas esperadas y las validaciones aplicadas.
# También mostrará cómo se usan enteros, flotantes y booleanos para tomar decisiones y controlar el flujo del programa.


# Problem 1: Temperature converter and range flag
"""
Description:
Converts a temperature in Celsius (float) to Fahrenheit and Kelvin. It also determines a boolean 
value `is_high_temperature`, which is true if the Celsius temperature is greater than or equal to
30.0, and false otherwise.

Inputs:
* `temp_c`: float value representing the temperature in °C.

Outputs:
* "Fahrenheit:" `<temp_f>`
* "Kelvin:" `<temp_k>`
* "High temperature:" true|false

Validations:
* Verify that `temp_c` can be converted to float.
* Do not allow physically impossible temperatures in Kelvin (e.g., `temp_k < 0.0`).

Test cases:
Normal:
Input: 25
Output: Fahrenheit: 77.0 | Kelvin: 298.15 | High temperature: false

Border:
Input: 30
Output: Fahrenheit: 86.0 | Kelvin: 303.15 | High temperature: true

Error:
Input: -500
Output: Error: invalid physical temperature.
"""


temp_input = input("Enter temperature in Celsius: ")

try:
    temp_c = float(temp_input)
    temp_k = temp_c + 273.15
    if temp_k < 0:
        print("Error: invalid physical temperature.")
    else:
        temp_f = temp_c * 9 / 5 + 32
        is_high_temperature = temp_c >= 30.0
        print("Fahrenheit:", temp_f)
        print("Kelvin:", temp_k)
        print("High temperature:", "true" if is_high_temperature else "false")
except:
    print("Error: invalid input.")


# Problem 2: Work hours and overtime payment
"""
Description:
Calculates the total weekly payment of a worker. Up to 40 hours are paid at the normal hourly rate (float). Overtime hours (more than 40) are paid at 150% of the normal rate. It also produces a boolean `has_overtime` indicating whether the worker worked overtime.

Inputs:
* `hours_worked`: float representing weekly hours worked.
* `hourly_rate`: float representing pay per hour.

Outputs:
* "Regular pay:" `<regular_pay>`
* "Overtime pay:" `<overtime_pay>`
* "Total pay:" `<total_pay>`
* "Has overtime:" true|false

Validations:
* `hours_worked` must be ≥ 0.
* `hourly_rate` must be > 0.
* If any validation fails, output: **"Error: invalid input"**.

Test cases:
Normal:
Input: hours=38, rate=10
Output: Regular pay: 380 | Overtime pay: 0 | Total pay: 380 | Has overtime: false

Border:
Input: hours=40, rate=12
Output: Regular pay: 480 | Overtime pay: 0 | Total pay: 480 | Has overtime: false

Error:
Input: hours=-5, rate=10
Output: Error: invalid input
"""


hours = input("Enter hours worked: ")
rate = input("Enter hourly rate: ")

try:
    hours = float(hours)
    rate = float(rate)

    if hours < 0 or rate <= 0:
        print("Error: invalid input")
    else:
        reg_hours = min(hours, 40)
        over_hours = max(hours - 40, 0)

        regular_pay = reg_hours * rate
        overtime_pay = over_hours * rate * 1.5
        total_pay = regular_pay + overtime_pay
        has_overtime = hours > 40

        print("Regular pay:", regular_pay)
        print("Overtime pay:", overtime_pay)
        print("Total pay:", total_pay)
        print("Has overtime:", str(has_overtime).lower())
except:
    print("Error: invalid input")



# Problem 3: Discount eligibility with booleans
"""
Description:
Determines whether a customer qualifies for a discount on a purchase. A discount is applied if the customer is a student, a senior, or if the purchase total is at least 1000.0. When eligible, a 10% discount is applied to calculate the final total.

Inputs:
* `purchase_total`: float representing the amount of the purchase.
* `is_student_text`: string that must be "YES" or "NO".
* `is_senior_text`: string that must be "YES" or "NO".

Outputs:
* "Discount eligible:" true|false
* "Final total:" `<final_total>`

Validations:
* `purchase_total` must be ≥ 0.0
* Convert `is_student_text` and `is_senior_text` to uppercase and then to booleans.
* If the text is not "YES" or "NO", output: **"Error: invalid input"**

Test cases:
Normal:
Input: total=500, student=NO, senior=YES
Output: Discount eligible: true | Final total: 450.0

Border:
Input: total=1000, student=NO, senior=NO
Output: Discount eligible: true | Final total: 900.0

Error:
Input: total=-10, student=YES, senior=NO
Output: Error: invalid input
"""

print("Enter purchase total:")
purchase_total = float(input().strip())

print("Are you a student? (YES/NO):")
is_student_text = input().strip().upper()

print("Are you a senior? (YES/NO):")
is_senior_text = input().strip().upper()

if purchase_total < 0.0:
    print("Error: invalid input")
    exit()

if is_student_text not in ("YES", "NO") or is_senior_text not in ("YES", "NO"):
    print("Error: invalid input")
    exit()

is_student = is_student_text == "YES"
is_senior = is_senior_text == "YES"

discount_eligible = is_student or is_senior or (purchase_total >= 1000.0)
final_total = purchase_total * 0.9 if discount_eligible else purchase_total

print("Discount eligible:", str(discount_eligible).lower())
print("Final total:", final_total)



# Problem 4: Basic statistics of three integers
"""
Description:
Reads three integers and calculates the sum, the average (as a float), the maximum value, the minimum value, and a boolean `all_even` that indicates whether all three numbers are even.

Inputs:
* n1 (int)
* n2 (int)
* n3 (int)

Outputs: 
* "Sum:" `<sum_value>`
* "Average:" `<average_value>`
* "Max:" `<max_value>`
* "Min:" `<min_value>`
* "All even:" true|false

Validations:
* Verify that all three inputs can be converted to integers.
* No further restrictions; negative values are allowed.

Test cases:
Normal:
Input: 4, 6, 8
Output: Sum: 18 | Average: 6.0 | Max: 8 | Min: 4 | All even: true

Border:
Input: 3, 3, 3
Output: Sum: 9 | Average: 3.0 | Max: 3 | Min: 3 | All even: false

Error:
Input: a, 5, 9
Output: Error: invalid input
"""


print("Enter three integers:")
try:
    n1 = int(input("Number 1: ").strip())
    n2 = int(input("Number 2: ").strip())
    n3 = int(input("Number 3: ").strip())
except:
    print("Error: invalid input")
    exit()

sum_value = n1 + n2 + n3
average_value = sum_value / 3
max_value = max(n1, n2, n3)
min_value = min(n1, n2, n3)
all_even = (n1 % 2 == 0) and (n2 % 2 == 0) and (n3 % 2 == 0)

print("Sum:", sum_value)
print("Average:", average_value)
print("Max:", max_value)
print("Min:", min_value)
print("All even:", str(all_even).lower())



# Problem 5: Loan eligibility (income and debt ratio)
"""
Description:
Determines whether a person is eligible for a loan based on:

* monthly_income (float)
* monthly_debt (float)
* credit_score (int)

The rule is:
* debt_ratio = monthly_debt / monthly_income
* A person is eligible if all of the following are true:

  * monthly_income ≥ 8000.0
  * debt_ratio ≤ 0.4
  * credit_score ≥ 650

Inputs:
* monthly_income (float; monthly income)
* monthly_debt (float; monthly debt payments)
* credit_score (int; credit score)

Outputs:
* "Debt ratio:" `<debt_ratio>`
* "Eligible:" true|false

Validations:
* monthly_income must be > 0.0 (to avoid division by zero)
* monthly_debt must be ≥ 0.0
* credit_score must be ≥ 0
* If any condition fails, output **"Error: invalid input"**

Test cases:
Normal:
Input: income=9000, debt=2000, score=700
Output: Debt ratio: 0.2222… | Eligible: true

Border:
Input: income=8000, debt=3200, score=650
Output: Debt ratio: 0.4 | Eligible: true

Error:
Input: income=0, debt=1000, score=700
Output: Error: invalid input
"""

print("Enter monthly income:")
monthly_income = float(input().strip())

print("Enter monthly debt:")
monthly_debt = float(input().strip())

print("Enter credit score:")
try:
    credit_score = int(input().strip())
except:
    print("Error: invalid input")
    exit()

if monthly_income <= 0.0 or monthly_debt < 0.0 or credit_score < 0:
    print("Error: invalid input")
    exit()

debt_ratio = monthly_debt / monthly_income
eligible = (monthly_income >= 8000.0 and debt_ratio <= 0.4 and credit_score >= 650)

print("Debt ratio:", debt_ratio)
print("Eligible:", str(eligible).lower())


# Problem 6: Body Mass Index (BMI) and category flag
"""
Description:
Calculates a person's Body Mass Index (BMI) using the formula:

* bmi = weight_kg / (height_m * height_m)

It also generates boolean values indicating:

* `is_underweight` (bmi < 18.5)
* `is_normal` (18.5 ≤ bmi < 25.0)
* `is_overweight` (bmi ≥ 25.0)

Inputs:
* weight_kg (float; weight in kilograms)
* height_m (float; height in meters)

Outputs:
* "BMI:" `<rounded_bmi>`
* "Underweight:" true|false
* "Normal:" true|false
* "Overweight:" true|false

Validations:
* weight_kg must be > 0.0
* height_m must be > 0.0
* If any validation fails, output **"Error: invalid input"**

Test cases:
Normal:
Input: weight=70, height=1.75
Output: BMI: 22.86 | Underweight: false | Normal: true | Overweight: false

Border:
Input: weight=50, height=1.65
Output: BMI: 18.37 | Underweight: true | Normal: false | Overweight: false

Error:
Input: weight=-5, height=1.7
Output: Error: invalid input
"""

print("Enter your weight in kilograms:")
weight_kg = float(input().strip())

print("Enter your height in meters:")
height_m = float(input().strip())

if weight_kg <= 0.0 or height_m <= 0.0:
    print("Error: invalid input")
    exit()

bmi = weight_kg / (height_m * height_m)

print("BMI:", round(bmi, 2))
print("Underweight:", str(bmi < 18.5).lower())
print("Normal:", str(18.5 <= bmi < 25.0).lower())
print("Overweight:", str(bmi >= 25.0).lower())

# CONCLUSIONES 
# Los enteros y flotantes se combinan para realizar cálculos reales, permitiendo mezclar valores exactos con cantidades decimales.
# Las comparaciones generan valores booleanos que se vuelven la base para tomar decisiones mediante estructuras if.
# Validar rangos y evitar divisiones entre cero es esencial para mantener cálculos seguros y evitar fallos inesperados.
# Diseñar condiciones con and, or y not enseña a controlar situaciones lógicas más complejas de manera clara.
# Estos mismos patrones se repiten en problemas de nómina, descuentos, préstamos y muchos otros escenarios cotidianos.
 
# References:
# 1) Python documentation – Built-in Types: Numeric Types (int, float) and Boolean Type (bool)
# 2) Python Tutorial – Operadores aritméticos, relacionales y lógicos
# 3) “Automate the Boring Stuff with Python” – Capítulos introductorios sobre tipos numéricos y control lógico
# 4) Apuntes de Algoritmos y Programación Básica – Sección de tipos numéricos y validación
# 5) Artículos sobre validación de datos numéricos y manejo de errores en cálculos

# REPOSITORIO DE GITHUB
https://github.com/2530057-oss/METODOLOGIAS_DE_LA_PROGRAMACION/blob/main/src/homework_unit2/2530057_ValentinRamirez.py