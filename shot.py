import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS

class Shot(CircleShape):
    COLOR = (255, 255, 0)

    def __init__(self, x, y, velocity):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = velocity
        self._init_sprite()
        for group in self.__class__.containers:
            group.add(self)

    def _init_sprite(self):
        diameter = self.radius * 2
        self.image = pygame.Surface((diameter, diameter), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=self.position)

    def update(self, dt):
        self.position += self.velocity * dt
        self.rect.center = self.position

    def draw(self, surface):
        # Draw the shape on the screen.
        pygame.draw.circle(surface, self.COLOR, (int(self.position.x), int(self.position.y)), self.radius)
