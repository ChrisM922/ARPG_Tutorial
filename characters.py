import pygame
from settings import *

class NPC(pygame.sprite.Sprite):
  def __init__(self, game, scene, group, pos, name):
    super().__init__(group)

    self.game = game
    self.scene = scene
    self.name = name
    self.import_images(f'assets/characters/{self.name}/')
    self.frame_index = 0
    self.image = self.animations['idle'][self.frame_index].convert()
    self.rect = self.image.get_frect(center = pos)
    self.speed = 90
    self.force = 2000
    self.acc = vec()
    self.vel = vec()
    self.fric = -15

  def import_images(self, path):
    self.animations = self.game.get_animations(path)

    for animation in self.animations.keys():
      full_path = path + animation
      self.animations[animation] = self.game.get_images(full_path)

  def animate(self, state, fps, loop=True):
    self.frame_index += fps

    if self.frame_index >= len(self.animations[state]) - 1:
      if loop:
        self.frame_index = 0
      else:
        self.frame_index = len(self.animations[state]) - 1

    self.image = self.animations[state][int(self.frame_index)]

  def physics(self, dt):
    # x axis
    self.acc.x += self.vel.x * self.fric
    self.vel.x += self.acc.x * dt
    self.rect.centerx += self.vel.x * dt + (self.vel.x/2) * dt

    # y axis
    self.acc.y += self.vel.y * self.fric
    self.vel.y += self.acc.y * dt
    self.rect.centery += self.vel.y * dt + (self.vel.y/2) * dt

    if self.vel.magnitude() >= self.speed:
      self.vel = self.vel.normalize() * self.speed

  def update(self, dt):
    self.physics(dt)
    self.animate('idle', 15 * dt)

class Player(NPC):
  def __init__(self, game, scene, group, pos, name):
    super().__init__(game, scene, group, pos, name)

  def movement(self):
    # x axis
    if INPUTS['left']:
      self.acc.x = -self.force
    elif INPUTS['right']:
      self.acc.x = self.force
    else:
      self.acc.x = 0

    # y axis
    if INPUTS['up']:
      self.acc.y = -self.force
    elif INPUTS['down']:
      self.acc.y = self.force
    else:
      self.acc.y = 0

  def update(self, dt):
    # overwriting the parent class update method
    self.physics(dt)
    self.movement()
    
    if self.vel.magnitude() < 1:
      self.animate('idle', 15 * dt)
    # player moves right then normal run animation
    elif self.vel.x > 0:
      self.animate('run', 15 * dt)
    # player moves left then flip the animation
    elif self.vel.x < 0:
      self.animate('run', 15 * dt)
      self.image = pygame.transform.flip(self.image, True, False)
