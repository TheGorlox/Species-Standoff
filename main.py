from kivy.core.audio import SoundLoader
from kivy.app import App
import random
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.screenmanager import FadeTransition
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from animals.animal import *
from kivy.clock import Clock
from kivy.core.audio import SoundLoader
from kivy.core.audio import Sound
from kivy.factory import Factory
from kivy.properties import (
    NumericProperty, StringProperty, BooleanProperty,
)
import asynckivy as ak
from kivy_garden.draggable import KXDraggableBehavior

pet_array = []
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


class ShopButton(BoxLayout, Button):
    pass


class DraggableItem(KXDraggableBehavior, BoxLayout):
    def on_drag_start(self, touch):
        if(App.get_running_app().money-self.cost <= 0 and self.drag_cls != "order"):
            self.drag_cancel()

    def myfunc(self):
        if(self.drag_cls == "buy"):
            App.get_running_app().money -= self.cost
            self.drag_cls = 'order'


class ShopScreen(Screen):
    money = NumericProperty(10)

    def on_load(self):

        # print(self.children)
        gl = self.ids["sh1"]
        DraggableItem = Factory.DraggableItem

        DraggableItem()
        for i in range(5):
            species = random.choice(
                ["cow", "fish", "cat", "panda", "dog", "chicken", "crow", "snake", "polarbear", "penguin", 'eel'])
            di = DraggableItem()
            im = Image(source="./images/" +
                       species+".png")
            im.allow_stretch = 1
            di.add_widget(im)
            lab = Label(text=species)
            di.species = species
            lab.size_hint_y = .2
            di.add_widget(lab)
            di.cost = 3
            gl.add_widget(di)

    def bfunction(self):
        # print(self.children[0].children[1].children)
        for i in self.children[0].children[1].children:
            pet_array.append(i.species)


class Magnet(Factory.Widget):
    '''
    Inspired by
    https://github.com/kivy-garden/garden.magnet
    '''
    do_anim = BooleanProperty(True)
    anim_duration = NumericProperty(1)
    anim_transition = StringProperty('out_quad')

    # default value of the instance attributes
    _coro = ak.sleep_forever()

    def __init__(self, **kwargs):
        self._anim_trigger = trigger = \
            Clock.create_trigger(self._start_anim, -1)
        super().__init__(**kwargs)
        self.fbind('pos', trigger)
        self.fbind('size', trigger)

    def add_widget(self, widget, *args, **kwargs):
        if self.children:
            raise ValueError('Magnet can have only one child')
        widget.pos = self.pos
        widget.size = self.size
        return super().add_widget(widget, *args, **kwargs)

    def _start_anim(self, *args):
        if self.children:
            child = self.children[0]
            self._coro.close()
            if not self.do_anim:
                child.pos = self.pos
                child.size = self.size
                return
            self._coro = ak.start(ak.animate(
                child,
                d=self.anim_duration,
                t=self.anim_transition,
                x=self.x, y=self.y, width=self.width, height=self.height,
            ))


class Shop(BoxLayout):
    pass


class FightScreen(Screen):
    def on_enter(self, *args):
        pet_array.reverse()
        for i in pet_array:
            print(self.children[0].children[0].children[1].add_widget(
                Image(source="./images/"+i+".png")))
            # .children[0]
            # # print(i)

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


# sound = SoundLoader.load('./sound/speciesstandoff3.wav')
sound = SoundLoader.load('./sound/spu1.wav')
if sound:
    sound.loop = True
    sound.play()
# sound = SoundLoader.load('./sound/spu1.wav')


class FightApp(App):
    money = NumericProperty(10)

    def build(self):

        global sm
        sm = ScreenManager()
        sm.add_widget(TitleScreen(name='menu'))
        sm.add_widget(SettingsScreen(name='settings'))
        sm.add_widget(MapScreen(name='map'))
        sm.add_widget(ShopScreen(name='shop'))
        sm.add_widget(FightScreen(name='fight'))

        return sm


if __name__ == '__main__':
    FightApp().run()
