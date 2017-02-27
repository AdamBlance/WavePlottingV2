import pygame
from GUIObject import GUIObject
from sympy.parsing.sympy_parser import \
    parse_expr, \
    standard_transformations, \
    implicit_multiplication_application, \
    function_exponentiation, \
    convert_xor
pygame.font.init()


class TextContainer(GUIObject):
    all_text_entries = []
    parsing_flags = standard_transformations + (implicit_multiplication_application,
                                                function_exponentiation,
                                                convert_xor)

    def __init__(self, event_manager, pos, colour, gui_object_blitted_to=None):
        super().__init__(pos, (400, 100))

        self.event_manager = event_manager
        self.all_chars = []
        self.is_current = True
        self.pointer = 0

    def make_new(self):
        self.all_chars.append(TextContainer())

    def update(self):

        if self.event_manager.entered_char() == '^':
            self.make_new()