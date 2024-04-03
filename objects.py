import pygame
from settings import *

class Object(pygame.sprite.Sprite):
  def __init__(self, groups, pos, surf=pygame.Surface((TILESIZE, TILESIZE))):
    super().__init__(groups)

    self.image = surf
    self.rect = self.image.get_rect(topleft=pos)
    self.hitbox = self.rect.copy().inflate(0,0)

  