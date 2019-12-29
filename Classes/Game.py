from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from Classes.Tile import Tile


class Game:
    def __init__(self, main_widget):
        self.main_widget = main_widget
        self.tile_size = 30
        # creating a two dimmentional list of tiles
        self.tiles = [[Tile() for j in range(
                      self.main_widget.size_of_game)] for i in range(
                      self.main_widget.size_of_game)]

    # changes number of bombs, size of game based on wchich key is given and
    # changes size of the window
    def change_difficulty(self, key):
        difficulty_settings = {'Easy':   ['040', 20],
                               'Normal': ['070', 25],
                               'Hard':   ['150', 30]}

        self.main_widget.number_of_bombs = difficulty_settings[key][0]
        self.main_widget.size_of_game = difficulty_settings[key][1]
        Window.size = (difficulty_settings[key][1] * self.tile_size,
                       difficulty_settings[key][1] * self.tile_size + 60)

    # Adds the tiles to the Game_Panel
    def add_tiles(self):
        for i in self.tiles:
            layout = BoxLayout()
            for j in i:
                layout.add_widget(j)
            self.main_widget.ids.Game_Panel.add_widget(layout)
