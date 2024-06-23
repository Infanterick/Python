"""***********************************************
Archivo Nro. 16 -  Listas
16_lists.py

 - Las listas permiten guardar varios tipos de datos. 
 - Las listas, pueden ser modificadas (mutadas).
 - Las listas se crean entre corchetes []
***********************************************"""

numbers = [1,2,3,4]
print(numbers)
print(type(numbers))        # Muesta el tipo de dato de la variable numbers (lista).

tasks = ["make a dishes", "play videogames"]    # Lista con elementos iguales. 
print(tasks)

types = [1, True, "Hola"]   # Lista con elementos de distintos tipos de dato.
print(types)

print(numbers[0])           # Muestra el 1er elemento de la lista numbers.
print(tasks[0])             # Muestra el 1er elemento de la lista tasks.

tasks[0] = "watch platzi courses"  # modificar el 1er elemento de la lista task
tasks[0] = "do the dishes"         # modificar el 1er elemento de la lista task
print(tasks)

print(numbers[0:3])         # Muestra los 1eros tres elementos de la lista numbers
print(True in tasks)        # Muestra si existe algún True en la lista tasks
print("Hola" in types)      # Muestra si existe algún "Hola" en la lista numbers


