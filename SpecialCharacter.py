import pygame
import pygame.freetype
pygame.freetype.init()

#  |0|
# _____
# \
#  \
#  /    (|2|)
# /
# _____
# x=|1|


class SpecialCharacter(pygame.Surface):
    font_location = 'media/DejaVuSans.ttf'

    def __init__(self, event_manager, text_container_order):

        self.event_manager = event_manager
        self.text_container_order = text_container_order

        self.leave_left = False
        self.leave_right = False

    def reinit_surface(self, size):
        super().__init__(size)

    def pointer_update(self):

        self.leave_left = False
        self.leave_right = False

        current_index = -1
        for i in range(len(self.text_container_order)):
            if self.text_container_order[i].is_current:
                current_index = i

        for box in self.text_container_order:
            if box.leave_left:
                if current_index == 0:
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

    # TODO: Move to next box when space is pressed
    # TODO: Make the delete key move back into previous box
