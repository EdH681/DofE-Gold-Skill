# --external modules--
import pygame
from screeninfo import get_monitors

# -- screens --
from menu import *

# -- setup values --
monitor = get_monitors()[0]
size = width, height = monitor.width, monitor.height

pygame.init()
win = pygame.display.set_mode(size, pygame.FULLSCREEN)

# storing the possible windows with a text identifier to retrieve from the text file
windows = {
    'menu': lambda: menu(win, size)
}


# --mainloop--
if __name__ == "__main__":
    running = True
    while running:

        with open('gamedata.dat', 'r+') as window:
            current = window.readlines()[1].split("=")
            display = current[1]

            run = windows[display]
            run()

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
