
import pygame
import os

from sound import Sound
from theme import Theme

class Config:

    def __init__(self) -> None:
        
        #List of themes
        self.themes = []

        #Method to add themes
        self._add_themes()

        #The index of the theme
        self.idx = 0

        #The individual themes
        self.theme = self.themes[self.idx]

        #font

        #The sound to be played when piece is moved 
        self.move_sound = Sound(
            os.path.join('assets/sounds/move.wav'))

        #The sound to be played when a piece is captured
        self.capture_sound = Sound(
            os.path.join('assets/sounds/capture.wav'))       

    def change_theme(self) -> None:
        
        #Changing the index of the theme 
        self.idx += 1

        #Resets the index to be 1 if no more themes are available
        self.idx %= len(self.themes)

        #Setting the theme to 
        self.theme = self.themes[self.idx]


    def _add_themes(self) -> None:
        
        #Adding the themes 
        #The first two are the colour of the square the next two are for the last move and the rest ar for showing valid moves
        green = Theme(( 234, 235,200), ( 119, 154, 88), (244, 247, 116 ), (172 ,195, 51), '#C86464', '#C84646')
        brown = Theme((235, 209, 166), (165, 117, 80), (245, 234, 100), (209, 185, 59), '#C86464', '#C84646')
        blue = Theme((229, 228, 200), (60, 95, 135), (123, 187, 227), (43, 119, 191), '#C86464', '#C84646')
        gray = Theme((120, 119, 118), (86, 85, 84), (99, 126, 143), (82, 102, 128), '#C86464', '#C84646')


        #Adding the theme to the list of themes 
        self.themes = [green, brown, blue, gray]
