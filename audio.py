import os
import pygame

def play_music(file_name):
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(file_name)
    pygame.mixer.music.play(-1)  
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

if __name__ == "__main__":
    file_name = "sigma.mp3"
    current_directory = os.path.dirname(__file__)
    file_path = os.path.join(current_directory, file_name)
    play_music(file_path)
