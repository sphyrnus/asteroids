import pygame
from constants import *
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")
    clock = pygame.time.Clock()
    dt = 0

    # Create sprite groups
    update_group = pygame.sprite.Group()
    draw_group = pygame.sprite.Group()

    # Create player and add it to the groups
    Player.containers = (update_group, draw_group)
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        screen.fill((0, 0, 0))

        # Update all sprites
        for group in update_group:
            group.update(dt)
        # Draw all sprites
        for group in draw_group:
            group.draw(screen)

        pygame.display.flip()
        clock.tick(60)
        dt = clock.get_time() / 1000


if __name__ == "__main__":
    main()
