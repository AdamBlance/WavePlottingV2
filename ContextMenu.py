import pygame
from GUIObject import GUIObject


class ContextMenu(GUIObject):
    colour = pygame.Color(100, 100, 100)
    highlight_colour = pygame.Color(255, 162, 31)

    def __init__(self, event_manager, pos, entries):

        self.event_manager = event_manager

        self.entries = entries

        index = 0
        max_len = len(entries[0].text)
        for i in range(1, len(entries)):
            current = len(entries[i].text)
            if current > max_len:
                max_len = current
                index = i

        self.segment_size = (2*self.padding + self.main_font.size(entries[index].text)[0],
                             2*self.padding + self.main_font.get_height())

        self.grey = pygame.Surface(self.segment_size)
        self.grey.fill(self.colour)

        self.highlighted = pygame.Surface(self.segment_size)
        self.highlighted.fill(self.highlight_colour)

        self.all_rendered_states = {}

        for i in range(0, len(self.entries)):
            rendered_text = self.main_font.render(self.entries[i].text, True, self.font_colour)
            grey_copy = self.grey.copy()
            highlighted_copy = self.highlighted.copy()

            grey_copy.blit(rendered_text, (self.padding, self.padding))
            highlighted_copy.blit(rendered_text, (self.padding, self.padding))

            self.all_rendered_states['state_%s' % i] = grey_copy
            self.all_rendered_states['highlight_state_%s' % i] = highlighted_copy

        size = self.segment_size[0], self.segment_size[1]*len(entries)
        super().__init__(pos, size)

    def update(self):
        segment_alignment = 0
        for i in range(0, len(self.entries)):
            if self.is_moused_over(self.entries[i]):
                self.blit(self.all_rendered_states['highlight_state_%s' % i], (0, segment_alignment))
                if self.event_manager.lmb_down:
                    self.entries[i].depressed = True
                if self.event_manager.lmb_up and self.entries[i].depressed:
                    self.entries[i].depressed = False
                    self.entries[i].call_function()
            else:
                self.blit(self.all_rendered_states['state_%s' % i], (0, segment_alignment))
            if self.entries[-1] != self.entries[i]:
                segment_alignment += self.segment_size[1]

    def is_moused_over(self, entry):
        mouse_pos = pygame.mouse.get_pos()
        local_x = mouse_pos[0] - self.pos[0]
        local_y = mouse_pos[1] - self.pos[1]
        index = local_y//self.segment_size[1]

        if (0 <= index <= len(self.entries)-1) and (0 <= local_x <= self.segment_size[0]):
            return self.entries[index] == entry
