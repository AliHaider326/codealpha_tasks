import random

def hangman_game():
    words = ["python", "rocket", "planet", "laptop", "banana"]
    word_to_guess = random.choice(words)
    guessed_letters = ['_' for _ in word_to_guess]
    attempts_left = 6
    guessed = []

    print("🎯 Welcome to Hangman!")
    print("Guess the word, one letter at a time.")
    print("You have 6 incorrect attempts.\n")

    while attempts_left > 0 and ''.join(guessed_letters) != word_to_guess:
        print("Word:", ' '.join(guessed_letters))
        print(f"Incorrect attempts left: {attempts_left}")
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid alphabet letter.\n")
            continue

        if guess in guessed:
            print("You already guessed that letter!\n")
            continue

        guessed.append(guess)

        if guess in word_to_guess:
            for i in range(len(word_to_guess)):
                if word_to_guess[i] == guess:
                    guessed_letters[i] = guess
            print("Correct guess!\n")
        else:
            attempts_left -= 1
            print("Wrong guess!\n")

    if ''.join(guessed_letters) == word_to_guess:
        print("🎉 Congratulations! You guessed the word:", word_to_guess)
    else:
        print("😢 You lost! The word was:", word_to_guess)
hangman_game()