"""
Class Point file
"""

class Point:
    """
    Class represents point with two coordinates x and y
    """
    def __init__(self, x_coord, y_coord):
        self.x_coord = x_coord
        self.y_coord = y_coord

    def adapt_coord(self, image_size):
        """
        Scales coordinates to the future picture size
        """
        new_x = (self.x_coord + 1)/2
        new_y = (self.y_coord + 1)/2
        self.x_coord = int(new_x * image_size)
        self.y_coord = int(new_y * image_size)
        return self

    def __str__(self):
        return f"{self.x_coord};{self.y_coord}"
        