'''
The goal of this exercise is to implement the hangman game. The game is
played by 2 players, in this case by the computer and the human.
The computer selects a secret word and the human tries to guess it
by suggesting letters or numbers, within a certain number of guesses.

The word to guess is represented by a row of dashes, representing each letter
of the word.

Each time the human player suggests a letter that is not present in the guessed
word, the counter of incorrect guesses is increased by one.

Computer wins and the game ends if the number of incorrect guesses reaches
specified amount. The human wins if the whole word is guessed before reaching
the limit of incorrect guesses.

The limit of incorrect guesses should be given to the function as a argument.

Example:

I am thinking of a word. What word is it?:

_ _ _ _ _ _ _
Guess a letter (9 guesses available): 'C'

No, the letter 'C' is not in my word

_ _ _ _ _ _ _
Guess a letter (8 guesses available): 'B'

No, the letter 'B' is not in my word

_ _ _ _ _ _ _
Guess a letter (7 guesses available): 'H'

Yes, there is 1 letter 'H'

H _ _ _ _ _ _

Guess a letter (7 guesses available): 'a'

Yes, there are 2 letters 'a'

H a _ _ _ a _


'''
import random
import re


def import_words(file_name):
    '''
    import words from a text file
    '''
    content = [x.strip() for x in open(file_name).readlines()]
    return content


def prompt_guess():
    '''
    Prompts the user for a character
    '''
    while True:
        guess = input("Enter Your guess: ")
        if len(guess) != 1:
            print("Wrong input")
            continue
        guess = guess.lower()
        return guess


def update_masked_word(word, masked_word, found_char):
    '''
    Updates the masked word with the newly found character
    '''
    new_word = list(masked_word)
    match_positions = [m.start() for m in re.finditer(found_char, word)]
    for position in match_positions:
        new_word[position] = found_char
    return "".join(new_word)


def main(word, guesses_available):
    '''
    Main Hangman loop
    '''
    known_letters = []
    guessed_chars = []
    masked_word = "_" * len(word)
    print("I am thinking of a word. What word is it?:")
    while guesses_available > 0:
        print("\nYou have {0} guesses left".format(guesses_available))
        print("{0}\n".format(masked_word))
        message = ""
        guess = prompt_guess()
        if guess in guessed_chars:
            print("This character has been already guessed!")
            continue
        guessed_chars.append(guess)
        if guess not in word:
            guesses_available -= 1
            message = "Letter {0} is not in the word".format(guess)
        else:
            known_letters.append(guess)
            masked_word = update_masked_word(word, masked_word, guess)
            message = "Letter {0} is in the word".format(guess)
        print(message)
        if len(known_letters) == len(set(word)):
            print("\nCongrats! You have won")
            print("The secret word was: {0}".format(word))
            return
        if guesses_available == 0:
            print("\nYou have lost!")
            print("The secret word was: {0}".format(word))
            return


if __name__ == '__main__':
    WORDS = import_words("random_words.txt")
    WORD = random.choice(WORDS).lower()
    main(WORD, 10)
