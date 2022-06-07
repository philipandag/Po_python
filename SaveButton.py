from Button import Button

class SaveButton(Button):
    def __init__(self, size: (int, int), pos: (int, int), window):
        super(SaveButton, self).__init__(size, pos, "Save")
        self.window = window

    def onClick(self):
        self.window.save_world()


