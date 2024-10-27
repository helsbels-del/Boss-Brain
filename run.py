# import random library
import random
import os
import sys
import time


# Constant variables - colors available to choose from, code length and how many attempts
colors = ["Red", "Blue", "Green", "Yellow", "Black", "Orange"]
code_length = 4
max_attempts = 10

#Title page
def main_page():
    """
    Main page with player options
    """
    clear_screen()
    print("This is the Boss Brain Challenge!\n")
    print("Can you decipher the secrect code?\n")
    print("What's your Level?\n")
    print ("Level 1 will give you 12 attempts")
    print ("Level 2 will give you 10 attempts")
    print ("Level 3 will give you 8 attempts\n")
    print("Choose '1' to Play")
    print("Choose '2' for Instructions")
    print("Choose '3' to Exit")

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
                
    print("\033[37;1m INSTRUCTIONS FOR PLAY")
    print("\033[37;1m The Boss Brain Challenge will create a 4 color code for you to decipher.\n")
    print("Your choice of colors is: \033[31;1m Red \033[34;1m Blue \033[32;1m Green \033[33;1m Yellow \033[37;1m White \033[1;35:47m Pink \n" )
    print("\033[37;1m Find the code in 8 or less attempts to become a Boss Brain!\n") 
    print("Choose 4 colors, leaving a space between each color")


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
    print(f"Choose from the following colors: {', '.join(colors)}\n")
    print(f"Code Length: {code_length}, Max Attempts: {max_attempts}\n")

# while loop to itereate over game until max attempts made
    attempts = 0
    code = generate_random_code()
    print(code)
    while attempts < max_attempts:
        answer = input(f"Attempt {attempts + 1}/{max_attempts}. Enter your answer: ").strip().split()
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


