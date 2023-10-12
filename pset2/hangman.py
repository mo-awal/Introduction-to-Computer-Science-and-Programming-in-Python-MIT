# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    return all([i in letters_guessed for i in secret_word])



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    return ''.join(letter if letter in letters_guessed else '_ ' for letter in secret_word)



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    letters = string.ascii_lowercase
    return ''.join(letter for letter in letters if letter not in letters_guessed)    
    


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    num_guesses = 6
    num_warnings = 3
    letters_guessed = []

    print('Welcome to the game Hangman!')
    print(f"I am thinking of a word that is {len(secret_word)} long")
    print(f"You have {num_warnings} warnings left.")
    print('=' * 25)

    # the game runs until the word is guessed or the user runs out of guesses
    # using (while num_guesses) can cause an infinite game because some inputs can result
    # in negative num_guesses e.g. if num_guesses==1 and the user enters an invalid vowel
    # that has not been guessed already, num_guesses will be equal to (1-2 = -1)
    while num_guesses > 0 and not is_word_guessed(secret_word, letters_guessed):
        print(f"You have {num_guesses} guesses left.")
        print("Available letters:", get_available_letters(letters_guessed))
        
        # get input from the user
        guess = ''
        while not guess.isalpha():        # this loop runs until the user enters a valid input, i.e. an alphabet or runs out of guesses
            guess = input('Please guess a letter: ').lower()

            # if guess is not an alphabet
            if not guess.isalpha():
                if num_warnings:          # if the user still has warnings left, we sutract 1 from num_warnings
                    num_warnings -= 1
                    print(f"Oops! That is not a valid letter. You have {num_warnings} warnings left:", get_guessed_word(secret_word, letters_guessed))
                elif num_guesses:           # if the user has no warnings left but still has guesses left, we subtract 1 from num_guesses
                    num_guesses -= 1
                    print(f'You have {num_guesses} guesses left.')
            
            # if the user runs out of guesses, break out of the while loop
            if not num_guesses:
                break
        
        # if guess has not been guessed already and it is in secret_word, the user loses no guesses
        # else if guess has not been guessed already and guess is not in secret_word,
        #   if guess is a consonant, the user loses one guess
        #   else, the user loses two guesses
        if guess not in letters_guessed:    # guess has not been guessed already
            if guess in secret_word:
              print('Good guess: ', end='')
            else:                           # guess is not in secret_word
              print(f"Oops! That letter is not in my word: ", end='')
              if guess not in 'aeiou':      # if guess is a consonant, we subtract 1 from num_guesses
                  num_guesses -= 1
              else:                         # if guess is a vowel, we subtract 2 from num_guesses
                  num_guesses -= 2
        else:                               # if guess has been guessed already
            if num_warnings:                # and the user still has warnings left, we subtract 1 from num_warnings
                num_warnings -= 1
                print(f"Oops! You have already guessed that letter. You have {num_warnings} warnings left: ")
            else:
                num_guesses -= 1          # if the user has no warnings left, we subtract 1 from num_guesses
        
        # adding guess to letters_guessed
        letters_guessed.append(guess)
        print(get_guessed_word(secret_word, letters_guessed))
        print('=' * 25)

        # if the user runs out of guesses before completing the word,
        # we tell them they lost and reveal the word to the user when the game ends
        if num_guesses <= 0:
            print(f"Sorry you ran out of guesses. The word was {secret_word}.")
        
        # if the user guesses the word correctly, we print a congratulatory message
        # and tell the user their score.
        if is_word_guessed(secret_word, letters_guessed):
            print('Congratulations, you won!')
            score = num_guesses * len(set(secret_word))
            print(f"Your total score for this game is: {score}")
        

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    my_word = my_word.replace('_ ', '_')
    if len(my_word) != len(other_word):
        return False
    else:
        for i in range(len(my_word)):
            if my_word[i] != '_':
              if (other_word.count(my_word[i]) != my_word.count(my_word[i])) or (my_word[i] != other_word[i]):
                return False
        return True



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    matches = [word for word in wordlist if match_with_gaps(my_word, word)]
    print(' '.join(matches)) if matches else print('No matches found')



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    num_guesses = 6
    num_warnings = 3
    letters_guessed = []

    print('Welcome to the game Hangman!')
    print(f"I am thinking of a word that is {len(secret_word)} long")
    print(f"You have {num_warnings} warnings left.")
    print('=' * 25)

    # the game runs until the word is guessed or the user runs out of guesses
    # using (while num_guesses) can cause an infinite game because some inputs can result
    # in negative num_guesses e.g. if num_guesses==1 and the user enters an invalid vowel
    # that has not been guessed already, num_guesses will be equal to (1-2 = -1)
    while num_guesses > 0 and not is_word_guessed(secret_word, letters_guessed): 
        print(f"You have {num_guesses} guesses left.")
        print("Available letters:", get_available_letters(letters_guessed))
        
        guess = ''
        while not guess.isalpha():    # while guess is not an alphabet
            guess = input('Please guess a letter: ').lower()

            # if the user enters *, we print all matching words
            if guess == '*':
                print('Possible word matches are:')
                show_possible_matches(get_guessed_word(secret_word, letters_guessed))
                break
            # if guess is not an alphabet
            elif not guess.isalpha():
                if num_warnings:          # if the user still has warnings left, we sutract 1 from num_warnings
                    num_warnings -= 1
                    print(f"Oops! That is not a valid letter. You have {num_warnings} warnings left:", get_guessed_word(secret_word, letters_guessed))
                elif num_guesses:         # if the user has no warnings left but still has guesses left, we subtract 1 from num_guesses
                    num_guesses -= 1
                    print(f'You have {num_guesses} guesses left.')
            
            # if the user runs out of guesses, break out of this while loop
            if not num_guesses:
                break
        
        # if guess has not been guessed already and it is in secret_word, the user loses no guesses
        # else if guess has not been guessed already and guess is not in secret_word,
        #   if guess is a consonant, the user loses one guess
        #   else, the user loses two guesses
        if guess != '*':
            if guess not in letters_guessed:  # guess has not been guessed already
                if guess in secret_word:
                  print('Good guess: ', end='')
                else:                         # guess is not in secret_word
                  print(f"Oops! That letter is not in my word: ", end='')
                  if guess not in 'aeiou':    # if guess is a consonant
                      num_guesses -= 1
                  else:                       # guess is a vowel
                      num_guesses -= 2
            else:                             # if guess has been guessed already
                if num_warnings:              # and the user still has warnings left, we subtract 1 from num_warnings
                    num_warnings -= 1
                    print(f"Oops! You have already guessed that letter. You have {num_warnings} warnings left: ")
                else:
                    num_guesses -= 1          # if the user has no warnings left, we subtract 1 from num_guesses
            
        # adding guess to letters_guessed
        letters_guessed.append(guess)
        print(get_guessed_word(secret_word, letters_guessed))
        print('=' * 25)

        # if the user runs out of guesses before completing the word,
        # we tell them they lost and reveal the word to the user when the game ends
        if num_guesses <= 0:
            print(f"Sorry you ran out of guesses. The word was {secret_word}.")
        
        # if the user guesses the word correctly, we print a congratulatory message
        # and tell the user their score.
        if is_word_guessed(secret_word, letters_guessed):
            print('Congratulations, you won!')
            score = num_guesses * len(set(secret_word))
            print(f"Your total score for this game is: {score}")
    



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    hangman(secret_word)

    # print(is_word_guessed('apple', ['e', 'i', 'k', 'p', 'r', 's', 'a', 'l']))
    # print(get_guessed_word('apple', ['e', 'i', 'k', 'p', 'r', 's']))
    # print(get_guessed_word('banana', ['b', 'a', 'n', 'p']))
    # print(get_available_letters(['e', 'i', 'k', 'p', 'r', 's']))

    # print(match_with_gaps('te_ t', 'tact'))
    # print(match_with_gaps('a_ _ le', 'banana'))
    # print(match_with_gaps('a_ _ le', 'apple'))
    # print(match_with_gaps('a_ ple', 'apple'))
    # print(match_with_gaps('a_ _ l_ ', 'atoll'))

    # show_possible_matches('t_ _ t')
    # show_possible_matches('abbbb_ ')
    # show_possible_matches('a_ pl_ ')

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    # secret_word = choose_word(wordlist)
    # hangman_with_hints(secret_word)
