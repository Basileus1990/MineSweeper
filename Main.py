# disabling resizing
from kivy.config import Config
Config.set('graphics', 'resizable', 0)

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.dropdown import DropDown
from kivy.properties import StringProperty
from kivy.properties import NumericProperty
from Classes.Game import Game


class SettingsDropDownList(DropDown):
    def change_difficulty(self, key):
        main_widget.game.change_difficulty(key)


class MainWidget(BoxLayout):

    number_of_bombs = StringProperty()
    size_of_game = NumericProperty(20)  # Repair this the future

    def __init__(self, **kwargs):
        super(MainWidget, self).__init__(**kwargs)

        # Adding Drop down list for settings
        s_button = self.ids.SettingsButton
        dropdown = SettingsDropDownList()
        s_button.bind(on_release=dropdown.open)

        # Game is created
        self.game = Game(self)

        # Sets difficulty to easy as default
        self.game.change_difficulty('Easy')

        self.game.add_tiles()


class MineSweeperApp(App):
    def build(self):
        # Global variable containing MainWidget object
        global main_widget
        main_widget = MainWidget()

        return main_widget


if __name__ == '__main__':
    MineSweeperApp().run()
