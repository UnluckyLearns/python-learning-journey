
def main():
    Birth_Year,Birth_Month,Birth_Day =  input("Birth Year Month And Day ").split("p")
    Current_Year = 2026
    Current_Month = 5
    Current_Day = 30

    Age_Year = Current_Year - int(Birth_Year)
    Age_Month = Current_Month - int(Birth_Month)
    Age_Day = Current_Day - int(Birth_Day)
    if Age_Day < 0:
        Age_Day = Age_Day + 30
        Age_Month = Age_Month - 1
    if Age_Month < 0:
        Age_Month = Age_Month + 12
        Age_Year = Age_Year - 1

    print ("You Are " + str(Age_Year) +" Years "+str(Age_Month) +" Months And" +str(Age_Day) +" Days Old")
        


if __name__ == "__main__":
    main()