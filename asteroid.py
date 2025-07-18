from circleshape import *
from constants import *
import random
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255),  self.position, self.radius, 2)

    def update(self, dt):

        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        random_angle = random.uniform(20,50)
        new_angle_1 = self.velocity.rotate(random_angle)
        new_angle_2 = self.velocity.rotate(random_angle * -1)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_1.velocity.x = new_angle_1.x * 1.2
        new_asteroid_1.velocity.y = new_angle_1.y * 1.2
        new_asteroid_2.velocity.x = new_angle_2.x * 1.2
        new_asteroid_2.velocity.y = new_angle_2.y * 1.2
    
