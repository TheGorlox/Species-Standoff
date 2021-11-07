from kivy_garden.draggable import KXDraggableBehavior
import asynckivy as ak
from kivy.properties import (
    NumericProperty, StringProperty, BooleanProperty,
)
from kivy.factory import Factory
from kivy.core.audio import Sound
from kivy.clock import Clock
from animals.animal import *
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import FadeTransition
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.lang import Builder
from kivy.core.audio import SoundLoader
from kivy.app import App
import random
import json

f = open('./data/levels.json',)
stages = json.load(f)


pet_array = []
cleared = 0
stage_cleared = 0

Builder.load_file("fight.kv")
# Declare both screens

sound = SoundLoader.load('./sound/spu1.wav')
if sound:
    sound.loop = True
    sound.play()
songs = []
songs.append(sound)


class TitleScreen(Screen):
    pass


class SettingsScreen(Screen):
    def stop_music(self):
        if sound.state == 'play':
            sound.stop()
        else:
            sound.play()


class MapScreen(Screen):
    clear = NumericProperty(cleared)
    stage_clear = NumericProperty(stage_cleared)

    def change_transition(self, type):
        if type == "fade":
            sm.transition = FadeTransition(duration=0.6)
        if type == "slide":
            sm.transition = SlideTransition()

    def on_enter(self, *args):
        if cleared == 1:
            self.children[0].children[1].children[3].disabled = False
        if cleared % 5 == 2:
            self.children[0].children[1].children[2].disabled = False
        if cleared % 5 == 3:
            self.children[0].children[1].children[1].disabled = False
        if cleared % 5 == 4:
            self.children[0].children[1].children[0].disabled = False

        if stage_cleared == 1:
            self.children[0].children[0].children[1].disabled = False
        if stage_cleared == 2:
            self.children[0].children[0].children[0].disabled = False


class ShopButton(BoxLayout, Button):
    pass


class DraggableItem(KXDraggableBehavior, BoxLayout):
    def on_drag_start(self, touch):
        print(App.get_running_app().total_pets)
        if((App.get_running_app().money-self.cost < 0 and self.drag_cls != "order") or App.get_running_app().total_pets >= 7):
            self.drag_cancel()

    def myfunc(self):
        if(self.drag_cls == "buy"):
            App.get_running_app().total_pets += 1
            App.get_running_app().money -= self.cost
            self.drag_cls = 'order'


class ShopScreen(Screen):
    def on_enter(self):
        sound = songs[0]
        if sound.state == 'play':
            sound.stop()
            sound = SoundLoader.load('sound/speciesstandoff3.wav')
            sound.play()
        self.ids["sh1"].clear_widgets()
        animal_instances[0] = []
        animal_instances[1] = []

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
            lab = Label(
                text=f"{species} - {load_animal(species).power}/{load_animal(species).toughness}")
            di.species = species
            lab.size_hint_y = .2
            di.add_widget(lab)
            di.cost = 3
            gl.add_widget(di)

    def bfunction(self):
        # print(self.children[0].children[1].children)\
        pet_array.clear()
        for i in self.children[0].children[1].children:
            pet_array.append(i.species)

    def sellfirst(self):
        gl = self.ids["play"]
        if(len(self.ids["play"].children) > 0):
            self.ids["play"].remove_widget(self.ids["play"].children[0])
            App.get_running_app().money += 1
            App.get_running_app().total_pets -= 1


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

    global animal_instances
    animal_instances = [[], []]

    def on_enter(self, *args):
        self.stage = App.get_running_app().current_stage
        self.ended = False
        pet_array.reverse()
        self.children[0].children[2].text = "Stage "+str(self.stage + 1)
        self.children[0].children[1].text = "Fight!"
        self.children[0].children[0].children[1].clear_widgets()
        self.children[0].children[0].children[0].clear_widgets()

        for i in pet_array:
            bl = BoxLayout(orientation="vertical")
            im = Image(source="./images/"+i+".png")
            animal_instances[0].append(load_animal(i))
            animal = animal_instances[0][-1]
            lab = Label(text=f"{i}\n{animal.power}/{animal.toughness}")
            bl.add_widget(im)
            bl.add_widget(lab)
            im.allow_stretch = 1
            im.size_hint_y = .5
            im.pos_hint = {"center_y": .5}
            self.children[0].children[0].children[1].add_widget(bl)

        i = stages["stages"][App.get_running_app().current_stage]

        for j in i:
            bl = BoxLayout(orientation="vertical")
            im = Image(source="./images/"+j+".png")
            animal_instances[1].append(load_animal(j))
            animal = animal_instances[1][-1]
            lab = Label(text=f"{j}\n{animal.power}/{animal.toughness}")
            bl.add_widget(im)
            bl.add_widget(lab)
            im.allow_stretch = 1
            im.size_hint_y = .5
            im.pos_hint = {"center_y": .5}
            self.children[0].children[0].children[0].add_widget(bl)

        animal_instances[0].reverse()
        animal_instances[1].reverse()

    def run_sim(self):
        sound = SoundLoader.load('sound/sfx/pixely hit.wav')
        if sound:
            sound.volume = .3
            sound.play()
        animal_instances[0], animal_instances[1] = fight(
            animal_instances[0], animal_instances[1])
        self.update()
        if len(animal_instances[0]) == 0 and len(animal_instances[1]) == 0:
            self.tie()
        else:
            if len(animal_instances[0]) == 0:
                self.lose()
            elif len(animal_instances[1]) == 0:
                self.win()

    def update(self):
        self.children[0].children[0].children[1].clear_widgets()
        animal_instances[0].reverse()
        for i in animal_instances[0]:
            bl = BoxLayout(orientation="vertical")
            string = i.species.replace(" ", "").replace("'", "")
            im = Image(source="./images/"+string+".png")
            lab = Label(text=f"{i.species}\n{i.power}/{i.toughness}")
            bl.add_widget(im)
            bl.add_widget(lab)
            im.allow_stretch = 1
            im.size_hint_y = .5
            im.pos_hint = {"center_y": .5}
            self.children[0].children[0].children[1].add_widget(bl)

        self.children[0].children[0].children[0].clear_widgets()
        # animal_instances[1].reverse()
        for j in animal_instances[1]:
            bl = BoxLayout(orientation="vertical")
            string = j.species.replace(" ", "").replace("'", "")
            im = Image(source="./images/"+string+".png")
            lab = Label(text=f"{j.species}\n{j.power}/{j.toughness}")
            bl.add_widget(im)
            bl.add_widget(lab)
            im.allow_stretch = 1
            im.size_hint_y = .5
            im.pos_hint = {"center_y": .5}
            self.children[0].children[0].children[0].add_widget(bl)

        animal_instances[0].reverse()
        animal_instances[1].reverse()

    def lose(self):
        self.children[0].children[2].text = "You lost!"
        self.children[0].children[1].text = "Back to Map"
        self.ended = True

    def win(self):
        App.get_running_app().money += 5
        self.children[0].children[2].text = "You won!"
        self.children[0].children[1].text = "Back to Map"
        self.ended = True
        global cleared
        cleared = App.get_running_app().current_stage+1
        if cleared == 4:
            stage_cleared == 1
        if cleared == 9:
            stage_cleared == 2

    def tie(self):
        self.children[0].children[2].text = "You tied."
        self.children[0].children[1].text = "Back to Map"
        self.ended = True


# sound = SoundLoader.load('./sound/speciesstandoff3.wav')

# sound = SoundLoader.load('./sound/spu1.wav')


class FightApp(App):
    money = NumericProperty(10)
    current_stage = NumericProperty(0)
    total_pets = NumericProperty(0)

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
