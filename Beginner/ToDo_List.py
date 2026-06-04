import os

def view_tasks(tasks):
    if not tasks:
        print("empty list")
    else:
        i = 1
        for task in tasks:
            print(str(i) +"- " +task)
            i = i + 1

def add_tasks(tasks):
    addition = input("What's the Task You Want To Add ?")
    tasks.append(addition)

def remove_tasks(tasks):
    view_tasks(tasks)
    removal = input("What's The Number Of The Task You Wanna Remove ?")
    if not removal.isdigit():
        print("invalid input")
    elif int(removal) > len(tasks):
        print("index out of range")
    else:
        del tasks[int(removal)-1]
    
def edit_tasks(tasks):
    view_tasks(tasks)
    index = input("whats the nmber of the task you wanna edit ")
    if not index.isdigit():
        print("invalid input")
    elif int(index) > len(tasks):
        print("index out of range ")
    else:
        tasks[int(index)-1] = input("What's The New Task ")

def save_file(tasks):
    with open(r'C:\Users\User\Desktop\test\tasks.txt', 'w') as tasks_txt:
     for task in tasks:
        tasks_txt.write(task+"\n")


def main():
    if os.path.isfile(r'C:\Users\User\Desktop\test\tasks.txt'):
        with open(r'C:\Users\User\Desktop\test\tasks.txt', 'r') as file:
            tasks = file.read().splitlines()
    else:
        tasks = []
    num  = "0"
    while num!= "5":
        num = input("------ TO-DO list ------- \n"
                "1. View Tasks\n"
                "2. Add Tasks\n"
                "3. Remove Task\n"
                "4. Edit Task\n"
                "5. Exit List\n"
                "Choose An option : ")
        if num != "1" and num != "2" and num != "3" and num != "4" and num != "5":
            print("Wrong Input Try Again")
        elif num == "1":
            view_tasks(tasks)
        elif num == "2":
            add_tasks(tasks)
        elif num == "3":
            remove_tasks(tasks)
        elif num == "4":
            edit_tasks(tasks)
    save_file(tasks)
    

if __name__ =="__main__":
    main()