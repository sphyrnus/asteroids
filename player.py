import pygame
from constants import *
from circleshape import CircleShape
from bullet import Bullet


# Player class
class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.color = (255, 255, 255)
        self.rotation = 0
        self.shoot_timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(
            surface=screen, color=self.color, points=self.triangle(), width=2
        )

    def rotate(self, dt):
        self.rotation += PLAYER_ROTATION_SPEED * dt

    def update(self, dt):
        self.shoot_timer = max(0, self.shoot_timer - dt)
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if self.shoot_timer > 0:
            return
        self.shoot_timer = PLAYER_SHOOT_COOLDOWN
        bullet = Bullet(self.position.x, self.position.y, self.rotation)
        bullet.velocity = (
            pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        )
