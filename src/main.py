#importing all the necessary files

import pygame
import sys

from const import *
from game import Game


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
            self.game.show_bg(screen)

            #Code for showing the pieces on the board
            self.game.show_piece(screen)

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
                        dragger.save_initial(event.pos)
                        dragger.drag_piece(piece)

                #Mouse Motion 
                elif event.type == pygame.MOUSEMOTION:

                    if dragger.dragging:

                        dragger.update_mouse(event.pos)
                        game.show_bg(screen)
                        game.show_piece(screen)
                        dragger.update_blit(screen)

                #On Mouse Release
                elif event.type == pygame.MOUSEBUTTONUP:
                    
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

