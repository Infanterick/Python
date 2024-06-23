"""***********************************************************
Archivo Nro. 17 -  CRUD -> Create, Read, Update & Delete
17_crud.py

***********************************************************"""

# Create
numbers = [1,2,3,4,5]
tasks = ["todo 1","todo 2","todo 3"]
strings = ["re", "ab", "ed"]
new_list = numbers + tasks          # Crear nueva lista a partir de concatenar listas. 

# Read
print(numbers[2])

# Update
numbers[-1] = 10            # Reemplazar el valor del ultimo elemento de la lista. 
numbers.append(700)         # Append por defecto agrega los elementos al final.
numbers.insert(0, "Hola")   # Insert, agrega el nuevo elemento en el lugar indicado (en este caso 0 -> primer elemento)
numbers.insert(3, "change") # No elimina el elemento de la posición indicada, solo lo desplaza. 

new_list.reverse()                # Invierte la posición de todos los elementos de la lista. 
numbers.sort()                  # Ordena los elementos (por defecto de menor a mayor).
strings.sort()                  # Tambien ordena string de letras según el abecedario. 

# Delete
new_list.remove("todo 1")       # Remove, elimina el elemento indicado. 
new_list.pop()                  # Pop por defecto elimina el ultimo elemento de la lista. 
new_list.pop(0)                 # Tambien, elimina los elementos de las posiciones indicadas. 


# CRUD
print(new_list.index("todo 2"))     # Leer la posición de un elemento de lista ("todo 2").
index = new_list.index("todo 2")    # Crear nueva variable con la posicíon del elemento en una variable (index).
new_list[index] = "todo change"     # Reemplazar el valor del elemento buscado.



# Playgrounds: Agrega, modifica y elimina elementos de una lista. 
letters = ['A', 'B', 'C', 'D', 'E', 'F']
letters.append("G")
letters[0] = "Z"
letters.pop(2)
letters.reverse()
print(letters)
