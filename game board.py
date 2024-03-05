import pygame
import random
from main import *
board =[["_","_","_","_","_"],["_","_","_","_","_"],["_","_","_","_","_"],["_","_","_","_","_"],["_","_","_","_","_"]]
array = ["x","0","*", "+"]
randomchar = random.choice(array)
used_coor = []

def mix_board():
    for i in range (0,5):
        for j in range (0,5):
            randomchar = random.choice(array)
            board[i][j]= randomchar


mix_board()

pygame.init()



width  = 800
height = 600
padding_x = (width - 400)/2
padding_y = (height - 400)/2
clock = pygame.time.Clock()
pygame.display.set_caption('Quick Start')
window_surface = pygame.display.set_mode((width, height))
counter, text = 600, '600'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)
font = pygame.font.SysFont('Consolas', 30)

background = pygame.Surface((800, 600))
background.fill(pygame.Color(255, 200, 200))


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




is_running = True

while is_running:
    #pygame.draw.rect(window_surface, (255, 150, 250), pygame.Rect(padding_x, padding_y, 400,400))
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()
            x = round((mouse_pos[0]-padding_x)/(400/4))
            y = round((mouse_pos[1]-padding_y)/(400/4))

            if(x>=0 and x <=4 and y >= 0 and y<=4):
                choice = board[y][x]
                check_logic(y,x)
                check_logic_game()

        if event.type == pygame.QUIT:
            is_running = False
        if event.type == pygame.USEREVENT: 
            counter -= 1
            text = str(counter).rjust(3) if counter > 0 else False




        
            

    window_surface.blit(background, (0, 0))
    window_surface.blit(font.render(text, True, (0, 0, 0)), (600, 20))

    window_surface.blit(font.render(str(board[0]), True, (0, 0, 0)), (200, 100))
    window_surface.blit(font.render(str(board[1]), True, (0, 0, 0)), (200, 200))
    window_surface.blit(font.render(str(board[2]), True, (0, 0, 0)), (200, 300))
    window_surface.blit(font.render(str(board[3]), True, (0, 0, 0)), (200, 400))
    window_surface.blit(font.render(str(board[4]), True, (0, 0, 0)), (200, 500))
    pygame.display.update()
    pygame.display.flip()
    clock.tick(60)

