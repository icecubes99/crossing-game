from gameobject import GameObject


class Player(GameObject):

    SPEED = 3

    def __init__(self, image_path, x, y, width, height):
        super().__init__(image_path, x, y, width, height)

    def move(self, directiony, directionx, max_height):
        if directiony > 0:
            self.y_pos -= self.SPEED
        elif directiony < 0:
            self.y_pos += self.SPEED
        if directionx > 0:
            self.x_pos += self.SPEED
        elif directionx < 0:
            self.x_pos -= self.SPEED

        if self.y_pos <= 0:
            self.y_pos = max_height
            return True

        if self.y_pos >= max_height - 40:
            self.y_pos = max_height - 40

        return False
