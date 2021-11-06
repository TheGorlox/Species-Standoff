from kivy.core.audio import SoundLoader
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.screenmanager import FadeTransition
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from animals.animal import *
from kivy.core.audio import SoundLoader
from kivy.core.audio import Sound
Builder.load_file("fight.kv")
# Declare both screens


class TitleScreen(Screen):
    pass


class SettingsScreen(Screen):
    def stop_music(self):
        if sound.state == 'play':
            sound.stop()
        else:
            sound.play()


class MapScreen(Screen):
    def change_transition(self, type):
        if type == "fade":
            sm.transition = FadeTransition(duration=0.6)
        if type == "slide":
            sm.transition = SlideTransition()


class ShopScreen(Screen):
    pass


# from kivy_garden.draggable import KXDraggableBehavior
animals = []
# for i in range(5):
animals.append(Cow())
animals.append(Chicken())
animals.append(Fish())


class BoxLayoutExample(BoxLayout):
    def __init__(self, **kwargs):
        super(BoxLayoutExample, self).__init__(**kwargs)
        for i in animals:
            # print(i.image)
            self.ids.test.add_widget(Image(source=i.image))

    def say_hello(self):
        self.ids.test.add_widget(Image(source='./images/cow.png'))

    pass


class MainWidget():
    pass


sound = SoundLoader.load('./sound/speciesstandoff3.wav')
if sound:
    sound.loop = True
    sound.play()
# sound = SoundLoader.load('./sound/speciesstandoff 3.wav')


class FightApp(App):
    def build(self):

        global sm
        sm = ScreenManager()
        sm.add_widget(TitleScreen(name='menu'))
        sm.add_widget(SettingsScreen(name='settings'))
        sm.add_widget(MapScreen(name='map'))
        sm.add_widget(ShopScreen(name='shop'))

        return sm


if __name__ == '__main__':
    FightApp().run()
