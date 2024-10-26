# import random library
import random
import os
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
                
    print(f"The Boss Brain Challenge will create a 4 color code for you to decipher.\n")
    print(f"The choice of colors is Red, Blue, Green, Yellow, Black and Orange") 
    print(f"Find the code in 8 or less attempts to become a Boss Brain!") 


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
    print("Welcome to the Boss Brain challenge")
    print("Decipher the color code to become a Boss Brain!")
    print(f"Choose from the following colors: {', '.join(colors)}")
    print(f"Code Length: {code_length}, Max Attempts: {max_attempts}")

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
            print("Congratulations! You cracked the code. You have a Boss Brain!")
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
main_page()


