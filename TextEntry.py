import pygame
from pygame.locals import *
pygame.font.init()


class TextEntry(pygame.Surface):
    all_text_entries = []
    text_entry_text = pygame.font.Font('DejaVuSans.ttf', 20)

    ascii_dict = {
        '-': '',
        '=': '+'
    }

    def __init__(self, pos, colour):

        super().__init__((1000, 100), SRCALPHA)

        self.pos = pos
        self.colour = colour
        self.text = ''

        self.normal_string = 'abcdefghijklmnopqrstuvwxyz1234567890 '
        self.special_string = '-=+/<>!()^*|%'

    def add_text(self, char):
        mod_mask = pygame.key.get_mods()

        if chr(char).isalpha():
        if chr(char) in self.normal_string:
            if chr(char).isalpha():
                if mod_mask & 0b10000000000011:  # Combining bits if both are on
                    self.text += chr(char-32)
            self.text += chr(char)

        # elif char == 8:
        #         self.text = self.text[0:len(self.text)-1]

    def set_surface(self):
        self.fill((0, 0, 0, 0))
        entry_text = self.text_entry_text.render(self.text, True, (255, 255, 255))
        self.blit(entry_text, (0, 0))