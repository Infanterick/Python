"""*************************************************
Juego: piedra, papel o tijera. 
Fecha: 22-06-2024
Autor: Erick Infante
*************************************************"""

import random
options = ("piedra", "papel", "tijera")

computer_option = random.choice(options)
user_option = input("Elija una opción (piedra, papel o tijera)\n=> ").lower()

print(f"\nEl computador eligió {computer_option}.")
print(f"Tu elegiste {user_option}.\n")

if user_option == computer_option:
    print("Empate...!!!\n")
elif user_option not in options:
    print("El valor ingresado no es correcto;\npor favor elija una opción correcta \
          \n(Piedra, papel o tijera)\n")
elif user_option == "piedra" and computer_option == "tijera" or \
    user_option == "tijera" and computer_option == "papel" or \
    user_option == "papel" and computer_option == "piedra":
    print(f"Has ganado...!!! \n{user_option} gana a {computer_option}.\n")
else:
    print(f"Perdiste...!!! \n{computer_option} gana a {user_option}.\n")

"""
continuar = input("¿Desea intentarlo nuevamente? (S/N)").lower()
if continuar == s:

"""