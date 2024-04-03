import pygame, sys
from settings import *
from state import SplashScreen

class Game:
  def __init__(self):
    
    pygame.init()
    self.clock = pygame.time.Clock()
    pygame.display.set_caption("ARPG")
    self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
    self.font = pygame.font.Font(FONT, TILESIZE)
    self.running = True

    self.states = []
    self.splash_screen = SplashScreen(self)
    self.states.append(self.splash_screen)

  def get_input(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.running = False
        pygame.quit()
        sys.exit()
      
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          INPUTS['escape'] = True
          self.running = False
        elif event.key == pygame.K_SPACE:
          INPUTS['space'] = True
        elif event.key in (pygame.K_LEFT, pygame.K_a):
          INPUTS['left'] = True
        elif event.key in (pygame.K_RIGHT, pygame.K_d):
          INPUTS['right'] = True
        elif event.key in (pygame.K_UP, pygame.K_w):
          INPUTS['up'] = True
        elif event.key in (pygame.K_DOWN, pygame.K_s):
          INPUTS['down'] = True

      if event.type == pygame.KEYUP:
        if event.key == pygame.K_SPACE:
          INPUTS['space'] = False
        elif event.key in (pygame.K_LEFT, pygame.K_a):
          INPUTS['left'] = False
        elif event.key in (pygame.K_RIGHT, pygame.K_d):
          INPUTS['right'] = False
        elif event.key in (pygame.K_UP, pygame.K_w):
          INPUTS['up'] = False
        elif event.key in (pygame.K_DOWN, pygame.K_s):
          INPUTS['down'] = False
        
      if event.type == pygame.MOUSEWHEEL:
        if event.y == 1:
          INPUTS['scroll_up'] = True
        elif event.y == -1:
          INPUTS['scroll_down'] = True

      if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
          INPUTS['left_click'] = True
        elif event.button == 3:
          INPUTS['right_click'] = True
        elif event.button == 4:
          INPUTS['scroll_down'] = True
        elif event.button == 2:
          INPUTS['scroll_up'] = True

      if event.type == pygame.MOUSEBUTTONUP:
        if event.button == 1:
          INPUTS['left_click'] = False
        elif event.button == 3:
          INPUTS['right_click'] = False
      
      if event.type == pygame.MOUSEBUTTONUP:
        if event.button == 1:
          INPUTS['left_click'] = False
        elif event.button == 3:
          INPUTS['right_click'] = False
        elif event.button == 4:
          INPUTS['scroll_down'] = False
        elif event.button == 2:
          INPUTS['scroll_up'] = False

  def reset_input(self):
    for key in INPUTS:
      INPUTS[key] = False

  def loop(self):
    while self.running:
      dt = self.clock.tick()/1000
      self.get_input()
      self.states[-1].update(dt)
      self.states[-1].draw(self.screen)
      pygame.display.update()

if __name__ == '__main__':
  game = Game()
  game.loop()