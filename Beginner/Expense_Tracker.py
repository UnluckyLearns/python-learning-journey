import os

def view_expenses(ex):
    if not ex["name"]:
        print("no expensees")
    else:
        for  i , expense in enumerate(ex["name"],start = 1):
            print(str(i) +"- " +ex["name"][i-1] + " : " + ex["amount"][i-1] + "$")

def add_expenses(ex):
    name = input("what was the name of the expense ")
    price = input("how much did it cost ")
    ex["name"].append(name)
    ex["amount"].append(price)
    print(ex)


def remove_expenses(ex):
    view_expenses(ex)
    index = input("what's the number of the expense you want to remove ")
    del ex["name"][int(index) - 1]
    del ex["amount"][int(index) - 1]
    

def total_spent(ex):
    total = 0
    for price in range(len(ex["amount"])):
        total = total + float(ex["amount"][price])
    print("Your Total is: " + str(total))

def largest_expense(ex):
    largest = 0
    index = 0
    for price in range(len(ex["amount"])):
        if float(ex["amount"][price]) > float(largest):
            largest = ex["amount"][price]
            index = price
    print("Your Biggest Expense Is : " + ex["name"][index] +"  - "+str(largest))

def save_expense(ex):
    with open(r'path','w') as file:
        for index in range(len(ex["name"])):
            file.write(ex["name"][index] + ':' + ex["amount"][index] + "\n")


def main():
    ex = {"name":[],"amount":[]}
    if os.path.isfile(r'path'):
        with open(r'path','r') as file:
            for lines in file:
                ex["name"].append(lines.split(":")[0])
                ex["amount"].append(lines.split(":")[1].rstrip("\n"))
    choice = "0"
    while choice != "7":
        choice = input("------ EXPENSE TRACKER ------\n\n"
                "1. View Expenses\n"
                "2. Add Expense\n"
                "3. Remove Expense\n"
                "4. Show Total Spent\n"
                "5. Show Largest Expense\n"
                "6. Save Expenses\n"
                "7. Exit\n"
                "\n"
                "Choose An option : ")
        if choice!= "1" and choice!= "2" and choice!= "3" and choice!= "4" and choice!= "5" and choice!= "6" and choice!= "7":
            print("wrong input")
        elif choice == "1":
            view_expenses(ex)
        elif choice == "2":
            add_expenses(ex)
        elif choice == "3":
            remove_expenses(ex)
        elif choice == "4":
            total_spent(ex)
        elif choice == "5":
            largest_expense(ex)
        elif choice == "6":
            save_expense(ex)

if  __name__ == "__main__":
    main()