
from const import *
from square import Square
from piece import *

class Board():

    def __init__(self) -> None:

        #Initializing the squares and creating eight squares for every column
        self.squares = [[0,0,0,0,0,0,0,0] for col in range(COLS)]

        #Initializing the create method
        self._create()
        
        #Initializing the pieces
        self._add_piece('white')
        self._add_piece('black')


    #These methods are private methods and are not to be called outside this class
    def _create(self) -> None:
        
        for row in range(ROWS):
            for col in range(COLS):

                self.squares[row][col] = Square(row,col)
    


    def _add_piece(self, colour) -> None:
        
        #Adding the pieces on the board
        row_pawn, row_other = (6, 7) if colour =='white' else (1, 0) 

        #Adding the pawns to the board
        for col in range(COLS):
            self.squares[row_pawn][col] = Square(row_pawn, col, Pawn(colour))

        #Adding the knight to the board   
        self.squares[row_other][1] = Square(row_other, 1, Knight(colour))
        self.squares[row_other][6] = Square(row_other, 6, Knight(colour))

        #Adding the bishop to the board   
        self.squares[row_other][2] = Square(row_other, 2, Bishop(colour))
        self.squares[row_other][5] = Square(row_other, 5, Bishop(colour))

        #Adding the rooks to the board   
        self.squares[row_other][0] = Square(row_other, 0, Rook(colour))
        self.squares[row_other][7] = Square(row_other, 7, Rook(colour))

        #Adding the queen to the board   
        self.squares[row_other][3] = Square(row_other, 3, Queen(colour))

        #Adding the king to the board   
        self.squares[row_other][4] = Square(row_other, 4, King(colour))