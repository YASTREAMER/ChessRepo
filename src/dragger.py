
import pygame

from const import *

class Dragger:

    def __init__(self) -> None:

        #Type of the piece clicked
        self.piece = None

        self.dragging = False
        
        #Position of the mouse
        self.MouseX: int = 0
        self.MouseY: int  = 0

        #The initial row and col 
        self.initial_row: int = 0
        self.initial_col: int = 0

    #Blit methods 

    def update_blit(self, surface) -> None:

        #Size =128 because we want the piece to bigger when dragging
        self.piece.set_texture(size=128)
        texture =self.piece.texture

        #image
        img = pygame.image.load(texture)

        #Centring the piece
        img_center = ( self.MouseX, self.MouseY)
        self.piece.texture_rect = img.get_rect( center = img_center )

        #blit
        surface.blit(img, self.piece.texture_rect)

    #Pther Methods

    def update_mouse(self, pos) -> None:
        self.MouseX, self.MouseY = pos

    def save_initial(self, pos ) -> None:
        self.initial_row = pos[1] // SQSIZE 
        self.initial_col = pos[0] // SQSIZE 

    def drag_piece(self, piece) -> None:
        self.piece = piece
        self.dragging = True

    def undrag_piece(self, piece) -> None:
        self.piece = None
        self.dragging = False