import os

def view_books(books):
    if not books["Title"]:
        print("No Books at the moment")
    else:
        stats = {"Total" : 0 ,"Available": 0,"Borrowed": 0}
        for  i in range(len(books["Title"])):
            if books["Status"][i] == "Available":
                stats["Available"] += 1
            else:
                stats["Borrowed"] += 1
            
            print("Book : " + str(i + 1)  + "\n" + "Title : " + books["Title"][i] + "\n"
                  +"Author : " + books["Author"][i] + "\n"
                  + "Status : " + books["Status"][i] + "\n")
            stats["Total"] += 1
        print("-------------- Stats ---------- \n\n"
              +"Total Books: "+  str(stats["Total"]) + "\n"
              +"Available Books: "+ str(stats["Available"]) + "\n"
              + "Borrowed Books: " + str(stats["Borrowed"]) + "\n")
def get_input(msg):
    fill =  input(msg)
    while not fill:
        print("Invalid Input Try Again ")
        fill =  input(msg)
    return fill

def get_index(msg,books):
    index = input(msg)
    while not index.isdigit() or int(index) > len(books["Title"]) or int(index) == 0 :
        print("Wrong Input Try Again : ")
        index = input(msg)
    return int(index)

def add_book(books):
    title = get_input("What's The Title Of The New Book ? ")
    author =  get_input("who's the Author ?")
    books["Title"].append(title)
    books["Author"].append(author)
    books["Status"].append("Available")

def remove_book(books):
    if not books["Title"]:
        print("No books available.")
        return
    view_books(books)
    index =  get_index("What's the Number Of The Book You Want To Remove ",books)
    del books["Title"][index - 1]
    del books["Author"][index - 1]
    del books["Status"][index - 1]

def search_book(books):
    search = get_input("What Book Do You Want To Search For ? ").lower()
    flag = 0
    for i,t in enumerate(books["Title"]):
        if search in t.lower():
            print("Book : " + str(i + 1)  + "\n" + "Title : " + books["Title"][i] + "\n"
                  +"Author : " + books["Author"][i] + "\n"
                  + "Status : " + books["Status"][i] + "\n")
            flag +=1
    if flag == 0:
        print("No Books Were Found")

def borrow_book(books):
    if not books["Title"]:
        print("No books available.")
        return
    view_books(books)
    index = get_index("What't The Number Of The Book You Want To Borrow ?",books)
    if books["Status"][index-1] == "Available":
        print("Congrats You Borrowed The Book ")
        books["Status"][index-1] =  "Borrowed"
    else:
        print("Sorry The Book Is Not Available ")

def return_book(books):
    view_books(books)
    index = get_index("What't The Number Of The Book You Want To Return ?",books)
    if books["Status"][index-1] == "Borrowed":
        print("Congrats You Borrowed The Book ")
        books["Status"][index-1] =  "Available"
    else:
        print("The Book Is Already Available ")

def save_library(books):
    with open(r"PATH","w") as file:
        for i in range(len(books["Title"])):
            file.write(books["Title"][i] + ":" + books["Author"][i] +":"+books["Status"][i] + "\n")



def main():
    books = {"Title": [],"Author": [],"Status": []}
    if os.path.isfile(r"PATH"):
        with open(r"PATH","r") as file:
            for line in file:
                books["Title"].append(line.split(":")[0])
                books["Author"].append(line.split(":")[1])
                books["Status"].append(line.split(":")[2].rstrip("\n"))

    while True:
        choice = input("-------------- LIB MANAGEMENT ------------- \n\n"
                     "1- View Books\n"
                     "2- Add Book\n"
                     "3- Remove Book \n"
                     "4- Search Book \n"
                     "5- Borrow Book \n"
                     "6- Return Book\n"
                     "7- Save Library\n"
                     "8- Exit \n\n"
                     "Choose An Option : ")
        if choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5" and choice != "6" and choice != "7" and choice != "8":
            print("invalid input")
        elif choice == "1":
            view_books(books)
        elif choice == "2":
            add_book(books)
        elif choice == "3":
            remove_book(books)
        elif choice == "4":
            search_book(books)
        elif choice == "5":
            borrow_book(books)
        elif choice == "6":
            return_book(books)
        elif choice == "7":
            save_library(books)
        elif choice == "8":
            break
if __name__ == "__main__":
    main()