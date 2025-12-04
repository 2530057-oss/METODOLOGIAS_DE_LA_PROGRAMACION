# Alejandro Valentin Ramirez Gonzalez
# 2530057
# 1-3

# Resumen ejecutivo
# Una lista es una colección ordenada y mutable, mientras que una tupla es ordenada pero inmutable y no puede modificarse después de crearse.
# Un diccionario almacena pares clave–valor, permitiendo acceder rápidamente a la información mediante su clave.
# La mutabilidad de las listas permite agregar, quitar o modificar elementos, a diferencia de las tuplas que permanecen fijas.
# Los diccionarios se usan para asociar datos, como códigos con productos, nombres con registros o categorías con valores.
# Validar datos es fundamental para asegurar que cada estructura contenga el tipo y formato correctos antes de procesarlos.
# El documento incluirá la descripción de cada problema, el diseño de entradas y salidas y las validaciones aplicadas.
# También mostrará el uso práctico de listas, tuplas y diccionarios en catálogos, registros y estadísticas básicas.



# Problem 1: Shopping list basics (list operations)
"""
Description:
Work with a list of products (strings) and their quantities (integers). The program must:

1. Create an initial list of products.
2. Add a new product to the end.
3. Display the total number of items in the list.
4. Check whether a specific product exists in the list (boolean **is_in_list**).

Inputs:

* **initial_items_text** (string; e.g., `"apple,banana,orange"`).
* **new_item** (string; product to add).
* **search_item** (string; product to search for).

Outputs:

* `Items list:` <items_list>
* `Total items:` <len_list>
* `Found item:` true/false

Validations:

* initial_items_text must not be empty after `strip()`.
* Split the string by commas and trim spaces in each element.
* new_item and search_item must not be empty.
* If the initial list is empty after processing, the program will allow an empty list but still accept the new item (design decision documented here).

Test cases:
Normal:
Input: `"apple, banana, orange"`, new=`grape`, search=`banana`
Output: Items list: ['apple','banana','orange','grape'] | Total items: 4 | Found item: true

Border:
Input: `"apple"`, new=`kiwi`, search=`mango`
Output: Items list: ['apple','kiwi'] | Total items: 2 | Found item: false

Error:
Input: `""`, new=`pear`, search=`apple`
Output: Error: initial items cannot be empty.

"""

print("Enter the initial items separated by commas:")
initial_items_text = input().strip()

print("Enter a new item to add:")
new_item = input().strip()

print("Enter an item to search for:")
search_item = input().strip()

if not initial_items_text:
    print("Error: invalid input")
    exit()

items_list = [item.strip() for item in initial_items_text.split(",") if item.strip()]

if not new_item or not search_item:
    print("Error: invalid input")
    exit()

items_list.append(new_item)

len_list = len(items_list)
is_in_list = search_item in items_list

print("Items list:", items_list)
print("Total items:", len_list)
print("Found item:", str(is_in_list).lower())


# Problem 2: Points and distances with tuples
"""
Description:
Uses tuples to represent two points in a 2D plane: **(x1, y1)** and **(x2, y2)**. The program must:

1. Create two tuples **point_a** and **point_b** from numeric inputs.
2. Compute the Euclidean distance between both points.
3. Create a new tuple **midpoint** containing the midpoint coordinates.

Inputs:
* **x1, y1, x2, y2** (float; coordinates of the points)

Outputs:
* `Point A:` (x1, y1)
* `Point B:` (x2, y2)
* `Distance:` <distance>
* `Midpoint:` (mx, my)

Validations:
* All four inputs must be convertible to `float`.
* No additional range restrictions.

Test cases:
Normal:
Input: 0, 0, 3, 4
Output: Point A: (0.0, 0.0) | Point B: (3.0, 4.0) | Distance: 5.0 | Midpoint: (1.5, 2.0)

Border:
Input: 1, 1,1, 1
Output: Point A: (1.0, 1.0) | Point B: (1.0, 1.0) | Distance: 0.0 | Midpoint: (1.0, 1.0)

Error:
Input: x1="a", y1=2, x2=3, y2=4
Output: Error: invalid input
"""

try:
    x1 = float(input("Enter x1: ").strip())
    y1 = float(input("Enter y1: ").strip())
    x2 = float(input("Enter x2: ").strip())
    y2 = float(input("Enter y2: ").strip())
except:
    print("Error: invalid input")
    exit()

point_a = (x1, y1)
point_b = (x2, y2)

distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
midpoint = ((x1 + x2) / 2, (y1 + y2) / 2)

print("Point A:", point_a)
print("Point B:", point_b)
print("Distance:", distance)
print("Midpoint:", midpoint)


# Problem 3: Product catalog with dictionary
"""
Description:
Manages a small product catalog using a dictionary where:

* key: product name (string)
* value: unit price (float)

The program must:

1. Create an initial dictionary with at least 3 products.
2. Read the name of a product and the quantity to buy.
3. Calculate the total to pay if the product exists.
4. If the product does not exist, show an error message.

Inputs:
* product_name (string)
* quantity (int; quantity to buy)

Outputs:
If the product exists:

* Unit price: <unit_price>
* Quantity: <quantity>
* Total: <total_price>

If the product does not exist:

* Error: product not found

Validations:
* quantity > 0
* product_name not empty after strip()
* Check if product_name exists in the dictionary

Test cases:
Normal:
Input: product="apple", quantity=3
Output: Unit price: 1.2 | Quantity: 3 | Total: 3.6

Border:
Input: product="milk", quantity=1
Output: Unit price: 0.99 | Quantity: 1 | Total: 0.99

Error:
Input: product="unknown", quantity=2
Output: Error: product not found
"""

product_prices = {
    "apple": 10.0,
    "banana": 6.5,
    "orange": 8.0
}

product_name = input("Enter product name: ").strip()
try:
    quantity = int(input("Enter quantity: ").strip())
except:
    print("Error: invalid input")
    exit()

if not product_name or quantity <= 0:
    print("Error: invalid input")
    exit()

if product_name not in product_prices:
    print("Error: product not found")
    exit()

unit_price = product_prices[product_name]
total_price = unit_price * quantity

print("Unit price:", unit_price)
print("Quantity:", quantity)
print("Total:", total_price)

# Problem 4: Student grades with dict and list
"""
Description:
Manages student grades using a dictionary:

* key: student name (string)
* value: list of grades (list of float)

The program must:

1. Create a dictionary with at least 3 students, each with a list of grades.
2. Read the name of a student.
3. Calculate the average of their grades.
4. Indicate if the student is passed (average >= 70.0) with a boolean is_passed.

Inputs:
* student_name (string)

Outputs:
If the student exists:

* Grades: <grades_list>
* Average: <average>
* Passed: true/false

If the student does not exist:

* Error: student not found

Validations:
* student_name not empty after strip()
* Check if student_name is a key in the dictionary
* Verify that the grade list is not empty before calculating the average

Test cases:
Normal:
Input: student="Maria"
Output: Grades: [80, 75, 90] | Average: 81.67 | Passed: true

Border:
Input: student="Luis"
Output: Grades: [70] | Average: 70.0 | Passed: true

Error:
Input: student="Unknown"
Output: Error: student not found
"""

grades = {
    "Alice": [90.0, 85.0, 88.0],
    "Bob": [70.0, 72.5, 68.0],
    "Carol": [95.0, 92.0, 98.0]
}

student_name = input("Enter student name: ").strip()

if not student_name:
    print("Error: invalid input")
    exit()

if student_name not in grades:
    print("Error: student not found")
    exit()

grades_list = grades[student_name]

if len(grades_list) == 0:
    print("Error: invalid input")
    exit()

average = sum(grades_list) / len(grades_list)
is_passed = average >= 70.0

print("Grades:", grades_list)
print("Average:", average)
print("Passed:", str(is_passed).lower())

# Problem 5: Word frequency counter (list + dict)
"""
Description:
Counts the frequency of each word in a sentence using:

* A list of words
* A dictionary where:

  * key: word (string)
  * value: frequency (int)

The program must:

1. Read a sentence.
2. Convert it to lowercase and split it into a word list.
3. Build a frequency dictionary.
4. Display the full dictionary and the most common word.

Inputs:
* sentence (string)

Outputs:
* Words list: <words_list>
* Frequencies: <freq_dict>
* Most common word: <word> (any is valid if there is a tie)

Validations:
* sentence not empty after strip()
* Handle simple punctuation if desired (e.g., using replace())
* Ensure the word list is not empty

Test cases:
Normal:
Input: "apple banana apple orange"
Output: Words list: ["apple", "banana", "apple", "orange"] | 
Frequencies: {"apple": 2, "banana": 1, "orange": 1} | Most common word: apple

Border:
Input: "one two two"
Output: Words list: ["one", "two", "two"] | Frequencies: {"one": 1, "two": 2} |
 Most common word: two

Error:
Input: ""
Output: Error: sentence cannot be empty.
"""

import string

sentence = input("Enter a sentence: ").strip()

if not sentence:
    print("Error: invalid input")
    exit()

# Remove basic punctuation
for p in string.punctuation:
    sentence = sentence.replace(p, "")

words_list = sentence.lower().split()

if len(words_list) == 0:
    print("Error: invalid input")
    exit()

freq_dict = {}
for word in words_list:
    if word in freq_dict:
        freq_dict[word] += 1
    else:
        freq_dict[word] = 1

most_common_word = max(freq_dict, key=freq_dict.get)

print("Words list:", words_list)
print("Frequencies:", freq_dict)
print("Most common word:", most_common_word)

# Problem 6: Simple contact book (dictionary CRUD)
"""
Description:
Implements a mini "contact book" using a dictionary where:

* key: contact name (string)
* value: phone number (string)

The program must:

1. Create an initial dictionary with some contacts.
2. Read an action `action_text` ("ADD", "SEARCH", or "DELETE").
3. Perform the action:

   * "ADD": read `name` and `phone`, add or update the contact.
   * "SEARCH": read `name` and display the phone if it exists.
   * "DELETE": read `name` and remove the contact if it exists.
4. Show a message indicating the result of the operation.

Inputs:

* `action_text` (string; "ADD", "SEARCH", or "DELETE")
* `name` (string; depends on the action)
* `phone` (string; only for "ADD")

Outputs:

* For "ADD":

  * Contact saved: name, phone
* For "SEARCH":

  * If exists: Phone: <phone>
  * If not: Error: contact not found
* For "DELETE":

  * If exists: Contact deleted: name
  * If not: Error: contact not found

Validations:

* Normalize `action_text` to uppercase
* Check that `action_text` is one of the three valid options
* `name` must not be empty after strip()
* For "ADD": `phone` must not be empty after strip()

Test cases:
Normal:
Input: action="ADD", name="Alice", phone="12345"
Output: Contact saved: Alice, 12345

Border:
Input: action="SEARCH", name="Alice"
Output: Phone: 12345

Error:
Input: action="DELETE", name="Bob"
Output: Error: contact not found
"""

contacts = {
    "Alice": "1234567890",
    "Bob": "9876543210",
    "Carol": "5555555555"
}

action_text = input("Enter action (ADD, SEARCH, DELETE): ").strip().upper()

if action_text not in ("ADD", "SEARCH", "DELETE"):
    print("Error: invalid input")
    exit()

name = input("Enter contact name: ").strip()

if not name:
    print("Error: invalid input")
    exit()

if action_text == "ADD":
    phone = input("Enter phone number: ").strip()
    if not phone:
        print("Error: invalid input")
        exit()
    contacts[name] = phone
    print("Contact saved:", name, phone)

elif action_text == "SEARCH":
    if name in contacts:
        print("Phone:", contacts[name])
    else:
        print("Error: contact not found")

elif action_text == "DELETE":
    if name in contacts:
        contacts.pop(name)
        print("Contact deleted:", name)
    else:
        print("Error: contact not found")

# CONCLUSIONES

# Las listas son ideales cuando necesitamos colecciones que cambien con frecuencia, permitiendo agregar o eliminar elementos fácilmente.
# Las tuplas son útiles para datos que deben permanecer constantes, garantizando que no se modifiquen accidentalmente.
# Los diccionarios facilitan búsquedas rápidas y precisas mediante claves únicas, lo que agiliza el acceso a la información.
# Combinar estas estructuras permite patrones útiles, como diccionarios cuyos valores son listas para agrupar elementos relacionados.
# También se usan listas de tuplas para almacenar registros que no deben cambiar o tuplas de diccionarios para datos inmutables con claves.
# Estas combinaciones muestran cómo organizar y acceder a datos complejos de forma eficiente y clara.

# References:

# 1) Python documentation – Built-in Types: list, tuple, dict
# 2) Python Tutorial – Sección de estructuras de datos básicas (listas, tuplas y diccionarios)
# 3) “Automate the Boring Stuff with Python” – Capítulos sobre colecciones y manejo de datos
# 4) Artículos sobre buenas prácticas en el uso de colecciones en Python (Real Python, GeeksforGeeks)
# 5) Apuntes de clase y recursos oficiales de programación básica sobre listas, tuplas y diccionarios

# REPOSITORIO DE GITHUB
https://github.com/2530057-oss/METODOLOGIAS_DE_LA_PROGRAMACION/blob/main/src/homework_unit2/2530057_RamirezValentin.py