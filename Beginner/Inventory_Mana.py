import os 

def view_inventory(inventory):
    if not inventory:
        print("Inventory Is Empty")
    else :
        for keys in inventory :
            print(keys + "    " + str(inventory[keys]))

def input_checker(msg,inventory):
    while True:
        name = input(msg)
        if not name:
            print("String cannot be empty")
        elif name in inventory:
            print("Item Already There")
        else:
            return name
        
def index_checker(msg,inventory):
    while True:
        quant = input(msg)
        if not quant:
            print("String cannot be empty")
        elif not quant.isdigit():
            print("The Quantity has to be A number")
        elif float(quant) == 0:
            print("The quantity has to be higher than 0")
        else:
            return quant

def add_item(inventory):
    name = input_checker("Item Name : ",inventory)
    quantity = index_checker("Quantity : ",inventory)
    inventory[name] = int(quantity)
    print("Item Added Successfully")

def remove_item(inventory):
    name = input("Item Name : ")
    if not name:
        print("Cannot be an empty string")
    else:
        if name in inventory:
            del inventory[name]
            print("Item Removed")
        else:
            print("No item Found")

def stock_manager(name,inventory):
    while True:
        choice = input("1- Add Stock\n"
               "2- Remove Stock\n")
        if choice != "1" and choice != "2":
            print("invalid Input")
        elif choice == "1":
            quant =  index_checker("Quantity to Add : ",inventory)
            inventory[name] += int(quant)
            print("quantity added")
            break
        elif choice == "2":
            quant =  index_checker("Quantity to remove : ",inventory)
            if (inventory[name] - int(quant)) < 0 : 
                print("Not Enough Stock Available")
            else:
                inventory[name] -= int(quant)
                print("quantity removed")
            break
        

def update_item(inventory):
    name = input("Item Name : ")
    if not name:
        print("Cannot be an empty string")
    else:
        if not  name in inventory:
            print("No item Found")
        else:
            stock_manager(name,inventory)


def search_item(inventory):
    f = 0
    name = input("Search : ").lower()
    if not name:
        print("Empty string : ")
    for keys in inventory:
        if name in keys.lower():
            print(keys)
            print(inventory[keys])
            f +=1
    if f==0 :
        print("No Matching Items Found")

def low_stock(inventory):
    f = 0
    for keys in inventory:
        if inventory[keys] < 5:
            if f ==0 :
                print("LOW STOCK ITEMS")
            f+=1
            print(keys +" : " + str(inventory[keys]))
    if f==0:
        print("No Low Stock Items Found")

def save_inventory(inventory):
    with open(r"C:\Users\User\Desktop\test\inventory.txt","w") as file:
        for keys in inventory :
            file.write(keys + ":"+str(inventory[keys]) + "\n")

def main():
    inventory = {}
    if os.path.isfile(r"C:\Users\User\Desktop\test\inventory.txt"):
        with open(r"C:\Users\User\Desktop\test\inventory.txt","r") as file:
            for lines in file:
                inventory[lines.split(":")[0]] = int(lines.split(":")[1].rstrip())
    while True:
        choice = input("-------------- Inventory Manager ------------- \n\n"
                        "1- View Inventory\n"
                        "2- Add Item\n"
                        "3- Remove Item \n"
                        "4- Update Stock \n"
                        "5- Search Item \n"
                        "6- Low Stock Report\n"
                        "7- Total Inventory Items\n"
                        "8- Save Data\n"
                        "9- Exit\n\n"
                        "Choose An Option : ")
        if choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5" and choice != "6" and choice != "7" and choice != "8" and choice != "9":
            print("invalid input")
        elif choice == "1":
            view_inventory(inventory) 
        elif choice == "2":
            add_item(inventory)
        elif choice == "3":
            remove_item(inventory)
        elif choice == "4":
            update_item(inventory)
        elif choice == "5":
            search_item(inventory)
        elif choice == "6":
            low_stock(inventory)
        elif choice == "7":
            print("Total Items In Inventory : " + str(sum(inventory.values())))
        elif choice == "8":
            save_inventory(inventory)
        elif choice == "9" :
            save_inventory(inventory)
            break

if __name__ == "__main__":
    main()