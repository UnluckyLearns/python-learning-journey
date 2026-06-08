def input_checker(msg,draw): 
    while True:
        check = input(msg)
        if not check:
            print("Please Choose A position")
        elif (not check.isdigit()) or check == "0" or len(check) != 1:
            print("Invalid Input")
        elif not check in draw:
            print("Position already Taken")
        else:
            return check

def drawing(draw):
    print(draw[0] + " | " + draw[1] + " | " + draw[2] + "\n" +
            "---------\n"+
            draw[3] + " | " + draw[4] + " | " + draw[5] + "\n"
            "---------\n"+
            draw[6] + " | " + draw[7] + " | " + draw[8] + "\n")

def win_check(draw,player):
    if draw[0] == draw[1] == draw[2] or  draw[3] == draw[4] == draw[5]  or draw[6] == draw[7] == draw[8] or draw[2] == draw[5] == draw[8] or draw[1] == draw[4] == draw[7] or draw[0] == draw[3] == draw[6] or  draw[2] == draw[4] == draw[6] or draw[0] == draw[4] == draw[8]:
        print("PLayer " + player + " Won ")
        return 1
    elif all(char.isalpha() for char in draw):
        return 2
    return 0

def main():
    draw = ['1','2','3','4','5','6','7','8','9']
    current_player = "X"
    while True:
        drawing(draw)

        player = input_checker("Player  " + current_player  +  " 's Move : ",draw)
        draw[int(player) - 1] = current_player
        result = win_check(draw,current_player)
        if result == 1:
            drawing(draw)
            break
        elif result  == 2:
            print("draw")
            break
        if current_player == "X":
            current_player = "O"
        else :
            current_player = "X"
        
        

if __name__ == "__main__":
    main()