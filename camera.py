import pygame
from settings import *

class Camera(pygame.sprite.Group):
  def __init__(self, scene):

    self.offset = vec()
    self.delay = 2

  def update(self, target, dt):
    mouse = pygame.mouse.get_pos()

    self.offset.x = target.rect.centerx - WIDTH/2
    self.offset.y = target.rect.centery - HEIGHT/2

  def draw(self, screen, group):
    screen.fill(COLORS['red'])
    for sprite in group:
      offset = sprite.rect.topleft - self.offset
      screen.blit(sprite.image, offset)