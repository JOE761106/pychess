######-------setup for the screen 
import pygame
pygame.init()
###sets the size of screen 1080 pixels of width (X) and 800 pixels of hight (y)
screen = pygame.display.set_mode((1080 , 800))
run = True
####

while run:
    #### -----------------------------#################
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            run = False
    ####---  ^handles event when user clicks on x button to close the screen----------#######
        board = pygame.image.load("chess_board.png") #loads the image 'board.png'
        board = pygame.transform.scale(board, (1080, 800))# sets the size of board.png

        screen.fill((30, 30, 30))  #fills the screen with color rgb code is 30 30 30

    screen.blit(board, (0, 0))#places the board on  x=0 and y=0
    



    
    pygame.display.flip()#displays the things that were put on screen
pygame.quit()
