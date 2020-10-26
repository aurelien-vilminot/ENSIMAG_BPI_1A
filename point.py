#!/usr/bin/env python3
"""
Class Point file
"""

class Point:
    """
    Class represents point with two coordinates x and y
    """
    def __init__(self, x_coord, y_coord):
        self.x = x_coord
        self.y = y_coord

    def adapt_coord(self, image_size):
        """
        Scales coordinates to the future picture size
        """
        new_x = (self.x + 1)/2
        new_y = (self.y + 1)/2
        self.x = int(new_x * image_size)
        self.y = int(new_y * image_size)
        return self

    def __str__(self):
        return f"{self.x};{self.y}"
        