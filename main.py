from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from animals.animal import *
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


"""    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        b1 = Button(text="A")
        b2 = Button(text="B")
        self.add_widget(b1)
        self.add_widget(b2)
"""


class MainWidget():
    pass


class FightApp(App):
    def build(self):
        return BoxLayoutExample()


if __name__ == '__main__':
    FightApp().run()
