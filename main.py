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
                    root.manager.current = 'settings'
            Label:

<SettingsScreen>:
    BoxLayout:
        orientation: "vertical"
        Button:
            text: 'Mute Music'
        Button:
            text: 'Back to menu'
            on_press:
                root.manager.transition.direction = 'right'
                root.manager.current = 'menu'
""")
# Declare both screens


class TitleScreen(Screen):
    pass


class SettingsScreen(Screen):
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


# sound = SoundLoader.load('./sound/speciesstandoff 3.wav')


class FightApp(App):
    def build(self):

        sound = SoundLoader.load('./sound/speciesstandoff3.wav')
        if sound:
            print("Sound found at %s" % sound.source)
            print("Sound is %.3f seconds" % sound.length)
            sound.play()

        sm = ScreenManager()
        sm.add_widget(TitleScreen(name='menu'))
        sm.add_widget(SettingsScreen(name='settings'))

        return sm


if __name__ == '__main__':
    FightApp().run()
