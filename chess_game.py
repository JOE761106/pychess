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
    black_rook = pygame.image.load("black_rook.png")
    rook_height = max(120 , 150)
    black_rook = pygame.transform.scale(black_rook, (120, rook_height))
    screen.blit(black_rook , (5 , -30))
    black_pawn_loc =15 
    black_pawns = pygame.image.load("black_pawn.png")
    black_pawns = pygame.transform.scale(black_pawns, (100, 100))
    
    for i in range(8):
        screen.blit(black_pawns, (black_pawn_loc , 100 ))
        black_pawn_loc +=136
    
    pygame.display.set_caption('Pychess')#sets tittle
    icon = pygame.image.load('black_rook.png')#sets icon on window
    pygame.display.set_icon(icon)




    
    pygame.display.flip()#displays the things that were put on screen
pygame.quit()
