import pygame
from game import Game

g = Game("background.png")

while g.running:
    g.curr_menu.display_menu()
    g.game_loop()
