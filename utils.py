"""
Dictionaries stores data as user messages or settings

Dictionaries are used to store all the settings used by the program.
"""

# Dictionary used to display error message when a exception is raised
ERROR_MESSAGES = {
    "program_stop": "An error has occurred, program stopped",
    "int_param": "Param must be int",
    "not_0_param": "Param must not be less or equal to 0",
    "nb_decimals_too_long": "Number of decimals is too large to enter in the picture"
}

# Dictionary used to set points color
RGB_TAB = {
    "pink": [255,20,147],
    "blue": [0,0,255],
    "black": [0,0,0],
    "background_color": [255,255,255]
}

# Dictionary used to configure the ppm files generation and their specifications
PPM_PARAMS = {
    "type": "P6",
    "max_value_color": "255",
    "dir_ppm": "./tmp_ppm/",
    "begin_pic_name": "img",
    "decimal_separator": "-",
    "picture_format": ".ppm"
}

# Dictionary used to give the division of total number of points and configure the gif file name
GIF_PARAMS = {
    "current_state" : 0.1,
    "name": "pi.gif"
}

# Dictionary used to configure the display and display number through a pattern
DISPLAY_NUMBER = {
    0: [[1,1,1],[1,0,1],[1,0,1],[1,0,1],[1,0,1],[1,0,1],[1,1,1]],
    1: [[0,0,1],[0,0,1],[0,0,1],[0,0,1],[0,0,1],[0,0,1],[0,0,1]],
    2: [[1,1,1],[0,0,1],[0,0,1],[1,1,1],[1,0,0],[1,0,0],[1,1,1]],
    3: [[1,1,1],[0,0,1],[0,0,1],[1,1,1],[0,0,1],[0,0,1],[1,1,1]],
    4: [[1,0,1],[1,0,1],[1,0,1],[1,1,1],[0,0,1],[0,0,1],[0,0,1]],
    5: [[1,1,1],[1,0,0],[1,0,0],[1,1,1],[0,0,1],[0,0,1],[1,1,1]],
    6: [[1,1,1],[1,0,0],[1,0,0],[1,1,1],[1,0,1],[1,0,1],[1,1,1]],
    7: [[1,1,1],[0,0,1],[0,0,1],[0,0,1],[0,0,1],[0,0,1],[0,0,1]],
    8: [[1,1,1],[1,0,1],[1,0,1],[1,1,1],[1,0,1],[1,0,1],[1,1,1]],
    9: [[1,1,1],[1,0,1],[1,0,1],[1,1,1],[0,0,1],[0,0,1],[1,1,1]],
    "dot": [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[1,0,0]],
    "scale": 5,
    "space_between": 10,
    "dic_color_before_number": dict(),
    "coord_init": None
}
