import json
import random
import string
import os

class Password:
    def __init__(self,web,user,pss):
        self.web = web
        self.user = user
        self.pss = pss

class PassManager:
    def __init__(self):
        self.entries = {}
        self.entries["Users"] = []

    def show_entries(self):
        if not self.entries:
            print("No Entries Recorded")
        else:
            print(self.entries)

    def add_entry(self,passwrd):
        self.entries["Users"].append({"Website" : passwrd.web ,"Username" : passwrd.user ,"Password" : passwrd.pss})

    def search_entry(self):
        flag = 0
        searching = input("Enter Website : ")
        for items in self.entries["Users"]:
            if searching in items["Website"]:
                print(items["Website"])
                flag +=1
        if flag == 0:
            print("No Item Found")

    def edit(self):
        flag = 0
        searching = input("Enter Website : ")
        for i,items in enumerate(self.entries["Users"]):
            if searching == items["Website"]:
                new_user = input("Enter New User : ")
                new_pass = input("Enter New Password  : ")
                self.entries["Users"][i]["Username"] = new_user 
                self.entries["Users"][i]["Password"] = new_pass
                print("Info Changed")
                flag +=1 
        if flag == 0:
            print("No Item Found")
    def delete(self):
        flag = 0
        searching = input("Enter Website : ")
        for i,items in enumerate(self.entries["Users"]):
            if searching == items["Website"]:
                del self.entries["Users"][i]
                print("Info Deleted")
                flag +=1 
        if flag == 0:
            print("Deletion Canceled")

    def generate_pass(self,lenght):
        characters = (
            string.ascii_letters +
            string.digits +
            string.punctuation
        )
        pss = ""
        for i in range(lenght):
            pss += random.choice(characters)
        print(pss)
        return pss
    def save_data(self):
        with open(PATH,"w") as file:
           json.dump(self.entries,file,indent=2)

    def load_data(self):
        with open(PATH,"r") as file:
           self.entries = json.load(file)



        

def main():
    manager = PassManager()
    if os.path.isfile(PATH):
        manager.load_data()
    while True:
        choice = input("-------------- PASSWORD MANAGER ------------- \n\n"
                        "1- View All Entries\n"
                        "2- Add Entry\n"
                        "3- Search Entry \n"
                        "4- Edit Entry \n"
                        "5- Delete Entry \n"
                        "6- Generate Password\n"
                        "7- Save Data\n"
                        "8- Exit \n\n"
                        "Choose An Option : ")
        if choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5" and choice != "6" and choice != "7" and choice != "8":
            print("invalid input")
        elif choice == "1":
            manager.show_entries()
        elif choice == "2":
            web = input('website : ')
            user = input('username : ')
            pss = input('Password : ')
            entry =  Password(web,user,pss)
            manager.add_entry(entry)
        elif choice == "3":
            manager.search_entry()
        elif choice == "4":
            manager.edit()
        elif choice == "5":
            manager.delete()
        elif choice == "6":
            pss = manager.generate_pass(6)
            inp = input("Do you Like TO use This Pass Word In An entry ?  Y or N")
            if inp == "Y":
                web = input('website : ')
                user = input('username : ')
                entry =  Password(web,user,pss)
                manager.add_entry(entry)
        elif choice == "7":
            manager.save_data()
        elif choice == "8":
            manager.save_data()
            break
        



if __name__ == "__main__":
    main()