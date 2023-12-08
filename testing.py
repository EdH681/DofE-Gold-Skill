import pygame

'''
For any function which needs testing before it is fully implemented
'''




x, y = 500, 500
map_width = 5000
map_height = 5000
backx, backy = -map_width/2, -map_height/2
background = pygame.image.load("background.png")
background = pygame.transform.scale(background, (map_width, map_height))


def movement(surface, x, y, backx, backy):
    global background



    background = pygame.image.load("background.png")
    background = pygame.transform.scale(background, (map_width, map_height))
    surface.fill("blue")
    surface.blit(background, (backx, backy))
    speed = 10

    xBorder = 200
    yBorder = 200

    # moving around within map
    key = pygame.key.get_pressed()
    if key[pygame.K_UP]:
        y -= speed
        print("up")
    if key[pygame.K_DOWN]:
        y += speed
    if key[pygame.K_LEFT]:
        x -= speed
    if key[pygame.K_RIGHT]:
        x += speed

    # moving bg image when the border is reached to move off map
    if x <= xBorder and key[pygame.K_LEFT]:
        x = xBorder
        backx += speed
    if x >= 1920-xBorder and key[pygame.K_RIGHT]:
        x = 1920-xBorder
        backx -= speed
    if y <= yBorder and key[pygame.K_UP]:
        y = yBorder
        backy += speed
    if y >= 1080-yBorder and key[pygame.K_DOWN]:
        y = 1080-yBorder
        backy -= speed
    pygame.draw.rect(surface, "red", (x, y, 10, 10))


    return x, y, backx, backy


def testing(surface):
    global x, y, backx, backy
    x, y, backx, backy = movement(surface, x, y, backx, backy)
