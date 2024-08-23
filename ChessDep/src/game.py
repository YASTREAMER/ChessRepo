import pygame

from const import *
from board import Board
from dragger import Dragger
from config import Config


class Game:
    def __init__(self) -> None:
        self.board = Board()
        self.dragger = Dragger()

        # Check the next player
        self.next_player = "white"

        # Check the square that is currently being hovered over
        self.hovered_sqr = None

        self.config = Config()

    # Show methods

    # This is to draw the graphic board
    def show_bg(self, surface) -> None:
        # loading the theme to be used
        theme = self.config.theme

        for row in range(ROWS):
            for col in range(COLS):
                # Setting the colour of the square
                colour = theme.bg.light if (row + col) % 2 == 0 else theme.bg.dark

                # recr
                rect = (col * SQSIZE, row * SQSIZE, SQSIZE, SQSIZE)

                # Drew a rectangle in pygame
                # blit
                pygame.draw.rect(surface, colour, rect)

    # This is to draw the pieces on the board
    def show_piece(self, surface) -> None:
        for row in range(ROWS):
            for col in range(COLS):
                # Check if there is a piece on the square
                if self.board.squares[row][col].has_piece():
                    piece = self.board.squares[row][col].piece

                    # Loading the Texture of the piece
                    img = pygame.image.load(piece.texture)

                    # Showing all the piece except the one being dragger
                    if piece is not self.dragger.piece:
                        # Setting the texture back to the original texture
                        piece.set_texture(size=80)

                        # Center the piece on the board based on the row and column
                        img_center = (
                            col * SQSIZE + SQSIZE // 2,
                            row * SQSIZE + SQSIZE // 2,
                        )
                        piece.texture_rect = img.get_rect(center=img_center)

                        surface.blit(img, piece.texture_rect)

    def show_moves(self, surface) -> None:
        theme = self.config.theme

        # Check for the piece we are dragging
        if self.dragger.dragging:
            # store the piece in the piece
            piece = self.dragger.piece

            # Looping for the valid moves
            for move in piece.moves:
                # colour
                colour = (
                    theme.moves.light
                    if (move.final.row + move.final.col) % 2 == 0
                    else theme.moves.dark
                )

                # rect
                rect = (
                    move.final.col * SQSIZE,
                    move.final.row * SQSIZE,
                    SQSIZE,
                    SQSIZE,
                )

                # blit
                pygame.draw.rect(surface, colour, rect)

    def show_last_move(self, surface) -> None:
        theme = self.config.theme

        # Checking if their is a last move
        if self.board.last_move:
            initial = self.board.last_move.initial
            final = self.board.last_move.final

            # Looping for the initial and final move
            for pos in [initial, final]:
                # colour
                colour = (
                    theme.trace.light
                    if (pos.row + pos.col) % 2 == 0
                    else theme.trace.dark
                )

                # rect
                rect = (pos.col * SQSIZE, pos.row * SQSIZE, SQSIZE, SQSIZE)

                # blit
                pygame.draw.rect(surface, colour, rect)

    def show_hover(self, surface) -> None:
        # Checking if their is a last move
        if self.hovered_sqr:
            # colour
            colour = (180, 180, 180)
            # rect
            rect = (
                self.hovered_sqr.col * SQSIZE,
                self.hovered_sqr.row * SQSIZE,
                SQSIZE,
                SQSIZE,
            )

            # blit
            pygame.draw.rect(surface, colour, rect, width=3)

    # Other methods
    def next_turn(self) -> None:
        # Changes the next player
        self.next_player = "white" if self.next_player == "black" else "black"

    def set_hovered(self, row, col) -> None:
        self.hovered_sqr = self.board.squares[row][col]

    def change_theme(self) -> None:
        self.config.change_theme()

    def play_sound(self, captured=False) -> None:
        if captured:
            self.config.capture_sound.play()

        else:
            self.config.move_sound.play()

    def reset(self) -> None:
        # Reset the game
        self.__init__()
