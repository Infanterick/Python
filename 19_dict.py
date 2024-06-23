"""********************************************************
Archivo Nro. 19 - Diccionarios  
19_dict.py

 - Se define con llaves {}
 - Sirve para guardar multiples atributos para consultar luego. 
********************************************************"""

my_dict = {}            # Se declara con {}
print(type(my_dict))    # La clase (tipo) del elemento es dict

my_dict = {
    "Nombre": "Erick",
    "Apellido": "Infante",
    "Edad": 37,
    "Bla bla": "bla bla bla"
}

print(my_dict)
print(len(my_dict))             # Para conocer la longitud del diccionario. 

print(my_dict["Apellido"])      # Es posible buscar una variable dentro del diccionacio de esta forma.
print(my_dict.get("Edad"))      # Con el metodo get en caso de no existir el atributo buscado el programa no arroja error y te indica que no se encuentra (None).

print("edad" in my_dict)        # Se puede buscar si existe o no un atributo dentro del diccionario. 
print("Tamaño" in my_dict)      

