#!/usr/bin/env python3
"""
Generation of PGM pictures as a GIF
"""
import sys
from simulator import pi_simulation
from utils import ERROR_MESSAGES

PPM_TYPE = "P3"
PPM_MAX_VALUE_COLOR = "255"

NEW_LINE = "\n"

RGB_PINK_TAB = [255,20,147]
RGB_BLUE_TAB = [0,0,255]
RGB_BLACK_TAB = [0,0,0]
RGB_WHITE_TAB = [255,255,255]

def generate_ppm_file(image_size, pi_simulation_results):
    """
    Generate picture in PPM format
    """
    points_in_circle = pi_simulation_results[1]
    points_out_circle = pi_simulation_results[2]

    file_name = "img0_piValue.ppm"
    ppm_file = open(file_name, "w")

    ppm_second_line = f"{image_size} {image_size}"
    ppm_header = PPM_TYPE + NEW_LINE + ppm_second_line + NEW_LINE + PPM_MAX_VALUE_COLOR + NEW_LINE
    ppm_file.write(ppm_header)

    tab_ppm = [[RGB_BLACK_TAB for _ in range (image_size)] for _ in range (image_size)]

    points_treatment(tab_ppm, points_in_circle, RGB_PINK_TAB)
    points_treatment(tab_ppm, points_out_circle, RGB_BLUE_TAB)

    extract_tab_to_ppm(tab_ppm, ppm_file)

def points_treatment(tab_ppm, points_tab, color):
    """
    Add to tab_ppm the rbg color code tab on cells when there is a point to be printed
    """
    for i, _ in enumerate(points_tab):
        tab_ppm[points_tab[i].x][points_tab[i].y] = color

def extract_tab_to_ppm(tab, ppm_file):
    """
    Extract number of tab to create a ppm file
    """
    tab_len = len(tab)
    for i in range (tab_len):
        for j in range (tab_len):
            for k in range (len(tab[i][j])):
                ppm_file.write(f"{tab[i][j][k]} ")

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
