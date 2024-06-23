"""***********************************************************
Archivo Nro. 18 - Tuplas  
18_tuples.py

 - A diferencia de las listas, se declara entre parentesis.
 - Son unmutable (no modificables).
 - Despues de ser creada, no se puede agregar mas información.
 - Puede ser convertida en lista y viceversa.
 - Puede tener varios tipos de datos.

***********************************************************"""


numbers = (1,2,3,4,5)               # Las tuplas se crean asignando los valores entre parentesis.
strings = ("Hola", "mundo","...")   # Pueden contener distintos tipos de datos.  

print(numbers[1])       # Se leer igual que en una lista. 
print(strings[-2])
print(strings.index("mundo"))
print(strings.count("..."))
print(type(numbers))    # Muestra la clase (tipo) del elemnto: Tupla.

my_list = list(strings) # Se puede convertir una tupla en una lista. 
print(type(my_list))

my_tuple = tuple(my_list) # Se puede convertir una lista en una tupla. 
print(type(my_tuple))

"""*******************************************************************************
La Principal ventaja de trabajar con tuplas, es que nos podemos asegurar
que los datos ingresados, no sean modificados. 
*******************************************************************************"""