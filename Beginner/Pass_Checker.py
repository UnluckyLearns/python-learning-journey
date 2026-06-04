import string

def main():
    while True:
        missing = []
        passw = input('Input Your Password    ')
        num_check = any(i.isdigit() for i in passw)
        upper_check = any(i.isupper() for i in passw)
        special_check = any(i in string.punctuation for i in passw)
        len_check = len(passw)
        if not num_check:
            missing.append("No Num")
        if not upper_check:
            missing.append("No Upper")
        if not special_check:
            missing.append("No Special Chara")


        if len_check < 8:
            print("Weak Password")
            missing.append("Password Too Short")
        else:
            if  upper_check and num_check and special_check:
                print("Excellent Password")
            elif upper_check and num_check:
                print("Very Strong Password")
            elif upper_check:
                print("Strong Password")
            else:
                print("Ok Password")
        if missing:
            print("Missing :")
            for item in missing:
                print(" - " + item)
        retry = input("wanna try another password Y or N ?   ").upper()

        if retry == "N":
            break
                
            

        

if __name__ == "__main__":
    main()