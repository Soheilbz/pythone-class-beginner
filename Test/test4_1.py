#   طراحی بازی tic - tac - toe
print ("Game tic-tac-toe")

game_board = [["-","-","-"],
              ["-","-","-"],
              ["-","-","-"]] 

def show () :
    for row in game_board :
        for cell in row :
            print (cell, end="")
        print ()
show ()

def check_game () :
    win_pos = [[[0,0],[0,1],[0,2]]]
    if game_board [0][0] == "X" and game_board [0][1]== "X" and game_board [0][2]== "X": 
        print ("you win") 

while True : 
        print ("player 1 choose youre cell ? ")
        while True : 
            row = int (input ())
            col = int (input ())
            if 0<=row<=2 and 0<=col<=2 :
                if game_board [row][col] == "-" :
                    game_board [row][col] = "X"
                    show ()
                    check_game ()
                    break
                else :
                    print ("Choose another cell")
            else :
                print ("Enter number between 0-2 : ")
                
        print ("player 2 choose youre cell ? ")
        while True :
            row = int (input ())
            col = int (input ())
            if 0<=row<=2 and 0<=col<=2 :
                if game_board [row][col] == "-" :
                    game_board [row][col] = "O"
                    show ()
                    break
                else :
                    print ("Choose another cell")
            else :
                print ("Enter number between 0-2 : ")
