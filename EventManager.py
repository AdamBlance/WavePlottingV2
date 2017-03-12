import pygame
from pygame.locals import *


class EventManager:

    def __init__(self):
        self.lmb_down = False
        self.lmb_up = False
        self.lmb_held = False
        self.rmb_down = False
        self.rmb_up = False
        self.rmb_held = False
        self.scrolled_up = False
        self.scrolled_down = False
        self.shift_held = False
        self.key_pressed = None
        self.clock = pygame.time.Clock()
        self.total_ticks = 0

        self.has_quit = False

        self.ascii_dict = {
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
            '/': '/',
            '-': '-',
            ',': '<',
            '.': '>',
            ' ': ' '}

    def reset_states(self):
        self.lmb_down = False
        self.lmb_up = False
        self.rmb_down = False
        self.rmb_up = False
        self.scrolled_up = False
        self.scrolled_down = False
        self.key_pressed = None

    def entered_chars(self):
        if self.key_pressed is not None:
            char = self.key_pressed
            self.key_pressed = None
            string = chr(char)
            if (string.isalpha() or string in self.ascii_dict) and char < 128:
                if self.shift_held:
                    if string in self.ascii_dict:
                        return self.ascii_dict[string]
                    else:
                        return chr(char-32)
                else:
                    return string
            elif char == 8:
                return 'backspace'
            elif char == 127:
                return 'delete'

    def update(self):
        self.total_ticks += 1

        self.reset_states()

        for event in pygame.event.get():

            if event.type == QUIT:
                self.has_quit = True

            elif event.type == KEYDOWN:
                self.key_pressed = event.key

            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.lmb_down = True
                    self.lmb_held = True
                elif event.button == 3:
                    self.rmb_down = True
                    self.rmb_held = True
                elif event.button == 4:
                    self.scrolled_up = True
                elif event.button == 5:
                    self.scrolled_down = True

            elif event.type == MOUSEBUTTONUP:
                if event.button == 1:
                    self.lmb_up = True
                    self.lmb_held = False
                elif event.button == 3:
                    self.rmb_up = True
                    self.rmb_held = False

        self.shift_held = pygame.key.get_mods() & (KMOD_SHIFT | KMOD_CAPS)
