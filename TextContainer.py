import Fraction
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

# Allowing y= AND x= functions is going to take too long to implement
# For the moment will not support an '=' symbol


class TextContainer(pygame.Surface):

    all_text_entries = []
    parsing_flags = standard_transformations + (implicit_multiplication_application,
                                                function_exponentiation,
                                                convert_xor)
    font_location = 'media/DejaVuSans.ttf'
    blank_char = '\u25a2'
    colour = pygame.Color('white')

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
                surface = self.font.render(self.divided_symbols[i], fgcolor=self.colour, bgcolor=pygame.Color('red'))[0]
                self.blit(surface, (width_sum, total_size.height/2 - symbol_rects[i].height/2))
            else:
                self.blit(self.divided_symbols[i], (width_sum, 0))
            width_sum += symbol_rects[i].width

    def backtrack_from_pointer(self):
        array = self.all_symbols[:self.pointer_index]
        for i in range(len(array)-1, -1, -1):
            if array[i] == ' ':
                return array[i+1:]
        else:
            return array

    def update(self):

        self.fill(pygame.Color('black'))

        if len(self.all_symbols) != 0:
            self.render_symbols()

        if self.event_manager.key_pressed == K_RIGHT and self.is_current:
            if self.pointer_index != len(self.all_symbols):
                if type(self.all_symbols[self.pointer_index + 1]) == str:
                    self.pointer_index += 1
                else:
                    if self.special_character_index+1 != len(self.all_symbols[self.pointer_index].text_container_order)-1:
                        self.is_current = False
                        self.special_character_index += 1
                        self.all_symbols[self.pointer_index+1].is_current = True
            else:
                if not self.is_master_container:
                    self.is_current = False

        pressed = self.event_manager.entered_chars()
        if pressed is not None:
            if pressed == 'backspace':
                self.backspace()
            elif pressed == 'delete':
                self.delete()
            elif pressed == '/':
                back = self.backtrack_from_pointer()
                self.all_symbols = self.all_symbols[:-len(back)]
                if back:
                    print('MAKING MORE ISTA')
                    symbol = Fraction.Fraction(self.event_manager, self.font.size*0.8, top=back)
                else:
                    symbol = Fraction.Fraction(self.event_manager, self.font.size*0.8)
                self.is_current = False
                symbol.denominator.is_current = True
                self.add_symbol(symbol)
                self.pointer_index += 1

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

        if self.is_master_container:
            print('master - ' + str(self.all_symbols))
        else:
            print('fraction - ' + str(self.all_symbols))

        for item in self.all_symbols:
            if type(item) != str:
                    item.update()
