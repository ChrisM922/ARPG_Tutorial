import pygame
from settings import *
from camera import Camera
from characters import Player
from objects import Object
from pytmx.util_pygame import load_pygame

class State: 
  def __init__(self, game):
    self.game = game
    self.prev_state = None

  def enter_state(self):
    if len(self.game.states) > 1:
      self.prev_state = self.game.states[-1]
    self.game.states.append(self)

  def exit_state(self):
    self.game.states.pop()

  def update(self, dt):
    pass

  def draw(self, screen):
    pass

class SplashScreen(State):
  def __init__(self, game):
    State.__init__(self, game)

  def update(self, dt):
    if INPUTS['space']:
      Scene(self.game).enter_state()
      self.game.reset_inputs()

  def draw(self, screen):
    screen.fill(COLORS['blue'])
    self.game.render_text('Splash Screen, press space!', COLORS['white'], self.game.font, (WIDTH/2, HEIGHT/2))

class Scene(State):
  def __init__(self, game):
    State.__init__(self, game)

    self.camera = Camera(self)
    self.update_sprites = pygame.sprite.Group()
    self.drawn_sprites = pygame.sprite.Group()

    self.player = Player(self.game, self, [self.update_sprites,self.drawn_sprites ], (WIDTH/2, HEIGHT/2), 'ninja')

    self.tmx_data = load_pygame('scenes/0/0.tmx')
    self.create_scene()

  def create_scene(self):
    layers = []
    for layer in self.tmx_data.layers:
      layers.append(layer.name)
      # if 'floor' in layers:
    if 'floor' in layers:
      for x, y, surf in self.tmx_data.get_layer_by_name('floor').tiles():
        Object([self.drawn_sprites], (x * TILESIZE, y * TILESIZE), surf)

    if 'blocks' in layers:
      for x, y, surf in self.tmx_data.get_layer_by_name('blocks').tiles():
        Object([self.drawn_sprites], (x * TILESIZE, y * TILESIZE), surf) 

    if 'entries' in layers:
      for obj in self.tmx_data.get_layer_by_name('entries'):
        if  obj.name == '0':
          self.player = Player(self.game, self, [self.update_sprites,self.drawn_sprites ], (obj.x, obj.y), 'ninja')    

  # delete later
  def debugger(self, debug_list):
    for index, name in enumerate(debug_list):
      self.game.render_text(name, COLORS['white'], self.game.font, (10, 15 * index), False)

  def update(self, dt):
    self.update_sprites.update(dt)
    self.camera.update(dt, self.player)

  def draw(self, screen):
    self.camera.draw(screen, self.drawn_sprites)
    self.debugger([
      str('FPS: ' + str(round(self.game.clock.get_fps(), 2))),
      str('Vel: ' + str(round(self.player.vel, 2)))
    ])