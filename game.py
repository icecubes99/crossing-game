import math
import random
import pygame
from enemy import Enemy
from menu import MainMenu
from player import Player
from gameover import GameOver

clock = pygame.time.Clock()


class Game():

    TICK_RATE = 60

    def __init__(self, image_path):
        # Initialize Pygame
        pygame.init()

        # Set the initial game state: running is True, playing is False
        self.running = True
        self.playing = False

        # Initialize control flags to False
        self.UP_KEY = False
        self.DOWN_KEY = False
        self.START_KEY = False
        self.BACK_KEY = False

        # Set the display width and height
        self.DISPLAY_W = 600
        self.DISPLAY_H = 600

        # Create a surface with the specified dimensions
        self.display = pygame.Surface((self.DISPLAY_W, self.DISPLAY_H))

        # Create a window with the specified dimensions
        self.window = pygame.display.set_mode((self.DISPLAY_W, self.DISPLAY_H))

        # Get the default system font
        self.font_name = pygame.font.get_default_font()

        # Define color constants
        self.BLACK = (0, 0, 0)  # RGB values for black
        self.WHITE = (255, 255, 255)  # RGB values for white

        # Set the current menu to the main menu
        self.curr_menu = MainMenu(self)

        # Initialize direction variables for x and y to 0
        self.directionx = 0
        self.directiony = 0

        # Set the initial difficulty level to 1
        self.difficulty = 1

        # Set the initial health level to 1.0
        self.health = 1.0

        # Load and scale the background image
        background = pygame.image.load(image_path)
        self.image = pygame.transform.scale(
            background, (self.DISPLAY_W, self.DISPLAY_H))  # Scale the image to fit the display

    # Start the game loop
    def game_loop(self):
        # Create a player object at the center of the display
        self.player = Player('player.png', self.DISPLAY_W / 2, self.DISPLAY_H, 30, 30)
        
        # Calculate the number of enemies based on the difficulty level
        num_enemies = int(math.pow(3, self.difficulty))
        
        # Create a list of enemy objects at random positions
        self.enemies = [Enemy('enemy.png', -100, random.randint(
            self.DISPLAY_H * 0.05, self.DISPLAY_H - int(self.DISPLAY_H * 0.2)), 30, 30) for _ in range(num_enemies)]
        
        # Create a game over menu
        game_over_menu = GameOver(self)

        # Continue the game loop as long as the game is in the playing state
        while self.playing:
            # Check for any events (like key presses)
            self.check_events()
            
            # Update the game state
            self.update_game_state()
            
            # If the player's GPA reaches 5, end the game and display the game over menu
            if self.health == 5:
                self.playing = False
                game_over_menu.display_menu()
                self.game_loop()
                continue
            
            # If a collision is detected, increase the player's GPA
            if self.check_collision():
                self.health = round(self.health + 0.1, 1)
                print("Collision detected")
            
            # Draw the current game state
            self.draw_game_state()
            
            # Update the display
            pygame.display.update()
            
            # Limit the frame rate
            clock.tick(self.TICK_RATE)
            
            # Reset the keys
            self.reset_keys()

    # This function checks for any key presses or events
    def check_events(self):
        # Get the state of all keyboard buttons
        keys = pygame.key.get_pressed()
        
        # If the down arrow key is pressed, set the y direction to -1
        if keys[pygame.K_DOWN]:
            self.directiony = -1
        # If the up arrow key is pressed, set the y direction to 1
        elif keys[pygame.K_UP]:
            self.directiony = 1
        # If neither up nor down is pressed, set the y direction to 0
        else:
            self.directiony = 0

        # If the left arrow key is pressed, set the x direction to -1
        if keys[pygame.K_LEFT]:
            self.directionx = -1
        # If the right arrow key is pressed, set the x direction to 1
        elif keys[pygame.K_RIGHT]:
            self.directionx = 1
        # If neither left nor right is pressed, set the x direction to 0
        else:
            self.directionx = 0

        # Loop through all the events
        for event in pygame.event.get():
            # If the event is a QUIT event (like closing the window), stop the game
            if event.type == pygame.QUIT:
                self.running, self.playing = (False, False)
                self.curr_menu.run_display = False
            # If the event is a key press
            elif event.type == pygame.KEYDOWN:
                # If the key is the Enter key, set the START_KEY flag to True
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                # If the key is the Backspace key, set the BACK_KEY flag to True
                elif event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                # If the key is the Up arrow key, set the UP_KEY flag to True
                elif event.key == pygame.K_UP:
                    self.UP_KEY = True
                # If the key is the Down arrow key, set the DOWN_KEY flag to True
                elif event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
            # Print the event
            print(event)

    # This function updates the game state
    def update_game_state(self):
        # Move the player based on the current direction
        # If the player has reached the top of the level, increase the difficulty and start a new game loop
        if self.player.move(self.directiony, self.directionx, self.DISPLAY_H, self.DISPLAY_W):
            self.difficulty += 1  # Increase difficulty
            self.game_loop()
        
        # Move each enemy
        for enemy in self.enemies:
            enemy.move(self.DISPLAY_W, self.DISPLAY_H)

    # This function draws the current game state
    def draw_game_state(self):
        # Draw the background image
        self.display.blit(self.image, (0, 0))
        
        # Draw the player
        self.player.draw(self.display)
        
        # Draw each enemy
        for enemy in self.enemies:
            enemy.draw(self.display)
        
        # Draw the current difficulty level (Year Level) at the top left of the screen
        self.draw_text(f"Year Level: {self.difficulty}", 30, self.BLACK, 100, 20)
        
        # Draw the player's current health (GPA) below the difficulty level
        self.draw_text(f"GPA: {self.health}", 30, self.BLACK, 70, 50)
        
        # Update the window with the current display
        self.window.blit(self.display, (0, 0))

    # This function resets all the control keys to False
    def reset_keys(self):
        self.UP_KEY = False  # Reset the UP_KEY flag
        self.DOWN_KEY = False  # Reset the DOWN_KEY flag
        self.START_KEY = False  # Reset the START_KEY flag
        self.BACK_KEY = False  # Reset the BACK_KEY flag

    # This function draws text on the screen at the specified position and color
    def draw_text(self, text, size, color, x, y):
        font = pygame.font.Font(self.font_name, size)  # Create a font object
        text_surface = font.render(text, True, color)  # Render the text into a surface
        text_rect = text_surface.get_rect()  # Get the rectangular area of the surface
        text_rect.center = (x, y)  # Set the center of the rectangle to the specified position
        self.display.blit(text_surface, text_rect)  # Draw the text surface on the display at the specified position

    # This function checks if the player has collided with any of the enemies
    def check_collision(self):
        # Create a rectangle for the player using its position and dimensions
        player_rect = pygame.Rect(
            self.player.x_pos, self.player.y_pos, self.player.width, self.player.height)
        
        # Loop through all the enemies
        for enemy in self.enemies:
            # Create a rectangle for the enemy using its position and dimensions
            enemy_rect = pygame.Rect(
                enemy.x_pos, enemy.y_pos, enemy.width, enemy.height)
            
            # If the player's rectangle and the enemy's rectangle overlap, return True
            if player_rect.colliderect(enemy_rect):
                return True
        
        # If the player has not collided with any enemies, return False
        return False
