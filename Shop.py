from kivy.app import App
from kivy.lang import Builder
import random
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.factory import Factory
from kivy.clock import Clock
from kivy.properties import (
    NumericProperty, StringProperty, BooleanProperty,
)
import asynckivy as ak

from kivy_garden.draggable import KXDraggableBehavior


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

KV_CODE = '''
#:import create_spacer kivy_garden.draggable._utils._create_spacer
<ReorderableGridLayout@KXReorderableBehavior+GridLayout>:
<DraggableItem>:
    do_anim: not self.is_being_dragged
    anim_duration: .2
    drag_cls: 'test'
    drag_timeout: 50
    font_size: 30
    on_drag_success: self.myfunc()
    opacity: .5 if self.is_being_dragged else 1.
    size_hint_min: 50, 50
    pos_hint: {'center_x': .5, 'center_y': .5, }
    sauce: ''
    canvas.after:
        Color:
            rgba: .5, 1, 0, 1 if root.is_being_dragged else .5
        Line:
            width: 2 if root.is_being_dragged else 1
            rectangle: [*self.pos, *self.size, ]
    
<MyButton@Button>:
    font_size: sp(20)
    size_hint_min_x: self.texture_size[0] + dp(10)
    size_hint_min_y: self.texture_size[1] + dp(10)

Shop:
    size : root.width, root.height


<Shop>:
    orientation:"vertical"
    BoxLayout:
        Label:
            text: str()

    ReorderableGridLayout:
        id:play
        spacing: 10
        padding: 10
        drag_classes: ['test', ]
        cols: 6
        spacer_widgets:
            [create_spacer(color=color)
            for color in "#000044 #002200 #440000".split()]
    ReorderableGridLayout:
        id:sh1
        spacing: 10
        padding: 10
        drag_classes: ['test', ]
        cols: 6
        spacer_widgets:
            [create_spacer(color=color)
            for color in "#000044 #002200 #440000".split()]

'''


class DraggableItem(KXDraggableBehavior, BoxLayout):
    def myfunc(self):
        pass
        

class SampleApp(App):
    def build(self):
        return Builder.load_string(KV_CODE)

    def on_start(self):
        gl = self.root.ids.sh1
        DraggableItem = Factory.DraggableItem
        DraggableItem()
        for i in range(5):
            di = DraggableItem()
            di.add_widget(Image(source="./images/"+random.choice(
                ["cow", "fish", "cat", "panda", "dog", "chicken", "glipglop"])+".png"))
            gl.add_widget(di)


if __name__ == '__main__':
    SampleApp().run()
