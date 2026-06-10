import os

def view_students(students):
    if not students:
        print("No StudenT Found")
    else:
        for keys in students:
            print(keys + " 's grades : " + str(students[keys]))


def input_checker(msg,students,flag):
    while True:
        name = input(msg)

        if not name:
            print("Invalid Input Empty String")
        elif name in students and flag == 0:
            print("already in there")
        elif (not name in students) and flag == 1: 
            print("Student Doesn't Exist")
        elif name in students and flag == 1:
            return name 
        elif (not name in students) and flag == 0: 
            return name
        else:
            return name.lower()


def grade_checker(msg):
    while True:
        grade = input(msg)
        if not grade:
            print("Empty String Choose A Number Between 1 And 20 ")
        elif not grade.isdigit():
            print("This Is not A number ")
        elif int(grade) < 0 or int(grade) > 20:
            print("Choose A number Between 0 and 20 ")
        else:
            return(grade)


def add_student(students):
    name = input_checker("What's the student name : ",students,0)
    students[name] = []
    print("The Student Was Added ")



def add_grade(students):
    name = input_checker("What's the student name : ",students,1)
    grade = grade_checker("Choose A grade Between 0 And 20 ")
    students[name].append(int(grade))
    print("The Grade Was Added")


def remove_student(students):
    name = input_checker("What's The Name Of The Student You Want To Remove ? ",students,1)
    del students[name]
    print("The Student Was Removed")


def search_student(students):
    name = input_checker("Search : ",students,3)
    flag = 0
    for keys in students:
        if name in keys.lower():
            print(keys)
            flag +=1
    if flag == 0:
        print("Student Not Found")

def student_average(students):
    name = input_checker("Student Name : ",students,1)
    if not students[name]:
        print("No Grades Available")
    else:
        print("The Average Of This Student Is : " + str(sum(students[name])/len(students[name])))

def class_average(students,i):
    total = 0
    count = 0
    top = 0
    st = ""
    flag = 0
    for keys in students:
        if not students[keys]:
            continue
        else:
            total += sum(students[keys])
            count += len(students[keys])
            if sum(students[keys])/len(students[keys]) > top:
                top = (sum(students[keys])/len(students[keys]))
                st = keys 
            flag += 1
    if flag == 0:
        print(" No Grades Available ")
    else :
        if i == 1:
            print("The Average Of The Class is : " + str(total/count))
        elif i == 2:
            print("The top Of The Class is : " + st + " With The Avg Score Of : " + str(top) )

def save_date(students):
    with open(r"PATH",'w') as file:
        for keys in students:
            file.write(keys+":"+ "".join(str(students[keys]).strip("[]")) + "\n")


def main():
    students  = {}
    if os.path.isfile(r"PATH"):
        with open(r"PATH",'r') as file:
            for lines in file:
                students[lines.split(":")[0]] = []
                for values in (lines.split(":")[1]).split(","):
                    values = values.strip()
                    if values:
                        students[lines.split(":")[0]].append(int((values.strip(" ")).strip("\n")))
                
    while True:
        choice = input("-------------- STUDENT GRADE MANAGER ------------- \n\n"
                        "1- View Students\n"
                        "2- Add Student\n"
                        "3- Add Grade \n"
                        "4- Remove Student \n"
                        "5- Search Student \n"
                        "6- Show Student Average\n"
                        "7- Show Class Average\n"
                        "8- Show Top Student\n"
                        "9- Save Data\n"
                        "10- Exit \n\n"
                        "Choose An Option : ")
        if choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5" and choice != "6" and choice != "7" and choice != "8" and choice != "9" and choice != "10":
            print("invalid input")
        elif choice == "1":
            view_students(students) 
        elif choice == "2":
            add_student(students)
        elif choice == "3":
            add_grade(students)
        elif choice == "4":
            remove_student(students)
        elif choice == "5":
            search_student(students)
        elif choice == "6":
            student_average(students)
        elif choice == "7":
            class_average(students,1)
        elif choice == "8":
            class_average(students,2)
        elif choice == "9" :
            save_date(students)
        elif choice == "10":
            save_date(students)
            break
if __name__=="__main__":
    main()