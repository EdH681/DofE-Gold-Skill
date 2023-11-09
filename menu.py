import pygame
__name__ = 'menu'

'''
This will be the menu screen with:
- a play button
- a character customise button
- a stats viewer button
- a settings button
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
