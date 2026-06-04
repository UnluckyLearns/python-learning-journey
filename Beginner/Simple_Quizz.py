def main():
    questions = [
        "what's my name ? ",
        "what's my last name ? ",
        "what's my age ? ",
        "what's my favorite anime ? ",
        "what's my favorite book ? "
    ]
    answers =  [
        "MR",
        "Clean",
        "200",
        "One Piece",
        "Crime And Punishment"
    ]
    score  =  0
    for items in range(len(questions)) :
        ans = input(questions[items]).upper()
        if ans == answers[items].upper() : 
            print("Correct")
            score = score  + 1
        else:
            print("wrong ")
            print("The Rights Answer Is " + answers[items])
    print("Your Score is " + str(score)+"/"+str(len(questions)))
    print("Percentage " + str((score/len(questions)) * 100) + "%")
if __name__ == "__main__":
    main()