from kivy.uix.button import Button
from kivy.properties import StringProperty
import os
import pathlib


class Tile(Button):

    # 'N' means not cliked, 'P' means user planted a flag, 'B' means there
    # is a bomb, 0 - it is empty and numbers mean how many bombs are around
    img_dic_paths = {'N': 'Images\\NTile.png', '0': 'Images\\0Tile.png',
                     'P': 'Images\\PTile.png', 'B': 'Images\\BTile.png',
                     '1': 'Images\\1Tile.png', '2': 'Images\\2Tile.png',
                     '3': 'Images\\3Tile.png', '4': 'Images\\4Tile.png',
                     '5': 'Images\\5Tile.png', '6': 'Images\\6Tile.png',
                     '7': 'Images\\7Tile.png', '8': 'Images\\8Tile.png'}

    img_path = StringProperty(os.path.join(
     pathlib.Path(__file__).parent.parent.absolute(),
     img_dic_paths['N']))

    def __init__(self, game, pos, **kwargs):
        super(Tile, self).__init__(**kwargs)
        self.game = game
        self.true_indentity = '0'
        self.positon = pos

    def change_img_path(self, to_which_path):
        self.img_path = os.path.join(
         pathlib.Path(__file__).parent.parent.absolute(),
         self.img_dic_paths[to_which_path])

    def set_true_indentity(self, indentity):
        self.true_indentity = indentity

    def on_touch_down(self, touch):
        if(self.collide_point(*touch.pos)):
            if(touch.button == 'left'):
                if(self.img_path[-9] == 'P'):
                    return
                elif(self.true_indentity == 'B'):  # Lose conditon
                    self.game.main_widget.ids.Lose_Label.opacity = 1
                    self.game.expose_all_tiles()
                    return

                self.expose_indentity()
                if(self.true_indentity == '0'):
                    self.game.seek_for_other_0tiles(self.positon)

            elif(touch.button == 'right'):
                if(self.img_path[-9] == 'N'):
                    self.change_img_path('P')
                    self.change_number_of_bombs(-1)
                    self.change_well_placed_bombs(1)

                elif(self.img_path[-9] == 'P'):
                    self.change_img_path('N')
                    self.change_number_of_bombs(1)
                    self.change_well_placed_bombs(-1)

    def expose_indentity(self):
        self.change_img_path(self.true_indentity)

    # adds how_change to number_of_bombs and fromats it
    def change_number_of_bombs(self, how_change):
        n = ''
        if('-' in self.game.main_widget.number_of_bombs):
            n = self.game.main_widget.number_of_bombs.split('-')[1]
            n = str((int(n) - int(n) * 2) + how_change)
        else:
            n = str(int(self.game.main_widget.number_of_bombs) + how_change)
        for i in range(3 - n.__len__()):
            n = '0' + n
        self.game.main_widget.number_of_bombs = n

    def change_well_placed_bombs(self, how_change):
        if(self.true_indentity == 'B'):
            self.game.well_placed_bombs += how_change
            if(self.game.well_placed_bombs ==
                    self.game.original_number_of_bombs and
                    self.game.main_widget.number_of_bombs == 0):  # Win condito
                self.game.main_widget.ids.Win_Label.opacity = 1
                self.game.expose_all_tiles()
