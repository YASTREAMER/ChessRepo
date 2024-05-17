
import pygame

class Sound:
    
    def __init__(self, path) -> None:
        
        self.path =path
        
        #Creating a object for sound
        self.sound = pygame.mixer.Sound(path)

    def play(self) -> None:
        
        #Playing the sound 
        pygame.mixer.Sound.play(self.sound)
        pass