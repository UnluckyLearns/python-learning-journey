import os

def view_contacts(contacts):
    if not contacts["name"]:
        print("No Contacts Recorded")
    else :
        for i,names in enumerate(contacts["name"]):
            print("Contact : " + str(i + 1)  + "\n" + "Name : " + contacts["name"][i] + "\n"
                  +"Email : " + contacts["email"][i] + "\n"
                  + "Phone : " + contacts["phone"][i] + "\n")



def add_contact(contacts):
    name = input("Name ? ")
    if name == "":
        print("Can't Accept An Empty String")
        return
    elif any(c.lower() == name.lower() for c in  contacts["name"]):
        print("contact Already Exists")
        return
    email = input ("Email ? ")
    if email == "":
        print("Can't Accept An Empty String")
        return 
    phone = input("Phone ? ")
    if phone == "":
        print("Can't Accept An Empty String")
        return 
    contacts["name"].append(name)
    contacts["email"].append(email)
    contacts["phone"].append(phone)
    print("contact Added Succefully ")



def remove_contact(contacts):
    view_contacts(contacts)
    contact_num=input("choose the number of the contact you Want to delete : ")
    if not contact_num.isdigit():
        print("not a valid input")
    elif int(contact_num)  > len(contacts["name"] ) or int(contact_num)  == 0:
        print("There is not a single contact matching that index " )
    else : 
        del contacts["name"][int(contact_num) - 1]
        del contacts["email"][int(contact_num) - 1]
        del contacts["phone"][int(contact_num) - 1]



def search_contact(contacts):
    contact = input("The name You wANT To Searchg For ").lower()
    flag = 0
    for i, c in enumerate(contacts["name"]):
        if contact in c.lower():
            print("Contact : " + str(i + 1) + "\n" +
                 "Name : " + contacts["name"][i] + "\n" +
                 "Email : " + contacts["email"][i] + "\n" +
                 "Phone : " + contacts["phone"][i] + "\n")
            flag += 1
    if flag == 0:
        print("contact Not Found")


def edit_contact(contacts):
    view_contacts(contacts)
    contact_num=input("choose the number of the contact you Want to edit : ")
    if not contact_num.isdigit():
        print("not a valid input")
    elif int(contact_num)  > len(contacts["name"] or int(contact_num)  == 0):
        print("There is not a single contact matching that index " )
    else:
        name = input(" New Name ? ")
        if name == "":
            print("Can't Accept An Empty String")
            return 
        email = input ("New Email ? ")
        if email == "":
            print("Can't Accept An Empty String")
            return 
        phone = input("New Phone ? ")
        if phone == "":
            print("Can't Accept An Empty String")
            return 
        contacts["name"][int(contact_num) - 1] = name
        contacts["email"][int(contact_num) - 1] = email
        contacts["phone"][int(contact_num) - 1] = phone




def save_contacts(contacts):
    with open(r"PATH","w") as file:
         for i,names in enumerate(contacts["name"]):
             file.write(contacts["name"][i] + ":" +contacts["email"][i] + ":" +contacts["phone"][i] + "\n" )





def main():
    contacts = {"name": [],"email": [],"phone": []}
    if os.path.isfile(r"PATH"):
        with open(r"PATH","r") as file:
            for lines in file:
                contacts["name"].append(lines.split(":")[0])  
                contacts["email"].append(lines.split(":")[1]) 
                contacts["phone"].append(lines.split(":")[2].rstrip("\n")) 
    print(contacts)
    while True:
        choice = input("-------------- CONTACT BOOK ------------- \n\n"
                     "1- View Contacts\n"
                     "2- Add Contacts\n"
                     "3- Remove Contacts \n"
                     "4- Search Contact\n"
                     "5- Edit Contact\n"
                     "6- Save Contacts\n"
                     "7- Exit\n\n"
                     "Choose An Option : ")
        if choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5" and choice != "6" and choice != "7":
            print("invalid Choice") 
        elif choice  == "1":
            view_contacts(contacts)
        elif choice == "2":
            add_contact(contacts)
        elif choice == "3":
            remove_contact(contacts)
        elif choice == "4":
            search_contact(contacts)
        elif choice == "5":
            edit_contact(contacts)
        elif choice == "6":
            save_contacts(contacts)
        elif choice == "7":
            break

if __name__ == "__main__":
    main()