import pygame
import pygame.freetype

from Fraction import Fraction
from SpecialCharacter import SpecialCharacter

from pygame.locals import *
from sympy.parsing.sympy_parser import \
    parse_expr, \
    standard_transformations, \
    implicit_multiplication_application, \
    function_exponentiation, \
    convert_xor
pygame.freetype.init()


class TextContainer(pygame.Surface):

    all_text_entries = []
    parsing_flags = standard_transformations + (implicit_multiplication_application,
                                                function_exponentiation,
                                                convert_xor)

    font_location = 'media/DejaVuSans.ttf'
    blank_char = '\u25a2'
    colour = pygame.Color('white')

# the size property dictates the actual bounds of the surface
# if not specified, the surface will scale with entered text by re-instantiating the Surface
# the font size variable will dictate the size of the font and the height of the Surface
# this is only true if the TextContainer contains no special characters - in that case the Surface will scale

    def __init__(self, event_manager, size=None, font_size=20):

        self.font = pygame.freetype.Font(self.font_location, font_size)

        self.size = size

        if self.size is None:
            self.is_master_container = False
        else:
            self.is_master_container = True

        self.event_manager = event_manager
        self.is_current = True

        self.all_symbols = []

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

    def add_symbol(self, symbol):
        self.all_symbols.insert(self.pointer_index, symbol)
        # self.pointer_index += 1

    def render_text(self):

        pass
        # must blit self.blank_char when TextContainer are blank (but only when part of SpecialCharacters)


    # delimiters could be changed - spaces for the now
    def backtrack_from_pointer(self):
        counter = self.pointer_index
        while self.all_symbols[counter] != ' ':
            counter -= 1
        return self.all_symbols[counter:self.pointer_index+1]

    def update(self):

        # POINTER STUFF

        # dec_pointer = self.pointer_index-1
        if self.event_manager.key_pressed == K_LEFT:
            if self.pointer_index == 0:
                if not self.is_master_container:
                    self.is_current = False
            else:
                self.pointer_index -= 1

        elif self.event_manager.key_pressed == K_RIGHT:
            if self.pointer_index == len(self.all_symbols):
                if not self.is_master_container:
                    self.is_current = False
            else:
                self.pointer_index += 1


        for symbol in self.all_symbols:
            if type(symbol).__bases__[0] == SpecialCharacter:




        # inc_pointer = self.pointer_index+1
        # if inc_pointer <= len(self.all_symbols) and self.event_manager.key_pressed == K_RIGHT:
        #     self.pointer_index = inc_pointer

        # ENTERED CHARS

        pressed = self.event_manager.entered_chars()
        if pressed is not None:
            if pressed == 'backspace':
                self.backspace()
            elif pressed == 'delete':
                self.delete()
            elif pressed == '/':

                # need to fix pointer first

                backtrack = self.backtrack_from_pointer()
                self.all_symbols.append(Fraction(self.event_manager, self.font.height))
            else:
                self.add_symbol(pressed)

        # REPLACE JOINS
        # NEW FORMAT IS ['5x

        joined = ''.join(self.all_symbols)
        pointer_join = ''.join(self.all_symbols[:self.pointer_index])

        half_entry = self.size[1]/2
        text_rect = self.font.get_rect('|')
        half = half_entry - text_rect[1]/2

        # REPLACE THIS WITH A RENDER FUNCTION THAT DOES SPECIALCHARS + RAW TEXT

        if len(self.all_symbols) != 0:
            rendered = self.font.render('|' + joined, fgcolor=self.colour)[0]
            self.blit(rendered, (-text_rect[0], half))
        self.pointer_pos = self.font.get_rect(pointer_join).width

        # BLINK POINTER

        if self.event_manager.total_ticks % 20 == 0:
            if self.pointer_visible:
                self.pointer_visible = False
            else:
                self.pointer_visible = True

        if self.pointer_visible and self.is_current:
            pygame.draw.line(self, self.colour, (self.pointer_pos+3, half-2), (self.pointer_pos+3, half + text_rect[1] + 2))
