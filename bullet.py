import pygame
from constants import *
from circleshape import CircleShape


class Bullet(CircleShape):
    def __init__(self, x, y, angle):
        super().__init__(x, y, 2)
        self.radius = BULLET_RADIUS

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius)

    def update(self, dt):
        self.position += self.velocity * dt
