import pygame
import pygame.freetype
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

    def __init__(self, event_manager, font_size=20, size=None):

        self.font = pygame.freetype.Font(self.font_location, font_size)

        self.event_manager = event_manager
        self.is_current = True

        self.all_symbols = []
        self.divided_symbols = []

        self.pointer_pos = 0
        self.pointer_index = 0
        self.pointer_visible = True

        self.special_character_index = -1

        if size is None:
            self.is_master_container = False
            super().__init__((0, 0))
        else:
            self.is_master_container = True
            super().__init__(size)

    def backspace(self):
        if self.pointer_index != 0:
            self.pointer_index -= 1
            print(self.pointer_index)
            print(self.all_symbols)
            self.all_symbols.pop(self.pointer_index)

    def delete(self):
        if self.pointer_index != len(self.all_symbols):
            self.all_symbols.pop(self.pointer_index)

    def add_symbol(self, symbol):
        self.all_symbols.insert(self.pointer_index, symbol)

    def set_symbols_to(self, symbols_list):
        self.all_symbols = symbols_list

    def divide_symbols(self):
        array = self.all_symbols
        output = []
        current_string = ''
        for i in range(0, len(array)):
            if type(array[i]) == str:
                current_string += array[i]
                if i == len(array)-1:
                    output.append(current_string)
            else:
                output.append(current_string)
                output.append(array[i])
                current_string = ''
        self.divided_symbols = output

    def find_symbol_rects(self):
        output = []
        if len(self.divided_symbols) == 0 and not self.is_master_container:
            output.append(self.font.get_rect(self.blank_char))
        for x in self.divided_symbols:
            if type(x) == str:
                output.append(self.font.get_rect(x))
            else:
                x.render_symbol()
                output.append(x.get_rect())
        return output

    @staticmethod
    def find_total_size(symbol_rects):
        width = sum([rect.width for rect in symbol_rects])
        height = max([rect.height for rect in symbol_rects])
        return pygame.Rect((0, 0), (width, height))

    def render_symbols(self):
        self.divide_symbols()
        symbol_rects = self.find_symbol_rects()
        total_size = self.find_total_size(symbol_rects)
        if not self.is_master_container:
            super().__init__((total_size.width, total_size.height))

        width_sum = 0
        if len(self.all_symbols) == 0:
            surface = self.font.render(self.blank_char, fgcolor=self.colour)[0]
            self.blit(surface, (total_size.width/2 - self.font.get_rect(self.blank_char).width/2,
                                total_size.height/2 - self.font.get_rect(self.blank_char).height/2))
        for i in range(0, len(self.divided_symbols)):
            if type(self.divided_symbols[i]) == str:
                surface = self.font.render(self.divided_symbols[i], fgcolor=self.colour)[0]
                self.blit(surface, (width_sum, total_size.height/2 - symbol_rects[i].height/2))
            else:
                self.blit(self.divided_symbols[i], (width_sum, 0))
            width_sum += symbol_rects[i].width

    def backtrack_from_pointer(self):
        operators = '+-*'
        if self.all_symbols[-1] in operators + '=' + ' ':
            return ''
        equals_pos = len(self.all_symbols)-1 - self.all_symbols[::-1].index('=')
        if equals_pos != -1:
            end = 0
        else:
            end = equals_pos
        for i in range(len(self.all_symbols)-1, end-1, -1):
            if self.all_symbols[i] == ' ':
                if self.all_symbols[i+1] in operators:
                    return self.all_symbols[i+2:]
                else:
                    return self.all_symbols[equals_pos+1:]

    def update(self):

        self.fill(pygame.Color('black'))

        if len(self.all_symbols) != 0:
            self.render_symbols()

        if self.event_manager.key_pressed == K_RIGHT and self.is_current:
            print(self.pointer_index, len(self.all_symbols))
            if self.pointer_index != len(self.all_symbols):
                if type(self.all_symbols[self.pointer_index + 1]) == str:

                    self.pointer_index += 1
                else:
                    if self.special_character_index+1 != len(self.all_symbols[self.pointer_index].text_container_order)-1:
                        self.is_current = False
                        self.special_character_index += 1
                        self.all_symbols[self.pointer_index+1].is_current = True
            else:
                self.is_current = False

        pressed = self.event_manager.entered_chars()
        if pressed is not None:
            if pressed == 'backspace':
                self.backspace()
            elif pressed == 'delete':
                self.delete()
            else:
                self.add_symbol(pressed)
                self.pointer_index += 1

        if self.event_manager.total_ticks % 20 == 0:
            if self.pointer_visible:
                self.pointer_visible = False
            else:
                self.pointer_visible = True
        if self.pointer_visible and self.is_current:
            rects = self.find_symbol_rects()
            temp = sum([x.width for x in rects[:self.pointer_index]])
            pygame.draw.line(self, self.colour, (temp, 0), (temp, self.get_rect().height))

        print(self.pointer_index, self.all_symbols)
