import sys
import pygame

# Local imports
from constants import *
from player import *
from asteroidfield import *
from asteroid import *


def main():
    # --- Initialize Pygame ---
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()

    # --- Delta time tracker ---
    dt = 0  

    # --- Sprite groups ---
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroid = pygame.sprite.Group()

    # --- Register containers for entities ---
    Asteroid.containers = (asteroid, updateable, drawable)
    AsteroidField.containers = (updateable,)
    Player.containers = (updateable, drawable)

    # --- Create game objects ---
    asteroid_field = AsteroidField()
    player_1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # --- Main game loop ---
    while True:
        # --- Event handling ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # --- Update game state ---
        screen.fill((0, 0, 0))
        updateable.update(dt)

        # --- Collision detection ---
        for big_rock in asteroid:
            if big_rock.collision(player_1):
                print("Game over!")
                sys.exit()

        # --- Draw entities ---
        for entity in drawable:
            entity.draw(screen)

        # --- Refresh screen ---
        pygame.display.flip()

        # --- Maintain frame rate ---
        dt = game_clock.tick(60) / 1000

    # --- Debug info (never reached in current code) ---
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
