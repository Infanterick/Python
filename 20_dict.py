"""********************************************************
Archivo Nro. 20 - Diccionarios  
20_dict.py

 - Archivo de práctica. 
********************************************************"""
# Creación del diccionario. 
person = {
    "name":"Erick",
    "last_name": "Infante",
    "age": 37,
    "langs": ["Python", "R"]
}

# Lectura del diccionario o atributos especificos. 
print(person)
print(person["name"])
print(person.items())   # Muestra todo los elementos del diccionario, clave y valor.
print(person.values())  # Muestra todos los valores, solo valores. 
print(person.keys())    # Muestra todas las claves, solo las claves. 


# Agregar atributos al diccionario. 
person["twitter"] = "@yoentwitter"


# Modificación de atributos. 
person["name"] = "Super Erick"
person["age"] -= 20
person["langs"].append("VBA")


# Eliminacion de atributos.
del person["langs"]
person.pop("age")



print(person)
