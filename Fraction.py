import pygame
import TextContainer
from SpecialCharacter import SpecialCharacter

pygame.init()


class Fraction(SpecialCharacter):

    line_padding = 7  # should always be odd if line is 1px thick
    side_padding = 8  # should always be even

    def __init__(self, event_manager, font_size, top=None, bottom=None):

        self.event_manager = event_manager

        self.numerator = TextContainer.TextContainer(self.event_manager, font_size)
        if top is not None:
            self.numerator.set_symbols_to(top)
        self.denominator = TextContainer.TextContainer(self.event_manager, font_size)
        if bottom is not None:
            self.denominator.set_symbols_to(bottom)

        self.leave_left = False
        self.leave_right = True

        self.render_symbol()

        rect = self.get_rect()
        super().__init__((rect.width, rect.height), [self.numerator, self.denominator])

    def render_symbol(self):

        self.numerator.render_symbols()
        self.denominator.render_symbols()

        top = self.numerator.get_rect()
        bottom = self.denominator.get_rect()

        total_height = top.height + self.line_padding + bottom.height
        total_width = max(top.width, bottom.width) + self.line_padding

        super().reinit_surface((total_width, total_height))

        halfway = top.height + (self.line_padding-1)/2
        pygame.draw.line(self, pygame.Color('white'), (0, halfway), (total_width, halfway))

        top_centre = total_width/2 - top.width/2
        self.blit(self.numerator, (top_centre, 0))

        bottom_centre = total_width/2 - bottom.width/2
        self.blit(self.denominator, (bottom_centre, total_height-bottom.height))

    def update(self):

        self.leave_left = False
        self.leave_right = False

        self.denominator.update()
        self.numerator.update()

        current_index = -1
        for i in range(len(self.text_container_order)):
            if self.text_container_order[i].is_current:
                current_index = i

        for box in self.text_container_order:
            if box.leave_left:
                if current_index == 0:
                    print('left left')
                    box.is_current = False
                    self.leave_left = True
                else:
                    box.is_current = False
                    current_box = self.text_container_order[current_index-1]
                    current_box.is_current = True
                    current_box.pointer_index = len(current_box.all_symbols)

            elif box.leave_right:
                if current_index == len(self.text_container_order)-1:
                    self.leave_right = True
                    box.is_current = False
                else:
                    box.is_current = False
                    current_box = self.text_container_order[current_index+1]
                    current_box.is_current = True
                    current_box.pointer_index = 0

