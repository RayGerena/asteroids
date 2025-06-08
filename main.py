import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  clock = pygame.time.Clock()

  updateable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()

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

if __name__ == "__main__":
    main()