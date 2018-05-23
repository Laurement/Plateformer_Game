#!/usr/env/bin python3

import pygame
import os
current_path = os.path.dirname(__file__)
resource_path = os.path.join(current_path, 'images')
player = os.path.join(resource_path, 'players')
elements = os.path.join(resource_path, 'elements')
background = os.path.join(resource_path, 'background')


class Platforms(pygame.sprite.Sprite):

    def __init__(self, x, y, w, h):
        pygame.sprite.Sprite.__init__(self)
        floorMid = pygame.image.load(os.path.join(elements, "cakeMid.png")).convert_alpha()
      #  self.image = pygame.Surface((w, h))
      #  self.image.fill(floorMid)
        self.image = floorMid
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y