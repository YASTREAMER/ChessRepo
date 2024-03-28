

class Square:
    
    def __init__(self, row, col, piece = None) -> None:

        self.row = row 
        self.col = col
        self.piece = piece
        pass

    def has_piece(self) -> bool:
        return self.piece != None