# Alejandro Valentin Ramirez Gonzalez
# 2530057
# 1-3

# Resumen ejecutivo
# Un CRUD es un conjunto de operaciones básicas para manejar datos: Create (crear), Read (leer), Update (actualizar) y Delete (eliminar).
# Elegí usar un diccionario o lista de diccionarios porque permite asociar claves con valores de cada registro, facilitando búsquedas y actualizaciones.
# Las funciones ayudan a organizar la lógica del CRUD, haciendo cada operación independiente y el código más limpio y reutilizable.
# El programa incluye un menú principal para seleccionar la operación deseada, así como funciones específicas para crear, leer, actualizar, eliminar y listar elementos.
# Esto permite manejar datos de manera estructurada y mantener la coherencia de los registros en memoria.



# Gestor CRUD usando diccionarios y/o listas con funciones.
"""
Description:
Implement a Python program that manages a collection of "items" in memory using CRUD operations. Each item can represent, for example, an inventory product with the following fields:

* id (string or int, unique)
* name (string)
* price (float)
* quantity (int)

Inputs:

* option (string or int; menu choice)
* item_id (string or int)
* name (string)
* price (float)
* quantity (int)

Outputs:
Messages like:

* "Item created"
* "Item updated"
* "Item deleted"
* "Item not found"
* "Items list:" followed by the list of items (any readable format)

Validations:

* option must be one of the defined options (e.g., 0-5)
* item_id not empty after strip()
* price and quantity must be valid numbers:

  * price ≥ 0.0
  * quantity ≥ 0
* If validation fails, show "Error: invalid input" and DO NOT perform the operation
* In CREATE: if id already exists, decide a policy (e.g., do not allow duplicates) and document it
* In READ/UPDATE/DELETE: if id does not exist, show "Item not found"

Test cases:

Normal
Input: Create item with id=101, name="Pen", price=1.5, quantity=20
Output: Item created

Border
Input: Create item with existing id=101
Output: Error: duplicate id

Error
Input: Update item with id=" ", price=-5
Output: Error: invalid input
"""

def create_item(data, item_id, name, price, quantity):
    if item_id in data:
        return False
    data[item_id] = {"name": name, "price": price, "quantity": quantity}
    return True

def read_item(data, item_id):
    return data.get(item_id)

def update_item(data, item_id, name, price, quantity):
    if item_id not in data:
        return False
    data[item_id] = {"name": name, "price": price, "quantity": quantity}
    return True

def delete_item(data, item_id):
    return data.pop(item_id, None) is not None

def list_items(data):
    if not data:
        print("There are no items.")
    else:
        for i, d in data.items():
            print(f"ID: {i} | {d}")

# VALIDATIONS 

def val_float(v):
    try: v=float(v); return v if v>=0 else None
    except: return None

def val_int(v):
    try: v=int(v); return v if v>=0 else None
    except: return None

# PRINCIPAL MENU 

print("Welcome to the HEB packet page") 

def main():
    items = {}
    while True:
        print("\n1) Create  2) Read  3) Update 4) Delete 5) List 0) Exit")
        option = input("Choose your option: ").strip()

        if option == "0":
            print("LEAVING..."); break
        
        if option not in {"1","2","3","4","5"}:
            print("Error: invalid input"); continue

        if option == "1":  # CREATE
            item_id = input("ID: ").strip()
            if not item_id: print("Error: invalid input"); continue
            name = input("Name: ")
            price = val_float(input("Price: "))
            quantity = val_int(input("Quantity: "))
            if price is None or quantity is None:
                print("Error: invalid input"); continue
            print("Item created" if create_item(items, item_id, name, price, quantity)
                  else "Error: ID already exists")

        elif option == "2":  # READ
            item = read_item(items, input("ID: ").strip())
            print(item if item else "Item not found")

        elif option == "3":  # UPDATE
            item_id = input("ID: ").strip()
            if item_id not in items:
                print("Item not found"); continue
            name = input("New name: ")
            price = val_float(input("New price: "))
            quantity = val_int(input("New quantity: "))
            if price is None or quantity is None:
                print("Error: invalid input"); continue
            update_item(items, item_id, name, price, quantity)
            print("Item updated")

        elif option == "4":  # DELETE
            print("Item deleted" if delete_item(items, input("ID: ").strip())
                  else "Item not found")

        elif option == "5":  # LIST
            print("Items list:")
            list_items(items)
            print("End of list")

if _name_ == "_main_":
    main()


# CONCLUSIONES 

# El uso de funciones permitió separar cada operación del CRUD, facilitando su implementación y mantenimiento.
# Usar diccionarios o listas de diccionarios facilita acceder y modificar datos mediante claves, haciendo el manejo de registros más eficiente.
# Al validar entradas, surgieron problemas como valores vacíos o tipos incorrectos, que se resolvieron con condicionales y bucles de reintento.
# Esta estructura también permite listar o buscar rápidamente registros específicos.
# El CRUD se podría extender a un sistema más grande guardando los datos en archivos o bases de datos para mantener la información de forma persistente.

# References:
# 1) Python documentation – Data structures (dict, list)
# 2) Python documentation – Defining functions
# 3) Tutoriales sobre implementación de CRUD básico en memoria con Python (Real Python, GeeksforGeeks)

# REPOSITORIO DE GITHUB
https://github.com/2530057-oss/METODOLOGIAS_DE_LA_PROGRAMACION/blob/main/src/homework_unit2/2530057_RamirezValentin_CRUD.py
