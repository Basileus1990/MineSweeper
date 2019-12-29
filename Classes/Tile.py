from kivy.uix.button import Button


class Tile(Button):
    def __init__(self, **kwargs):
        super(Tile, self).__init__(**kwargs)

        # 'N' means not cliked, 'P' means user planted a flag, 'B' means there
        # is a bomb and numbers mean how many bombs are around
        self.status = 'N'
