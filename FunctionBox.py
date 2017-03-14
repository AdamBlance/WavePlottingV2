import pygame
from GUIObject import GUIObject
import TextContainer
import Button


class FunctionBox(GUIObject):

    all_function_boxes = []

    def __init__(self, event_manager, pos, size, font_size):

        self.event_manager = event_manager

        self.pos = pos
        self.size = size

        super().__init__(pos, size)
        self.text_entry = TextContainer.TextContainer(event_manager, font_size, size)
        self.button = Button.Button(event_manager, (size[0]-28, size[1]-50), self.text_entry.rand_colour, 'X',
                                    self.queue_deletion, gui_object_blitted_to=self)

        self.wants_to_die = False

        self.all_function_boxes.append(self)

    def queue_deletion(self):
        self.wants_to_die = True

    def update(self):
        if self.text_entry.is_on:
            self.text_entry.update()
        self.button.update()
        self.blit(self.text_entry, (0, 0))
        self.blit(self.button, self.button.pos)

    def delete(self):
        del self.text_entry
        del self.button
