import pygame
import random
from constants import *
from circleshape import CircleShape


# Asteroid class
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        # self.image = pygame.image.load("asteroid.png")
        # self.image = pygame.transform.scale(self.image, (radius * 2, radius * 2))
        # self.rect = self.image.get_rect()
        # self.rect.center = (x, y)

    def draw(self, screen):
        pygame.draw.circle(
            surface=screen,
            color=(255, 255, 255),
            center=self.position,
            radius=self.radius,
            width=2,
        )

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        for _ in range(2):
            radius = self.radius - ASTEROID_MIN_RADIUS
            angle = random.uniform(-50, 50)
            asteroid = Asteroid(self.position.x, self.position.y, radius)
            asteroid.velocity = self.velocity.rotate(angle) * 1.2
            # asteroid_group.add(asteroid)
