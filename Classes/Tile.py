from kivy.uix.button import Button
from kivy.properties import StringProperty


class Tile(Button):

    img_dic_paths = {'N': 'Images\\NTile.png', '0': 'Images\\0Tile.png',
                     'P': 'Images\\PTile.png', 'B': 'Images\\BTile.png',
                     '1': 'Images\\1Tile.png', '2': 'Images\\2Tile.png',
                     '3': 'Images\\3Tile.png', '4': 'Images\\4Tile.png',
                     '5': 'Images\\5Tile.png', '6': 'Images\\6Tile.png',
                     '7': 'Images\\7Tile.png', '8': 'Images\\8Tile.png'}

    img_path = img_dic_paths['N']  # default img path

    def __init__(self, **kwargs):

        super(Tile, self).__init__(**kwargs)

        # 'N' means not cliked, 'P' means user planted a flag, 'B' means there
        # is a bomb, 0 - it is empty and numbers mean how many bombs are around
        #self.true_indentity = indentity
