import pygame
from pygame.math import Vector2 as PVector

import random


class Master:
    def __init__(self, width, height, surface):
        self.win = surface

        self.pos = PVector(random.random()*(width - 10) + 5,
                           random.random()*(height - 10) + 5)
        # self.pos = PVector(width/4, height*3/4)

    def getPos(self):
        return self.pos

    def draw(self):
        pygame.draw.circle(self.win, (255, 0, 0), self.pos, 10)
