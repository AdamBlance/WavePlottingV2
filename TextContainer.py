import pygame
import pygame.freetype
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

        self.pointer_visible = True

    def make_new(self):
        # self.all_chars.append(TextContainer(event_manager, ))
        pass

    def update(self):

        self.fill(pygame.Color('black'))

        pressed = self.event_manager.entered_chars()
        if pressed is not None:
            if pressed != 'backspace':
                self.all_chars.append(pressed)
            else:
                self.all_chars = self.all_chars[:-1]

        joined = ''.join(self.all_chars)

        text_height = self.maths_font.get_rect('\u2588')[1]
        halfway = self.size[1]/2 - text_height/2

        # ONLY ONE CHARACTER AT A TIME

        if len(self.all_chars) != 0:
            rendered = self.maths_font.render('|' + joined, fgcolor=pygame.Color('white'), bgcolor=pygame.Color('blue'))[0]
            blit_height = text_height - rendered.get_rect().height
            self.blit(rendered, (0, halfway + blit_height))
        self.pointer = self.main_font.size(joined)[0]
        if self.event_manager.total_ticks % 20 == 0:
            if self.pointer_visible:
                self.pointer_visible = False
            else:
                self.pointer_visible = True

        if self.pointer_visible:
            pygame.draw.line(self, pygame.Color('white'), (self.pointer+3, halfway), (self.pointer, halfway + 15))
