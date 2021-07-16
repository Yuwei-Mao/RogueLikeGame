#! /usr/bin/env python3
import random
from views import itemview
import pygame

""" start items classes """


class Item(itemview.Drop):

    def __init__(self, item, x, y):
        '''
            item - the item that dropped after monster die or randomly
        '''
        itemview.Drop.__init__(self, item, x, y)
        self.item = item

    def __str__(self):
        s = f'Drop items: {self.item}'
        return s

    def effect(self, player):
        pass


class Apple(Item):
    """
        Increase max hp
    """

    def __init__(self, x, y):
        Item.__init__(self, 'apple', x, y)

    def __str__(self):
        pass

    def effect(self, player):
        health_ratio = player.current_health / player.max_health
        player.max_health += 20
        player.current_health = int(player.max_health * health_ratio)


class BloodBottle(Item):
    """
        restore current hp
    """

    def __init__(self, x, y):
        Item.__init__(self, 'blood_bottle', x, y)

    def __str__(self):
        pass

    def effect(self, player):
        player.get_health(player.max_health/4)


class ChickenLeg(Item):
    """
        Increase attack
    """

    def __init__(self, x, y):
        Item.__init__(self, 'chicken_leg', x, y)

    def __str__(self):
        pass

    def effect(self, player):
        player.attack += 2


class Book(Item):
    """
        random effect:
        Increase attack
        upgrade weapon
        restore health
    """

    def __init__(self, x, y):
        Item.__init__(self, 'book', x, y)

    def __str__(self):
        pass

    def effect(self, player):
        r_n = random.randint(1, 4)
        if r_n <= 1:
            player.attack += 2
        elif r_n == 2:
            player.upgrade_weapon()
        elif r_n == 3:
            player.get_health(player.max_health / 4)
        elif r_n == 4:
            player.get_health(player.max_health / 4)


class Bomb(Item):
    """
        Increase attack
    """

    def __init__(self, x, y):
        Item.__init__(self, 'bomb', x, y)

    def __str__(self):
        pass

    def effect(self, player, monster_list):
        for i in monster_list:
            r_n = (abs(self.rect.x - i.rect.x)**2 + abs(self.rect.y - i.rect.y)**2)**0.5
            if r_n <= 350:
                monster_list = player.attack_monster_long_range(pygame.sprite.Group(i), monster_list)
        return monster_list





