# import random library
import random
import os
import sys
import time


# Constant variables - colors available to choose from, code length and how many attempts
colors = ["R", "B", "G", "Y", "W", "P"]
code_length = 4
max_attempts_level1 = 12
max_attempts_level2 = 10
max_attempts_level3 = 8

#Title page
def main_page():
    """
    Main page with player options
    """
    clear_screen()
    print("\033[4;96m THIS IS THE BOSS BRAIN CHALLENGE! \033[0;96\n")
    print("\033[0;37m Can you crack the secrect code?\n")
    print("\x1B[3m With a code length of 4 and 6 available colours...")
    print(" ...there are only 1,296 different combinations!\x1B[0m\n")
    print("\033[0;92m **** Good luck CodeBreaker, May the force be with you! ****\n")    
    print("\033[0;33m  Choose \033[37;1m '1' \033[0;33m to Play")
    print("  Choose \033[37;1m '2' \033[0;33m for Instructions")
    print("  Choose \033[37;1m '3' \033[0;33m to Exit\n")

    while True:
        try:
            menu_choice = int(input("\033[37;1m Enter choice: \n"))
            if menu_choice == 1:
                choose_level()
                break
            elif menu_choice == 2:
                instructions()
                break
            elif menu_choice == 3:
                print(f"Exiting game....Game ended")
                break
            else:
                raise ValueError

        except ValueError:
            print(" Invalid key press. Please choose 1, 2 or 3")
# Instructions of play
def instructions():
    """
    Instructions for the user of how to play the game
    """
    clear_screen()
                
    print("\033[4;96m INSTRUCTIONS FOR PLAY \033[0;96m\n")
    print("\033[0;37m The CodeMaker (computer) creates a secret 4 colour code, choosing from 6 available colours.\n")
    print(" The CodeBreaker (player) needs to crack the secret code in a given number of attempts.\n")
    print(" The number of attempts will depend on which level is choosen.\n")
    print(" After each attempt, feedback is given as to how many colours are correct and how many colours are in the correct position.\n")
    print(" If the player cracks the secret code before running out of attempts, this is the end of the game.")
    print(" The player then has the choice to play again, return to the main page or exit the game completely.\n")
    print(" If the player runs out of attempts before cracking the correct secret code, this is the end of the game.")
    print(" The player then has the choice to play again, return to the main page or exit the game completely.\n")
    print(" If the player enters an incorrect letter or anything other than a letter, or if they don't leave a space between each letter,")
    print(" a message will appear to tell the player that they have entered something incorrectly and to check their guess.")
    print(" This does not count as an attempt and the player will have the same remaining number of attempts as before they made the incorrect guess.\n")
    print(" The choice of colors is: \033[31;1m Red(R) \033[34;1m Blue(B) \033[32;1m Green(G) \033[33;1m Yellow(Y) \033[37;1m White(W) \033[1;35:47m Pink(P) \n" )    
    print("\033[0;37m Choose 4 colors by entering the first letter of your choosen colours. You can use lower or upper case letters, leaving a space between each letter.\n")
    print(" The secret code can contain multiples of the same colour.\n")
    print("\033[0;37m Find the code in 12, 10 or 8 attempts, depending on which level is choosen, to become a Boss Brain!\n")
    print("\033[0;92m **** Good luck CodeBreaker, The force will be with you always ****\n") 
    print("\n" * 3)
    print("\033[33;1m Choose \033[37;1m '1' \033[33;1m to play")
    print(" Choose \033[37;1m '2' \033[33;1m to return to main page")
    print(" Choose \033[37;1m '3' \033[33;1m to Exit\n")
    while True:
                try:
                    menu_choice = int(input("\033[37;1m Enter choice: \n"))
                    if menu_choice == 1:
                        choose_level()
                        break
                    elif menu_choice == 2:
                        main_page()
                        break
                    elif menu_choice == 3:
                        print(f"Exiting game....Game ended")
                        break
                    else:
                        raise ValueError

                except ValueError:
                    print(" Invalid key press. Please choose 1, 2 or 3")
                    break

    exit()
           
# generate random code
def generate_random_code():
    """
    Genertes a 4-color random code from the 6 x color choices in the COLORS
    """
    code = random.choices(colors, k=code_length)
    
    return(code)

# choose level

def choose_level():
    """
    Choose level function
    """
    clear_screen()
    print("  \033[4;96m CHOOSE YOUR LEVEL \033[0;96m\n")
    print("\033[0;37m  Level 1 will give you 12 attempts")
    print("  Level 2 will give you 10 attempts")
    print("  Level 3 will give you 8 attempts\n")
    print("\033[0;92m **** Good luck CodeBreaker, Fear is the path to the darkside ****\n")
    print("\033[0;33m \x1B[3m(Choose \033[0;37m '4' \033[0;33m \x1B[3mto return to main page)")
    print(" \x1B[3m(Choose \033[0;37m '5' \033[0;33m \x1B[3mto Exit)\x1B[0m\n")

    while True:
        try:
            menu_choice = int(input("\033[37;1m Choose level (Enter '1', '2' or '3'): \n"))
            
            if menu_choice == 1:
                play_game_level1()
                break
            elif menu_choice == 2:
                play_game_level2()
                break 
            elif menu_choice == 3:
                play_game_level3()
                break                      
            elif menu_choice == 4:
                main_page()
                break
            elif menu_choice == 5:
                print(f"Exiting game....Game ended")
                break 
            else:
                raise ValueError

        except ValueError:
            print(" Invalid key press. Please choose 1, or 2")
    exit()
    
    
    print ("Please choose your level: \n")
    


# main game play
def play_game_level1():
    """
    Play game function
    """
    clear_screen()
    print(" \033[4;96m WELCOME TO THE BOSS BRAIN CHALLENGE - Level 1 \033[0;96m\n")
    print(" \033[0;37m Crack the color code to become a Boss Brain!\n")   
    print("  Choose from the following colors: \033[31;1m Red(R) \033[34;1m Blue(B) \033[32;1m Green(G) \033[33;1m Yellow(Y) \033[37;1m White(W) \033[1;35:47m Pink(P) \n")
    print(f" \033[0;37m Code Length: \033[33;1m{code_length}, \033[0;37m Max Attempts: \033[33;1m {max_attempts_level1}\n")
    
# while loop to itereate over game until max attempts made
    attempts = 0
    code = generate_random_code()
    print(code)
    while attempts < max_attempts_level1:
        answer = input(f"\033[0;37m Attempt {attempts + 1}/{max_attempts_level1}. Enter your guess(first letter): \n").upper().strip().split()
        if len(answer) != code_length or not all(color in colors for color in answer):
            print("\033[31;1m You've done something wrong! \033[32;1m Check your guesses and try again!")
            continue

        correct_position = sum(a == c for a, c in zip(answer, code))
        correct_color = sum(min(answer.count(c), code.count(c)) for c in set(code))
        correct_color -= correct_position

        print(f"\033[32;1m{correct_position} \033[37;1m colors in the correct place!")
        print(f"\033[32;1m{correct_color} \033[37;1m correct colors but in the wrong place!\n")

        if correct_position == code_length:
            blink_text("\033[1;32:40m Congratulations!\n")
            blink_text("\033[31;1m You have a Boss Brain!!!\n")
            blink_text(f"\033[33;1m You cracked the secret code: {code}\n")  
            print("\n" * 3)          
            print("\033[0;96m  Choose \033[37;1m '1' \033[0;96m to play again")
            print("  Choose \033[37;1m '2' \033[0;96m to return to main page")
            print("  Choose \033[37;1m '3' \033[0;96m to Exit\n")
            while True:
                try:
                    menu_choice = int(input("\033[37;1m Enter choice: \n"))
                    if menu_choice == 1:
                        choose_level()
                        break
                    elif menu_choice == 2:
                        main_page()
                        break
                    elif menu_choice == 3:
                        print(f"Exiting game....Game ended")
                        break
                    else:
                        raise ValueError

                except ValueError:
                    print(" Invalid key press. Please choose 1, 2 or 3")
                    break

            exit()

        attempts += 1

    print("\033[31;1m You ran out of attempts!\n")
    print(f"\033[33;1m The correct code is: {code}\n")
    print("Choose '1' to play again")
    print("choose '2' to return to main page")

    while True:
        try:
            menu_choice = int(input(" Press choice: \n"))
            if menu_choice == 1:
                choose_level()
                break
            elif menu_choice == 2:
                main_page()
                break            
            else:
                raise ValueError

        except ValueError:
            print(" Invalid key press. Please choose 1, or 2")

def play_game_level2():
    """
    Play game function
    """
    clear_screen()
    print(" \033[4;96m WELCOME TO THE BOSS BRAIN CHALLENGE - Level 2 \033[0;96m\n")
    print(" \033[0;37m Crack the color code to become a Boss Brain!\n")   
    print("  Choose from the following colors: \033[31;1m Red(R) \033[34;1m Blue(B) \033[32;1m Green(G) \033[33;1m Yellow(Y) \033[37;1m White(W) \033[1;35:47m Pink(P) \n")
    print(f" \033[0;37m Code Length: \033[33;1m{code_length}, \033[37;0m Max Attempts: \033[33;1m {max_attempts_level2}\n")

# while loop to itereate over game until max attempts made
    attempts = 0
    code = generate_random_code()
    print(code)
    while attempts < max_attempts_level2:
        answer = input(f"\033[0;37m Attempt {attempts + 1}/{max_attempts_level1}. Enter your guess(first letter of colours): \n").upper().strip().split()
        if len(answer) != code_length or not all(color in colors for color in answer):
            print("\033[31;1m You've done something wrong! \033[32;1m Check your guesses and try again!")
            continue

        correct_position = sum(a == c for a, c in zip(answer, code))
        correct_color = sum(min(answer.count(c), code.count(c)) for c in set(code))
        correct_color -= correct_position

        print(f"\033[32;1m{correct_position} \033[37;1m colors in the correct place!")
        print(f"\033[32;1m{correct_color} \033[37;1m correct colors but in the wrong place!\n")

        if correct_position == code_length:
            blink_text("\033[1;32:40m Congratulations!\n")
            blink_text("\033[31;1m You have a Boss Brain!!!\n")
            blink_text(f"\033[33;1m You cracked the secret code: {code}\n")
            print("\n" * 3)
            print("\033[0;96m  Choose \033[37;1m '1' \033[0;96m to play again")
            print("  Choose \033[37;1m '2' \033[0;96m to return to main page")
            print("  Choose \033[37;1m '3' \033[0;96m to Exit\n")

            while True:
                try:
                    menu_choice = int(input("\033[37;1m Enter choice: \n"))
                    if menu_choice == 1:
                        choose_level()
                        break
                    elif menu_choice == 2:
                        main_page()
                        break
                    elif menu_choice == 3:
                        print(f"Exiting game....Game ended")
                        break
                    else:
                        raise ValueError

                except ValueError:
                    print(" Invalid key press. Please choose 1, 2 or 3")
                    break

            exit()

        attempts += 1

    print("You ran out of attempts!\n")
    print(f"\033[33;1m The correct code is: {code}\n")
    print("Choose '1' to play again")
    print("choose '2' to return to main page")

    while True:
        try:
            menu_choice = int(input(" Press choice: \n"))
            if menu_choice == 1:
                choose_level()
                break
            elif menu_choice == 2:
                main_page()
                break            
            else:
                raise ValueError

        except ValueError:
            print(" Invalid key press. Please choose 1, or 2")

def play_game_level3():
    """
    Play game function
    """
    clear_screen()
    print(" \033[4;96m WELCOME TO THE BOSS BRAIN CHALLENGE1 - Level 3 \033[0;96m\n")
    print(" \033[0;37m Crack the color code to become a Boss Brain!\n")   
    print("  Choose from the following colors: \033[31;1m Red(R) \033[34;1m Blue(B) \033[32;1m Green(G) \033[33;1m Yellow(Y) \033[37;1m White(W) \033[1;35:47m Pink(P) \n")
    print(f" \033[0;37m Code Length: \033[33;1m{code_length}, \033[0;37m Max Attempts: \033[33;1m {max_attempts_level3}\n")

# while loop to itereate over game until max attempts made
    attempts = 0
    code = generate_random_code()
    print(code)
    while attempts < max_attempts_level3:
        answer = input(f"\033[0;37m Attempt {attempts + 1}/{max_attempts_level1}. Enter your guess(first letter of colours): \n").upper().strip().split()
        if len(answer) != code_length or not all(color in colors for color in answer):
            print("\033[31;1m You've done something wrong! \033[32;1m Check your guesses and try again!")
            continue

        correct_position = sum(a == c for a, c in zip(answer, code))
        correct_color = sum(min(answer.count(c), code.count(c)) for c in set(code))
        correct_color -= correct_position

        print(f"\033[32;1m{correct_position} \033[0;37m colors in the correct place!")
        print(f"\033[32;1m{correct_color} \033[0;37m correct colors but in the wrong place!\n")

        if correct_position == code_length:
            blink_text("\033[1;32:40m Congratulations!\n")
            blink_text("\033[31;1m You have a Boss Brain!!!\n")
            blink_text(f"\033[33;1m You cracked the secret code: {code}\n")
            print("\n" * 3)
            print("\033[0;96m  Choose \033[37;1m '1' \033[0;96m to play again")
            print("  Choose \033[37;1m '2' \033[0;96m to return to main page")
            print("  Choose \033[37;1m '3' \033[0;96m to Exit\n")

            while True:
                try:
                    menu_choice = int(input("\033[37;1m Enter choice: \n"))
                    if menu_choice == 1:
                        choose_level()
                        break
                    elif menu_choice == 2:
                        main_page()
                        break
                    elif menu_choice == 3:
                        print(f"Exiting game....Game ended")
                        break
                    else:
                        raise ValueError

                except ValueError:
                    print(" Invalid key press. Please choose 1, 2 or 3")
                    break

            exit()

        attempts += 1

    print("You ran out of attempts!\n")
    print(f"\033[33;1m The correct code is: {code}\n")
    print("\n" * 3)
    print("Choose '1' to play again")
    print("choose '2' to return to main page")

    while True:
        try:
            menu_choice = int(input(" Press choice: \n"))
            if menu_choice == 1:
                choose_level()
                break
            elif menu_choice == 2:
                main_page()
                break            
            else:
                raise ValueError

        except ValueError:
            print(" Invalid key press. Please choose 1, or 2")
# clear screen function

def clear_screen():
    """
    Clears the terminal screen/window
    """
    print("\n" * 50)
    print("\033c")

def blink_text(text):
    while True:
        sys.stdout.write('\033[5m' + text + '\033[0m')
        sys.stdout.flush()
        time.sleep(0.5)
        sys.stdout.write('\r' + ' ' * len(text) + '\r')
        sys.stdout.flush()
        time.sleep(0.5)
        
        break

main_page()


