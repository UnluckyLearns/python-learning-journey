def main():
    n1 = input("enter the first number ")
    op = input("choose between + - / * ")
    n2 = input("enter the second number ")
    res = 0
    if op != "+" and op != "-" and op != "/" and op != "*":
        print("invalide operation")
    elif op == "+":
        res = float(n1) + float(n2)
        print(res)
    elif op == "-":
        res = float(n1) - float(n2)
        print(res)
    elif op == "/":
        if float(n2) == 0:
            print("cannot divide by 0")
        else:
            res = float(n1) / float(n2)
            print(res)
    elif op == "*":
        res = float(n1) * float(n2)
        print(res)
    retry= input("Would you like another calculation? (Y/N)")
    if retry == 'Y':
        main()

if __name__ == "__main__":
    main()
