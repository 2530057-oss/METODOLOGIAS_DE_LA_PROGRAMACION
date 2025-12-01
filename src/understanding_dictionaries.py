#Empty Dictionary

"""
homer_0 = {
    "color": "yellow", 
    'bag': "maggie-bag", 
    
}
print(homer_0)
print(type(homer_0))

marge = {
    "color": "yellow",
    'bag': "homer-donut",
    "hair": "blue",
    "dress": "green",
    "mom": True 
}
gun_0 = {"Scar": "yellow-orange", "headshot": 1.5}

# Modifying an element of a dictionary

alien_0["color"] = "Blue"
print(alien_0)

# Adding elements to a dictionnary
alien_0["x_position"] = 0
alien_0["y_position"] = 25
alien_0["name"]="paul"

print(alien_0)

## Looping though items
print("\n Looping though items")
for key, value in alien_0.items():
    print(f"The key {key} has value {value}")

## Looping though keys
print("\n Looping though keys")
for key in alien_0.keys():
    print(key)

## Looping though values
print("\n Looping though values")
for value in alien_0.values():
    print(value)

"""

#NESTING
# Listas de diccionarios
# Listas en diccionarios
# Diccionarios en diccionarios 

covenant_grunt = {
    "color": "orange", 
    "weapon": "plasma-gun"
    "armament": "plasma-granade",
    "health": 2,
}


covenant_elite = {
    "color": "blue", 
    "weapon": "plasma-sword"
    "armament": "plasma-granade",
    "health": 7,
}

covenant_jackal = {
    "color": "gray", 
    "weapon": "plasma-gun"
    "armament": "plasma-granade",
    "health": 5,
}


# Lista de dicionarios
covenants = [
    covenant_grunt, 
    covenant_elite, 
    covenant_jacka
]

for covenant in covenants:
    print("\n", covenant)
    for key, value in covenants.items():
        print(key, value)

## Listas en diccionarios
students = {
    "Santiago": ["reprobado", "prepa1", "rebelde"],
    "jorge crack", ["aprobado", "cbtis271", "goleador"],
    "gabriel": ["aprobado", "119muerte", "crack-fortnite"],
}

# Diccionarios en diccionarios 
sensores = {

}



# Estudiar el metodo 