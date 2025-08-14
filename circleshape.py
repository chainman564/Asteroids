import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # Draw the shape on the screen. Subclasses should override this.
        pygame.draw.polygon(screen, "white", self.triangle(), width=2)

    def update(self, dt):
        # Update the object's state. Subclasses should override this.
        pass

    def collides_with(self, other: "CircleShape") -> bool:
        # Check if this shape collides with another CircleShape.
        distance = self.position.distance_to(other.position)
        return distance <= self.radius + other.radius
