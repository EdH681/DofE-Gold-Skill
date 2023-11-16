import pygame

'''
To do:
- Create assets and update buttons
'''


def level_check(compare):
    levels = ["bronze", "silver", "gold"]
    with open("gamedata.dat", "r") as file:
        tiers = file.readlines()[2:5]
        status = []
        for tier in tiers:
            status.append(tier.split("=")[1].replace("\n", ""))

        for i in range(len(status)):
            if status[i] == "active":
                return levels[i] == compare


def bronze(surface, colour, screensize, mouse, click):
    width = screensize[0]/2
    height = screensize[1]/5

    x = screensize[0]/2 - width/2
    y = 50 + height + screensize[0]*(10/1920)

    full = 1
    if level_check("bronze"):
        full = 0

    bronzeButton = pygame.draw.rect(surface, colour, (x, y, width, height), full)
    if click and bronzeButton.collidepoint(mouse) and level_check("bronze"):
        print("bronze")


def silver(surface, colour, screensize, mouse, click):
    width = screensize[0]/2
    height = screensize[1]/5

    x = screensize[0]/2 - width/2
    y = 50 + (height*2) + screensize[0]*(10/1920)*2

    full = 1
    if level_check('silver'):
        full = 0

    silverButton = pygame.draw.rect(surface, colour, (x, y, width, height), full)
    if click and silverButton.collidepoint(mouse) and level_check("silver"):
        print("silver")


def gold(surface, colour, screensize, mouse, click):
    width = screensize[0]/2
    height = screensize[1]/5

    x = screensize[0]/2 - width/2
    y = 50 + (height*3) + screensize[0]*(10/1920)*3

    full = 1
    if level_check('gold'):
        full = 0

    goldButton = pygame.draw.rect(surface, colour, (x, y, width, height), full)
    if click and goldButton.collidepoint(mouse) and level_check("gold"):
        print("gold")


# the part that runs
def selection(surface, screensize=(1920, 1080)):
    surface.fill("black")
    mousepos = pygame.mouse.get_pos()
    LMB = pygame.mouse.get_pressed()[0]
    bronze(surface, 'red', screensize, mousepos, LMB)
    silver(surface, 'red', screensize, mousepos, LMB)
    gold(surface, 'red', screensize, mousepos, LMB)
    pygame.display.update()
