import pygame
from views import playerview


class attack():

    def __init__(self, type, distance, x, y):
        self.distance = distance
        self.type = type

        self.images = []
        if self.type == "sword":
            self.images.append(pygame.image.load('image/weapons/sword1.png'))
        elif self.type == "axe":
            self.images.append(pygame.image.load('pass'))
        elif self.type == "hammer":
            self.images.append(pygame.image.load('pass'))

        self.current = 0
        self.image = self.images[self.current]
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()

        self.x = x
        self.y = y

    def straight_attack(self, surface):
        increment = self.distance
        reverse = False
        while not reverse and increment >= 0:
            if increment == 0:
                reverse = True
            surface.blit(self.image, (self.x + 5, self.y+50))
            increment -= 1
        while reverse and increment < self.distance:
            self.rect.x -= 1
            surface.blit(self.image, (self.x - 5, self.y+50))
            increment += 1

    # def rotate_attack(self, surf, topleft, angle):
    #     rotated_image = pygame.transform.rotate(self.image, angle)
    #     new_rect = rotated_image.get_rect(center=self.image.get_rect(topleft=topleft).center)
    #
    #     surf.blit(rotated_image, new_rect.topleft)
    #     pygame.draw.rect(surf, (255, 0, 0), new_rect, 2)
    #
    # def blitRotate(surf, image, pos, originPos, angle):
    #     # calcaulate the axis aligned bounding box of the rotated image
    #     w, h = image.get_size()
    #     box = [pygame.math.Vector2(p) for p in [(0, 0), (w, 0), (w, -h), (0, -h)]]
    #     box_rotate = [p.rotate(angle) for p in box]
    #     min_box = (min(box_rotate, key=lambda p: p[0])[0], min(box_rotate, key=lambda p: p[1])[1])
    #     max_box = (max(box_rotate, key=lambda p: p[0])[0], max(box_rotate, key=lambda p: p[1])[1])
    #
    #     # calculate the translation of the pivot
    #     pivot = pygame.math.Vector2(originPos[0], -originPos[1])
    #     pivot_rotate = pivot.rotate(angle)
    #     pivot_move = pivot_rotate - pivot
    #
    #     # calculate the upper left origin of the rotated image
    #     origin = (
    #         pos[0] - originPos[0] + min_box[0] - pivot_move[0], pos[1] - originPos[1] - max_box[1] + pivot_move[1])
    #
    #     # get a rotated image
    #     rotated_image = pygame.transform.rotate(image, angle)
    #
    #     # rotate and blit the image
    #     surf.blit(rotated_image, origin)
    #
    #     # draw rectangle around the image
    #     pygame.draw.rect(surf, (255, 0, 0), (*origin, *rotated_image.get_size()), 2)
