import pygame


class Player:
    def __init__(self, game, x, y):
        self.game = game
        self.x = x
        self.y = y
        # Add other attributes as needed

    def move(self):
        if self.game.UP_KEY:
            self.y -= 5
        if self.game.DOWN_KEY:
            self.y += 5

    def draw(self, display):
        # Draw the player on the display
        pygame.draw.rect(display, self.game.WHITE, pygame.Rect(self.x, self.y, 50, 50))