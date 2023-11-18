import pygame

'''
For any function which needs testing before it is fully implemented
'''


def movement(surface, x, y, backx, backy):

    background = pygame.image.load("background.jpg")
    background = pygame.transform.scale(background, (10000, 5000))
    surface.blit(background, (backx, backy))

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
        backx += 1
    if x >= 1920-xBorder and key[pygame.K_RIGHT]:
        x = 1920-xBorder
        backx -= 1
    if y <= yBorder and key[pygame.K_UP]:
        y = yBorder
        backy += 1
    if y >= 1080-yBorder and key[pygame.K_DOWN]:
        y = 1080-yBorder
        backy -= 1
    pygame.draw.rect(surface, "red", (x, y, 10, 10))
    return x, y, backx, backy


def testing(surface):
    return movement(surface)
