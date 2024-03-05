# Import the pygame library
import pygame
# Import the Game class from the game module
from game import Game

# Create a new Game object with the specified background image
g = Game("background.png")

# While the game is running
while g.running:
    # Display the current menu
    g.curr_menu.display_menu()
    # Start the game loop once the previous menu has returned
    g.game_loop()