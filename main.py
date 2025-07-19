import pygame
from constants import *
from player import *
from asteroidfield import *
from asteroid import *

def main():

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    game_clock = pygame.time.Clock()

    dt = 0 

    updateable = pygame.sprite.Group()

    drawable = pygame.sprite.Group()

    asteroid = pygame.sprite.Group()

    Asteroid.containers = (asteroid, updateable, drawable)

    AsteroidField.containers = (updateable)

    Player.containers = (updateable, drawable)

    asteroid_field = AsteroidField()

    player_1 = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))

        updateable.update(dt)

        for entity in drawable:
            entity.draw(screen)

        pygame.display.flip()
        
        dt = game_clock.tick(60) / 1000

    print("Starting Asteroids!")

    print(f"Screen width: {SCREEN_WIDTH}")

    print(f"Screen height: {SCREEN_HEIGHT}")
    
    

if __name__ == "__main__":
    main()
