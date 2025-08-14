import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    COLOR = (255, 255, 255)

    def __init__(self, x, y, radius, velocity=None):
        super().__init__(x, y, radius)
        self.position = pygame.Vector2(x, y)
        self.radius = radius

        if velocity is not None:
            self.velocity = velocity
        else:
            angle = random.uniform(0, 360)
            speed = random.uniform(50, 150)
            self.velocity = pygame.Vector2(1, 0).rotate(angle) * speed

        self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, self.COLOR, (radius, radius), radius, 2)
        self.rect = self.image.get_rect(center=self.position)

        for group in self.__class__.containers:
            group.add(self)


    def draw(self, surface):
        pygame.draw.circle(surface, self.COLOR, (int(self.position.x), int(self.position.y)), self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
        self.rect.center = (self.position.x, self.position.y)

    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        random_angle = random.uniform(20, 50)

        vel1 = self.velocity.rotate(random_angle) * 1.2
        vel2 = self.velocity.rotate(-random_angle) * 1.2

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        Asteroid(self.position.x, self.position.y, new_radius, vel1)
        Asteroid(self.position.x, self.position.y, new_radius, vel2)
