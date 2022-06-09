from Button import Button

class SpinnerButton(Button):
    def __init__(self, size: (int, int), pos: (int, int), values):
        self.list = values
        self.selected_index = 0
        super(SpinnerButton, self).__init__(size, pos, self.list[self.selected_index].__name__)

    def onClick(self):
        self.selected_index += 1
        if self.selected_index >= len(self.list):
            self.selected_index = 0
        self.setText(self.list[self.selected_index].__name__)

    def get_value(self):
        return self.list[self.selected_index]


