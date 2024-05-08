import pygame
from settings import *

class Camera(pygame.sprite.Group):
  def __init__(self, scene):

    self.offset = vec()
    self.visible_window = pygame.FRect(0,0, WIDTH, HEIGHT)
    self.delay = 2

  def update(self, dt, target):
    mouse = pygame.mouse.get_pos()

    # generates a delay to the camera
    self.offset.x = -target.rect.centerx + WIDTH/2
    self.offset.y = -target.rect.centery + HEIGHT/2

    # camera follows the player
    self.visible_window.x =  -self.offset.x
    self.visible_window.y =  -self.offset.y  

  def draw(self, screen, group):
    screen.fill(COLORS['blue'])
    # group.draw(screen)
    for sprite in group:
      if self.visible_window.colliderect(sprite.rect):
        offset = sprite.rect.topleft + self.offset
        screen.blit(sprite.image, offset)