"""********************************************************
Archivo Nro. 21 - Ciclos (While)  -   Mientras.
21_while.py

 - Este tipo de ciclos, se ejecutará siempre y cuando se cumpla una condición. 
 - Los ciclos infinistos se pueden detener con Ctrl + C
 - Los ciclos se pueden romper forzadamente con la instrucción break.
 - Otro condicional para trabajar en los ciclos, es la instrución continue, la 
 cual salta el código que le siga mientras se cumpla con la condición.

********************************************************"""

# Contador del 1 al 20
counter = 0
while counter <20:
    counter += 1
    print(counter)


# Contador del 1 al 15
counter = 0
while counter <20:
    counter += 1
    print(counter)
    if counter == 15:
        break
    

# Contador del 15 al 20
counter = 0
while counter <20:
    counter += 1
    if counter < 15:
        continue
    print(counter)


# Contador del 10 al 15
counter = 0
while counter < 20:
    counter += 1
    if counter < 10:
        continue
    print(counter)
    if counter == 15:
        break