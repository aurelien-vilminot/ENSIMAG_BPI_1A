#!/usr/bin/env python3
"""
π simulation
"""
import sys
from random import uniform
from utils import ERROR_MESSAGES
from point import Point

CENTER_COORD = Point(0, 0)
RADIUS_CIRCLE = 1

def pi_simulation(nb_points, image_size = 1, nb_points_in_circle = 0):
    """
    Return the pi simulation number

    Params : nb_points is a int
    """
    nb_points = check_param(nb_points)

    points_in_circle = []
    points_out_circle = []
    for _ in range(nb_points):
        x_coord = uniform(-1, 1)
        y_coord = uniform(-1, 1)
        point = Point(x_coord, y_coord)
        if is_in_circle(CENTER_COORD, RADIUS_CIRCLE, point):
            nb_points_in_circle += 1
            points_in_circle.append(point.adapt_coord(image_size))
        else:
            points_out_circle.append(point.adapt_coord(image_size))

    return points_in_circle, points_out_circle, nb_points_in_circle

def pi_calcul(nb_points_in_circle, nb_points):
    """
    Return pi value
    """
    return 4 * (nb_points_in_circle / nb_points)

def check_param(nb_points):
    """
    Throw an exception if nb_points is an int or equal to 0
    """
    try:
        nb_points = int(nb_points)
        assert nb_points > 0
    except ValueError:
        print(ERROR_MESSAGES["int_param"])
        sys.exit(ERROR_MESSAGES["program_stop"])
    except AssertionError:
        print(ERROR_MESSAGES["not_0_param"])
        sys.exit(ERROR_MESSAGES["program_stop"])
    else:
        return nb_points


def is_in_circle(center, radius, point):
    """
    Return true if the point is in the circle

    Params : circle and point are Point, radius is an int
    """
    return (point.x_coord - center.x_coord)**2 + (point.y_coord - center.y_coord)**2 <= radius**2

def main():
    """
    Print the pi simulation if the program is called by command line
    """
    if len(sys.argv) != 2 or sys.argv[1] == "-h" or sys.argv[1] == "--help":
        print("Usage:", sys.argv[0], "points_number (int)")
        sys.exit(1)

    nb_points = sys.argv[1]
    results = pi_simulation(nb_points)
    nb_points_in_circle = results[2]
    pi_value = pi_calcul(nb_points_in_circle, int(nb_points))
    print(pi_value)

if __name__ == "__main__":
    main()
