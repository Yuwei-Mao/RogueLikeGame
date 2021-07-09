import random
import pygame
from views import weaponview


class Weapon(weaponview.attack):

    def __init__(self, type, attack, cooldown, distance, x, y):
        '''
            type - type of the weapon(e.g. sword)
            attack - damage a weapon causes
            cooldown- time interval between two continuous attacks. impacts dps of a weapon
        '''
        super().__init__(type, distance, x, y)
        self.type = type
        self.attack = attack
        self.cooldown = cooldown

    def cool_down(self):
        pass


class Sword(Weapon):
    def __init__(self, x, y):
        Weapon.__init__(self, "sword", 5, 2, 10, x, y)

    def attack(self, surface):
        weaponview.attack.straight_attack(self, surface)


# class Wand(Weapon):
#     def __init__(self, x, y):
#         Weapon.__init__(self, "wand", 9, 6)
#
#
# class Spear(Weapon):
#     def __init__(self, x, y):
#         Weapon.__init__(self, "spear", 6, 3)
#
#
# class Axe(Weapon):
#     def __init__(self, x, y):
#         Weapon.__init__(self, "axe", 8, 5)


class Hammer(Weapon):
    def __init__(self, x, y):
        Weapon.__init__(self, "hammer", 9, .8, 5, x, y)


def roll_3_dice():
    total = 0
    for _ in range(3):
        total += random.randrange(1, 4)
    return total
