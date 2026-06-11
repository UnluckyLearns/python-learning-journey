import random
import os

def view_cards(cards):
    if not cards:
        print("No Flashcards Found ")
    else:
        for i, (keys,values) in  enumerate(cards.items()):
            print(str(i+ 1)+'.'+" " + keys +  "\n" + "Answer : " + values + "\n")

def input_checker(msg,cards):
    while True:
        quest = input(msg)
        if not quest:
            print("Empty string ")
        elif quest in cards:
            print("Question Already There ")
        else:
            return quest

def index_checker(msg,cards):
    while True:
        index = input(msg)
        if not index:
            print("Empty string ")
        elif not index.isdigit():
            print("not a number")
        elif int(index) > len(cards) or int(index) == 0:
            print("Index Out of Range ")
        else:
            return int(index)

def add_card(cards):
    quest = input_checker("What's The Question ? ",cards)
    answer = input("What's The Answer ? ")
    while not answer:
        print("Empty String Try Again. ")
        answer = input("What's The Answer ? ")
    cards[quest] = answer 
    print("Card Added")

def remove_card(cards):
    view_cards(cards)
    index = index_checker("What's the Number Of The flashcard YUou Want To Remove ? ",cards) - 1
    key = list(cards.keys())[index]
    del cards[key]

def search_card(cards):
    name = input("Search : ").lower()
    f = 0
    if not name:
        print("empty string ")
        return 
    else:
        for keys in cards:
            if name in keys.lower():
                print( keys +  "\n" + "Answer : " +  cards[keys] + "\n")
                f +=1
    if f == 0:
        print("No Flash cARDS Found")
        
def random_card(cards):
    retry =""
    while retry != "n":
        if not cards:
            print("No Flashcards Found . ")
            return 
        rand_card = random.choice(list(cards))
        print(rand_card)
        ans = input("Answer ? ").lower()

        if not ans:
            print("empty string")
        elif ans ==  cards[rand_card].lower():
            print("Corrent Answer")
        else:
            print("Wrong Answer . " + "\n" +"The Correct Answer Is : " + cards[rand_card])
        retry = input("If You Want To Stop Press N or n ")

def save_data(cards):
    with open(r"PATH",'w') as file:
        for keys in cards:
            file.write(keys + ":" + cards[keys] + "\n")
    
def main():
    cards = {}
    if os.path.isfile(r"PATH"):
        with open(r"PATH","r") as file:
            for lines in file:
                 cards[lines.split(":")[0]] = (lines.split(":")[1]).rstrip("\n")
    while True:
        choice = input("-------------- Inventory Manager ------------- \n\n"
                        "1- View Cards\n"
                        "2- Add Card\n"
                        "3- Remove Card \n"
                        "4- Search card \n"
                        "5- Random Card \n"
                        "6- Save data\n"
                        "7- Exit \n\n"
                        "Choose An Option : ")
        if choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5" and choice != "6" and choice != "7":
            print("invalid input")
        elif choice == "1":
            view_cards(cards) 
        elif choice == "2":
            add_card(cards)
        elif choice == "3":
            remove_card(cards)
        elif choice == "4":
            search_card(cards)
        elif choice == "5":
            random_card(cards)
        elif choice == "6":
            save_data(cards)
        elif choice == "7":
            save_data(cards)
            break
    print("test")

if __name__ == "__main__":
    main()