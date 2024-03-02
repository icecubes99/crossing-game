import pygame
from menu import MainMenu
from player import Player

class Game():
    def __init__(self):
        pygame.init()
        self.player = Player(self, 100, 100)
        # Set the initial game state: running is True, playing is False
        self.running = True
        self.playing = False

        # Initialize control flags to False
        self.UP_KEY = False
        self.DOWN_KEY = False
        self.START_KEY = False
        self.BACK_KEY = False

        # Set the display width and height
        self.DISPLAY_W = 480
        self.DISPLAY_H = 270

        # Create a surface with the specified dimensions
        self.display = pygame.Surface((self.DISPLAY_W, self.DISPLAY_H))

        # Create a window with the specified dimensions
        self.window = pygame.display.set_mode((self.DISPLAY_W, self.DISPLAY_H))

        # Get the default system font
        self.font_name = pygame.font.get_default_font()

        # Define color constants
        self.BLACK = (0,0,0)
        self.WHITE = (255,255,255)

        self.curr_menu = MainMenu(self)

    def game_loop(self):
        while self.playing:
            self.check_events()
            self.update_game_state()
            self.draw_game_state()
            pygame.display.update()
            self.reset_keys()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = (False, False)
                self.curr_menu.run_display = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                elif event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                elif event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                elif event.key == pygame.K_UP:
                    self.UP_KEY = True 

    def reset_keys(self):
        # Initialize control flags to False
        self.UP_KEY = False
        self.DOWN_KEY = False
        self.START_KEY = False
        self.BACK_KEY = False

    def draw_text(self, text, size, x, y):
        font = pygame.font.Font(self.font_name,size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.display.blit(text_surface, text_rect)
    
    def update_game_state(self):
        # Update player position
        self.player.move()
        # Move cars
        # Check for collisions
        # etc

    def draw_game_state(self):
        # Clear the screen
        self.display.fill(self.BLACK)
        # Draw player
        self.player.draw(self.display)
        # Draw cars
        # etc.
        # Draw the display to the window
        self.window.blit(self.display, (0,0))