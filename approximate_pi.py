#!/usr/bin/env python3
"""
Generation of PPM pictures as a GIF

This program uses simulator.py to approximate the value of π.
The points generated and the value of π are printed in a PPM picture.
All PPM files are aggregated through a GIF file.
"""
import sys
import os
import subprocess
import copy
import time

from simulator import pi_simulation, pi_calcul
from utils import ERROR_MESSAGES, RGB_TAB, PPM_PARAMS, GIF_PARAMS, DISPLAY_NUMBER
from point import Point

def generate_ppm_file(tab_ppm, input_params, pi_simulation_results, nb_image, pi_value):
    """
    Required : tab_ppm, list, no type cheking
               image_size, int, no type cheking
               pi_simulation_results, tuple, no type cheking
               nb_decimals, int, no type cheking
               nb_image, int, no type cheking
               pi_value, float, no type cheking

    Generate picture in PPM format
    """
    points_in_circle = pi_simulation_results[0]
    points_out_circle = pi_simulation_results[1]
    image_size = input_params[0]
    nb_decimals = input_params[1]

    # Get the correct format file name and create the new PPM file (opened in binary mode)
    format_name_pi = format_file_name(pi_value, nb_decimals, nb_image)
    file_name = format_name_pi[0]
    pi_format = format_name_pi[1]
    ppm_file = open(PPM_PARAMS["dir_ppm"] + file_name, "wb")

    # Write ppm header in utf-8 mode
    ppm_second_line = f"{image_size} {image_size}"
    ppm_header = f'{PPM_PARAMS["type"]} {ppm_second_line} {PPM_PARAMS["max_value_color"]} '
    ppm_file.write(bytearray(ppm_header, "utf-8"))

    # Add generated points and their correponding color to tab_ppm
    add_color_points(tab_ppm, points_in_circle, RGB_TAB["blue"])
    add_color_points(tab_ppm, points_out_circle, RGB_TAB["pink"])

    write_number(pi_format, tab_ppm)

    extract_tab_to_ppm(tab_ppm, ppm_file)

    ppm_file.close()

    return tab_ppm

def generate_all_ppm_files(image_size, nb_points, nb_decimals):
    """
    Required : image_size, int, no type cheking
               nb_points, int, no type cheking
               nb_decimals, int, no type cheking

    Loop to generate successively all PPM pictures
    """
    # Initialize parameters for the loop
    nb_points_in_circle = 0
    counter = GIF_PARAMS["current_state"]
    nb_image = 0
    tab_ppm = init_tab_ppm(image_size)

    # Calculate the initials coordinates where the number must be placed in the picture
    init_coord_number_results = calculate_init_coord_number(tab_ppm, nb_decimals)
    DISPLAY_NUMBER["coord_init"] = Point(init_coord_number_results[0], init_coord_number_results[1])

    while counter < 1:
        # Execute fonctions of simulator.py to simulate the value of π
        total_nb_points = nb_points * counter
        pi_simulation_results = pi_simulation(nb_points * GIF_PARAMS["current_state"], image_size)

        nb_points_in_circle += pi_simulation_results[2]
        pi_value = pi_calcul(nb_points_in_circle, total_nb_points)

        # Generate PPM file and keep in memory all generated points
        tab_ppm = generate_ppm_file(tab_ppm, (image_size, nb_decimals), pi_simulation_results, nb_image, pi_value)
        counter += GIF_PARAMS["current_state"]
        nb_image += 1

def init_tab_ppm(image_size):
    """
    Required : image_size, int, no type cheking

    Initialize a list of list fulfilled with a background color
    """
    return [[RGB_TAB["background_color"] for _ in range (image_size)] for _ in range (image_size)]

def add_color_points(tab_ppm, points_tab, color):
    """
    Required : tab_ppm, list, no type cheking
               points_tab, list, no type cheking
               color, list, no type checking

    Add to tab_ppm the rbg color code tab on cells when there is a point to be printed
    """
    for i, _ in enumerate(points_tab):
        tab_ppm[points_tab[i].x_coord][points_tab[i].y_coord] = color

def write_number(pi_format, tab_ppm):
    """
    Required : pi_format, str, no type cheking
               tab_ppm, list, no type cheking

    Write the π approximation number on tab_ppm
    """
    scale_number = DISPLAY_NUMBER["scale"]

    # Copy of coord_init in another memory area not to modify the initial value
    coord_init = copy.deepcopy(DISPLAY_NUMBER["coord_init"])

    # Treat all digits from π approximation
    for number in pi_format:
        if number != ".":
            number_tab = DISPLAY_NUMBER[int(number)]
            coord_init.x_coord = browse_number_tab(number_tab, scale_number, tab_ppm, coord_init)
        else:
            dot_tab = DISPLAY_NUMBER["dot"]
            coord_init.x_coord = browse_number_tab(dot_tab, scale_number, tab_ppm, coord_init)

def browse_number_tab(number_tab, scale_number, tab_ppm, coord_init):
    """
    Required : number_tab, list, no type cheking
               scale_number, int, no type cheking
               tab_ppm, list, no type cheking
               coord_init, Point, no type cheking

    Browse the number_tab pattern to write it on tab_ppm
    """
    x_coord = coord_init.x_coord
    y_coord = coord_init.y_coord
    number_tab_len = len(number_tab)

    # Get the dictionary that contains all colored points before the display of number
    dic = DISPLAY_NUMBER["dic_color_before_number"]

    for i in range(number_tab_len):
        for _ in range(scale_number):
            for j in range(len(number_tab[i])):
                for _ in range(scale_number):

                    # Search in the dictionary if the pixel was colored in the previous step
                    if (y_coord, x_coord) in dic and tab_ppm[y_coord][x_coord] in (RGB_TAB["background_color"], RGB_TAB["black"]):
                        tab_ppm[y_coord][x_coord] = dic[(y_coord, x_coord)]

                    # If the pixel must be black color, keep in the dictionary the intial color of this pixel
                    if number_tab[i][j] == 1:
                        dic[(y_coord, x_coord)] = tab_ppm[y_coord][x_coord]
                        tab_ppm[y_coord][x_coord] = RGB_TAB["black"]
                    x_coord += 1
            y_coord += 1
            x_coord = coord_init.x_coord
    y_coord = coord_init.y_coord

    # Return the next x coordinate to begin at right place the process for the next digit
    return coord_init.x_coord + (3 * scale_number) + DISPLAY_NUMBER["space_between"]

def calculate_init_coord_number(tab_ppm, nb_decimals):
    """
    Required : tab_ppm, list, no type cheking
               nb_decimals, int, no type cheking

    Calculate the coordinates of the place to begin to write number (must be center to the picture)
    Is called only once because of no changes about size picture during the program execution
    In this fonction : the number 3 represents the minimal length of the pattern number tab
                       the number 7 represents the minimal height of the pattern number tab
    """
    # Calculate the x and y coordinates of the center of the picture
    half_lenght_tab_ppm = int(len(tab_ppm[0]) / 2)
    half_height_tab_ppm = half_lenght_tab_ppm
    scale_number = DISPLAY_NUMBER["scale"]

    # Calculate the place used by the decimals only counting spaces
    if nb_decimals != 0:
        space_between_lenght = DISPLAY_NUMBER["space_between"] * (nb_decimals + 1)
        decimals_lenght = 3 * scale_number * (nb_decimals + 1) + space_between_lenght
    else:
        decimals_lenght = 0

    # Add the lenght of the first number (before the dot) to the final lenght
    number_length = (3 * scale_number) + decimals_lenght
    number_height = 7 * scale_number

    x_coord_init = int(half_lenght_tab_ppm - (number_length / 2))
    y_coord_init = int(half_height_tab_ppm - (number_height / 2))

    # Test if the full decimal number may be display on the picture (constraint by size)
    try:
        assert x_coord_init > 0
        assert y_coord_init > 0
    except AssertionError:
        print(ERROR_MESSAGES["nb_decimals_too_long"])
        init_dir_ppm()
        sys.exit(ERROR_MESSAGES["program_stop"])
    else:
        return x_coord_init, y_coord_init

def extract_tab_to_ppm(tab_ppm, ppm_file):
    """
    Required : tab_ppm, list, no type cheking
               ppm_file, FileObject, no type cheking

    Extract rgb colors of the tab_ppm to insert it in the PPM file in binary
    """
    tab_len = len(tab_ppm)
    for i in range(tab_len):
        for j in range(tab_len):
            ppm_file.write(bytearray(tab_ppm[i][j]))

def format_file_name(pi_value, nb_decimals, image_number):
    """
    Required : pi_value, int, no type cheking
               nb_decimals, int, no type cheking
               image_number, int, no type cheking

    Format the file name for the PPM file
    """
    file_name = f'{PPM_PARAMS["begin_pic_name"]}{image_number}_'
    formate = "{0:." + str(nb_decimals) + "f}"
    pi_float = formate.format(pi_value)
    pi_format = pi_float.replace(".", PPM_PARAMS["decimal_separator"], 1)
    file_name += pi_format + PPM_PARAMS["picture_format"]

    return file_name, pi_float

def init_dir_ppm():
    """
    Create a directory used to temporarily store the PPM files
    """
    directory_ppm = PPM_PARAMS["dir_ppm"]

    if os.path.isdir(directory_ppm):
        empty_directory(directory_ppm)
    else:
        os.mkdir(directory_ppm)

def empty_directory(directory):
    """
    Required : directory, str, no type cheking

    Delete recursively all files contain in the directory
    """
    for root, _, files in os.walk(directory):
        for file in files:
            try:
                os.remove(os.path.join(root, file))
            except OSError as error:
                print("Error: %s : %s" % (file, error.strerror))
                sys.exit(ERROR_MESSAGES["program_stop"])

def check_params(image_size, nb_points, nb_decimals):
    """
    Required : image_size, str/int, type checked
               nb_points, str/int, type checked
               nb_decimals, str/int, type checked

    Throw an exception if params are not int and if they are less or equal to 0
    """
    try:
        image_size = int(image_size)
        nb_points = int(nb_points)
        nb_decimals = int(nb_decimals)
        assert image_size > 0
        assert nb_points > 0
        assert nb_decimals >= 0
    except ValueError:
        print(ERROR_MESSAGES["int_param"])
        sys.exit(ERROR_MESSAGES["program_stop"])
    except AssertionError:
        print(ERROR_MESSAGES["not_0_param"])
        sys.exit(ERROR_MESSAGES["program_stop"])
    else:
        return image_size, nb_points, nb_decimals

def main():
    """
    Execute the main program to create gif
    """
    #remove
    start_time = time.time()

    if len(sys.argv) != 4 or sys.argv[1] == "-h" or sys.argv[1] == "--help":
        print(f'Usage: {sys.argv[0]} image_size (int), nb_points (int), nb_decimals (int)')
        sys.exit(ERROR_MESSAGES["program_stop"])

    params = check_params(sys.argv[1], sys.argv[2], sys.argv[3])
    image_size = params[0]
    nb_points = params[1]
    nb_decimals = params[2]

    init_dir_ppm()
    generate_all_ppm_files(image_size, nb_points, nb_decimals)

    # Assemble all images to create a gif with convert program
    subprocess.call(["convert", "-delay", "100", "-loop", "0", f'{PPM_PARAMS["dir_ppm"]}*{PPM_PARAMS["picture_format"]}', f'./{GIF_PARAMS["name"]}'])
    init_dir_ppm()

    #remove
    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
    main()
