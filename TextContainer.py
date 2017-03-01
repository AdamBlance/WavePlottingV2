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


class TextContainer(GUIObject):
    all_text_entries = []
    parsing_flags = standard_transformations + (implicit_multiplication_application,
                                                function_exponentiation,
                                                convert_xor)

    maths_font = pygame.freetype.Font('DejaVuSans.ttf', 15)

    colour = pygame.Color('white')

    def __init__(self, event_manager, pos, gui_object_blitted_to=None):
        super().__init__(pos, (400, 100))

        self.event_manager = event_manager
        self.all_chars = []
        self.font_height = self.main_font.get_height()
        self.is_current = True
        self.pointer = 0
        self.pointer_index = 0

        self.pointer_visible = True

    def make_new(self):
        # self.all_chars.append(TextContainer(event_manager, ))
        pass

    def update(self):

        self.fill(pygame.Color('black'))

        if not (0 < self.pointer_index < len(self.all_chars)):
            if self.event_manager.key_pressed == K_LEFT:
                self.pointer_index -= 1
            if self.event_manager.key_pressed == K_RIGHT:
                self.pointer_index += 1

        pressed = self.event_manager.entered_chars()
        if pressed is not None:
            if pressed != 'backspace':
                self.all_chars.insert(self.pointer, pressed)
            else:
                self.all_chars = self.all_chars[:-1]

        joined = ''.join(self.all_chars)

        half_entry = self.size[1]/2
        text_height = self.maths_font.get_rect('\u2588')[1]
        half = half_entry - text_height/2

        if len(self.all_chars) != 0:
            rendered = self.maths_font.render('|' + joined, fgcolor=pygame.Color('white'))[0]
            self.blit(rendered, (-1, half))
        self.pointer = self.main_font.size(joined)[0]
        if self.event_manager.total_ticks % 20 == 0:
            if self.pointer_visible:
                self.pointer_visible = False
            else:
                self.pointer_visible = True

        if self.pointer_visible:
            pygame.draw.line(self, pygame.Color('white'), (self.pointer+3, half), (self.pointer+3, half + text_height))
