import pygame
import TextContainer
from SpecialCharacter import SpecialCharacter

pygame.init()


class Fraction(SpecialCharacter):

    line_padding = 7  # should always be odd if line is 1px thick
    side_padding = 8  # should always be even

    def __init__(self, event_manager, font_size, top=None, bottom=None):

        self.event_manager = event_manager

        self.numerator = TextContainer.TextContainer(self.event_manager, font_size)
        if top is not None:
            self.numerator.set_symbols_to(top)
        self.denominator = TextContainer.TextContainer(self.event_manager, font_size)
        if bottom is not None:
            self.denominator.set_symbols_to(bottom)

        self.render_symbol()

        super().__init__(self.event_manager, [self.numerator, self.denominator])

    def render_symbol(self):

        self.numerator.render_symbols()
        self.denominator.render_symbols()

        top = self.numerator.get_rect()
        bottom = self.denominator.get_rect()

        total_height = top.height + self.line_padding + bottom.height
        total_width = max(top.width, bottom.width) + self.line_padding

        super().reinit_surface((total_width, total_height))

        halfway = top.height + (self.line_padding-1)/2
        pygame.draw.line(self, pygame.Color('white'), (0, halfway), (total_width, halfway))

        top_centre = total_width/2 - top.width/2
        self.blit(self.numerator, (top_centre, 0))

        bottom_centre = total_width/2 - bottom.width/2
        self.blit(self.denominator, (bottom_centre, total_height-bottom.height))

    def update(self):

        self.denominator.update()
        self.numerator.update()
        self.pointer_update()