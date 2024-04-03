from typing import Iterable
import pygame
from pygame.sprite import AbstractGroup
from settings import *

class Camera(pygame.sprite.Group):
  def __init__(self, scene):

    self.offset = vec()
    self.delay = 2

  def update(self, target, dt):
    pass

  def draw(self, screen, group):
    pass