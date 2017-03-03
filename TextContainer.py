import pygame
import pygame.freetype
from pygame.locals import *
from GUIObject import GUIObject
from sympy.parsing.sympy_parser import \
    parse_expr, \
    standard_transformations, \
    implicit_multiplication_application, \
    function_exponentiation, \
    convert_xor
pygame.font.init()


class TextContainer(pygame.Surface):

    all_text_entries = []
    parsing_flags = standard_transformations + (implicit_multiplication_application,
                                                function_exponentiation,
                                                convert_xor)

    maths_font = pygame.freetype.Font('media/DejaVuSans.ttf')
    colour = pygame.Color('white')

    def __init__(self, event_manager, size=None, font_size=20):

        self.size = size

        self.maths_font.size = font_size
        if self.size is not None:
            super().__init__(self.size)

        self.event_manager = event_manager
        self.is_current = True

        self.all_symbols = []
        self.font_height = self.maths_font.height

        self.pointer_pos = 0
        self.pointer_index = 0
        self.pointer_visible = True

    def backspace(self):
        if self.pointer_index != 0:
            self.pointer_index -= 1
            self.all_symbols.pop(self.pointer_index)

    def delete(self):
        if self.pointer_index != len(self.all_symbols):
            self.all_symbols.pop(self.pointer_index)

    def add_char(self, key):
        self.all_symbols.insert(self.pointer_index, key)
        self.pointer_index += 1

    def render_all(self):
        pass

    def update(self):

        dec_pointer = self.pointer_index-1
        if dec_pointer >= 0 and self.event_manager.key_pressed == K_LEFT:
            self.pointer_index = dec_pointer

        inc_pointer = self.pointer_index+1
        if inc_pointer <= len(self.all_symbols) and self.event_manager.key_pressed == K_RIGHT:
            self.pointer_index = inc_pointer

        pressed = self.event_manager.entered_chars()
        if pressed is not None:
            if pressed == 'backspace':
                self.backspace()
            elif pressed == 'delete':
                self.delete()
            else:
                self.add_char(pressed)

        joined = ''.join(self.all_symbols)
        pointer_join = ''.join(self.all_symbols[:self.pointer_index])

        half_entry = self.size[1]/2
        text_rect = self.maths_font.get_rect('|')
        half = half_entry - text_rect[1]/2

        if len(self.all_symbols) != 0:
            rendered = self.maths_font.render('|' + joined, fgcolor=self.colour)[0]
            self.blit(rendered, (-text_rect[0], half))
        self.pointer_pos = self.maths_font.get_rect(pointer_join).width

        if self.event_manager.total_ticks % 20 == 0:
            if self.pointer_visible:
                self.pointer_visible = False
            else:
                self.pointer_visible = True

        if self.pointer_visible and self.is_current:
            pygame.draw.line(self, self.colour, (self.pointer_pos+3, half-2), (self.pointer_pos+3, half + text_rect[1] + 2))
