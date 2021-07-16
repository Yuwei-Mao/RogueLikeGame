import pygame
import random
import math


class BossV(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.sprites = []
        self.sprites.append(pygame.image.load('image/boss/boss_1.png'))
        self.sprites.append(pygame.image.load('image/boss/boss_2.png'))

        self.updateSpeed = 0.1
        self.current = 0
        self.image = self.sprites[self.current]
        self.rect = self.image.get_rect()
        self.x = self.rect.x
        self.y = self.rect.y

        """ Play ground """
        self.restrictx = 1024
        self.restricty = 0
        self.rand_point_x = random.randint(-20, 20)
        self.rand_point_y = random.randint(-10, 10)
        self.seed_x = random.randint(-15, 15)
        self.seed_y = random.randint(-10, 10)

    def setPlayGround(self, x, y):
        self.restrictx = x
        self.restricty = y

    def walk(self, x, y):
        x += self.seed_x
        y += self.seed_y
        distx = self.x - x
        disty = self.y - y
        diagonal_dist = math.sqrt(distx ** 2 + disty ** 2)

        self.current = (self.current + self.updateSpeed) % len(self.sprites)
        self.image = self.sprites[int(self.current)]
        if diagonal_dist < 300:
            self.approach(distx, disty)
        else:
            self.stroll(x, y)

    def approach(self, distx, disty):
        back = 32
        if self.rect.x <= 0:  # Left
            self.rect.x += back
        if self.rect.x >= self.restrictx - 64:  # Right
            self.rect.x -= back
        if self.rect.y <= self.restricty:  # Up
            self.rect.y += back
        if self.rect.y >= 786 - 64:  # Bottom
            self.rect.y -= back
        if distx > 0:
            self.x -= self.vel
        elif distx <= 0:
            self.x += self.vel
        if disty > 0:
            self.y -= self.vel
        elif disty <= 0:
            self.y += self.vel

    def stroll(self, x, y):
        distx = self.x - self.rand_point_x - x
        disty = self.y - self.rand_point_y - y
        self.approach(distx, disty)
