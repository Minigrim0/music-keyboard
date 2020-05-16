import pygame
from pygame.locals import *

class Button(object):

    def __init__(self, pos, size, image, imageOFF=None, isBinnary=False):
        self.position = pos
        self.size = size
        self.images = [imageOFF, image]
        self.isOn = False
        self.isBinnary = isBinnary
        self.rect = pygame.Rect(self.position, self.size)

    def draw(self, screen):
        screen.blit(self.images[int(self.isOn)], self.position)

    def collide(self, position):
        if self.rect.collidepoint(position):
            if self.isBinnary:
                self.isOn = not self.isOn
            return True
        return False

    def toggle(self):
        self.isOn = not self.isOn

    def getValue(self):
        return self.isOn
