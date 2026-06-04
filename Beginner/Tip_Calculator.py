def main():
    price = input("What was your Tab ")
    Percent = input("How Much Do You Wanna Tip? % ")
    tip = int(price) * (int(Percent)/100)
    print("Your Tip Is " + str(tip))


if __name__ == '__main__':
    main()