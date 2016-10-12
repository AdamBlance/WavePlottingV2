class ContextMenuEntry:

    def __init__(self, text, function, *args):

        self.text = text
        self.function = function
        self.args = args
        self.depressed = False

    def call_function(self):
        self.function(*self.args)
