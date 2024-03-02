import pygame


class Vehicle:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        # Add other attributes as needed

    def move(self):
        # Update the vehicle's position
        self.x += self.speed

    def draw(self, display):
        # Draw the vehicle on the display
        pygame.draw.rect(display, self.WHITE, pygame.Rect(self.x, self.y, 50, 50))