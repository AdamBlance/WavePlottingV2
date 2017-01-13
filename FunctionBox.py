from GUIObject import GUIObject
from Button import Button


class FunctionBox(GUIObject):

    def __init__(self, event_manager, pos, size, gui_object_blitted_to):
        super().__init__(pos, size)

        self.blitted_to = gui_object_blitted_to
        self.fill((67, 188, 53))
        if gui_object_blitted_to is not None:
            self.delete_button = Button(event_manager, (self.size[0] - 50, self.size[1] - 50), (200, 0, 0), 'X', print, 'thisisatest', gui_object_blitted_to=self)

    def update(self):
        self.delete_button.update()
        self.blit(self.delete_button, self.delete_button.pos)
