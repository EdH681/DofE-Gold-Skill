import pygame

'''
For any function which needs testing before it is fully implemented
'''


def movement(surface, x, y):

    surface.fill("black")
    xBorder = 100
    yBorder = 100

    key = pygame.key.get_pressed()
    if key[pygame.K_UP]:
        y -= 1
    if key[pygame.K_DOWN]:
        y += 1
    if key[pygame.K_LEFT]:
        x -= 1
    if key[pygame.K_RIGHT]:
        x += 1

    if x <= xBorder and key[pygame.K_LEFT]:
        x = xBorder
        print("left")
    if x >= 1920-xBorder and key[pygame.K_RIGHT]:
        x = 1920-xBorder
        print("right")
    if y <= yBorder and key[pygame.K_UP]:
        y = yBorder
        print("up")
    if y >= 1080-yBorder and key[pygame.K_DOWN]:
        y = 1080-yBorder
        print("down")

    pygame.draw.rect(surface, "red", (x, y, 10, 10))
    return x, y
