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

    def __init__(self, size, text_container_order, font_sizes):

        self.text_container_order = []

    def get_blank_size(self, container_index):
        char = self.text_container_order[container_index].blank_char
        font = self.text_container_order[container_index].font.get_rect(char)
        return pygame.Rect((0, 0), (font.width, font.height))

    def reinit_surf(self):
        super().__init__(self.size)
