# **Boss Brain Challenge**

## **Introduction**

I have created a terminal-based code breaker game called Boss Brain Challenge, based on the original MasterMind board game that I loved playing in my younger years with my family and friends.
It has the same rules as the Mastermind game. The PC takes the place of the codemaker and teh player is the codebreaker. The codemaker generates a secret code of 4 colours, there are 6 colours to choose from. Then the codebreaker has to guess the secret code in a number of attempts. The number of attempts depends on the level selected. Level 1 is 12 attempts, level 2 is 10 attempts and level 3 is 8 attempts.

## **Target Audience**

The original Mastermind game is suitable for ages 8+. This version of the game would be suitable for 8+ also though the younger ages may require adult supervision. It is a great family game, as a board game, though this is more a one person game playing against the PC, though you could play alternate games against the PC as a family and keep score as you would in the original board games, where the winner is the person who guesses the secret code in the least attempts.

## **User Requirements**

- The player wants to engage in a challenging game to solve a secret code to become a Boss Brain.
- The player wants the choice to read the instructions prior to playing the game.
- The player wants to access the game from the main menu and choose which level they would like to play.
- When playing the game, the player wants to have feedback to which of their colors are correct and how many are in the correct place.
- The player needs to know how many attempts they have left as they are playing.
- The player wants to know if they have been successful in guessing the correct code in the given amount of attempts.
- If the player does not guess the correct code in the given amount of attempts, then they want to know what the secret code is.
- The player will wont to exit the game after it has finished.

## **Flow Chart**

## **Technology**

I used Python (version 3.12.2 latest version at time of produce)

I also imported the below libraries

Random

OS

## **Current Features**

### **Main Page**

The first page that the player sees when the program is started tells the player that this is the Boss Brain Challenge and lists a choice of 3 options.

add screen shot

The player can choose to play the game, go to the instructions or exit the game.
If the player chooses option 1 to play the game, they are then asked which level they would like to play. 

## **Instructions Page**

After selecting option 2 from the main page, the player can read the Instruction For Play. At the bottom of the page the player has options to either 'Play' or 'Return to main Page'. 

add screenshot

## **Exit Game**

On selecting option 3 from the main page, the below message is shown and the program is ended.

add screenshot

## **Play Game**

Option 1 from the main page or the instructions page takes the player to choose of levels. There are 3 levels to choose from. There are 3 different levels. Each level has a different amount of attempts at guessing the secret code. 

add screenshot

### **Level options**

Add screeshot


## **The secret Code generation**

To generate the secret code, I have imported the random library. I have created constants for the generation of this code. The COLORS list and also the CODE_LENGTH.

add screenshot





## **Input Error Handling**

## **How guess is compared to code**

## **Credits**

I used this website for the blink_text function code.

https://handhikayp.medium.com/generate-a-blinking-text-with-very-simple-python-4c10750978f5#:~:text=The%20blink_text%20function%20continuously%20prints,state%2C%20creating%20the%20blink%20effect

## **Bugs Fixed**

When I first added the blink_text function to get the Congratulations! message to flash, it was flashing continuously though this seemed to stop the rest of the code from runnint. It was stuck in an infinate while loop. I then put a break in the while loop. This made the Congratulations! message flash up, however then it dissappeared and then the next line was printed. If I put the print text function ton the 3 messages that come up after the game has been won, they flash up one by one. I like this affect though this wasn't what I wanted initially. I was hoping for the congratulations message to be flashing continously with the to messages below printed. 


When I was trying to add the secret code at the end of the game to confirm the code if you win or let you know the code if you loose, I couldn't get this to work but then realised I was using {generat_random_code_} instead of {code}.

I wanted the names of the colours written on the game play screens to be coloured. As they were being picked up from the color constant list, I couldn't see how to change the colour of the text. I tried by adding the ANSI codes to the color list items, however this did not work. I then decided to use the same coding that I had used to change the color of the text for the colours on the instructions part. This has worked well.

## **Improvements as going along**

Initially the player had to write the name of each of the colours out. I was was testing out my coding I was finding this very time consuming and heavy on the finger usage. I decided to use the first letters of each of the colours instead which made it much simpler and enjoyable. I also added the .upper so that the player can inut lowercase or uppercase letters and either will be excepted.

One of the messages that comes up at the end of the game is 'You have a Boss Brain!'. This message is slightly different in each of the levels. In level 1 there is 1 exclamation mark to end the message. In level 2, there are 2 exclamation marks and in level 3 there are 3 exclamation marks. This marks a greater level of achievement for the hogher levels.


