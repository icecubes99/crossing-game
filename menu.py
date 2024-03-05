import pygame


class Menu():
    def __init__(self, game):
        self.game = game
        # Calculate the middle width and height of the game display
        self.mid_w = self.game.DISPLAY_W / 2
        self.mid_h = self.game.DISPLAY_H / 2

        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = -100

    # def draw_cursor(self):
    #     self.game.draw_text('*', 15, self.game.WHITE,
    #                         self.cursor_rect.x, self.cursor_rect.y)

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()


class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Start"

        # Start game text
        # self.startx, self.starty = self.mid_w, self.mid_h + 30
        # self.aboutx, self.abouty = self.mid_w, self.mid_h + 50
        # self.exitx, self.exity = self.mid_w, self.mid_h + 70
        # self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
        self.start_img = pygame.image.load('startNormal.png')
        self.start_hover_img = pygame.image.load('startHover.png')
        self.about_img = pygame.image.load('abouttNormal.png')
        self.about_hover_img = pygame.image.load('aboutHover.png')
        self.exit_img = pygame.image.load('exitNormal.png')
        self.exit_hover_img = pygame.image.load('exitHover.png')

        self.startx = self.mid_w - self.start_img.get_width() / 2
        self.aboutx = self.mid_w - self.about_img.get_width() / 2
        self.exitx = self.mid_w - self.exit_img.get_width() / 2


        self.starty = self.mid_h + 50
        self.abouty = self.mid_h + 100
        self.exity = self.mid_h + 150

        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('Main Menu', 20, self.game.WHITE,
                                self.game.DISPLAY_W/2, self.game.DISPLAY_H/2 - 20)
            

            # self.game.draw_text(
            #     'Start Game', 20, self.game.WHITE, self.startx, self.starty)
            # self.game.draw_text('About', 20, self.game.WHITE,
            #                     self.aboutx, self.abouty)
            # self.game.draw_text('Exit', 20, self.game.WHITE,
            #                     self.exitx, self.exity)
            if self.state == 'Start':
                self.game.display.blit(self.start_hover_img, (self.startx, self.starty))
            else:
                self.game.display.blit(self.start_img, (self.startx, self.starty))

            if self.state == 'About':
                self.game.display.blit(self.about_hover_img, (self.aboutx, self.abouty))
            else:
                self.game.display.blit(self.about_img, (self.aboutx, self.abouty))

            if self.state == 'Exit':
                self.game.display.blit(self.exit_hover_img, (self.exitx, self.exity))
            else:
                self.game.display.blit(self.exit_img, (self.exitx, self.exity))


            self.game.difficulty = 1
            self.game.health = 1.0
            # self.draw_cursor()
            self.blit_screen()

    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (
                    self.aboutx + self.offset, self.abouty)
                self.state = 'About'
            elif self.state == 'About':
                self.cursor_rect.midtop = (
                    self.exitx + self.offset, self.exity)
                self.state = 'Exit'
            elif self.state == 'Exit':
                self.cursor_rect.midtop = (
                    self.startx + self.offset, self.starty)
                self.state = 'Start'

        if self.game.UP_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (
                    self.exitx + self.offset, self.exity)
                self.state = 'Exit'
            elif self.state == 'About':
                self.cursor_rect.midtop = (
                    self.startx + self.offset, self.starty)
                self.state = 'Start'
            elif self.state == 'Exit':
                self.cursor_rect.midtop = (
                    self.aboutx + self.offset, self.abouty)
                self.state = 'About'

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Start':
                self.game.playing = True
            elif self.state == 'About':
                pass
            elif self.state == 'Exit':
                pygame.exit()
            self.run_display = False
