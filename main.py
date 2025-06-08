import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  clock = pygame.time.Clock()

  updateable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()
  shots = pygame.sprite.Group()

  Shot.containers = (shots, updateable, drawable)

  Asteroid.containers = (asteroids, updateable, drawable)
  AsteroidField.containers = (updateable)
  asteroid_field = AsteroidField()

  Player.containers = (updateable, drawable)

  player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

  dt = 0

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return

    updateable.update(dt)

    screen.fill("black")

    for sprite in drawable:
        sprite.draw(screen)
        
    pygame.display.flip()

    dt = clock.tick(60) / 1000

    for asteroid in asteroids:
      if asteroid.collides_with(player):
        print("Game over!")
        sys.exit()
        
      for shot in shots:
        if asteroid.collides_with(shot):
          shot.kill()
          asteroid.kill()

if __name__ == "__main__":
    main()