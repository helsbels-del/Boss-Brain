# import random library
import random
import os
import sys
import time


# Constant variables - colors available to choose from, code length and how many attempts
colors = ["Red", "Blue", "Green", "Yellow", "Black", "Orange"]
code_length = 4
max_attempts_level1 = 8
max_attempts_level2 = 10
max_attempts_level3 = 12

#Title page
def main_page():
    """
    Main page with player options
    """
    clear_screen()
    print("This is the Boss Brain Challenge!\n")
    print("Can you decipher the secrect code?\n")    
    print("Choose '1' to Play")
    print("Choose '2' for Instructions")
    print("Choose '3' to Exit\n")

    while True:
        try:
            menu_choice = int(input(" Press choice: \n"))
            if menu_choice == 1:
                play_game()
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
                
    print("\033[37;1m INSTRUCTIONS FOR PLAY\n")
    print(" The codemaker (computer) creates a secret 4 colour code, choosing from 6 available colours.\n")
    print(" The codebreaker (player) needs to guess the secret code in a given number of attempts.\n")
    print(" The number of attempts will depend on which level is choosen.\n")
    print(" After each attempt, feedback is given as to how many colours are correct and how many are in the correct position.\n")
    print(" If the player guesses the secret code before running out of attempts, this is the end of the game.")
    print(" The player then has the choice to play again or return to the main page.\n")
    print(" If the player runs out of attemts before guessing the correct secret code, this is the end of the game.")
    print(" The player then has the choice to play again or return to the main page.\n")
    print(" Your choice of colors is: \033[31;1m Red \033[34;1m Blue \033[32;1m Green \033[33;1m Yellow \033[37;1m White \033[1;35:47m Pink \n" )
    print("\033[37;1m Find the code in 12, 10 or 8 attempts, depending on level, to become a Boss Brain!\n") 
    print(" Choose 4 colors, leaving a space between each color.\n")
    print("Choose '1' to play")
    print("choose '2' to return to main page")

    while True:
        try:
            menu_choice = int(input(" Press choice: \n"))
            if menu_choice == 1:
                play_game()
                break
            elif menu_choice == 2:
                main_page()
                break            
            else:
                raise ValueError

        except ValueError:
            print(" Invalid key press. Please choose 1, or 2")


# generate random code
def generate_random_code():
    """
    Genertes a 4-color random code from the 6 x color choices in the COLORS
    """
    code = random.choices(colors, k=code_length)
    
    return(code)

# main game play
def play_game():
    """
    Play game function
    """
    clear_screen()
    print("Welcome to the Boss Brain challenge.\n")
    print("Decipher the color code to become a Boss Brain!\n")
    print("What's your Level?\n")
    print ("Level 1 will give you 12 attempts")
    print ("Level 2 will give you 10 attempts")
    print ("Level 3 will give you 8 attempts\n")
    print ("Please choose your level: ")
    print(f"Choose from the following colors: {', '.join(colors)}\n")
    print(f"Code Length: {code_length}, Max Attempts: {max_attempts_level2}\n")

# while loop to itereate over game until max attempts made
    attempts = 0
    code = generate_random_code()
    print(code)
    while attempts < max_attempts_level2:
        answer = input(f"Attempt {attempts + 1}/{max_attempts_level2}. Enter your answer: ").strip().split()
        if len(answer) != code_length or not all(color in colors for color in answer):
            print("Incorrect Answer! Try again!")
            continue

        correct_position = sum(a == c for a, c in zip(answer, code))
        correct_color = sum(min(answer.count(c), code.count(c)) for c in set(code))
        correct_color -= correct_position

        print(f"{correct_position} colors in the correct place!")
        print(f"{correct_color} correct colors but in the wrong place!")

        if correct_position == code_length:
            blink_text("\033[1;32:40m Congratulations! You cracked the code.")
            print("\033[1;31:40m You have a Boss Brain!!!!")
            print(f"The correct code is: {generate_random_code(code)}")
            exit()

        attempts += 1

    print("You ran out of attempts!")
# clear screen function
def clear_screen():
    """
    Clears the terminal screen/window
    """
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")

def blink_text(text):
    while True:
        sys.stdout.write('\033[5m' + text + '\033[0m')
        sys.stdout.flush()
        time.sleep(0.5)
        sys.stdout.write('\r' + ' ' * len(text) + '\r')
        sys.stdout.flush()
        time.sleep(0.5)

main_page()


