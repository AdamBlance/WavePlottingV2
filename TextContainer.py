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

    maths_font = pygame.freetype.Font('DejaVuSans.ttf', 20)

    colour = pygame.Color('white')

    def __init__(self, event_manager, pos, gui_object_blitted_to=None):
        super().__init__(pos, (400, 100))

        self.event_manager = event_manager
        self.all_chars = []
        self.font_height = self.maths_font.height
        self.is_current = True
        self.pointer_pos = 0
        self.pointer_index = 0

        self.pointer_visible = True

    def make_new(self):
        self.all_chars.append(TextContainer(self.event_manager, (self.pointer_pos, self.maths_font.height*0.3)))

    def join_chars(self):
        output = ''
        for char in self.all_chars:
            if type(char) == str:
                output += char

    def update(self):
        self.fill(pygame.Color('black'))

        dec_pointer = self.pointer_index-1
        if dec_pointer >= 0 and self.event_manager.key_pressed == K_LEFT:
            self.pointer_index = dec_pointer

        inc_pointer = self.pointer_index+1
        if inc_pointer <= len(self.all_chars) and self.event_manager.key_pressed == K_RIGHT:
            self.pointer_index = inc_pointer

        pressed = self.event_manager.entered_chars()
        if pressed is not None:
            if pressed == 'backspace':
                if self.pointer_index != 0:
                    self.pointer_index -= 1
                    self.all_chars.pop(self.pointer_index)
            elif pressed == 'delete':
                if self.pointer_index != len(self.all_chars):
                    self.all_chars.pop(self.pointer_index)
            else:
                self.all_chars.insert(self.pointer_index, pressed)
                self.pointer_index += 1

        joined = ''.join(self.all_chars)
        pointer_join = ''.join(self.all_chars[:self.pointer_index])

        half_entry = self.size[1]/2
        text_height = self.maths_font.get_rect('|')[1]
        half = half_entry - text_height/2

        if len(self.all_chars) != 0:
            rendered = self.maths_font.render('|' + joined, fgcolor=pygame.Color('white'))[0]
            self.blit(rendered, (-self.maths_font.get_rect('|').width, half))
        self.pointer_pos = self.maths_font.get_rect(pointer_join).width

        if self.event_manager.total_ticks % 20 == 0:
            if self.pointer_visible:
                self.pointer_visible = False
            else:
                self.pointer_visible = True

        if self.pointer_visible:
            pygame.draw.line(self, pygame.Color('white'), (self.pointer_pos+3, half-2), (self.pointer_pos+3, half + text_height + 2))
