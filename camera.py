import pygame, csv
from settings import *

class Camera(pygame.sprite.Group):
  def __init__(self, scene):

    self.offset = vec()
    self.visible_window = pygame.FRect(0,0, WIDTH, HEIGHT)
    self.scene_size = self.get_scene_size(scene)
    self.delay = 3

  def get_scene_size(self, scene):
    with open('scenes/0/0.csv', newline='') as csvfile:
      reader = csv.reader(csvfile, delimiter=',')
      for row in reader:
        rows = (sum(1 for row in reader) + 1)
        cols = len(row)
    return (cols * TILESIZE, rows * TILESIZE)

  def update(self, dt, target):
    mouse = pygame.mouse.get_pos()

    # makes the camera follow the player and the mouse
    self.offset.x += (-target.rect.centerx + WIDTH / 2 + (WIDTH/2 - mouse[0]) / 4 - self.offset.x) * (self.delay * dt)
    self.offset.y += (-target.rect.centery + HEIGHT / 2 + (HEIGHT/2 - mouse[1]) / 4 - self.offset.y) * (self.delay * dt)

    self.offset.x += max(0, min(self.offset.x,self.scene_size[0] / WIDTH))
    self.offset.y += max(0, min(self.offset.y, self.scene_size[1] / HEIGHT))

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