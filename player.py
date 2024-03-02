from gameobject import GameObject


class Player(GameObject):

    SPEED = 5

    def __init__(self, image_path, x, y, width, height):
        super().__init__(image_path, x, y, width, height)

    def move(self, direction, max_height):
        if direction > 0:
            self.y_pos -= self.SPEED
        elif direction < 0:
            self.y_pos += self.SPEED

        if self.y_pos <= 0:
            self.y_pos = max_height
            return True

        if self.y_pos >= max_height - 40:
            self.y_pos = max_height - 40

        return False
