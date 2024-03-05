import pygame

'''
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()
            print(mouse_pos)

if event.type == pygame.QUIT:
    running = False

    if mouse_pos[0 > 0] and mouse_pos[0]/5:
        user_x = 0
        print("user_x", user_x)
'''

background_colour = (255, 200, 200)

width = 600
height= 600
padding_x = (width - 400)/2
padding_y = (height - 400)/2
screen = pygame.display.set_mode((width, height))

# Set the caption of the screen
pygame.display.set_caption('Geeksforgeeks')

# Fill the background colour to the screen
screen.fill(background_colour)

# Update the display using flip
pygame.display.flip()

running = True
user_x =0
user_y =0
while running:
    # for loop through the event queue
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()
            x = round((mouse_pos[0]-padding_x)/(400/4))
            y = round((mouse_pos[1]-padding_y)/(400/4))

            if(x>=0 and x <=4 and y >= 0 and y<=4):
                print(x,y)



            # if mouse_pos[0] > 0 and mouse_pos[0] < width / 5:
            #     user_x = 0
            #     print("user_x=", user_x)
            # if mouse_pos[1] > 0 and mouse_pos[1] < height / 5:
            #     user_y = 0
            #     print("user_y=", user_y)
            #
            # if mouse_pos[0] > width / 5 and mouse_pos[0] < width / 4:
            #     user_x = 1
            #     print("user_x=", user_x)
            #
            # if mouse_pos[1]  > height / 5  and mouse_pos[1] < height / 4:
            #     user_y = 1
            #     print("user_y=", user_y)

      # Check for QUIT event
        if event.type == pygame.QUIT:
            running = False