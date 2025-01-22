import pygame
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
