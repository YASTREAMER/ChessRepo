#importing all the necessary files

import pygame
import sys

from const import *
from game import Game
from square import Square
from move import Move


class Main:

    def __init__(self) -> None:
        #Initializing pygamge method
        pygame.init()

        #Init the screen
        self.screen = pygame.display.set_mode( (WIDTH,HEIGHT) )

        #Init the caption(window name )
        pygame.display.set_caption("Chess")

        #init the game class
        self.game = Game()
        

    def mainloop(self) -> None:


        game = self.game
        screen = self.screen
        board = self.game.board
        dragger = self.game.dragger

        #The main Game loop
        while True:

            #Code for displaying the board 
            game.show_bg(screen)

            #Code for showing the moves on the screem
            game.show_moves(screen)

            #Code for showing the pieces on the board
            game.show_piece(screen)

            #Code for updating the piece when its being dragged
            if dragger.dragging:
                dragger.update_blit(screen)

            #Loop for all the event in pygame
            for event in pygame.event.get():

                #On Mouse Click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    dragger.update_mouse(event.pos)

                #Checking if the clicked mouse has a piece
                    clicked_row = dragger.MouseY // SQSIZE
                    clicked_col = dragger.MouseX // SQSIZE

                    if board.squares[clicked_row][clicked_col].has_piece():

                        #Save the information of the piece ie the type of piece and its position 
                        piece = board.squares[clicked_row][clicked_col].piece

                        #Calculate the possible moves
                        board.calc_moves(piece,clicked_row,clicked_col)
                        
                        #Save the initial position of the piece
                        dragger.save_initial(event.pos)
                        dragger.drag_piece(piece)

                        #show method
                        game.show_bg(screen)
                        game.show_moves(screen)
                        game.show_piece(screen)

                #Mouse Motion 
                elif event.type == pygame.MOUSEMOTION:

                    if dragger.dragging:

                        dragger.update_mouse(event.pos)

                        game.show_bg(screen)
                        game.show_moves(screen)
                        game.show_piece(screen)

                        dragger.update_blit(screen)

                #On Mouse Release
                elif event.type == pygame.MOUSEBUTTONUP:
                    
                    #Check is if the piece is being dragged
                    if dragger.dragging:

                        dragger.update_mouse(event.pos)

                        #Setting the released row and released column
                        released_row = dragger.MouseY // SQSIZE
                        released_col = dragger.MouseX // SQSIZE

                        #Check if the move is valid or not 
                        initial = Square(dragger.initial_row, dragger.initial_col)
                        final = Square(released_row, released_col)

                        move = Move(initial, final)

                        #Checking if it is a valid move
                        if board.valid_move(dragger.piece, move):

                            #Updating the board
                            board.move(dragger.piece, move)

                            #Upadte the graphics/show methods
                            game.show_bg(screen)
                            game.show_piece(screen)

                    #We want this to be the last line for this elif sentence
                    dragger.undrag_piece(piece)
                
                #Code to exit the game
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            
            #Make sure this is the last line of code in this function. This updates the display
            pygame.display.update()

if __name__ == "__main__":
    main = Main()
    main.mainloop()

