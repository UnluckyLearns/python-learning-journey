import string
def count_words():
    word_counter = {}
    with open(r"PATH","r") as file:
        for lines in file:
            words = lines.lower().split()
            for word in words:
                word = word.strip(string.punctuation) 
                if not word:
                    continue
                elif (not word in word_counter):
                    word_counter[word] = 1
                else:
                    word_counter[word] += 1
        return word_counter

def view_counts(word_counter):
    for keys in word_counter:
        print(keys + ": " + str(word_counter[keys]))
    
def search_word(word_counter):
    name = input("Search : ").lower()
    if not name:
        print("empty string")
        return
    else:
        if name in word_counter:
            print(name+ " Has Appears " + str(word_counter[name]) +" Times")
        else:
            print("Word Not Found")

def most_word(word_counter):
    max_value = max(word_counter.values())
    for keys in word_counter:
        if word_counter[keys] == max_value:
            print(keys + " : " + str(word_counter[keys]))

def save_words(word_counter):
    with open(r"PATH","w") as file:
        for keys in word_counter:
            file.write(keys + ":" + str(word_counter[keys]) +"\n" )

def main():
    word_counter = count_words()
    while True:
        choice = input("-------------- Word Counter ------------- \n\n"
                        "1- View All Counts\n"
                        "2- Search Word \n"
                        "3- Most Frequent Word \n"
                        "4- Total Words \n"
                        "5- Unique Words\n"
                        "6- Save Results\n"
                        "6- Exit\n\n"
                        "Choose An Option : ")
        if choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5" and choice != "6" and choice != "7":
            print("invalid input")
        elif choice =="1":
            view_counts(word_counter)
        elif choice == "2":
            search_word(word_counter)
        elif choice == "3":
            most_word(word_counter)
        elif choice == "4":
            print("Total Words :" + str(sum(word_counter.values())))
        elif choice == "5":
            print("Unique Words : " + str(len(word_counter)))
        elif choice == "6":
            save_words(word_counter)
        elif choice =="7":
            save_words(word_counter)
            break
    
    
if  __name__=="__main__":
    main()