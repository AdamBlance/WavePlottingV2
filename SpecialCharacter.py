import pygame.freetype


class SpecialCharacter(pygame.Surface):
    blank_character = '\u25a2'

    char_font = pygame.freetype.Font('media/DejaVuSans.ttf')

    def __init__(self, size, font_size):

        self.char_font.size(font_size)

        self.size = size
        self.font_size = font_size
        super().__init__(self.size)

    def get_blank_size(self):
        self.char_font.size(self.font_size)

        return pygame.Rect((0, 0), self.char_font.get_rect(self.blank_character))

    def reinit_surf(self):
        super().__init__(self.size)
