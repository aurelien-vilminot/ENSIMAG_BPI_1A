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

DIRECTORY_PICTURE = "./tmp_ppm/"
BEGIN_FILE_NAME = "img"
DECIMAL_SEPARATOR = "-"
FORMAT_PICTURE = ".ppm"

RGB_PINK_TAB = [255,20,147]
RGB_BLUE_TAB = [0,0,255]
RGB_GREEN_TAB = [0,255,0]
RGB_BLACK_TAB = [0,0,0]
RGB_WHITE_TAB = [255,255,255]

THREE_NUMBER = [
    [RGB_GREEN_TAB, RGB_GREEN_TAB, RGB_GREEN_TAB, RGB_GREEN_TAB, RGB_GREEN_TAB],
    [RGB_GREEN_TAB, RGB_GREEN_TAB, RGB_GREEN_TAB, RGB_GREEN_TAB, RGB_GREEN_TAB],
    [0,0,0,RGB_GREEN_TAB, RGB_GREEN_TAB],
    [0,0,0,RGB_GREEN_TAB, RGB_GREEN_TAB],
    [0,0,0,RGB_GREEN_TAB, RGB_GREEN_TAB],
    [0,0,RGB_GREEN_TAB,RGB_GREEN_TAB, RGB_GREEN_TAB],
    [0,0,RGB_GREEN_TAB,RGB_GREEN_TAB, RGB_GREEN_TAB],
    [RGB_GREEN_TAB, RGB_GREEN_TAB, RGB_GREEN_TAB, RGB_GREEN_TAB, RGB_GREEN_TAB],
    [RGB_GREEN_TAB, RGB_GREEN_TAB, RGB_GREEN_TAB, RGB_GREEN_TAB, RGB_GREEN_TAB],
    [0,0,0,RGB_GREEN_TAB, RGB_GREEN_TAB],
    [0,0,0,RGB_GREEN_TAB, RGB_GREEN_TAB],
    [0,0,0,RGB_GREEN_TAB, RGB_GREEN_TAB],
]

def generate_ppm_file(image_size, pi_simulation_results, decimal_number):
    """
    Generate picture in PPM format
    """
    pi_value = pi_simulation_results[0]
    points_in_circle = pi_simulation_results[1]
    points_out_circle = pi_simulation_results[2]

    format_name_pi = format_file_name(pi_value, decimal_number, 0)
    file_name = format_name_pi[0]
    pi_format = format_name_pi[1]
    ppm_file = open(DIRECTORY_PICTURE + file_name, "w")

    ppm_second_line = f"{image_size} {image_size}"
    ppm_header = PPM_TYPE + NEW_LINE + ppm_second_line + NEW_LINE + PPM_MAX_VALUE_COLOR + NEW_LINE
    ppm_file.write(ppm_header)

    tab_ppm = [[RGB_BLACK_TAB for _ in range (image_size)] for _ in range (image_size)]

    points_treatment(tab_ppm, points_in_circle, RGB_PINK_TAB)
    points_treatment(tab_ppm, points_out_circle, RGB_BLUE_TAB)

    display_number(THREE_NUMBER, tab_ppm)

    extract_tab_to_ppm(tab_ppm, ppm_file)

def points_treatment(tab_ppm, points_tab, color):
    """
    Add to tab_ppm the rbg color code tab on cells when there is a point to be printed
    """
    for i, _ in enumerate(points_tab):
        tab_ppm[points_tab[i].x][points_tab[i].y] = color

def display_number(pi_format, tab_ppm):
    """
    Write pi number on tab_ppm
    """
    modif = False
    lignes = 0
    colones = 0
    tab_len = len(tab_ppm)
    for i in range (tab_len):
        for j in range (tab_len):
            if i == tab_len / 2 and j == tab_len / 2:
                modif = True

            if colones < len(pi_format[lignes]) and modif:
                if pi_format[lignes][colones] != 0 :
                    print(lignes)
                    print(pi_format[lignes][colones])
                    print(str(i) + ';' + str(j))
                    tab_ppm[i][j] = pi_format[lignes][colones]
                colones += 1

        if modif:
            if lignes == len(pi_format) - 2:
                modif = False
            lignes += 1
            colones = 0


def extract_tab_to_ppm(tab_ppm, ppm_file):
    """
    Extract number of tab to create a ppm file
    """
    tab_len = len(tab_ppm)
    for i in range (tab_len):
        for j in range (tab_len):
            for k in range (len(tab_ppm[i][j])):
                ppm_file.write(f"{tab_ppm[i][j][k]} ")

def format_file_name(pi_value, decimal_number, image_number):
    """
    Return file name for the ppm file with correct format
    """
    file_name = f"{BEGIN_FILE_NAME}{image_number}_"
    formate = "{0:." + str(decimal_number) + "f}"
    pi_float = formate.format(pi_value)
    pi_format = pi_float.replace(".", DECIMAL_SEPARATOR, 1)
    file_name += f"{pi_format}{FORMAT_PICTURE}"
    return file_name, pi_float

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

    generate_ppm_file(image_size, pi_simulation(points_number, image_size), decimal_number)

if __name__ == "__main__":
    main()
