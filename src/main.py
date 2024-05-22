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
            
            #Show the last move on the screen
            game.show_last_move(screen)

            #Code for showing the moves on the screem
            game.show_moves(screen)

            #Code for showing the pieces on the board
            game.show_piece(screen)

            #Code for showing hovering motion
            game.show_hover(screen)

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

                        #Checking if the clicked piece is of valid colour
                        if piece.colour == game.next_player:

                            #Calculate the possible moves
                            board.calc_moves(piece,clicked_row,clicked_col)
                            
                            #Save the initial position of the piece
                            dragger.save_initial(event.pos)
                            dragger.drag_piece(piece)

                            #show method
                            game.show_bg(screen)
                            game.show_last_move(screen)
                            game.show_moves(screen)
                            game.show_piece(screen)

                #Mouse Motion 
                elif event.type == pygame.MOUSEMOTION:

                    #Creating a hovering motion
                    motion_row = event.pos[1] // SQSIZE
                    motion_col = event.pos[0] // SQSIZE

                    #Setting the hovered 
                    game.set_hovered(motion_row, motion_col)

                    if dragger.dragging:

                        dragger.update_mouse(event.pos)

                        game.show_bg(screen)
                        game.show_last_move(screen)
                        game.show_moves(screen)
                        game.show_hover(screen)
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

                            #Check if the piece was captured or not 
                            captured = board.squares[released_row][released_col].has_piece()

                            #Updating the board
                            board.move(dragger.piece, move)

                            #Play the sound
                            game.play_sound(captured)

                            #Upadte the graphics/show methods
                            game.show_bg(screen)

                            #Showing the last move on the screen
                            game.show_last_move(screen)

                            #Showing the pieces on the screen
                            game.show_piece(screen)

                            #Updating the next player
                            game.next_turn()

                    #We want this to be the last line for this elif sentence
                    dragger.undrag_piece(piece)
                
                #Code for changing the theme
                elif event.type == pygame.KEYDOWN:

                    #Changing the theme 
                    if event.key == pygame.K_t:
                        
                        #Change the theme 
                        game.change_theme()

                    if event.key == pygame.K_r:
                
                        #Reset the games
                        game.reset()

                        #We wanna reset the values 
                        game = self.game
                        board = self.game.board
                        dragger = self.game.dragger


                #Code to exit the game
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            
            #Make sure this is the last line of code in this function. This updates the display
            pygame.display.update()

if __name__ == "__main__":
    main = Main()
    main.mainloop()

