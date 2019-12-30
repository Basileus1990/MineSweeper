from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from Classes.Tile import Tile


class Game:

    difficulty = ''

    def __init__(self, main_widget):
        self.main_widget = main_widget
        self.tile_size = 30

        self.change_difficulty('Easy', 'NR')
        self.start_game()

    # Starts the game creating tiles and adding them to the game panel
    def start_game(self):
        # creating a two dimmentional list of tiles
        self.tiles = [[Tile() for j in range(
                      self.main_widget.size_of_game)] for i in range(
                      self.main_widget.size_of_game)]
        self.add_tiles()

    # clears Game Panel
    def restart_game(self):
        # This strange line rapairs a bug where after restart drop down can't
        # be openned
        self.main_widget.dropdown.open

        self.main_widget.ids.Game_Panel.clear_widgets()
        self.start_game()

    # changes number of bombs, size of game based on wchich key is given,
    # size of the window and restarts the game if there is no additional args
    def change_difficulty(self, key, *args):
        difficulty_settings = {'Easy':   ['040', 20],
                               'Normal': ['070', 25],
                               'Hard':   ['150', 30]}

        self.main_widget.number_of_bombs = difficulty_settings[key][0]
        self.main_widget.size_of_game = difficulty_settings[key][1]
        Window.size = (difficulty_settings[key][1] * self.tile_size,
                       difficulty_settings[key][1] * self.tile_size + 60)
        if len(args) == 0:
            self.restart_game()

    # Adds the tiles to the Game_Panel
    def add_tiles(self):
        for i in self.tiles:
            layout = BoxLayout()
            for j in i:
                layout.add_widget(j)
            self.main_widget.ids.Game_Panel.add_widget(layout)
