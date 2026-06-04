def main():
    farc = input("Is the temp ins Celsius(C) Or Ferinhet(F) ")
    temp  = input("Give me a Temperature ")
    repeat = 'N'
    if farc == "C" or farc == "c":
        fahr = 1.8*float(temp) + 32
        print(str(fahr) + " F")
        repeat = input("Would you like to convert another temperature? (Y/N)")
        if repeat == "Y":
            main()
    if farc == "F" or farc == "f" :
        cels = (float(temp) - 32) / 1.8
        print(str(cels) + " C")
        repeat = input("Would you like to convert another temperature? (Y/N)")
        if repeat == "Y":
            main()
        
        
    else :
        print("Invalid Temperature Type.")


if __name__ == "__main__":
    main()