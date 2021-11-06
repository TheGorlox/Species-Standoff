from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


class BoxLayoutExample(BoxLayout):
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
