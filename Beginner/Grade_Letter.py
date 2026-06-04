def main():
    many  = input("how many students grades do you wanna convert ")
    x = 1
    while x <= int(many) :
        grade = input("enter the grade for the student number" + str(x) + "from 0 to 100 ")
        if int(grade)  > 100 or int(grade) < 0:
            print("its not a valid score")
        else:
            if int(grade)  >= 90 and int(grade) <= 100:
                print('A')
            elif int(grade)  >= 80 and int(grade) <= 89:
                print('B')
            elif int(grade)  >= 70 and int(grade) <= 79:
                print('C')
            elif int(grade)  >= 60 and int(grade) <= 69:
                print('D')
            elif int(grade)  >= 0 and int(grade) <= 59:
                print('F')
        x = x + 1

if __name__ == "__main__":
    main()