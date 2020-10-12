#!/usr/bin/env python3
"""
π simulation
"""
import sys
from random import uniform
from collections import namedtuple

# Define Point structure composed of attributes : x and y
Point = namedtuple('Point', 'x y')

CENTER_COORD = Point(0, 0)
RADIUS_CIRCLE = 1

def pi_simulation(nb_points):
    """
    Return the pi simulation number

    Params : nb_points is a int
    """
    nb_points = int(nb_points)

    if not check_param(nb_points):
        sys.exit("An error has occurred")

    counter = 0
    for _ in range(1, nb_points + 1):
        x_coord = uniform(-1, 1)
        y_coord = uniform(-1, 1)
        if is_in_circle(CENTER_COORD, RADIUS_CIRCLE, Point(x_coord, y_coord)):
            counter += 1

    return 4 * (counter / nb_points)

def check_param(nb_points):
    """
    Throw an exception if nb_points is not equal to 0
    """
    try:
        # Test if the denominator nb_points is valid
        1 / nb_points
    except ZeroDivisionError:
        print("number_of_points param must not be equal to 0")
    else:
        return True


def is_in_circle(center, radius, point):
    """
    Return true if the point is in the circle

    Params : circle and point are Point
    """
    return (point.x - center.x)**2 + (point.y - center.y)**2 <= radius**2

def main():
    """
    Print the pi simulation if the program is called by command line
    """
    if len(sys.argv) != 2 or sys.argv[1] == "-h" or sys.argv[1] == "--help":
        print("Usage:", sys.argv[0], "number_of_points (int)")
        sys.exit(1)

    nb_points = sys.argv[1]
    print(pi_simulation(nb_points))


if __name__ == "__main__":
    main()
