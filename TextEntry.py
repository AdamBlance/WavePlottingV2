import pygame
from pygame.locals import *
pygame.font.init()


class TextEntry(pygame.Surface):
    all_text_entries = []
    text_entry_text = pygame.font.SysFont('Courier New', 15, bold=True)

    def __init__(self, key_event, pos, colour, size):
        self.pos = pos
        self.colour = colour
        self.size = size
        self.text = ''

    def set_text(self):
        