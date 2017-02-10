from GUIObject import GUIObject
from Button import Button
from TextEntry import TextEntry


class FunctionBox(GUIObject):

    all_function_boxes = []

    def __init__(self, event_manager, pos, size, gui_object_blitted_to):
        super().__init__(pos, size)

        self.event_manager = event_manager

        self.blitted_to = gui_object_blitted_to
        self.fill((255, 255, 255))

        self.text_entry = TextEntry(event_manager, (0, 0), (255, 255, 255), gui_object_blitted_to=self)
        self.delete_button = Button(event_manager, (self.size[0] - 50, self.size[1] - 50), (200, 0, 0), 'X', print,
                                    'pressed_delete', gui_object_blitted_to=self)

        self.all_function_boxes.append(self)

    def update(self):
        if self.event_manager.keys_pressed:
            self.delete_button.update()
            self.text_entry.update()
            self.blit(self.delete_button, self.delete_button.pos)
            self.blit(self.text_entry, self.text_entry.pos)
