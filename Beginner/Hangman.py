import random

def main():
    print("test")
    word_list = [
    "PYTHON",
    "COMPUTER",
    "KEYBOARD",
    "MONITOR",
    "PROGRAM",
    "HANGMAN",
    "FUNCTION",
    "VARIABLE"]
    word = list(random.choice(word_list).upper())
    hidden = list("-" * len(word))
    letter_guessed = []
    lives = 6
    retry = ""
    while True:
        guess = input("What's your Guess : " + "".join(hidden) + " ").upper()
        if not guess:
            print("You Should Guess One Letter")
        elif not guess.isalpha():
            print("You Should Only Guess Letters ")
        elif len(guess) > 1 :
            print("You should Guess Only One Letter: ")
        elif guess in letter_guessed:
            print("You Already Guessed This Letter")
        else:
            letter_guessed.append(guess)
            print("Guessed Letters : " + ",".join(letter_guessed))
            if guess in word:
                print("Correct Guess")
                for i,let in enumerate(word):
                    if let == guess:
                        hidden[i] = guess
            else:
                print("Wrong Guess")
                lives -=  1
                print("Tries Left: " + str(lives))
            if "-" not in hidden:
                print("You Have Guess The Word " + "".join(hidden))
                retry = input("do you wanna play again ? ")
            elif lives == 0:
                print("You Are Out Of Tries You Lost .")
                retry = input("do you wanna play again ? ")
            if retry == "N":
                break
            if retry == "Y":
                word = list(random.choice(word_list).upper())
                hidden = list("-" * len(word))
                letter_guessed = []
                lives = 6

if __name__ == "__main__":
    main()