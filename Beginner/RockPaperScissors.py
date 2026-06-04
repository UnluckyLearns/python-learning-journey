import random
def main():
    choice = ["R", "P", "S"]
    while True:
        user = input("pick between Rock Paper And Scissors ").upper()
        comp = random.choice(choice)
        if user not in choice:
            print("wront input")
            continue
        elif user == "S":
            if  comp  == "S":
                print("DRAW The Computer Chose Scissors ")
            elif comp == "P":
                print("WON The Computer Chose Paper ")
            elif comp  == "R":
                print("LOST The Computer Chose Rock ")
        elif user == "P":
            if comp  == "S":
                print("LOST The Computer Chose Scissors ")
            elif comp == "P":
                print("DRAW The Computer Chose Paper " )
            elif comp  == "R":
                print("Won The Computer Chose Rock ")
        elif user == "R":
            if comp  == "S":
                print("WON The Computer Chose Scissors ")
            elif comp  == "P":
                print("LOST The Computer Chose Paper ")
            elif comp  == "R":
                print("DRAW The Computer Chose Rock ")
       
        retry = input("Wanna PLay Again ? Y or N ")
        if retry == "N":
            break
            
            
if __name__ == "__main__":
    main()