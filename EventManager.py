import pygame
from pygame.locals import *


class EventManager:

    def __init__(self):
        self.lmb_down = None
        self.lmb_up = None
        self.rmb_down = None
        self.rmb_up = None

        self.screen_focused = None
        self.has_quit = False

    def reset_states(self):
        self.lmb_down = False
        self.lmb_up = False
        self.rmb_down = False
        self.rmb_up = False

    def update(self):

        self.reset_states()

        for event in pygame.event.get():
            if event.type == QUIT:
                self.has_quit = True

            elif event.type == ACTIVEEVENT:
                self.screen_focused = event.gain

            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.lmb_down = True
                elif event.button == 3:
                    self.rmb_down = True

            elif event.type == MOUSEBUTTONUP:
                if event.button == 1:
                    self.lmb_up = True
                elif event.button == 3:
                    self.rmb_up = True
