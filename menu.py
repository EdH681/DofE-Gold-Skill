import pygame

'''
To do:
- settings button 
- complete assets and update buttons
'''


# the button to begin playing
def play_button(surface, colour, size, screensize, mouse, clicked):
    width, height = size, size
    x =(screensize[0]/2) - (width/2)
    y =(screensize[1]/2) - (height/2)
    play = pygame.draw.rect(surface, colour, (x, y, width, height), 1)

    if play.collidepoint(mouse) and clicked:
        with open("gamedata.dat", "r") as data:
            full = data.read()
            current = full.split()[1].split("=")[1]
            print(current)
            full = full.replace(current, "modules")
        with open("gamedata.dat", "w") as file:
            file.write(full)


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

    mousePos = pygame.mouse.get_pos()
    LMB = pygame.mouse.get_pressed()[0]

    play_button(surface, 'red', 300, screensize, mousePos, LMB)
    character_change(surface, 'red', 200, screensize)
    stats_viewer(surface, 'red', 200, screensize)
    pygame.display.update()
