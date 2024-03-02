class GameObject:
    def __init__(self, game, x, y, width, height):
        self.game = game
        self.x_pos = x
        self.y_pos = y

        self.width = width
        self.height = height