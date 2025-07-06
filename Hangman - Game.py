import random

# Word bank with 2 levels (each level has specific category)
levels = {
    1: ["cat", "dog", "lion", "tiger", "elephant"],        # Animals
    2: ["eagle", "peacock", "dove", "bat", "owl"]    # Birds
   
}

# Level categories for display
level_categories = {
    1: "Animals ",
    2: "Birds "
}


# Hangman stages
hangman = [
    """
     +---+
     |   |
     |
     |
     |
     |
         
    =========""",
    """
     +---+
     |   |
     |   O
     |
     |
     |
    =========""",
    """
     +---+
     |   |
     |   O
     |   |
     |
     |
    =========""",
    """
     +---+
     |   |
     |   O
     |   |\\
     |
     |
    =========""",
    """
     +---+
     |   |
     |   O
     |  /|\\
     |
     |

    =========""",
    """
     +---+
     |   |
     |   O
     |  /|\\
     |    \\
     |
    =========""",
    """
     +---+
     |   |
     |   O
     |  /|\\
     |  / \\
     |
    ========="""
]
# Play one round (one word)
def play_level(level, word):
    guessed = []
    wrong = 0
    limit = 6
    category = level_categories[level]

    print(f"\nLevel {level} Guess the word ({category})")
    print("_ " * len(word))

    while wrong < limit:
        print(hangman[wrong])
        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print(" Enter a single alphabet.")
            continue

        if guess in guessed:
            print("Already guessed.")
            continue

        guessed.append(guess)

        if guess not in word:
            wrong += 1
            print(f" Wrong! Tries left: {limit - wrong}")

        display = [letter if letter in guessed else "_" for letter in word]
        print( " ".join(display))

        if "_" not in display:
            print(hangman[wrong])
            print(f"\nLevel {level} Complete! Word: {word}")
            print(" *BOOM* ")
            return True  # Win

    # Lose
    
    print(hangman[wrong])
    print(f"\n You lost at Level {level}. Word was: {word}")
    print(" Try again from the beginning!")
    return False
# Main game loop with 2 levels
def play_game():
    print(" Welcome to Hangman 2-Level Challenge Mode!")
    print(" Categories: Animals | Birds ")

    level = 1
    while level <= 2:
        word = random.choice(levels[level])
        won = play_level(level, word)
        if won:
            level += 1
        else:
            retry = input("Do you want to restart from Level 1? (y/n): ").lower()
            if retry != 'y':
                print(" Thanks for playing! See you again!")
                break
            level = 1  # restart

    if level > 2:
        print("\nYOU COMPLETED ALL 2 LEVELS! YOU ARE A HANGMAN CHAMPION! ")

# Run the game
play_game()
