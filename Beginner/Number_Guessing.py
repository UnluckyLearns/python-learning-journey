import random
import os
def play_game(diff):
    if diff == "1":
         max = 50
    elif diff == "2":
         max = 100
    else:
         max = 500
    num =  random.randint(1,max)
    guess_tracker = []
    attempts = 0
    guess = 0
    while guess != num:
        guess= input("guess the number it's between 1 and " + str(max) + " ")
        if not guess.isdigit():
                print("Invalid Input")
        elif int(guess)  > max or int(guess) <= 0:
                print("The Number is Not Between 1 and " + str(max) + " ")
        else:
            if int(guess) > num:
                    print("Guess Too High")
                    guess_tracker.append(guess)
                    attempts += 1
            elif int(guess) < num:
                    print("Guess Too Low")
                    guess_tracker.append(guess)
                    attempts += 1
            else:
                    guess_tracker.append(guess)
                    print("Correct The Number Generated is : " + guess)
                    print("guess history")
                    print(*guess_tracker,sep= "\n")
                    attempts += 1
                    return attempts

def update_stats(tracker,attempts):
    tracker["games_played"] = tracker["games_played"]  + 1
    tracker["full_attempts"] = tracker["full_attempts"] + attempts
    if tracker["best_score"] == 0:
        tracker["best_score"] = attempts
    elif  tracker["best_score"] > attempts:
        tracker["best_score"] = attempts
    tracker["average_attempts"] = tracker["full_attempts"] / tracker["games_played"]
    print("------STATS--------\n\n"
          "Games Played : " + str(tracker["games_played"]) + "\n"
          "Best Score : " +  str(tracker["best_score"])  + "\n" 
          "Average Attempts : " +  str(tracker["average_attempts"])  + "\n" ) 
    with open(r"PATH","w") as file:
         file.write(str(tracker["best_score"]))

def main():
    tracker = {"games_played" : 0, "best_score" : 0 ,"average_attempts" : 0 , "full_attempts" : 0}
    if os.path.isfile(r"PATH"):
         with open(r"PATH","r") as file:
              tracker["best_score"] = int(file.readline())
    while True:
        diff = input("pick a difficulty \n"
                     "1- Easy (Guess A number Between 1 and 50 \n"
                     "2- Medium (Guess A number Between 1 and 100 \n"
                     "3- Hard (Guess A number Between 1 and 500 \n")
        if diff !="1" and diff !="2" and diff != "3":
             print("Choose between Diff 1 2 and 3")
        else:
            attempts = play_game(diff)
            update_stats(tracker,attempts)
            retry = input("Wanna Play Again ? Y/N ").upper()
            if retry != "Y"  and retry != "N":
                print("invalid input")
            if retry == "N":
                break
             

            

        

if __name__== "__main__":
    main()