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
    
    white_pawns = pygame.image.load("white_pawn.png")
    white_pawns = pygame.transform.scale(white_pawns, (100, 100))
    white_pawn_loc = 15
    
    black_pawns = pygame.image.load("black_pawn.png")
    black_pawns = pygame.transform.scale(black_pawns, (100, 100))
    black_pawns = pygame.transform.scale(black_pawns, (100, 100))
    black_pawn_loc =15 

   
    black_knight = pygame.image.load("black_knight.png")
    black_knight = pygame.transform.scale(black_knight, (120, 120))
    
    black_knight2 = pygame.image.load("black_knight.png")
    black_knight2 = pygame.transform.scale(black_knight2, (120, 120))
         

    white_knight = pygame.image.load("white_knight.png")
    white_knight = pygame.transform.scale(white_knight, (120, 120))
    
    white_knight2 = pygame.image.load("white_knight.png")
    white_knight2 = pygame.transform.scale(white_knight2, (120, 120))
    #creates black rook
    rook_height = max(120 , 150)
    black_rook = pygame.image.load("black_rook.png")
    black_rook = pygame.transform.scale(black_rook, (120, rook_height))

    black_rook2 = pygame.image.load("black_rook.png")
    black_rook2= pygame.transform.scale(black_rook, (120, rook_height))

    #creates white rook
    white_rook = pygame.image.load("white_rook.png")
    white_rook = pygame.transform.scale(white_rook, (120, rook_height))
    white_rook2 = pygame.image.load("white_rook.png")
    white_rook2 = pygame.transform.scale(white_rook2, (120, rook_height))

    white_bishop = pygame.image.load("white_bishop.png")
    white_bishop = pygame.transform.scale(white_bishop, (120, 120))
    white_bishop2 = pygame.image.load("white_bishop.png")
    white_bishop2 = pygame.transform.scale(white_bishop2, (120, 120))

    white_queen = pygame.image.load("white_queen.png")
    white_queen = pygame.transform.scale(white_queen, (120, 120))

    white_king = pygame.image.load("white_king.png")
    white_king = pygame.transform.scale(white_king, (120, 120))
    
    black_king = pygame.image.load("black_king.png")
    black_king = pygame.transform.scale(black_king, (120, 120))
    
    black_queen = pygame.image.load("black_queen.png")
    black_queen = pygame.transform.scale(black_queen, (120, 120))

    black_bishop2 = pygame.image.load("black_bishop.png")
    black_bishop2 = pygame.transform.scale(black_bishop2, (120, 120))

    
    black_bishop = pygame.image.load("black_bishop.png")
    black_bishop = pygame.transform.scale(black_bishop, (120, 120))
    
    
    screen.blit(black_king , (550 , -20))
    screen.blit(black_queen , (410 , -20)) 
    screen.blit(black_bishop2 , (280 , -20))
    screen.blit(black_bishop , (680 , -20))
    screen.blit(black_knight2 , (815 , -20))     
    screen.blit(white_king , (550 , 680))
    screen.blit(white_queen , (410 , 680)) 
    screen.blit(white_bishop2 , (280 , 680))
    screen.blit(white_bishop , (680 , 680))
    screen.blit(black_knight2 , (815 , -20))
    screen.blit(white_rook2 , (6 , 670))
    screen.blit(white_knight2 , (820 , 680))
    screen.blit(black_rook2 , (950 , -30))
    screen.blit(white_knight , (140 , 680))
    screen.blit(black_knight , (150 , -20))
    screen.blit(white_rook , (955 , 670))
    screen.blit(black_rook , (5 , -30))
    for i in range(8):
        screen.blit(black_pawns, (black_pawn_loc , 100 ))
        screen.blit(white_pawns, (white_pawn_loc , 600 ))
        black_pawn_loc +=136
        white_pawn_loc +=136 
    pygame.display.set_caption('Pychess')#sets tittle
    icon = pygame.image.load('black_rook.png')#sets icon on window
    pygame.display.set_icon(icon)




    
    pygame.display.flip()#displays the things that were put on screen
pygame.quit()
