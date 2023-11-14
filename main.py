# --external modules--
from screeninfo import get_monitors

# -- screens --
from menu import *
from modules import *

# -- setup --
monitor = get_monitors()[0]
size = width, height = monitor.width, monitor.height

pygame.init()
win = pygame.display.set_mode(size, pygame.FULLSCREEN)

# setting screen to menu
#with open("gamedata.dat", "r") as file:
#    full = file.read()
#    current = full.split()[1].split("=")[1]
#    full = full.replace(current, "menu")
#with open("gamedata.dat", "w") as file:
#    file.write(full)

# storing the possible windows with a text identifier to retrieve from the text file
windows = {
    "menu": lambda: menu(win, size),
    "modules": lambda: selection(win, size)
}


# --mainloop--
if __name__ == "__main__":
    running = True
    while running:

        # runs the current selected window in gamedata.dat
        with open('gamedata.dat', 'r+') as data:
            current = data.readlines()[1].split("=")
            window = current[1]
            window=window.replace("\n", "")

            run = windows[window]
            run()

            data.close()

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
