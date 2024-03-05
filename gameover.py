import pygame

from menu import Menu


class GameOver(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Start"

        # Load button images and their hovered states
        self.start_img = pygame.image.load('startNormal.png')
        self.start_hover_img = pygame.image.load('startHover.png')
        self.exit_img = pygame.image.load('exitNormal.png')
        self.exit_hover_img = pygame.image.load('exitHover.png')

        # Calculate the x-coordinates for the images
        self.startx = self.mid_w - self.start_img.get_width() / 2
        self.exitx = self.mid_w - self.exit_img.get_width() / 2

        # Calculate the y-coordinates for the images
        self.starty = self.mid_h + 50
        self.exity = self.mid_h + 100

        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.BLACK)
            # gameover.py, in the display_menu method
            self.game.draw_text('Game Over', 20, self.game.WHITE,
                                self.game.DISPLAY_W/2, self.game.DISPLAY_H/2 - 20)

            # Draw the buttons
            if self.state == 'Start':
                self.game.display.blit(self.start_hover_img, (self.startx, self.starty))
            else:
                self.game.display.blit(self.start_img, (self.startx, self.starty))

            if self.state == 'Exit':
                self.game.display.blit(self.exit_hover_img, (self.exitx, self.exity))
            else:
                self.game.display.blit(self.exit_img, (self.exitx, self.exity))

            self.game.difficulty = 1
            self.game.health = 1.0
            self.blit_screen()

    def move_cursor(self):
        if self.game.DOWN_KEY or self.game.UP_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.exitx + self.offset, self.exity)
                self.state = 'Exit'
            elif self.state == 'Exit':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Start':
                self.game.playing = True
            elif self.state == 'Exit':
                pygame.quit()
                quit()
            self.run_display = False