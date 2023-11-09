# --external modules--
import pygame
from screeninfo import get_monitors

# --screens--
from menu import *

monitor = get_monitors()[0]
size = width, height = monitor.width, monitor.height

pygame.init()
win = pygame.display.set_mode(size, pygame.FULLSCREEN)


# --mainloop--
if __name__ == "__main__":
    running = True
    while running:

        menu(win)

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
