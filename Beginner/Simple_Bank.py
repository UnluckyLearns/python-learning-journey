import re
import os
from  datetime import datetime

def amount_check(amount):
    pattern =  r'^\d+\.{0,1}\d*$'
    if not re.search(pattern,amount):
        print("Invalid Input Please Enter A Number")
    elif float(amount) <= 0:
        print("You cant Withdraw or Deposit Nothing ")
    else:
        return True
    return False
def deposit_money(account):
    amount = input("How Much Do You Want To Deposit ? ")
    if amount_check(amount):
         account["Balance"] += float(amount)
         account["History"].append("Deposit : " + amount + " At " + str(datetime.now()).split(".")[0]) 
         print("The Amount Has Been Deposited Into Your Account")

def withdraw_money(account):
    amount = input("How Much Do You Want To Withdraw ? ")
    if amount_check(amount):
        if float(amount) > account["Balance"]:
             print("Insufficient Balance")
        else:
         account["Balance"] -= float(amount)
         account["History"].append("Withdraw : " + amount + " At " + str(datetime.now()).split(".")[0]) 
         print("The Amount Has Been Withdrawn From Your Account")


def history(account):
    print("-------------- Transaction History ------------- \n\n")
    for trans in account["History"] : 
        print(trans + "\n")

def save_data(account):
    with open(r"PATH","w") as file:
        file.write(str(account["Balance"]))
    with open(r"PATH","w") as file:
        for trans in account["History"]:
            file.write(trans + "\n")

def data_import(account):
    if os.path.isfile(r"PATH"):
        with open(r"PATH","r") as file:
            account["Balance"] = float(file.readline())
    if os.path.isfile(r"PATH"):
        with open(r"PATH","r") as file:
            for lines in file:
                account["History"].append(lines.rstrip("\n"))

def main():
    account = {"Balance": 0,"History": [],}
    data_import(account)
    while True:
        choice = input("-------------- BANK ACCOUNT ------------- \n\n"
                "1- View Balance\n"
                "2- Deposit Money\n"
                "3- Withdraw Money\n"
                "4- Transaction History \n"
                "5- Exit \n\n"
                "Choose An Option : ")
        if choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5":
            print("Invalid Input")
        elif choice == "1":
            print("Your Current Balance Is : "  + str(account["Balance"])+"$")
        elif choice == "2":
            deposit_money(account)
        elif choice == "3":
            withdraw_money(account)
        elif choice == "4":
            history(account)
        elif choice == "5":
            save_data(account)
            break

if __name__ == "__main__":
    main()