import pygame
from pygame.math import Vector2 as PVector

import Station_Class
import Master_Class

import random


class EVA():

    def __init__(self, width, height, surface, charging_Station: Station_Class, master: Master_Class):
        self.master = master
        self.charging_Station = charging_Station
        self.win = surface

        self.facing = PVector.from_polar((10, 0))

        self.pos = PVector(random.random()*(width - 10) + 5,
                           random.random()*(height - 10) + 5)
        # self.pos = PVector(width/2, height/2)
        self.vel = PVector(0, 0)
        self.accel = PVector(0, 0)

        self.max_speed = 10

        self.battery = 100

    # Functions for EVA movement
    def control_EVA(self):
        keys = pygame.key.get_pressed()
        sum = PVector(0, 0)

        if keys[pygame.K_LEFT]:
            # eva.moveWith(PVector(-1,0))
            sum += PVector(-1, 0)

        if keys[pygame.K_UP]:
            # eva.moveWith(PVector(0,-1))
            sum += PVector(0, -1)

        if keys[pygame.K_RIGHT]:
            # eva.moveWith(PVector(1,0))
            sum += PVector(1, 0)

        if keys[pygame.K_DOWN]:
            # eva.moveWith(PVector(0,1))
            sum += PVector(0, 1)

        self.moveWith(sum)

        # if not True in keys:
        #    eva.moveWith(PVector(0,0))

    def stop(self):
        self.vel = (0, 0)

    def moveWith(self, vel: PVector):
        self.vel = vel

        # multiply the speed
        if self.vel.length() != 0:
            self.vel.scale_to_length(self.max_speed)

    # Functions to run it in the simulation in pygame
    def update(self):
        self.pos += self.vel
        self.vel += self.accel

    def draw(self):
        pygame.draw.circle(self.win, (0, 255, 0), self.pos, 10)
        pygame.draw.line(self.win, (255, 255, 255),
                         self.pos, self.pos + self.facing)

    def run(self):
        # set updating states
        distance_vector: PVector = self.charging_Station.getPos() - self.pos
        self.batteryUpdate(distance_vector)

        self.control_EVA()

        self.control_overrides(distance_vector)
        self.draw()

        # debug
        print(self.battery)

    # Behaviour logic functions
    def batteryUpdate(self, distance_vector: PVector):
        if distance_vector.length() < 10 and self.battery <= 100:
            self.battery += 1
        else:
            self.battery -= 1

    def control_overrides(self, distance_vector: PVector):
        # battery low override
        if self.battery < 30:
            self.seek_recharge(distance_vector)
        else:
            self.update()

    def seek_recharge(self, distance_vector: PVector):
        if distance_vector.length() > 10:
            # print(self.pos)
            # print(distance_vector.length())

            distance_vector.scale_to_length(self.max_speed)
            self.moveWith(distance_vector)
            self.update()
