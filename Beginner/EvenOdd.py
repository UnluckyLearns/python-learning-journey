def main():
    x =1
    while True:
        number = input("Enter Your Number ")
        if float(number) % 2 == 0 :
            print("Number Even")
        else:
            print("Number Odd")
        retry = input("Would you like to check another number? (Y/N)")
        if retry == "Y":
            x = x + 1
        else :
            break
    print(x)


if __name__ == "__main__":
    main()