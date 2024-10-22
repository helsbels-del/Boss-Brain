# import random library
import random
# define colors available to choose from, code length and how many attempts
colors = ["Red", "Blue", "Green", "Yellow", "Black", "Orange"]
code_length = 4
max_attempts = 10

# generate random code
code = random.choices(colors, k=code_length)
attempts = 0
print(code)
print("Welcome to the Boss Brain challenge")
print("Decipher the color code to become a Boss Brain!")
print(f"Choose from the following colors: {', '.join(colors)}")
print(f"Code Length: {code_length}, Max Attempts: {max_attempts}")

# while loop to itereate over game until max attempts made
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




