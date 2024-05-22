
import os

class Piece :

    def __init__(self, name, colour, value: float, texture = None, texture_rect = None) -> None:
        
        #Define the colour and name of the piece
        self.name = name
        self.colour = colour

        #Define the value of the piece depending on the colour
        value_sign = 1 if colour == "white" else -1 
        self.value = value * value_sign

        #Defining the variable for if a piece is moved or not and what moves are avialable
        self.moves = []
        self.moved = False

        #Setting the texture 
        self.texture =texture
        self.set_texture()
        self.texture_rect = texture_rect

    def set_texture(self, size: int =80) -> None:

        #Adding the texture of the piece and adding the path
        self.texture=os.path.join(
            f'assets/images/imgs-{size}px/{self.colour}_{self.name}.png'
        )

    def add_move(self, move) -> None:

        #Appending the moves that can be played
        self.moves.append(move)

    def clear_moves(self):
        
        #Setting the moves to be empyt
        self.moves=[]

#/home/yash/Documents/ChessRepo/assets/images/imgs-128px/black_rook.png
#Below are the class for every piece in the game

class Pawn(Piece) :

    def __init__(self, colour) -> None:

        #The pawn need a direction based on their colour so we just specificed the direction
        self.dir = -1 if colour == 'white' else 1

        super().__init__('pawn', colour, 1.0 )

class Knight(Piece):

    def __init__(self, colour) -> None:

        super().__init__('knight', colour, 3.0 )

class Bishop(Piece):

    def __init__(self, colour) -> None:

        super().__init__('bishop', colour, 3.001 )
        
class Rook(Piece):

    def __init__(self, colour) -> None:

        super().__init__('rook', colour, 5.0 )

class Queen(Piece):

    def __init__(self, colour) -> None:

        super().__init__('queen', colour, 9.0 )

class King(Piece):

    def __init__(self, colour) -> None:

        super().__init__('king', colour, float(1e6) )