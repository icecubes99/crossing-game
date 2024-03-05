from gameobject import GameObject


# This class represents the player in the game
class Player(GameObject):
    # Set the speed of the player
    SPEED = 3

    # Initialize the player with an image, position, dimensions
    def __init__(self, image_path, x, y, width, height):
        # Call the superclass's constructor
        super().__init__(image_path, x, y, width, height)

    # This method moves the player
    def move(self, directiony, directionx, max_height, max_width):
        # If the y direction is positive, move up
        if directiony > 0:
            self.y_pos -= self.SPEED
        # If the y direction is negative, move down
        elif directiony < 0:
            self.y_pos += self.SPEED
        # If the x direction is positive, move right
        if directionx > 0:
            self.x_pos += self.SPEED
        # If the x direction is negative, move left
        elif directionx < 0:
            self.x_pos -= self.SPEED

        # If the player has reached the top of the screen, move it to the bottom and return True
        if self.y_pos <= 0:
            self.y_pos = max_height
            return True

        # If the player has reached the bottom of the screen, stop it there
        if self.y_pos >= max_height - 40:
            self.y_pos = max_height - 40

        # If the player has reached the right side of the screen, stop it there
        if self.x_pos >= max_width - 40:
            self.x_pos = max_width - 40
        # If the player has reached the left side of the screen, stop it there
        elif self.x_pos <= 10:
            self.x_pos = 10

        # If the player has not reached the top of the screen, return False
        return False