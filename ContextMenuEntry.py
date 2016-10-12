class ContextMenuEntry:

    def __init__(self, text, icon, function, *args):

        self.text = text
        self.icon = icon
        self.function = function
        self.args = args