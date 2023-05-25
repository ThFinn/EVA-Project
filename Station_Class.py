import pygame
from pygame.math import Vector2 as PVector

import random


class Station:
    def __init__(self, width, height, surface):
        self.win = surface

        self.pos = PVector(random.random()*(width - 40) + 10,
                           random.random()*(height - 40) + 10)

    def getPos(self):
        return self.pos

    # show on simulation
    def draw(self):
        # pygame.draw.rect(self.win, (255, 255, 255), (self.pos.x, self.pos.y, 40, 40))
        pygame.draw.circle(self.win, (255, 255, 255), self.pos, 30)
