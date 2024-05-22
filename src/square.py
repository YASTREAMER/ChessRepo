

class Square:
    
    def __init__(self, row, col, piece = None) -> None:

        self.row = row 
        self.col = col
        self.piece = piece
        pass

    def __eq__(self, other) -> bool:
        
        return self.row == other.row and self.col == other.col

    def has_piece(self) -> bool:
        return self.piece != None
    
    def isempty(self) -> bool:
        return not self.has_piece()
    
    #
    def has_enemy_piece(self, colour) -> bool:
        return self.has_piece() and self.piece.colour != colour
    
    def has_team_piece(self, colour) -> bool:
        return self.has_piece() and self.piece.colour == colour

    #Checks if the attacked square is empty or has as enemy piece
    def isempty_or_enemy(self, colour) -> bool:
        return  self.isempty() or self.has_enemy_piece(colour) 
    
    #Defining a static method
    #A static method is one that does no need a object to be created to be called

    @staticmethod
    def in_range(*args) -> bool:

        #*args means that the method can recieve a number of arguments 
        for arg in args:

            #Checking if the move will be inside the board
            if arg < 0 or arg > 7:
                return False
            
        return True
    
    