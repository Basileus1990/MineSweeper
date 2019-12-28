from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.dropdown import DropDown
from kivy.properties import StringProperty


class SettingsDropDownList(DropDown):

    # Keys are assigned ammount of boms
    difficulty_settings = {'Easy': '020', 'Normal': '040', 'Hard': '060'}

    def change_difficulty(self, button):
        main_widget.number_of_bombs = self.difficulty_settings[button.text]


class MainWidget(BoxLayout):

    number_of_bombs = StringProperty('020')

    def __init__(self, **kwargs):
        super(MainWidget, self).__init__(**kwargs)

        # Adding Drop down list for settings
        s_button = self.ids.SettingsButton
        dropdown = SettingsDropDownList()
        s_button.bind(on_release=dropdown.open)


class MineSweeperApp(App):
    def build(self):
        # Global variable containing MainWidget object
        global main_widget
        main_widget = MainWidget()

        return main_widget


if __name__ == '__main__':
    MineSweeperApp().run()
