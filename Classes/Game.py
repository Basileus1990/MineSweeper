from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from Classes.Tile import Tile
import random


class Game:

    def __init__(self, main_widget):
        self.main_widget = main_widget
        self.tile_size = 30
        self.current_difficulty = 'Easy'  # a deffault one
        self.well_placed_bombs = 0
        self.original_number_of_bombs = 0

        self.change_difficulty(self.current_difficulty, 'NR')
        self.start_game()

    # Starts the game creating tiles and adding them to the game panel
    def start_game(self):
        # creating a two dimmentional list of tiles
        self.tiles = [[Tile(self, [i, j]) for j in range(
                      self.main_widget.size_of_game)] for i in range(
                      self.main_widget.size_of_game)]
        self.fill_tiles()
        self.add_tiles()

    # clears Game Panel
    def restart_game(self):
        self.main_widget.ids.Lose_Label.opacity = 0
        self.main_widget.ids.Win_Label.opacity = 0

        self.well_placed_bombs = 0

        self.main_widget.ids.Game_Panel.clear_widgets()
        self.change_difficulty(self.current_difficulty, 'NR')
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
        self.current_difficulty = key
        self.original_number_of_bombs = difficulty_settings[key][0]
        if len(args) == 0:
            self.restart_game()

    # Adds bombs and increases numbers of tiles around them
    def fill_tiles(self):
        r_pos = []
        for i in range(int(self.main_widget.number_of_bombs)):
            # checks if random position was't used earlier
            is_not_used = False
            while(not is_not_used):
                is_not_used = True
                r = [int(random.uniform(0,
                         self.main_widget.size_of_game)),
                     int(random.uniform(0,
                         self.main_widget.size_of_game))]
                for j in r_pos:
                    if(j == r):
                        is_not_used = False
                        break
                if(is_not_used):
                    r_pos.append(r)

            self.tiles[r_pos[i][0]][r_pos[i][1]].set_true_indentity('B')
            # adds 1 to every tile around
            for j in range(r_pos[i][0] - 1, r_pos[i][0] + 2):
                if(j < 0 or j > self.tiles.__len__()):
                    continue
                for k in range(r_pos[i][1] - 1, r_pos[i][1] + 2):
                    if(k < 0 or k > self.tiles.__len__()):
                        continue
                    try:
                        if(([j, k] == r_pos[i]) or
                           (self.tiles[j][k].true_indentity == 'B')):
                            continue
                        self.tiles[j][k].true_indentity = str(
                         int(self.tiles[j][k].true_indentity) + 1)
                    except IndexError:
                        continue

    # Adds the tiles to the Game_Panel
    def add_tiles(self):
        for i in self.tiles:
            layout = BoxLayout()
            for j in i:
                layout.add_widget(j)
            self.main_widget.ids.Game_Panel.add_widget(layout)

    def expose_all_tiles(self):
        for i in self.tiles:
            for tile in i:
                pass
                tile.expose_indentity()

    # Called when user cliks on 0tile. searchech aroud for 0tiles and exposes
    # them and all tiles around. Then calls itself for next 0tile
    def seek_for_other_0tiles(self, pos):
        for j in range(pos[0] - 1, pos[0] + 2):
            if(j < 0 or j > self.tiles.__len__()):
                continue
            for k in range(pos[1] - 1, pos[1] + 2):
                if(k < 0 or k > self.tiles.__len__()):
                    continue
                if([j, k] == pos):
                    continue
                try:
                    if(self.tiles[j][k].img_path[-9] == 'N'):
                        self.tiles[j][k].expose_indentity()
                        if(self.tiles[j][k].true_indentity == '0'):
                            self.seek_for_other_0tiles([j, k])
                except IndexError:
                    continue
