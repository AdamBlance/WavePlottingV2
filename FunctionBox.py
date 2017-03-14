import pygame
import TextContainer
import Button


class FunctionBox(pygame.Surface):

    all_function_boxes = []

    def __init__(self, event_manager, size, font_size):

        super().__init__(size)
        self.text_entry = TextContainer.TextContainer(event_manager, font_size, size)
        self.button = Button.Button(event_manager, (size[0]-28, size[1]-50), self.text_entry.rand_colour, 'X',
                                    print, 'penis')

        self.wants_to_die = False

        self.all_function_boxes.append(self)

    def update(self):
        self.text_entry.update()
        self.button.update()
        self.blit(self.text_entry, (0, 0))
        self.blit(self.button, self.button.pos)

    def delete(self):
        self.wants_to_die = True
