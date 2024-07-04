"""*************************************************
Juego: piedra, papel o tijera. 
Fecha: 22-06-2024
Autor: Erick Infante
*************************************************"""

print("""
*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
/*/   Piedra, papel o tijera   /*/
*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
""")

import random

def choose_options():
    options = ("piedra", "papel", "tijera")
    computer_option = random.choice(options)
    user_option = input("Elija una opción (piedra, papel o tijera) => ").lower()

    if user_option not in options:
        print("\nEl valor ingresado no es correcto;\npor favor elija una opción correcta \
            \n(Piedra, papel o tijera)\n")
        return None, None
    
    print(f"\nEl computador eligió: {computer_option}.")
    print(f"Tu elegiste: {user_option}.\n")
    return user_option, computer_option


def check_rules(user_option, computer_option, user_wins, computer_wins):
        
        if user_option == computer_option:
            print("Empate...!!!\n")
       
        elif user_option == "piedra" and computer_option == "tijera" or \
            user_option == "tijera" and computer_option == "papel" or \
            user_option == "papel" and computer_option == "piedra":
            print(f"Has ganado...!!! {user_option.capitalize()} le gana a {computer_option}.\n")
            user_wins += 1
       
        else:
            print(f"Perdiste...!!! {computer_option.capitalize()} le gana a {user_option}.\n")    
            computer_wins +=1
       
        return user_wins, computer_wins


def run_game():

    user_wins = 0
    computer_wins = 0
    rounds = 1

    while user_wins <2 and computer_wins <2:
        
        print("*" * 20)
        print("ROUND # ", rounds,"\n")
        print("Computador:", computer_wins)
        print("usuario:", user_wins)        
        print("*" * 20,"\n")
    
        rounds +=1

        user_option, computer_option = choose_options()
        user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)

        if computer_wins == 2:
            print("LO SIENTO, EL COMPUTADOR HA GANADO...!!!\n")
            break
        if user_wins == 2:
            print("FELICITACIONES, LE HAS GANADO AL COMPUTADOR...!!!\n")
            break

run_game()