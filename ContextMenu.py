import pygame
from GUIObject import GUIObject


class ContextMenu(GUIObject):
    colour = pygame.Color(100, 100, 100)
    highlight_colour = pygame.Color(255, 162, 31)
    context_menu_text = pygame.font.Font('DejaVuSans.ttf', 15)

    def __init__(self, pos, entries):
        self.entries = entries

        self.opacity = 255

        index = 0
        max_len = len(entries[0].text)
        for i in range(1, len(entries)):
            current = len(entries[i].text)
            if current > max_len:
                max_len = current
                index = i

        self.segment_size = (2*self.padding + self.context_menu_text.size(entries[index].text)[0],
                             2*self.padding + self.context_menu_text.get_height())

        self.state0 = pygame.Surface(self.segment_size)
        self.state0.fill(self.colour)

        self.state1 = pygame.Surface(self.segment_size)
        self.state1.fill(self.highlight_colour)

        size = self.segment_size[0], self.segment_size[1]*len(entries)
        super().__init__(pos, size)

    def set_surface(self):
        text_alignment = self.padding
        segment_alignment = 0
        for entry in self.entries:
            if self.is_moused_over(entry):
                self.blit(self.state1, (0, segment_alignment))
            else:
                self.blit(self.state0, (0, segment_alignment))
            rendered_text = self.context_menu_text.render(entry.text, True, (255, 255, 255))
            self.blit(rendered_text, (self.padding, text_alignment))
            if self.entries[-1] != entry:
                text_alignment += self.context_menu_text.get_height() + 2*self.padding
                segment_alignment += self.segment_size[1]

    def is_moused_over(self, entry):
        mouse_pos = pygame.mouse.get_pos()
        local_x = mouse_pos[0] - self.pos[0]
        local_y = mouse_pos[1] - self.pos[1]
        index = local_y//self.segment_size[1]

        if (0 <= index <= len(self.entries)-1) and (0 <= local_x <= self.segment_size[0]):
            # todo: Override equals
            return self.entries[index] == entry

    def fade_in(self):
        self.opacity = 0
