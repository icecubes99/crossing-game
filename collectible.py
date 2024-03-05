from gameobject import GameObject


class Collectible(GameObject):
    # Initialize the collectible with an image, position, dimensions
    def __init__(self, image_path, x, y, width, height):
        # Call the superclass's constructor
        super().__init__(image_path, x, y, width, height)

    # This method moves the collectible
    def move(self, max_width, max_height):
        # Move the collectible to the left by 5
        self.x_pos -= 5

        # If the collectible has moved off the left side of the screen
        if self.x_pos < -self.width:
            # Move the collectible to the right side of the screen
            self.x_pos = max_width

            # Set the collectible's y position to a random value within the bounds of the screen
            self.y_pos = max_height * 0.05