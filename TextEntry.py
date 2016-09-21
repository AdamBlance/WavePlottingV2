import pygame
from pygame.locals import *
pygame.font.init()


class TextEntry(pygame.Surface):
    all_text_entries = []
    text_entry_text = pygame.font.Font('DejaVuSans.ttf', 15)

    ascii_dict = {
        '=': '+',
        '1': '!',
        '2': '2',
        '3': '3',
        '4': '4',
        '5': '%',
        '6': '^',
        '7': '7',
        '8': '*',
        '9': '(',
        '0': ')',
        ',': '<',
        '.': '>',
        ' ': ' '}

    def __init__(self, pos, colour):

        super().__init__((1000, 100), SRCALPHA)

        self.pos = pos
        self.colour = colour
        self.text = ''

    def add_text(self, char):
        string = chr(char)
        shifted = pygame.key.get_mods() & (KMOD_SHIFT | KMOD_CAPS)

        if (string.isalpha() or string in self.ascii_dict) and char < 128:
            if shifted:
                if string in self.ascii_dict:
                    self.text += self.ascii_dict[string]
                else:
                    self.text += chr(char-32)
            else:
                self.text += string
        elif char == 8:
            self.text = self.text[:len(self.text)-1]

    def set_surface(self):
        self.fill((0, 0, 0, 0))
        entry_text = self.text_entry_text.render(self.text, True, self.colour)
        self.blit(entry_text, (0, 0))