from kivy.uix.button import Button
from kivy.properties import StringProperty


class Tile(Button):

    # 'N' means not cliked, 'P' means user planted a flag, 'B' means there
    # is a bomb, 0 - it is empty and numbers mean how many bombs are around
    img_dic_paths = {'N': 'Images\\NTile.png', '0': 'Images\\0Tile.png',
                     'P': 'Images\\PTile.png', 'B': 'Images\\BTile.png',
                     '1': 'Images\\1Tile.png', '2': 'Images\\2Tile.png',
                     '3': 'Images\\3Tile.png', '4': 'Images\\4Tile.png',
                     '5': 'Images\\5Tile.png', '6': 'Images\\6Tile.png',
                     '7': 'Images\\7Tile.png', '8': 'Images\\8Tile.png'}

    img_path = StringProperty(img_dic_paths['N'])  # default img path

    def __init__(self, game, **kwargs):
        super(Tile, self).__init__(**kwargs)
        self.game = game
        self.true_indentity = '0'

    def set_true_indentity(self, indentity):
        self.true_indentity = indentity

    def on_touch_down(self, touch):
        if(self.collide_point(*touch.pos)):
            if(touch.button == 'left'):
                self.expose_indentity()
            elif(touch.button == 'right'):
                if(self.img_path[7] == 'N'):
                    self.img_path = self.img_dic_paths['P']
                else:
                    self.img_path = self.img_dic_paths['N']

    def expose_indentity(self):
        self.img_path = self.img_dic_paths[self.true_indentity]
