# import random library
import random
import os
import sys
import time


# Constant variables - colors available to choose from, code length and how many attempts
colors = ["R", "B", "G", "Y", "W", "P"]
code_length = 4

#Title page
def main_page():
    """
    Main page with player options
    """
    clear_screen()
    print("\033[1;96m THIS IS THE BOSS BRAIN CHALLENGE!\n")
    print("\033[37;1m Can you crack the secrect code?\n")
    print("\x1B[3m With a code length of 4 and 6 available colours...")
    print(" ...there are only 1,296 different combinations!\x1B[0m\n")
    print("\033[1;92m **** Good luck CodeBreaker ****")
    print(" Tough situations build strong people! \n")
    print("\033[0;33m  Choose \033[37;1m '1' \033[0;33m to Play")
    print("  Choose \033[37;1m '2' \033[0;33m for Instructions")
    print("  Choose \033[37;1m '3' \033[0;33m for the Bonus Challenge\n")
    print(" Choose \033[37;1m '0' \033[0;33m to Exit\n")

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
                play_bonus_game('self')
                break
            elif menu_choice == 0:
                print(f"Exiting game....Game ended")
                break
            else:
                raise ValueError

        except ValueError:
            print(" Invalid key press. Please choose 1, 2, 3 or 0")
# Instructions of play
def instructions():
    """
    Instructions for the user of how to play the game
    """
    clear_screen()
    print("\033[1;96mINSTRUCTIONS FOR PLAY \033\n")
    print(" Main Game\n")
    print(" \033[37;1mThe CodeMaker (computer) creates a secret 4 colour code,")
    print(" choosing from 6 available colours.\n")
    print(" The CodeBreaker (player) needs to crack the secret code,")
    print(" in a given number of attempts.\n")
    print(" The number of attempts will depend on which level is choosen.\n")
    print(" After each attempt, feedback is given as to how many colours are correct,")
    print(" and how many colours are in the correct position.\n")
    print(" If the player cracks the secret code before running out of attempts,")
    print (" this is the end of the game.")
    print(" The player then has the choice to play again or return to the main page.\n")
    print(" If the player runs out of attempts before cracking the correct secret code,")
    print(" this is the end of the game.") 
    print(" The player then has the choice to play again, or return to the main page.\n")
    print(" If the player enters an incorrect letter or anything other than a letter,")
    print(" or if they don't leave a space between each letter,") 
    print(" a message will appear to tell the player,")
    print(" that they have entered something incorrectly and to check their guess.") 
    print(" This does not count as an attempt,")
    print(" and the player will have the same remaining number of attempts,")
    print(" as before they made the incorrect guess.\n")
    print(" The choice of colors is:")
    print(" \033[31;1m Red(R) \033[34;1m Blue(B) \033[32;1m Green(G) \033[33;1m Yellow(Y) \033[37;1m White(W) \033[1;35m Pink(P) \n")
    print("\033[37;1m Choose 4 colors by entering the first letter of your choosen colours.")
    print(" You can use lower or upper case letters, leaving a space between each letter.\n")
    print(" The secret code can contain multiples of the same colour.\n")
    print("\033[37;1m Find the code in 12, 10 or 8 attempts, to become a Boss Brain!\n")
    print("\033[0;96m Bonus Challenge Game \033[0;96m\n")
    print(" \033[37;1mThe computer generates a code word from a bank of code words in its memory.\n")
    print(" The player must guess each letter at a time to crack the code word.\n")
    print(" The player is told how many letters are in the word,")
    print(" and the amount of attempts they have.\n")
    print(" If the player cracks the code word before runnning out of attempts,")
    print(" this is the end of the game.")
    print(" The player then has the choice to play again or return to the main page.\n")
    print(" If the player runs out of attempts before cracking the code word,")
    print(" This is the end of the game.")
    print(" The player then has the choice to play again, or return to the main page.\n")
    print(" If the player enters an incorrect letter or anything other than a letter,")
    print(" a message will appear to tell the player,")
    print(" that they have entered something incorrectly and to check their guess.")
    print(" This does not count as an attempt,")
    print(" and the player will have the same remaining number of attempts,")
    print(" as before they made the incorrect guess.\n")
    print(" If the player enters a letter that they have already entered,")
    print(" and it is not in the code word multiple times,")
    print(" a message will appear to tell the player,")
    print(" that they have already entered this letter and to try again.")
    print(" This does not count as an attempt,")
    print(" and the player will have the same remaining number of attempts")
    print(" as before they made the incorrect guess.\n")
    print(" The player starts by entering a letter of choice,")
    print(" this can be lower or upper case.\n")
    print(" The computer then gives feedback,")
    print(" to tell the player if the letter is in the code word or not in the code word.\n")
    print(" The player repeats entering a letter until they guess the code word,")
    print(" or they run out of attempts, which ever happens first.")
    print("\n" * 2)
    print("\033[1;92m **** Good luck CodeBreaker ****")
    print(" Just because it's hard, it doesn't make it impossible! \n")
    print("\n" * 3)
    print("\033[33;1m Choose \033[37;1m '1' \033[33;1m to play")
    print("\033[33;1m Choose \033[37;1m '2' \033[33;1m to play bonus challenge")
    print(" Choose \033[37;1m '3' \033[33;1m to return to main page")
    while True:
        try:
            menu_choice = int(input("\033[37;1m Enter choice: \n"))
            if menu_choice == 1:
                choose_level()
                break
            elif menu_choice == 2:
                play_bonus_game('self')
                break
            elif menu_choice == 3:
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

# choose level


def choose_level():
    """
    Choose level function
    """
    clear_screen()
    print("  \033[1;96m CHOOSE YOUR LEVEL \033\n")
    print("\033[37;1m  Level 1 will give you 12 attempts")
    print("  Level 2 will give you 10 attempts")
    print("  Level 3 will give you 8 attempts\n")
    print("\033[1;92m **** Good luck CodeBreaker ****")
    print(" Always believe the impossible is possible! \n")
    print("\033[0;33m (Choose \033[0;37m '4' \033[0;33m to return to main page)")
    while True:
        try:
            menu_choice = int(input("\033[37;1m Choose level (Enter '1', '2', or '3'): \n"))

            if menu_choice == 1:
                play_game(12, 1)
                break
            elif menu_choice == 2:
                play_game(10, 2)
                break
            elif menu_choice == 3:
                play_game(8, 3)
                break
            elif menu_choice == 4:
                main_page()
                break
            else:
                raise ValueError

        except ValueError:
            print(" Invalid key press. Please choose 1, 2, 3 or 4")

# main game play
def play_game(max_attempts, level):
    """
    Play game function
    """
    clear_screen()
    print(f" \033[1;96m WELCOME TO THE BOSS BRAIN CHALLENGE - Level {level}\n")
    print(" \033[37;1m  Crack the color code to become a Boss Brain!\n")
    print("   Choice of colours: \033[31;1m Red(R) \033[34;1m Blue(B) \033[32;1m Green(G) \033[33;1m Yellow(Y) \033[37;1m White(W) \033[35;1m Pink(P) \n")
    print(f" \033[37;1m  Code Length: \033[33;1m{code_length} \033[37;1m  Max Attempts: \033[33;1m {max_attempts}\n")
# while loop to itereate over game until max attempts made
    attempts = 0
    code = generate_random_code()
    #print(', '.join(code))
    while attempts < max_attempts:
        answer = input(f"\033[1;32m Attempt {attempts + 1}/{max_attempts}. Enter your guess(Leave a space between each letter guessed):\033[0;37m \n").upper().strip().split()
        if len(answer) != code_length or not all(color in colors for color in answer):
            print("\033[31;1m You've done something wrong! \033[33;1m Check your guesses and try again!")
            continue

        correct_position = sum(a == c for a, c in zip(answer, code))
        correct_color = sum(min(answer.count(c), code.count(c)) for c in set(code))
        correct_color -= correct_position

        print(f"\033[33;1m{correct_position} \033[37;1m color(s) in the correct place!")
        print(f"\033[33;1m{correct_color} \033[37;1m correct color(s) but in the wrong place!\n")

        if correct_position == code_length:
            blink_text("\033[1;32:40m Congratulations!\n")
            blink_text("\033[31;1m You have a Boss Brain!!!\n")
            blink_text(f"\033[33;1m You cracked the secret code: {', '.join(code)}\n")
            print("\n" * 3)
            print("\033[0;96m  Choose \033[37;1m '1' \033[0;96m to play again")
            print("  Choose \033[37;1m '2' \033[0;96m to return to main page")
            while True:
                try:
                    menu_choice = int(input("\033[37;1m Enter choice: \n"))
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
 
                    exit()

        attempts += 1

    print("\033[31;1m You ran out of attempts!\n")
    print(f"\033[33;1m The correct code is: {', '.join(code)}\n")
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

# Bonus game
# Generate code word
code_words = ["Obfuscation", "Coding", "Challenge", "Master", "Eagle", "Phoenix", "Banana", "Galaxy", "Pirate", "Alpha"]
def generate_code_word():
    """
    Generates a random word from a given list
    """
    code_word = random.choice(code_words).lower()

    return(code_word)

# Check letters guessed in words

def letters_in_word(code_word, attempts):
    letters_in_word = ""
    for letter in code_word:
        if letter in attempts:
            letters_in_word += letter
        else:
            letters_in_word += "*"
    return letters_in_word

# Play Code Word Bonus Game

def play_bonus_game(code_word):
    """
    Play game function
    """
    clear_screen()
    print(" \033[1;96m THIS IS THE BOSS BRAIN BONUS CHALLENGE!\n")
    print(" \033[37;1m Are you Boss Brain enough for the bonus challenge?\n")
    print("  Can you guess the code word before running out of attempts?")
    print("  This time I can give you a hint!\n")
# while loop to iterate over game until max attempts made

    code_word = generate_code_word()
    #print(code_word)
    lettersguessed = []
    attempts = int(len(code_word) * 2)
    print("  \033[31;1m**** The code word has " + str(len(code_word)) + " letters.**** ")

    while True:
        if attempts != 0:
            print("\n\033[37;1mYou have " + str(attempts) + " attempts remaining.\n")
            print("\033[1;33mCurrent word guess: " + letters_in_word(code_word, lettersguessed))
            print("\n")
            print("\033[1;32mLetters guessed so far: " + str(', '.join(lettersguessed)))
            print("\n")
            attempt = (input("\033[37;1mEnter your letter of choice:\033[1;32m ")).lower()
            if not attempt.isalpha():
                print("You entered an incorrect character! Check your guess and try again.\n")
                continue

            if attempt in lettersguessed:
                print("You have aready entered this letter. Try again.\n")
                continue

            if attempt not in lettersguessed:
                lettersguessed.append(attempt)

            if letters_in_word(code_word, lettersguessed) == code_word:
                print("\n" * 3)
                print("\033[31;1mAmazing! You cracked the code word!\033[0m \033[0;33m " + code_word)
                print("\n" * 3)
                print("\033[0;96m  Choose \033[37;1m '1' \033[0;96m to play bonus challenge again")
                print("  Choose \033[37;1m '2' \033[0;96m to return to main page")
 
                while True:
                    try:
                        menu_choice = int(input("\033[37;1m Enter choice: \n"))
                        if menu_choice == 1:
                            play_bonus_game(code_word)
                            break
                        elif menu_choice == 2:
                            main_page()
                            break
                        else:
                            raise ValueError

                    except ValueError:
                        print(" Invalid key press. Please choose 1, or 2")
                        exit()
            else:
                attempts -= 1
                if attempt in code_word:
                    print("Letter Correct!")
                else:
                    print(attempt + "\033[0m \033[0;37m is not in the code word.")
        else:
            print("\033[31;1mUh oh, you ran out of attempts.\033[33;1m The code word is " + code_word)
            print("\n\033[96;1mChoose\033[37;1m '1'\033[0;96m to play again")
            print("choose \033[37;1m'2'\033[0;96m to return to main page")

            while True:
                try:
                    menu_choice = int(input(" Press choice: \n"))
                    if menu_choice == 1:
                        play_bonus_game(code_word)
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
