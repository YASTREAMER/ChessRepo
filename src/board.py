
from const import *
from square import Square
from piece import *
from move import *

import pygame
import copy

class Board():

    def __init__(self) -> None:

        #Initializing the squares and creating eight squares for every column
        self.squares = [[0,0,0,0,0,0,0,0] for col in range(COLS)]

        #Initializing the last move 
        self.last_move =  None

        #Checking promotiion
        self.prom:bool = True

        #Initializing the create method
        self._create()
        
        #Initializing the pieces
        self._add_piece('white')
        self._add_piece('black')

    def calc_moves(self, piece, row, col, bool = True) -> None:

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

                    if self.squares[possible_move_row][possible_move_col].isempty_or_enemy(piece.colour):

                        #Create square of the move
                        initial = Square(row, col)
                        final_piece = self.squares[possible_move_row][possible_move_col].piece
                        final = Square(possible_move_row, possible_move_col,final_piece)

                        #Create the move 
                        move = Move(initial, final)

                        if bool:
                            #Checking if the moves cause our king to be in check
                            if not self.in_check(piece, move):
                                #Adding move
                                piece.add_move(move)
                            
                            else:break 

                        else:
                            piece.add_move(move)
        
        #Calcautle the valid moves for a pawn
        def pawn_moves() -> None:
            
            #checking if the pawn has already moved or not 
            steps = 1 if piece.moved else 2

            #Vertical Movement
            #Movement of pawn in vertical direction
            start = row + piece.dir
            end = row + (piece.dir * (1 + steps))

            for possible_move_row in range(start, end, piece.dir):

                #Checking is the piece is in range 
                if Square.in_range(possible_move_row):

                    #Checking if the square in the range of the move is empty
                    if self.squares[possible_move_row][col].isempty():
                        
                        #Create the intital and final move square 
                        initial = Square(row, col)

                        final = Square(possible_move_row,col)

                        #Creating a move 
                        move = Move(initial, final)

                        if bool:
                            #Checking if the moves cause our king to be in check
                            if not self.in_check(piece, move):
                                #Adding move
                                piece.add_move(move)

                        else:
                            piece.add_move(move)

                    else: break

                #Piece not is range
                else: break

            #Diagonal moves
            possible_move_row = row + piece.dir
            possible_move_cols = [col-1, col+1]

            for possible_move_col in possible_move_cols:

                #Checking if the possible move is in range\
                if Square.in_range(possible_move_row,possible_move_col):

                    #Checking if the possible square has a rival pieve
                    if self.squares[possible_move_row][possible_move_col].has_enemy_piece(piece.colour):

                        #Create the intital and final move square 
                        initial = Square(row, col)

                        #Storing the piece on the final move
                        final_piece = self.squares[possible_move_row][possible_move_col].piece

                        final = Square(possible_move_row,possible_move_col,final_piece)

                        #Create a new move
                        move = Move(initial, final)

                        if bool:
                            #Checking if the moves cause our king to be in check
                            if not self.in_check(piece, move):
                                #Adding move
                                piece.add_move(move)

                        else:
                            piece.add_move(move)
                    
        def straightline_moves(incrs) -> None:

            #Looing over all the incrs
            for incr in incrs:

                #Possible increment
                row_incr, col_incr = incr

                possible_move_row = row + row_incr
                possible_move_col = col + col_incr

                while True:
                    if Square.in_range(possible_move_row, possible_move_col):

                        #Creating a new possible move 

                        initial = Square(row, col)
                        final_piece = self.squares[possible_move_row][possible_move_col].piece
                        final = Square(possible_move_row,possible_move_col,final_piece)

                        #Creating a move 
                        move = Move(initial, final)


                        #Checking if the possible squares are empty
                        if self.squares[possible_move_row][possible_move_col].isempty():
                            
                            if bool:
                                #Checking if the moves cause our king to be in check
                                if not self.in_check(piece, move):
                                    #Adding move
                                    piece.add_move(move)

                            else:
                                piece.add_move(move)   
                        
                        #Checking if the possible square has a rival piece
                        elif self.squares[possible_move_row][possible_move_col].has_enemy_piece(piece.colour):
                            
                            #Append the new move
                            if bool:
                            #Checking if the moves cause our king to be in check
                                if not self.in_check(piece, move):
                                    #Adding move
                                    piece.add_move(move)

                            else:
                                piece.add_move(move)
                            break

                        elif self.squares[possible_move_row][possible_move_col].has_team_piece(piece.colour):
                            
                            #Break if the possible square has a team piece
                            break

                    #not in range    
                    else: break

                        #increment the 
                    possible_move_row = possible_move_row + row_incr 
                    possible_move_col = possible_move_col + col_incr

        def king_move():

            #Checking all the eight squares

            # This is very similar to knight moves
            adjs = [
                (row - 1 , col + 0), #Up
                (row - 1 , col + 1), #Up-Right
                (row - 0 , col + 1), #RIght
                (row + 1 , col + 1), #Down-Right
                (row + 1 , col + 0), #Down
                (row + 1 , col - 1), #Down-Left
                (row + 0 , col - 1), #Left
                (row - 1 , col - 1)  #Up-Left
            ]


            #Checking for normal moves and not for casting
            for possible_move in adjs:
                
                #Checking if the move is possible
                possible_move_row, possible_move_col = possible_move
                
                #Check if the move is in range
                if Square.in_range(possible_move_row, possible_move_col):

                    #Checking if the possible square is empty or has an enemy piece
                    if self.squares[possible_move_row][possible_move_col].isempty_or_enemy(piece.colour):

                            #Create square of the move
                            initial = Square(row, col)
                            final = Square(possible_move_row, possible_move_col)

                            #Create the move 
                            move = Move(initial, final)

                            if bool:
                                #Checking if the moves cause our king to be in check
                                if not self.in_check(piece, move):
                                    #Adding move
                                    piece.add_move(move)
                                else:
                                    break

                            else:
                                piece.add_move(move)

            #Castling moves
            if not piece.moved:

                #Queen side castling 
                left_rook = self.squares[row][0].piece

                #Checking if the left row has moved or not 
                if isinstance(left_rook, Rook):
                    if not left_rook.moved:

                        #Checking the board has piece in between the rook and the king
                        for c in range(1,4):

                            if self.squares[row][c].has_piece():
                                #Castling is not possible
                                break

                            if c == 3:
                                
                                #Adding the left rook move to the king move
                                piece.left_rook = left_rook

                                #Rook move
                                initial = Square(row,0 )
                                final = Square(row, 3 )
                                move = Move(initial, final)

                                #Adding the move 
                                left_rook.add_move(move)

                                #King move
                                initial = Square(row,col)
                                final = Square(row, 2)
                                move = Move(initial, final)

                                #Adding the move 
                                piece.add_move(move)

                right_rook = self.squares[row][7].piece

                #Checking if the left row has moved or not 
                if isinstance(right_rook , Rook):
                    if not right_rook.moved:

                        #Checking the board has piece in between the rook and the king
                        for c in range(5,7):

                            if self.squares[row][c].has_piece():
                                #Castling is not possible
                                break

                            if c == 6:
                                
                                #Adding the left rook move to the king move
                                piece.right_rook = right_rook

                                #Rook move
                                initial = Square(row,7)
                                final = Square(row, 5)
                                move = Move(initial, final)

                                #Adding the move 
                                right_rook.add_move(move)

                                #King move
                                initial = Square(row,col)
                                final = Square(row, 6)
                                move = Move(initial, final)

                                #Adding the move 
                                piece.add_move(move)

        #Calculates the valid moves for a piece
        if isinstance(piece, Pawn):

            pawn_moves()

        elif isinstance(piece,Knight):

            knight_moves()

        elif isinstance(piece,Bishop): 
            
            straightline_moves([
                (-1 ,  1), #UpRight
                (-1 , -1), #UpLeft
                ( 1 ,  1), #DownRight
                ( 1 , -1)  #DownLeft
            ])

        elif isinstance(piece,Rook): 

            straightline_moves([
                ( 1 ,  0), #Up
                ( 0 ,  1), #Right
                (-1 ,  0), #Down
                ( 0 , -1)  #Left 

            ])

        elif isinstance(piece,Queen):

            straightline_moves([
                (-1 ,  0), #Up
                ( 0 ,  1), #Right
                ( 1 ,  0), #Down
                ( 0 , -1),  #Left
                (-1 ,  1), #UpRight
                (-1 , -1), #UpLeft
                ( 1 , -1),  #DownLeft
                ( 1 ,  1) #DownRight
            ])

        elif isinstance(piece,King): 

            king_move()

    def move(self, piece, move) -> None:
        
        initial = move.initial
        final = move.final

        #Updating the console board state

        #Setting the initial piece to be none
        self.squares[initial.row][initial.col].piece = None

        #Setting the final squrae to contain the piece
        self.squares[final.row][final.col].piece = piece

        #Checking if the moved piece is a pawn or not
        if isinstance(piece, Pawn):

            #If true we are gonna check for promotion 
            self.check_promotion(piece, final)

        #King castling
        if isinstance(piece,King):

            #Seeing if the condition for the castling are valid 
            if self.castling(initial, final):
                
                #Checking if the difference if less than 0 or more than zero
                diff = final.col - initial.col
                rook = piece.left_rook if (diff <0) else piece.right_rook 

                self.move(rook, rook.moves[-1])

        #Move
        piece.moved = True

        #Clearing the valid move
        piece.clear_moves()

        #Setting the last move to the last move played
        self.last_move = move

    def valid_move(self, piece, move) -> move:
        
        return move in piece.moves
    
    def check_promotion(self, piece , final) -> None:

        #Checking if the row is the last row or not
        if final.row == 0 or final.row == 7:

            prom = True
            
            while prom:

                for event in pygame.event.get():


                    if event.type == pygame.KEYDOWN:

                        if event.key == pygame.K_1:

                            #Promootion
                            self.squares[final.row][final.col].piece = Queen(piece.colour)
                            prom = False
                            break

                        if event.key == pygame.K_2:
                            
                            self.squares[final.row][final.col].piece = Rook(piece.colour)
                            self.prom = False
                            break

                        if event.key == pygame.K_3:

                            self.squares[final.row][final.col].piece = Knight(piece.colour)
                            prom = False
                            break

                        if event.key == pygame.K_4:

                            self.squares[final.row][final.col].piece = Bishop(piece.colour)
                            prom = False
                            break

    def castling(self, initial , final) -> bool:
        
        #Checking if the king has moved by 2 squares
        return abs(initial.col - final.col) == 2
    
    def in_check(self, piece, move) -> bool:

        #Creating a tempory board ie a deep copy of the board
        temp_board = copy.deepcopy(self)

        #Creating a temporay copy of the piece ie deep copy
        temp_piece = copy.deepcopy(piece)

        #Moving the piece on the board
        temp_board.move(temp_piece, move)

        for row in range(ROWS):
            for col in range(COLS):

                 if temp_board.squares[row][col].has_enemy_piece(piece.colour):
                     
                     p = temp_board.squares[row][col].piece 
                     temp_board.calc_moves(p, row,col,False)

                     #Checking if the temporay move cause a king to be underattach
                     for m in p.moves:
                         
                         if isinstance(m.final.piece, King):
                             return True
                         
        return False

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
        