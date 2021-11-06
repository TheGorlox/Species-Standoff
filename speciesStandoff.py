from importlib.abc import Loader
import kivy
import os

from kivy.logger import BLACK
kivy.require('2.0.0') # replace with your current kivy version !

from kivy import *
from kivy.graphics import Color
from kivy.graphics import *

from kivy.lang import Builder

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout

Builder.load_file("speciesStandoff.kv")

class FightScreen(GridLayout):
    def __init__(self, **kwargs):
        super(FightScreen, self).__init__(**kwargs)
        self.cols = 2
        self.rows = 2
        self.spacing = 30
        self.add_widget(Label(text='Enemies'))
        self.add_widget(Label(text='Friends'))
        self.add_widget(Container())
        self.add_widget(Container())

class Container(GridLayout):
    def __init__(self, **kwargs):
        super(Container, self).__init__(**kwargs)
        self.cols = 5
        self.spacing = 10
        self.add_widget(Label(text='1'))
        self.add_widget(Label(text='2'))
        self.add_widget(Label(text='3'))
        self.add_widget(Label(text='4'))
        self.add_widget(Label(text='5'))

        

class speciesStandoff(App):

    def build(self):
        return FightScreen()


if __name__ == '__main__':
    speciesStandoff().run()