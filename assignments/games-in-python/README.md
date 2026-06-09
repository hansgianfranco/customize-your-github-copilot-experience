 # 📘 Assignment: Hangman Game Challenge

 ## 🎯 Objective

 Build a command-line Hangman game in Python that leAts a player guess letters to reveal a hidden word, practicing string manipulation, loops, conditionals, and user input.

 ## 📝 Tasks

 ### 🛠️ Implement Hangman

 #### Description
 Create a command-line Hangman game that:

 - Chooses a secret word at random from a predefined list.
 - Prompts the player to guess single letters until they either guess the word or run out of attempts.
 - Displays the current word progress (e.g., _ a _ g _ a _).
 - Shows letters already guessed and the remaining attempts.

 #### Requirements
 Completed program should:

 - Randomly select a secret word from a list.
 - Display the masked word using underscores for unknown letters.
 - Accept single-letter guesses (case-insensitive) and ignore repeated guesses without penalizing.
 - Reduce remaining attempts only on incorrect, new guesses.
 - Show guessed letters and remaining attempts after each guess.
 - End with a clear win or lose message and reveal the secret word on loss.
 - Include a configurable maximum number of attempts (e.g., 6).

 Example I/O:

 ```text
 Secret: _ a _ g _ a _
 Guess: n
 Result: _ a n g _ a _
 Remaining attempts: 5
 ```
