
import pygame

from const import *
from board import Board
from dragger import Dragger

class Game:

    def __init__(self) -> None:
        
        self.board = Board()
        self.dragger = Dragger() 

    #Show methods

    #This is to draw the graphic board 
    def show_bg(self, surface) -> None:

        for row in range(ROWS):
            for col in range(COLS):

                if( (row+col) % 2 == 0):

                    # Light green colour
                    colour = ( 234, 235,200) 
                
                else:

                    # Dark green colour
                    colour = ( 119, 154, 88) 

                rect = (col * SQSIZE, row * SQSIZE, SQSIZE, SQSIZE )

                #Drew a rectangle in pygame
                pygame.draw.rect(surface, colour, rect)

    # This is to draw the pieces on the board
    def show_piece(self, surface) -> None:

        for row in range(ROWS):
            for col in range(COLS):

                #Check if there is a piece on the square
                if self.board.squares[row][col].has_piece():

                    piece = self.board.squares[row][col].piece

                    #Loading the Texture of the piece 
                    img = pygame.image.load(piece.texture)

                    #Center the piece on the board based on the row and column
                    img_center = col * SQSIZE + SQSIZE // 2, row * SQSIZE + SQSIZE // 2
                    piece.texture_rect = img.get_rect(center = img_center)

                    surface.blit(img, piece.texture_rect)


