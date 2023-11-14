import pygame
__name__ = 'menu'

'''
To do:
- settings button 
- complete assets and update buttons
'''


# the button to begin playing
def play_button(surface, colour, size, screensize):
    width, height = size, size
    x =(screensize[0]/2) - (width/2)
    y =(screensize[1]/2) - (height/2)
    play = pygame.draw.rect(surface, colour, (x, y, width, height), 1)


# the button to open the character customisation screen
def character_change(surface, colour, size, screensize):
    width, height = size, size
    x = (screensize[0]/2) - (width/2) - (size * 1.5)
    y = (screensize[1] / 2) - (size/2)
    character = pygame.draw.rect(surface, colour, (x, y, width, height), 1)


# the button to open the stats viewer screen
def stats_viewer(surface, colour, size, screensize):
    width, height = size, size
    x = (screensize[0]/2) - (width/2) + (size * 1.5)
    y = (screensize[1] / 2) - (size/2)
    stats = pygame.draw.rect(surface, colour, (x, y, width, height), 1)


# the part that runs
def menu(surface, screensize=(1920, 1080)):
    surface.fill('black')
    play_button(surface, 'red', 300, screensize)
    character_change(surface, 'red', 200, screensize)
    stats_viewer(surface, 'red', 200, screensize)
    pygame.display.update()
