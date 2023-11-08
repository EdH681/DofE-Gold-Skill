import pygame
from screeninfo import get_monitors

monitor = get_monitors()[0]
size = width, height = monitor.width, monitor.height

pygame.init()
win = pygame.display.set_mode(size)


if __name__ == "__main__":
    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
