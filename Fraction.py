import pygame
import pygame.freetype

class Fraction(pygame.Surface):

    fraction_font = pygame.freetype.Font('media/DejaVuSans.ttf')

    def __init__(self, top='\u25af', bottom='\u25af'):
        self.numerator = top
        self.denominator = bottom

        super().__init__()

        self.render()


    def render(self):
        self.