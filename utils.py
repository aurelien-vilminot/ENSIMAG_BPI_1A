"""
Dictionaries stores user messages
"""

ERROR_MESSAGES = {
    "program_stop": "An error has occurred, program stopped",
    "int_param": "Param must be int",
    "not_0_param": "Param must not be less or equal to 0",
    "nb_decimals_too_long": "Number of decimals is too large to enter in the picture"
}

RGB_TAB = {
    "pink": [255,20,147],
    "blue": [0,0,255],
    "green": [0,255,0],
    "black": [0,0,0],
    "white": [255,255,255]
}

PPM_PARAMS = {
    "type": "P6",
    "max_value_color": "255",
    "new_line": "\n",
    "dir_ppm": "./tmp_ppm/",
    "begin_pic_name": "img",
    "decimal_separator": "-",
    "picture_format": ".ppm"
}

GIF_PARAMS = {
    "current_state" : 0.1,
    "name": "pi.gif"
}

NUMBER = {
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
    "scale": 10,
    "space_between": 10
}
