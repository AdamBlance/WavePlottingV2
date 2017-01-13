import pygame
from pygame.locals import *
from GUIObject import GUIObject
pygame.font.init()


class TextEntry(GUIObject):
    all_text_entries = []

    ascii_dict = {
        '=': '+',
        '1': '!',
        '2': '@',
        '3': '#',
        '4': '$',
        '5': '%',
        '6': '^',
        '7': '7',
        '8': '*',
        '9': '(',
        '0': ')',
        ',': '<',
        '.': '>',
        ' ': ' '}

    def __init__(self, event_manager, pos, colour):

        super().__init__(pos, (1000, 100))

        self.colour = colour
        self.text = ''
        self.event_manager = event_manager

    def update(self):

        for char in self.event_manager.keys_pressed:
            string = chr(char)

            if (string.isalpha() or string in self.ascii_dict) and char < 128:
                if self.event_manager.shift_held:
                    if string in self.ascii_dict:
                        self.text += self.ascii_dict[string]
                    else:
                        self.text += chr(char-32)
                else:
                    self.text += string
            elif char == 8:
                self.text = self.text[:len(self.text)-1]

        self.fill((0, 0, 0, 0))
        entry_text = self.main_font.render(self.text, True, self.colour)
        self.blit(entry_text, (0, 0))
