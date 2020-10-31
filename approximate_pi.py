#!/usr/bin/env python3
"""
Generation of PPM pictures as a GIF
"""
import sys
import os
import glob
import subprocess

from simulator import pi_simulation, pi_calcul
from utils import ERROR_MESSAGES, RGB_TAB, PPM_PARAMS, GIF_PARAMS

def generate_ppm_file(tab_ppm, image_size, pi_simulation_results, decimal_number, nb_image, pi_value = 0):
    """
    Generate picture in PPM format
    """
    points_in_circle = pi_simulation_results[0]
    points_out_circle = pi_simulation_results[1]

    format_name_pi = format_file_name(pi_value, decimal_number, nb_image)
    file_name = format_name_pi[0]
    pi_format = format_name_pi[1]
    ppm_file = open(PPM_PARAMS["dir_ppm"] + file_name, "wb")

    ppm_second_line = f"{image_size} {image_size}"
    ppm_header = PPM_PARAMS["type"] + PPM_PARAMS["new_line"] + ppm_second_line + PPM_PARAMS["new_line"] + PPM_PARAMS["max_value_color"] + PPM_PARAMS["new_line"]
    ppm_file.write(bytearray(ppm_header, "utf-8"))

    points_treatment(tab_ppm, points_in_circle, RGB_TAB["blue"])
    points_treatment(tab_ppm, points_out_circle, RGB_TAB["pink"])

    # display_number(THREE_NUMBER, tab_ppm)

    extract_tab_to_ppm(tab_ppm, ppm_file)

    return tab_ppm

def generate_all_ppm_files(image_size, points_number, decimal_number):
    """
    Loop to generate all pictures and assemble it to gif
    """
    nb_points_in_circle = 0
    counter = GIF_PARAMS["current_state"]
    nb_image = 0
    tab_ppm = init_tab_ppm(image_size)

    while counter < 1:
        total_nb_points = points_number * counter
        pi_simulation_results = pi_simulation(points_number * GIF_PARAMS["current_state"], image_size)

        nb_points_in_circle += pi_simulation_results[2]
        pi_value = pi_calcul(nb_points_in_circle, total_nb_points)

        tab_ppm = generate_ppm_file(tab_ppm, image_size, pi_simulation_results, decimal_number, nb_image, pi_value)
        counter += GIF_PARAMS["current_state"]
        nb_image += 1


def init_tab_ppm(image_size):
    """
    Initialize ppm tab with black color
    """
    return [[RGB_TAB["white"] for _ in range (image_size)] for _ in range (image_size)]

def points_treatment(tab_ppm, points_tab, color):
    """
    Add to tab_ppm the rbg color code tab on cells when there is a point to be printed
    """
    for i, _ in enumerate(points_tab):
        tab_ppm[points_tab[i].x_coord][points_tab[i].y_coord] = color

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
            ppm_file.write(bytearray(tab_ppm[i][j]))


def format_file_name(pi_value, decimal_number, image_number):
    """
    Return file name for the ppm file with correct format
    """
    file_name = PPM_PARAMS["begin_pic_name"] + f"{image_number}_"
    formate = "{0:." + str(decimal_number) + "f}"
    pi_float = formate.format(pi_value)
    pi_format = pi_float.replace(".", PPM_PARAMS["decimal_separator"], 1)
    file_name += pi_format + PPM_PARAMS["picture_format"]
    return file_name, pi_float

def init_dir_ppm():
    """
    Create the directory "tmp_ppm" or empty this directory if already exists
    """
    if os.path.isdir(PPM_PARAMS["dir_ppm"]):
        empty_directory(PPM_PARAMS["dir_ppm"])
    else:
        os.mkdir(PPM_PARAMS["dir_ppm"])

def empty_directory(directory):
    """
    Recursively deletion of the files
    """
    for root, _, files in os.walk(directory):
        for file in files:
            os.remove(os.path.join(root, file))

def delete_ppm_files():
    """
    Delete all .ppm files in the directory ./tmp_ppm/
    """
    files = glob.glob(PPM_PARAMS["dir_ppm"] + "*" + PPM_PARAMS["picture_format"])

    for file in files:
        try:
            os.remove(file)
        except OSError as error:
            print("Error: %s : %s" % (file, error.strerror))
            sys.exit(ERROR_MESSAGES["program_stop"])

def check_params(image_size, points_number, decimal_number):
    """
    Throw an exception if params are not int and if they are less or equal to 0
    """
    try:
        image_size = int(image_size)
        points_number = int(points_number)
        decimal_number = int(decimal_number)
        assert image_size > 0
        assert points_number > 0
        assert decimal_number >= 0
    except ValueError:
        print(ERROR_MESSAGES["int_param"])
        sys.exit(ERROR_MESSAGES["program_stop"])
    except AssertionError:
        print(ERROR_MESSAGES["not_0_param"])
        sys.exit(ERROR_MESSAGES["program_stop"])
    else:
        return image_size, points_number, decimal_number

def main():
    """
    Execute the main program to create gif
    """
    if len(sys.argv) != 4 or sys.argv[1] == "-h" or sys.argv[1] == "--help":
        print("Usage:", sys.argv[0], "image_size (int), points_number (int), decimal_number (int)")
        sys.exit(1)

    params = check_params(sys.argv[1], sys.argv[2], sys.argv[3])
    image_size = params[0]
    points_number = params[1]
    decimal_number = params[2]

    init_dir_ppm()
    generate_all_ppm_files(image_size, points_number, decimal_number)
    subprocess.call(["convert", "-delay", "100", "-loop", "0", PPM_PARAMS["dir_ppm"] + "*" + PPM_PARAMS["picture_format"], "./"+ GIF_PARAMS["name"]])
    init_dir_ppm()

if __name__ == "__main__":
    main()
