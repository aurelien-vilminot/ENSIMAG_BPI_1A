#!/usr/bin/env python3
"""
Class Point
"""

class Point:
    def __init__(self, x_coord, y_coord):
        self.x = x_coord
        self.y = y_coord

    def adapt_coord(self, image_size):
        self.x = int((self.x * image_size) % image_size)
        self.y = int((self.y * image_size) % image_size)
        return self

    def __str__(self):
        return str(self.x) + ';' + str(self.y)
        