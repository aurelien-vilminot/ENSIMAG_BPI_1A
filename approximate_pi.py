#!/usr/bin/env python3
"""
Generation of PGM pictures as a GIF
"""
import sys
from simulator import pi_simulation
from utils import ERROR_MESSAGES

PPM_FIRST_LINE = "P3"
PPM_THIRD_LINE = "255"

COLOR_IN_CIRCLE = "255  20 147"
COLOR_OUT_CIRCLE = "  0   0 255"

def generate_ppm_file(image_size, pi_simulation_results):
    """
    Generate picture in PPM format
    """
    ppm_second_line = str(image_size) + ' ' + str(image_size)
    ppm_header = PPM_FIRST_LINE + '\n' + ppm_second_line + '\n' + PPM_THIRD_LINE + '\n'
    print(ppm_header, end='')

    tab_ppm = [[[0,0,0] for _ in range (image_size)] for _ in range (image_size)]

    points_in_circle = pi_simulation_results[1]
    points_out_circle = pi_simulation_results[2]

    #points_treatment(points_in_circle, 0)

    #for i in range (image_size):
     #   for j in range (image_size):
      #      tab_ppm[i][j] = [255, 20, 147]

    for i in range(len(points_in_circle)):
        tab_ppm[points_in_circle[i].x][points_in_circle[i].y] = [255, 20, 147]

    for i in range(len(points_out_circle)):
        tab_ppm[points_out_circle[i].x][points_out_circle[i].y] = [0, 0, 255]
    
    extract_tab_to_ppm(tab_ppm)
    points_treatment(points_in_circle, points_out_circle)


def points_treatment(points_in_circle, points_out_circle):
    for i in range(len(points_in_circle)):
        print(str(points_in_circle[i].x) + ';' + str(points_in_circle[i].y))

def extract_tab_to_ppm(tab):
    """
    Extract number of tab to create a ppm file
    """
    counter = 0
    tab_len = len(tab)
    for i in range (tab_len):
        for j in range (tab_len):
            for k in range (len(tab[i][j])):
                print(str(tab[i][j][k]) + " ", end='')
                counter += 2
            if counter > 70:
                print("\n", end='')
                counter = 0

def check_params(image_size, points_number, decimal_number):
    """
    Throw an exception if params are not int
    """
    try:
        # Convert params into int
        image_size = int(image_size)
        points_number = int(points_number)
        decimal_number = int(decimal_number)
    except ValueError:
        print(ERROR_MESSAGES["int_param"])
        sys.exit(ERROR_MESSAGES["program_stop"])
    else:
        return image_size, points_number, decimal_number

def main():
    """
    Print the pi simulation if the program is called by command line
    """
    if len(sys.argv) != 4 or sys.argv[1] == "-h" or sys.argv[1] == "--help":
        print("Usage:", sys.argv[0], "image_size (int), points_number (int), decimal_number (int)")
        sys.exit(1)

    params = check_params(sys.argv[1], sys.argv[2], sys.argv[3])
    image_size = params[0]
    points_number = params[1]
    decimal_number = params[2]

    generate_ppm_file(image_size, pi_simulation(points_number, image_size))


if __name__ == "__main__":
    main()
