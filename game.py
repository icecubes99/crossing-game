import math
import random
import pygame
from enemy import Enemy
from menu import MainMenu
from player import Player

clock = pygame.time.Clock()


class Game():

    TICK_RATE = 60

    def __init__(self):
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
        self.DISPLAY_W = 800
        self.DISPLAY_H = 900

        # Create a surface with the specified dimensions
        self.display = pygame.Surface((self.DISPLAY_W, self.DISPLAY_H))

        # Create a window with the specified dimensions
        self.window = pygame.display.set_mode((self.DISPLAY_W, self.DISPLAY_H))

        # Get the default system font
        self.font_name = pygame.font.get_default_font()

        # Define color constants
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)

        self.curr_menu = MainMenu(self)
        self.directionx = 0
        self.directiony = 0
        self.difficulty = 1
        self.health = 1.0

    def game_loop(self):
        self.player = Player('player.png', 375, 900, 30, 30)
        num_enemies = int(math.pow(3, self.difficulty))
        self.enemies = [Enemy('enemy.png', -100, random.randint(
            50, 700), 30, 30) for _ in range(num_enemies)]
        while self.playing:
            self.check_events()
            self.update_game_state()
            if self.health == 5:
                self.playing = False
                continue
            if self.check_collision():
                self.health = round(self.health + 0.1, 1)
                print("Collision detected")
            self.draw_game_state()
            pygame.display.update()
            clock.tick(self.TICK_RATE)
            self.reset_keys()

    def check_events(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
            self.directiony = -1
        elif keys[pygame.K_UP]:
            self.directiony = 1
        else:
            self.directiony = 0

        if keys[pygame.K_LEFT]:
            self.directionx = -1
        elif keys[pygame.K_RIGHT]:
            self.directionx = 1
        else:
            self.directionx = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = (False, False)
                self.curr_menu.run_display = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                elif event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                elif event.key == pygame.K_UP:
                    self.UP_KEY = True
                elif event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
            print(event)

    def update_game_state(self):
        # Player has reached the top of the level
        if self.player.move(self.directiony, self.directionx, self.DISPLAY_H):
            self.difficulty += 1  # Increase difficulty
            self.game_loop()
        for enemy in self.enemies:
            enemy.move(self.DISPLAY_W)

    def draw_game_state(self):
        self.display.fill(self.BLACK)
        self.player.draw(self.display)
        for enemy in self.enemies:
            enemy.draw(self.display)
        self.draw_text(f"Year Level: {self.difficulty}", 30, 70, 20)
        self.draw_text(f"CGA: {self.health}", 30, 70, 50)
        self.window.blit(self.display, (0, 0))

    def reset_keys(self):
        # Initialize control flags to False
        self.UP_KEY = False
        self.DOWN_KEY = False
        self.START_KEY = False
        self.BACK_KEY = False

    def draw_text(self, text, size, x, y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.display.blit(text_surface, text_rect)

    def check_collision(self):
        player_rect = pygame.Rect(
            self.player.x_pos, self.player.y_pos, self.player.width, self.player.height)
        for enemy in self.enemies:
            enemy_rect = pygame.Rect(
                enemy.x_pos, enemy.y_pos, enemy.width, enemy.height)
            if player_rect.colliderect(enemy_rect):
                return True
        return False
