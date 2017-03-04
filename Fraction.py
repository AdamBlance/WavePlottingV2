from SpecialCharacter import SpecialCharacter
from TextContainer import TextContainer


class Fraction(SpecialCharacter):

    line_padding = 7  # PPP|PPP
    side_padding = 8

    def __init__(self, event_manager, font_size, top=None, bottom=None):

        self.event_manager = event_manager
        self.numerator = TextContainer(self.event_manager, font_size)
        self.denominator = TextContainer(self.event_manager, font_size)

        bound_size = self.get_frac_size()
        super().__init__(bound_size, [self.numerator, self.denominator], [font_size]*2)

    def get_frac_size(self):
        blank_size = self.numerator.blank_char
        if not self.numerator.all_symbols:
            top = blank_size
        else:
            pass
            # calculate size of textcontainer with special chars
        if not self.denominator.all_symbols:
            bottom = blank_size
        else:
            pass
            # calculate size of textcontainer with special chars

        total_height = top.height + self.line_padding + bottom.height
        total_width = max(top.width, bottom.width) + self.line_padding
        return total_width, total_height

