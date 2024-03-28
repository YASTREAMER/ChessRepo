#importing all the necessary files

import pygame
import sys

from const import *
from game import Game


class Main:

    def __init__(self) -> None:
        #Initializing pygame method
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
        dragger = self.game.dragger

        #The main Game loop
        while True:

            #Code for displaying the board 
            self.game.show_bg(screen)

            #Code for showing the pieces on the board
            self.game.show_piece(screen)

            #Loop for all the event in pygame
            for event in pygame.event.get():

                #On Mouse Click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pass

                #Mouse Motion 
                elif event.type == pygame.MOUSEMOTION:
                    pass

                #On Mouse Release
                elif event.type == pygame.MOUSEBUTTONUP:
                    pass
                
                #Code to exit the game
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            
            #Make sure this is the last line of code in this function. This updates the display
            pygame.display.update()

if __name__ == "__main__":
    main = Main()
    main.mainloop()

