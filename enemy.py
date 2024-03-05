import random
import pygame

from gameobject import GameObject

# This class represents an enemy in the game
class Enemy(GameObject):
    # Initialize the enemy with an image, position, dimensions, and speed
    def __init__(self, image_path, x, y, width, height):
        # Call the superclass's constructor
        super().__init__(image_path, x, y, width, height)
        
        # Set the speed of the enemy to a random value between 5 and 5 (inclusive)
        self.SPEED = random.randint(5, 5)
        
        # Get the current time in milliseconds
        self.start_time = pygame.time.get_ticks()
        
        # Set the initial delay to 0
        self.delay = 0

    # This method moves the enemy
    def move(self, max_width, max_height):
        # If the current time is less than the start time plus the delay, do nothing
        if pygame.time.get_ticks() - self.start_time < self.delay:
            return

        # Move the enemy to the left by its speed
        self.x_pos -= self.SPEED
        
        # If the enemy has moved off the left side of the screen
        if self.x_pos < -self.width:
            # Move the enemy to the right side of the screen
            self.x_pos = max_width
            
            # Set the enemy's y position to a random value within the bounds of the screen
            self.y_pos = random.randint(
                max_height * 0.05, max_height - int(max_height * 0.2))
            
            # Set the speed of the enemy to a random value between 5 and 5 (inclusive)
            self.SPEED = random.randint(5, 5)
            
            # Set the delay to a random value between 500 and 4000 (inclusive)
            self.delay = random.randint(500, 4000)
            
            # Get the current time in milliseconds
            self.start_time = pygame.time.get_ticks()
