from Button import Button

class NextTurnButton(Button):
    def __init__(self, size: (int, int), pos: (int, int), window):
        super(NextTurnButton, self).__init__(size, pos, "Save")
        self.window = window

    def onClick(self):
        self.window.save_world()


