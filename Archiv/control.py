import sys
import pygame

pygame.init()


class Control:

    def __init__(self):

        self.pressed_Key = None

    def keyboard(self):

        loop = True

        while loop:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                pressed = pygame.key.get_pressed()
                if pressed[pygame.K_UP]:
                    self.pressed_Key = pygame.key.get_pressed()

        return self.pressed_Key


