#!/usr/bin/env python3


# This way pygame doesn't welcome us and conda envs doesn't print trash
import os, sys
with open(os.devnull, 'w') as dev_null:
    std_out, std_err = sys.stdout, sys.stderr
    sys.stdout, sys.stderr = dev_null, dev_null
    import pygame
    sys.stdout, sys.stderr = std_out, std_err


def main_ex() -> None:
    background = (0, 0, 0)
    width, height = 1280, 720
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Turtle')

    running = True
    while running:
        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # draw
        screen.fill(background)
        pygame.draw.circle(screen, (255, 0, 0), (width / 2, height / 2), 100)

        pygame.display.flip()



if __name__ == '__main__':
    pygame.init()
    main_ex()
    pygame.quit()
