import Fraction
import Indice
import Root
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

        self.leave_left = False
        self.leave_right = False

        self.all_symbols = []
        self.divided_symbols = []

        self.pointer_index = 0

        self.pointer_visible = True

        self.special_character_index = 0

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

    def divide_symbols(self, up_to):
        array = self.all_symbols[:up_to]
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
        for x in self.divided_symbols:
            if type(x) == str:
                output.append(self.font.get_rect(x))
            else:
                x.render_symbol()
                output.append(x.get_rect())
        return output

    def find_total_size(self, symbol_rects):
        if symbol_rects:
            width = sum([rect.width for rect in symbol_rects])
            height = max([rect.height for rect in symbol_rects])
            return pygame.Rect((0, 0), (width, height))
        else:
            rect = self.font.get_rect(self.blank_char)
            return pygame.Rect((0, 0), (rect.height, rect.width))

    def render_symbols(self):

        self.divide_symbols(len(self.all_symbols))
        temp = self.divided_symbols.copy()
        symbol_rects = self.find_symbol_rects()

        total_size = self.find_total_size(symbol_rects)
        if not self.is_master_container:
            super().__init__((total_size.width+1, total_size.height))

        self.divide_symbols(self.pointer_index)
        pointer_rect = self.find_symbol_rects()

        self.divided_symbols = temp

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

        if self.pointer_visible and self.is_current:
            total_to_point = sum([x.width for x in pointer_rect])
            pygame.draw.line(self, self.colour, (total_to_point, 0), (total_to_point, self.get_rect().height))

    def backtrack_from_pointer(self):
        output = 0

        if self.all_symbols:
            if self.all_symbols[-1] not in [' ', '+', '-', '*']:
                array = self.all_symbols[:self.pointer_index]
                for i in range(len(array)-1, -1, -1):
                    if array[i] == ' ':
                        output = i+1
                        break

        track = self.pointer_index
        if self.pointer_index != output:
            track = output
            while self.all_symbols[:self.pointer_index][track] in ['+', '-', '*']:
                track += 1
        return track

    def compile_expression(self):
        full_expr = ''
        for item in self.all_symbols:
            if type(item) == str:
                full_expr += item
            elif type(item) == Fraction.Fraction:
                full_expr += '((%s)/(%s))' % (item.numerator.compile_expression(),
                                              item.denominator.compile_expression())
            elif type(item) == Indice.Indice:
                full_expr += '**(%s)' % item.indice.compile_expression()
            elif type(item) == Root.Root:
                if item.has_nroot:
                    full_expr += 'root(%s, %s)' % (item.contents.compile_expression(), item.nth_root.compile_expression())
                else:
                    full_expr += 'sqrt(%s)' % item.contents.compile_expression()

        return full_expr

    def update(self):

        self.leave_left = False
        self.leave_right = False

        self.fill(pygame.Color('black'))

        if self.event_manager.key_pressed == K_RIGHT and self.is_current:
            self.event_manager.key_pressed = None
            if self.pointer_index != len(self.all_symbols):
                if type(self.all_symbols[self.pointer_index]) == str:
                    self.pointer_index += 1
                else:
                    self.is_current = False
                    self.all_symbols[self.pointer_index].text_container_order[0].is_current = True
            else:
                if not self.is_master_container:
                    self.leave_right = True

        if self.event_manager.key_pressed == K_LEFT and self.is_current:
            self.event_manager.key_pressed = None
            if self.pointer_index != 0:
                if type(self.all_symbols[self.pointer_index-1]) == str:
                    self.pointer_index -= 1
                else:
                    self.is_current = False
                    self.all_symbols[self.pointer_index-1].text_container_order[-1].is_current = True
            else:
                if not self.is_master_container:
                    self.leave_left = True

        for i in range(len(self.all_symbols)):
            if type(self.all_symbols[i]) != str:
                if self.all_symbols[i].leave_right:
                    self.pointer_index = i+1
                    self.is_current = True
                elif self.all_symbols[i].leave_left:
                    self.pointer_index = i
                    self.is_current = True

        if self.is_current:
            pressed = self.event_manager.entered_chars()
            if pressed is not None:
                if pressed == 'backspace':
                    self.backspace()
                elif pressed == 'delete':
                    self.delete()
                elif pressed == '(':
                    print(self.compile_expression())
                elif pressed == '%':
                    self.is_current = False
                    symbol = Root.Root(self.event_manager, self.font.size, True)
                    # symbol.contents.is_current = True
                    symbol.contents.is_current = False
                    symbol.nth_root.is_current = True
                    self.add_symbol(symbol)
                elif pressed == '^':
                    self.is_current = False
                    symbol = Indice.Indice(self.event_manager, self.font.size*0.7)
                    symbol.indice.is_current = True
                    self.add_symbol(symbol)
                elif pressed == '/':
                    back = self.backtrack_from_pointer()

                    if back != self.pointer_index:
                        temp = self.all_symbols.copy()
                        del self.all_symbols[back:self.pointer_index]
                        symbol = Fraction.Fraction(self.event_manager, self.font.size*0.8, top=temp[back:self.pointer_index])
                        self.pointer_index -= self.pointer_index-back
                        symbol.numerator.is_current = False
                        symbol.denominator.is_current = True
                    else:
                        symbol = Fraction.Fraction(self.event_manager, self.font.size*0.8)
                        symbol.numerator.is_current = True
                        symbol.denominator.is_current = False

                    self.is_current = False
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

        for item in self.all_symbols:
            if type(item) != str:
                item.update()

        if len(self.all_symbols) != 0:
            self.render_symbols()
