import pygame
__name__ = 'menu'

'''
To do:
- character button
- stats button
- settings button 
- complete assets and update buttons
'''


def play_button(surface, colour, size, screensize):
    width, height = size, size
    x =(screensize[0]/2) - (width/2)
    y =(screensize[1]/2) - (height/2)
    pygame.draw.rect(surface, colour, (x, y, width, height), 1)


def menu(surface, screensize=(1920, 1080)):
    surface.fill('black')
    play_button(surface, 'red', 300, screensize)
    pygame.display.update()
