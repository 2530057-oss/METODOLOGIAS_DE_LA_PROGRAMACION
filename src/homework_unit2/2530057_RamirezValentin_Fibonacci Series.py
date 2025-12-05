# Alejandro Valentin Ramirez Gonzalez
# 2530057
# 1-3

# Resumen ejecutivo
# La serie de Fibonacci es una secuencia donde cada número se obtiene sumando los dos anteriores, iniciando típicamente en 0 y 1.
# Calcular la serie hasta un número de términos n significa generar los primeros n valores de esta secuencia en orden.
# El programa incluirá la lectura de n desde la entrada, una validación básica para asegurar que n sea un entero positivo,
# y finalmente la generación y presentación de la serie completa hasta alcanzar la cantidad solicitada de términos.


# Problem: Fibonacci series up to n terms
"""
Description:
Implement a program that calculates and prints the Fibonacci sequence up to **n** terms. The sequence must start with 0 and 1.

If n = 1 → output: 0
If n = 2 → output: 0, 1
If n = 7 → output: 0, 1, 1, 2, 3, 5, 8

The program must:

1. Read **n**.
2. Validate **n**.
3. Generate the Fibonacci sequence using a loop.
4. Print all terms in one line separated by spaces or commas.

Inputs:
n (int; number of terms)

Outputs:
Number of terms: <n> (optional)
Fibonacci series: <t1> <t2> ... <tn>

Validations:
n must be convertible to int
n ≥ 1

Test cases:

Normal
Input: n=7
Output:
Fibonacci series: 0 1 1 2 3 5 8

Border
Input: n=1
Output:
Fibonacci series: 0

Error
Input: n=0
Output:
Error: invalid input
"""

print("Welcome to the fibonacci sequence")
try: 
    num = int(input("How many values do you want?: "))
    if num>=1 and num<=35:
        a = 0
        b = 1
        sum = 0 
        count = 1
        print("This is the fibonacci serie")
        while(count<=num):
            print(sum)
            count+=1
            a=b
            b=sum
            sum=a+b
    else:
        print(ValueError)
except: 
    print(ValueError)


# Conclusiones

# El uso de un bucle facilitó generar cada nuevo término de la serie tomando los dos anteriores de forma automática.
# Es importante manejar los casos especiales n = 1 y n = 2 porque la serie tiene valores iniciales fijos que no siguen la regla general.
# Esta lógica puede reutilizarse en otros programas que necesiten secuencias acumulativas, simulaciones o cálculos iterativos basados en valores previos.

# References:

# 1) Python documentation – while and for loops
# 2) Tutoriales de Python sobre la serie de Fibonacci (Real Python, GeeksforGeeks)
# 3) Apuntes de clase y recursos oficiales de la materia sobre secuencias y bucles

# REPOSITORIO DE GITHUB
