import pygame
from GUIObject import GUIObject
from io import BytesIO
from matplotlib.mathtext import math_to_image
from sympy.parsing.sympy_parser import \
    parse_expr, \
    standard_transformations, \
    implicit_multiplication_application, \
    function_exponentiation, \
    convert_xor
from sympy import latex
pygame.font.init()


class TextEntry(GUIObject):
    all_text_entries = []
    parsing_flags = standard_transformations + (implicit_multiplication_application,
                                                function_exponentiation,
                                                convert_xor)
    ascii_dict = {
        '=': '+',
        '1': '!',
        '2': '2',
        '3': '3',
        '4': '4',
        '5': '%',
        '6': '^',
        '7': '7',
        '8': '*',
        '9': '(',
        '0': ')',
        ',': '<',
        '.': '>',
        ' ': ' '}

    def __init__(self, event_manager, pos, colour, gui_object_blitted_to=None):

        super().__init__(pos, (1000, 100))

        self.char_dict = {'sum': self.big_main_font.render('\u2211')}

        self.colour = colour
        self.text = ''
        self.event_manager = event_manager
        self.input = ''
        self.invalid_function = False
        self.parsed_function = None
        self.function_surface = pygame.Surface((200, 200))

    def parse(self, string_function):
        if string_function.replace(' ', '') == '':
            return None
        else:
            try:
                sympy_function = parse_expr(string_function, transformations=self.parsing_flags, evaluate=False)
                self.invalid_function = False
                return sympy_function
            except SyntaxError:
                self.invalid_function = True
                return None

    def update(self):

        self.fill((255, 255, 255))

        for char in self.event_manager.keys_pressed:
            string = chr(char)

            if (string.isalpha() or string in self.ascii_dict) and char < 128:
                if self.event_manager.shift_held:
                    if string in self.ascii_dict:
                        self.text += self.ascii_dict[string]
                    else:
                        self.text += chr(char-32)
                else:
                    self.text += string
            elif char == 8:
                self.text = self.text[:-1]

        self.parsed_function = self.parse(self.text)

