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
    
    #word=list(secret_word)
    for w in secret_word:
        if w not in letters_guessed:
            #word.remove(w)
            return False
    return True

    #return len(word)== 0

    #return all(letter in letters_guessed for letter in secret_word)



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    guessed_word = ""
    for w in secret_word:
        if w in letters_guessed:
                guessed_word += w
        else:
            guessed_word += " _ "
    return guessed_word

    #return ' '.join(letter if letter in letters_guessed else '_'
     #               for letter in secret_word)       


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    #import string
    letters = list(string.ascii_lowercase)
    for i in letters_guessed:
        letters.remove(i)
    letters = "".join(letters)
    return letters
    
    #return ''.join(letter for letter in string.ascii_lowercase
                  # if letter not in letters_guessed)
    

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
    print("Welcome to the game Hangman!")
    word_length = len(secret_word)
    print("I am thinking of a word that is ", word_length, " letters long")
    print("-------------")
    guesses = 6
    letters_guessed = []
    game = True
    warnings=3
    vowels = ["a", "e", "i", "o", "u"]
    guessed_word = get_guessed_word(secret_word, letters_guessed)
    unique_letters = 0
    while game and guesses>0:
        print("you have ", warnings, " warnings left")
        print("you have ", guesses, " guesses left")
        available_letters = get_available_letters(letters_guessed)
        print("Available letters: ", available_letters)
        letter = input("Please guess a letter: ")
        if not str.isalpha(letter) or len(letter)>1:
            warnings -=1
            if warnings < 0:
                guesses -=1
                print("Oops! That is not a valid letter. You have no warnings left: ", guessed_word)
            else: 
                print("Oops! That is not a valid letter. You have ", warnings, " warnings left: ", guessed_word)
        else:
            letter = str.lower(letter)
            if letter in letters_guessed:
                warnings -=1
                if warnings < 0:
                    warnings = 0
                    guesses -=1
                print("Oops! You've already guessed that letter. You now have ", warnings, " warnings: ", guessed_word)
            else:
                letters_guessed.append(letter)
                guessed_word = get_guessed_word(secret_word, letters_guessed)
                if letters_guessed[-1] in guessed_word:
                    print("Good guess: ", guessed_word)
                    unique_letters += 1
                else:
                    print("Oops! That letter is not in my word: ", guessed_word)
                    if letter in vowels:
                            guesses -=2
                    else:
                        guesses -=1
        #game termination
        if is_word_guessed(secret_word,letters_guessed):
            score=unique_letters*guesses
            print("Congratulations you won!")
            print("Your total score for this game is :", score)
            game=False
        print("------------")
    if guesses<1:
        print("Sorry you ran out of guesses. The word was ", secret_word)

        


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
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    Match = True
    letters_used = []
    guessed_word = "".join(my_word.split())

    if len(guessed_word)==len(other_word):
        for g in guessed_word:
            if g != "_" and g not in letters_used:
                    letters_used.extend(g)
        #letters_used.sort()
        for i in range(0,len(guessed_word)):
            if guessed_word[i] != "_":
                if guessed_word[i] != other_word[i]:
                    Match = False
                    break
            else:
                for w in letters_used:
                    if other_word[i]== w:
                        Match = False
                        break
    else: 
        Match = False
                    
    return Match


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    #wordlist = load_words()
    matches = []
    for w in wordlist:
        if match_with_gaps(my_word,w):
            matches.append(w)
    if len(matches) >0:
        print(matches)
    else:
        print("no matches found")



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
    print("Welcome to the game Hangman!")
    word_length = len(secret_word)
    print("I am thinking of a word that is ", word_length, " letters long")
    print("-------------")
    guesses = 6
    letters_guessed = []
    #is_guessed = False
    game = True
    warnings=3
    vowels = ["a", "e", "i", "o", "u"]
    guessed_word = get_guessed_word(secret_word, letters_guessed)
    unique_letters = 0
    while game:
        v = False
        already_used = False
        print("you have ", warnings, " warnings left")
        print("you have ", guesses, " guesses left")
        available_letters = get_available_letters(letters_guessed)
        print("Available letters: ", available_letters)
        letter = input("Please guess a letter: ")
        if letter == "*":
            print("Possible word matches are: ", show_possible_matches(guessed_word))
        if not str.isalpha(letter):
            warnings -=1
            if warnings < 1:
                warnings = 0
                guesses -=1
            print("Oops! That is not a valid letter. You have ", warnings, " warnings left: ", guessed_word)
        else:
            letter = str.lower(letter)
            for l in letters_guessed:
                if l == letter:
                    already_used = True
            if already_used == True:
                warnings -=1
                if warnings < 1:
                    warnings = 0
                    guesses -=1
                print("Oops! You've already guessed that letter. You now have ", warnings, " warnings: ", guessed_word)
            else:
                letters_guessed.append(letter)
                guessed_word = get_guessed_word(secret_word, letters_guessed)
                good_guess = False
                for i in guessed_word:
                    if letters_guessed[-1]==i:
                        good_guess = True
                if good_guess:
                    print("Good guess: ", guessed_word)
                    unique_letters += 1
                else:
                    print("Oops! That letter is not in my word: ", guessed_word)
                    for i in vowels:
                        if letter == i:
                            v = True
                            guesses -=2
                    if not v:
                        guesses -=1

        #game termination
        if guesses<1:
            print("Sorry you ran out of guesses. The word was ", secret_word)
            game=False
        blanks=0
        score=unique_letters*guesses
        #x = list(guessed_word)
        for g in guessed_word:
            if g=="_":
                blanks +=1
        if blanks==0:
            print("Congratulations you won!")
            print("Your total score for this game is :", score)
            game=False
        print("------------")


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    secret_word = "apple"
    hangman(secret_word)
    
    '''testing'''
    

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
