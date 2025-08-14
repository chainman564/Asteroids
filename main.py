import pygame
import random
from player import Player
from shot import Shot
from constants import *
from circleshape import CircleShape
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroid = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroid, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    clock = pygame.time.Clock()
    dt = 0

    running = True
    while running:
        dt = clock.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                 return

        updatable.update(dt)

        for a in asteroid:
            if player.collides_with(a):
                print("Game over!")
                pygame.quit()
                return

        for a in asteroid:
            for bullet in shots:
                if bullet.collides_with(a):
                    a.split()
                    a.kill()
                    bullet.kill()

        screen.fill((0, 0, 0))
        for drawable_object in drawable:
            drawable_object.draw(screen)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()