# **Testing**

I found it inportant to be constantly testing my code as I progressd further through my project.
It was important to make sure that all the input options worked correctly and that only the correct data could be entered by the player and that the correct messages where received depending on what had been inputed.

Using a print statement to print out the secret code in the main game and the code word in the bonus game was essential as part of the testing so that I could check all the different combinations by deliberatley getting the colurs in the incorrect places as well as the correct places to make sure that the feedback was correct every time.
See below examples of different outcomes and messages.

Ths shows main game level 1, game won in 5 attempts.

![Main Game Level 1](docs/images/main_game_example.png)

This shows main game level 2 to include a guess with no spaces to show the 'you've done something wrong message!' appears.

![Main Game Level 2](docs/images/main_game_example_two.png)

This shows main game level 3 to include a guess with numbers to show the 'you've done something wrong message!' appears.

![Main Game Level 3](docs/images/main_game_example_three.png)

This shows main game level 1, winning in 3 attempts and shows that the feedback is correct.

![Main Game Level 1b](docs/images/main_game_example_four.png)

This shows main game level 2 with some different combinations of incorrect answers before the game is won in 6 attempts.

![Main Game Level 2b](docs/images/main_game_example_five.png)

This shows main game level 3 with some different combinations of incorrect answers before the game is won in 4 attempts.

![Main Game Level 3b](docs/images/main_game_example_six.png)

This shows the message after an incorrect guess has been made, and asks the player to try again. You can see that the attempt number stays the same.

![Attempt after incorrect entry](docs/images/attempt_after_incorrect_entry.png)

Here you can see that if you enter a number and as well only 1 character the message 'you've done something wrong message!' appears.

![Attempt Number Error](docs/images/attempt_number_error.png)

This shows the first attempt of the guess works.

![First Guess Result](docs/images/firstguess_result.png)

This shows an incorrect guess with no spaces and that the number of attempts is still the same after this incorrect guess.

![Incorrect Guess With No Spaces](docs/images/incorrect_guess_main.png)

This shows that you can use upper case letters also and the answer will still be accepted.

![Upper Case Answer](docs/images/uppercase_answer.png)

This shows the winning message on the main game.

![Winning Message](docs/images/winnng_page_main.png)

This shows that in the bonus game, if you try to enter the same letter twice, you get the error message.

![Bonus error message](docs/images/bonus_attempt_later.png)

This shows the bonus level first guess is working.

![Bonus game fisrt guess](docs/images/bonus_attempt_one.png)

This shows that if you try to enter a number in the bonus game, you will get the error message.

![Bonus game number error](docs/images/bonus_incorrect_char.png)

This shows winning the bonus games.

![Bonus Game Win](docs/images/bonus_win_example.png)


## **Validation Testing with CI Python Linter**

Once my code was completed and I was happy that I had solved all the bugs that I had encountered and deemed there to be no more bugs in my program at this time, I ran my code thorugh the CI Pythn linter for validation. It did at first contain white space and trailing white space along with messagesa bout some lines being too long. Once the program had been deployed, I then went through the code and made sure that each of the sentences fitted on the screen. There are still some long sentences that show up as error codes in the linter however these are comments or sentences that include the ANSI colour codes for the text.

![CI Python Linter](docs/images/CI_Python_Linter.png)


## **Testing in the field**

Once I had deployed my game I sent it out to friends and family for some player feedback.
I have written about the feedback I was given in the README file. This feedback was very valuble to me and helped me to add some clearer instructions on how to play the game and make sure it was both simple and enjoyable to play. Some other feedback I had was that the game was quite addictive and the players liked the challenge of playing again to try and guess the code in fewer attempts.
Not many people tried the bonus game.

Follow this link to return to the [**README.md**](README.md)