
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

    def calc_moves(self, piece, row, col) -> None:

        #Calculate the valid moves for a knight
        def knight_moves() -> None:

            #There are 8 possible moves for a knight if it is unrestriceted if max moves pool = 8 
            possible_moves= [
                (row - 2, col + 1),
                (row - 2, col - 1),
                (row - 1, col + 2),
                (row - 1, col - 2),
                (row + 1, col - 2),
                (row + 1, col + 2),
                (row + 2, col - 1),
                (row + 2, col + 1)
            ]

            #Checiking for the possible moves 
            for possible_move in possible_moves:
                possible_move_row, possible_move_col = possible_move

                #Check if the move is in range
                if Square.in_range(possible_move_row, possible_move_col):
                    if self.squares[possible_move_row][possible_move_col].isempty_or_rival(piece.colour):

                        #Create a new piece
                        pass
        #Calculates the valid moves for a piece
        if isinstance(piece, Pawn):

            pass

        elif isinstance(piece,Knight):
            
            knight_moves()

        elif isinstance(piece,Bishop):
            
            pass

        elif isinstance(piece,Rook):
            
            pass

        elif isinstance(piece,Queen):
            
            pass

        elif isinstance(piece,King):
            
            pass

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