import pygame
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN
from circleshape import CircleShape
from shot import Shot

class Player(CircleShape):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 180
        self.PLAYER_TURN_SPEED = PLAYER_TURN_SPEED
        self.shoot_cooldown_timer: float = 0.0

    def rotate(self, dt):
        self.rotation += self.PLAYER_TURN_SPEED * dt
        self.rotation %= 360

    def get_rotation(self):
        self.rotation += PLAYER_TURN_SPEED * dt * direction
        self.rotation %= 360

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        
        if self.shoot_cooldown_timer > 0:
            self.shoot_cooldown_timer -= dt
            if self.shoot_cooldown_timer < 0:
                self.shoot_cooldown_timer = 0

        if keys[pygame.K_SPACE] and self.shoot_cooldown_timer == 0:
            self.shoot()
            self.shoot_cooldown_timer = PLAYER_SHOOT_COOLDOWN

    def shoot(self):
        direction = pygame.Vector2(0, 1).rotate(self.rotation)
        velocity = direction * PLAYER_SHOOT_SPEED
        Shot(self.position.x, self.position.y, velocity)

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5

        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right

        return [a, b, c]