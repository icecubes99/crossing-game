import random
import pygame

from gameobject import GameObject


class Enemy(GameObject):
    def __init__(self, image_path, x, y, width, height):
        super().__init__(image_path, x, y, width, height)
        self.SPEED = random.randint(5, 15)
        self.start_time = pygame.time.get_ticks()
        self.delay = 0

    def move(self, max_width):
        if pygame.time.get_ticks() - self.start_time < self.delay:
            return

        self.x_pos -= self.SPEED
        if self.x_pos < -self.width:
            self.x_pos = max_width
            self.y_pos = random.randint(100, 500)
            self.SPEED = random.randint(5, 15)
            self.delay = random.randint(1000, 5000)  # Assign a random delay
            self.start_time = pygame.time.get_ticks()
