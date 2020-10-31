"""
Dictionaries stores user messages
"""

ERROR_MESSAGES = {
    "program_stop": "An error has occurred, program stopped",
    "int_param": "Param must be int",
    "not_0_param": "Param must not be less or equal to 0"
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

# THREE_NUMBER = [
#     [RGB_GREEN_TAB, RGB_GREEN_TAB, RGB_GREEN_TAB, RGB_GREEN_TAB, RGB_GREEN_TAB],
#     [RGB_GREEN_TAB, RGB_GREEN_TAB, RGB_GREEN_TAB, RGB_GREEN_TAB, RGB_GREEN_TAB],
#     [0,0,0,RGB_GREEN_TAB, RGB_GREEN_TAB],
#     [0,0,0,RGB_GREEN_TAB, RGB_GREEN_TAB],
#     [0,0,0,RGB_GREEN_TAB, RGB_GREEN_TAB],
#     [0,0,RGB_GREEN_TAB,RGB_GREEN_TAB, RGB_GREEN_TAB],
#     [0,0,RGB_GREEN_TAB,RGB_GREEN_TAB, RGB_GREEN_TAB],
#     [RGB_GREEN_TAB, RGB_GREEN_TAB, RGB_GREEN_TAB, RGB_GREEN_TAB, RGB_GREEN_TAB],
#     [RGB_GREEN_TAB, RGB_GREEN_TAB, RGB_GREEN_TAB, RGB_GREEN_TAB, RGB_GREEN_TAB],
#     [0,0,0,RGB_GREEN_TAB, RGB_GREEN_TAB],
#     [0,0,0,RGB_GREEN_TAB, RGB_GREEN_TAB],
#     [0,0,0,RGB_GREEN_TAB, RGB_GREEN_TAB],
# ]
