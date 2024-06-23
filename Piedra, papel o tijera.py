"""*************************************************
Juego: piedra, papel o tijera. 
Fecha: 22-06-2024
Autor: Erick Infante
*************************************************"""

import random
options = ("piedra", "papel", "tijera")
user_wins = 0
computer_wins = 0
rounds = 1

print("""
      [ 🤖 Bienvenido al juego Piedra, Papel o tijera 🙋]
                  >>> Ingresa una opción <<<
      """)


while user_wins <2 and computer_wins <2:
    
    print("*" * 10)
    print("ROUND # ", rounds)
    print("*" * 10,"\n")
    
    computer_option = random.choice(options)
    user_option = input("Elija una opción (piedra, papel o tijera)\n=> ").lower()

    print(f"\nEl computador eligió {computer_option}.")
    print(f"Tu elegiste {user_option}.\n")

    if user_option == computer_option:
        print("Empate...!!!\n")
    elif user_option not in options:
        print("El valor ingresado no es correcto;\npor favor elija una opción correcta \
            \n(Piedra, papel o tijera)\n")
        continue
    elif user_option == "piedra" and computer_option == "tijera" or \
        user_option == "tijera" and computer_option == "papel" or \
        user_option == "papel" and computer_option == "piedra":
        print(f"Has ganado...!!! \n{user_option.capitalize()} le gana a {computer_option}.\n")
        user_wins += 1
    else:
        print(f"Perdiste...!!! \n{computer_option.capitalize()} le gana a {user_option}.\n")    
        computer_wins +=1
    rounds +=1
    print("Computador:", computer_wins, "veces.")
    print("usuario:", user_wins, "veces.\n")

if computer_wins == 2:
    print("LO SIENTO, EL COMPUTADOR HA GANADO...!!!")
else:
    print("FELICITACIONES, LE HAS GANADO AL COMPUTADOR...!!!")

# Fin