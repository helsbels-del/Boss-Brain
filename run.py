# import random library
import random
#define colors available to choose from, code length and how many attempts
colors = ["Red", "Blue", "Green", "Yellow", "Black", "Orange"]
code_length = 4
max_attempts = 10
#generate randon code
code = random.choices(colors, k=code_length)
attempts = 0

print("Welcome to the Boss Brain challenge")
print(f"Choose from the following colors: {', '.join(colors)}")
print(f"Code Length: {code_length}, Max Attempts: {max_attempts}")


