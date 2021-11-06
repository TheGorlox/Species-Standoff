from importlib.abc import Loader
import kivy
import os
kivy.require('2.0.0') # replace with your current kivy version !

from kivy import *
from kivy.graphics import Color
from kivy.graphics import *

from kivy.lang import Builder

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout

class FightScreen(GridLayout):
    def __init__(self, **kwargs):
        super(FightScreen, self).__init__(**kwargs)
        self.cols = 2
        self.rows = 2
        self.add_widget(Label(text='Enemies'))
        self.add_widget(Label(text='Friends'))
        self.add_widget(Container())
        self.add_widget(Container())

class Container(GridLayout):
    def __init__(self, **kwargs):
        super(Container, self).__init__(**kwargs)
        self.cols = 5
        with self.canvas:
            Color(1.0, 0.5, 0.5, 1.0)

class speciesStandoff(App):

    def build(self):
        Builder.load_file("speciesStandoff.kv")
        return FightScreen()


if __name__ == '__main__':
    speciesStandoff().run()