import pygame
import pygame.freetype
pygame.freetype.init()

#  |0|
# _____
# \
#  \
#  /    (|2|)
# /
# _____
# x=|1|


class SpecialCharacter(pygame.Surface):
    font_location = 'media/DejaVuSans.ttf'

    def __init__(self, size, text_container_order):

        self.text_container_order = text_container_order

    # @staticmethod
    def reinit_surface(self, size):
        super().__init__(size)
