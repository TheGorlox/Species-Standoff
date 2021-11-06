from kivy.core.audio import SoundLoader
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from animals.animal import *
from kivy.core.audio import SoundLoader
from kivy.core.audio import Sound
Builder.load_string("""
<TitleScreen>:
    Image:
        allow_stretch:1
        keep_ratio:0
        source:"./images/stars.zip"
    BoxLayout: 
        orientation: "vertical"
        
            
        Label:
            font_size: 42
            text: "Species Standoff"
        BoxLayout:
            orientation: "vertical"
            Button:
                text: 'Play'
                size_hint: .5, .5
                pos_hint: {"center_x": .5}
                
                background_color: .9,.1,.8
                on_press:
                    root.manager.transition.direction = 'up'
                    root.manager.current = 'map'
            Button:
                text: 'Settings'
                size_hint: .1, .1
                pos_hint: {"center_x": .8}

                background_color: .9,.1,.8
                on_press:
                    root.manager.transition.direction = "left"
                    root.manager.current = 'settings'

<SettingsScreen>:
    BoxLayout:
        orientation: "vertical"
        Button:
            text: 'Toggle Music'
            on_press:
                root.stop_music()
        Button:
            text: 'Back to menu'
            on_press:
                root.manager.transition.direction = 'right'
                root.manager.current = 'menu'

<MapScreen>:
    BoxLayout:
        orientation: "vertical"
        Button:
            text: "back"
            on_press:
                root.manager.transition.direction = "down"
                root.manager.current = "menu"
        BoxLayout:
            orientation: "horizontal"
            Button:
                text: "Level 1"
            Button:
                text: "Level 2"
                disabled: True
            Button:
                text: "Level 3"
                disabled: True
            Button:
                text: "Level 4"
                disabled: True
            Button:
                text: "Level 5"
                disabled: True
        BoxLayout:
            orientation: "horizontal"
            Button:
                text: "Tier 1"
            Button:
                text: "Tier 2"
                disabled: True
            Button:
                text: "Tier 3"
                disabled: True

""")
# Declare both screens


class TitleScreen(Screen):
    pass


class SettingsScreen(Screen):
    def stop_music(self):
        if sound.state == 'play':
            sound.stop()
        else: sound.play()

class MapScreen(Screen):
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

        sm = ScreenManager()
        sm.add_widget(TitleScreen(name='menu'))
        sm.add_widget(SettingsScreen(name='settings'))
        sm.add_widget(MapScreen(name='map'))

        return sm


if __name__ == '__main__':
    FightApp().run()
