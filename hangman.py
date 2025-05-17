import random

def hangman():
    words = ['fruits', 'python', 'football', 'computer', 'keyboard', 'developing']

    secret_word = random.choice(words)
    guessed_letters = []
    attempts_play = 6

    print("Welcome to Hangman game!")
    print("Guess the word. You have only 6 attempts to save the hangman.")

    while attempts_play > 0:
        display_word = ""
        for letters in secret_word:
            if letters in guessed_letters:
                display_word += letters
            else:
                display_word += "_"
        print(display_word)

        if "_" not in display_word:
            print(f"Congratulations! You've guessed the word: {secret_word}")
            break

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in secret_word:
            attempts_play -= 1
            print(f"Wrong guess! You have {attempts_play} attempts left.")
            print_hangman(attempts_play)

    if attempts_play == 0:
        print(f"Game over! The word was: {secret_word}")
        print_hangman(0)

def print_hangman(attempts_left):
    stages = [
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        """,
        """
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        """
    ]
    print(stages[attempts_left])

if __name__ == "__main__":
    hangman()