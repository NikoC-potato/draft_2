import random
import pygame

board =[["_","_","_","_","_"],["_","_","_","_","_"],["_","_","_","_","_"],["_","_","_","_","_"],["_","_","_","_","_"]]
array = ["x","0","*", "+"]
randomchar = random.choice(array)
int_UY=0
int_UX=0
endgame = False

def mix_board():
    for i in range (0,5):
        for j in range (0,5):
            randomchar = random.choice(array)
            board[i][j]= randomchar


mix_board()

def print_board():
    global int_UX
    global int_UY
    global  choice
    global score
    global used_coor

    for i in board:
        print(i)
        used_coor = []

def get_info():
    global int_UX
    global int_UY
    global choice
    global score
    global used_coor
    global array
    UX = input("give x coordinates")
    int_UX = int(UX)


    UY = input("give y coordinates")
    int_UY = int(UY)

    choice = board[int_UY][int_UX]

    if choice in array:
        print(choice , "choice")
    if choice not in array:
        print("PICK AGAIN")



def check_logic(int_UY,int_UX):
    #global int_UX
    #global int_UY
    global board
    global  choice
    global score
    global used_coor
    choice = board[int_UY][int_UX]


# BACK
    if int_UX - 1 >= 0:
        back = board[int_UY][int_UX - 1]
        if back == choice in array not in used_coor:
            print(back, "= BACK - connected")
            board[int_UY][int_UX] = ("_")
            board[int_UY][int_UX - 1] = ("_")



# UP
    if int_UY - 1 >= 0:
        up = board[int_UY - 1][int_UX]
        if up == choice in array not in used_coor:
            print(up, "= UP - connected")
            board[int_UY][int_UX] = ("_")
            board[int_UY - 1][int_UX] = ("_")


#DOWN
    if int_UY + 1 <= 4:
        down = board[int_UY + 1][int_UX]
        if down == choice in array not in used_coor:
            print(down, "= DOWN - connected")
            board[int_UY][int_UX] = ("_")
            board[int_UY + 1][int_UX] = ("_")




    #FRONT
    if int_UX + 1 <= 4:
        front = board[int_UY][int_UX + 1]
        if front == choice in array not in used_coor:
            print(front, "= FRONT - connected")
            board[int_UY][int_UX] = ("_")
            board[int_UY][int_UX + 1] = ("_")





#make a not statment for the dash if location found a dash
def check_logic_game():
    i_counter = 0
    j_counter = 0

    for i in range(0,len(board)):
        #print(i, "iiii")
        for j in range(0, len(board[i])):
            #print(j,"jjjj")
            if i+1 <len(board):
                if ( board[i][j] == board[i+1][j] and board[i][j] !="_"):
                    print("still going")
                else:
                    i_counter = i_counter +1
                    print(i_counter, "icount")


    for i in range(0,len(board)):
        #print(i, "iiii")
        for j in range(0, len(board[i])):
            #print(j,"jjjj")
            if j+1 <len(board):
                if ( board[i][j] == board[i][j+1] and board[i][j] !="_"):
                    print("still going")
                else:
                    j_counter = j_counter + 1
                    print(j_counter,"jcount")

    if j_counter ==20 and i_counter == 20:
        print("mixing")
        mix_board()





def game_end():
    # win check



    endgame == True



#
# while endgame == False:
#     print_board()
#     get_info()
#     check_logic(int_UY,int_UX)
#     check_logic_game()
#     pygame.quit()


