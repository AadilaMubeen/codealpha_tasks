import random
WORDS=["python","computer","technology","programming","developer"]
MAX_INCORRECT_GUESSES=6;
def display_word(word,guessed_letters):
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)#display guessed letters and underscores for unknown letters.
def play_game():
    guessed_letters=set()
    incorrect_guesses=0
    print("\n" + "=" * 30)
    print("      HANGMAN GAME")
    print("=" * 30)
    print("Guess the word one letter at a time.")
    print(f"You have {MAX_INCORRECT_GUESSES} incorrect guesses at a time.")
    word=random.choice(WORDS)
    while incorrect_guesses < MAX_INCORRECT_GUESSES:
        print("\nWord:",display_word(word,guessed_letters))
        print(f"Incorrect guesses: "f"{incorrect_guesses}/{MAX_INCORRECT_GUESSES}")
        guess=input("Enter a letter").strip().lower() #to read a letter as input from user
        if len(guess)!=1 or not guess.isalpha():
            print("Enter a valid input")            #to check the validation of input
            continue
        if guess in guessed_letters:
            print("You already guessed that letter")  #Check for duplicates
            continue
        guessed_letters.add(guess)  #to store the guessed letter in a set
        if guess in word:
            print("Correct guess!")    #Check whether the guess is correct
        else:
            incorrect_guesses+=1
            print("Wrong guess!")
            
        if set(word).issubset(guessed_letters):
            print("\nCongratulations")
            print("You guessed the word:",word)        #to check if the player has guessed the complete word
            return
    print("\n" + "=" * 30)
    print("Game over!")
    print("\n" + "=" * 30)
    print("The correct word was:",word)       #Game ends after maximum incorrect guesses
def main():
    play_game()       
if __name__=="__main__":
    main()