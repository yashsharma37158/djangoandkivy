import kivy
from kivy.app import App
from kivy.uix.label import Label

kivy.require("1.11.1")

class TestApp(App):
    def build(self):
        return Label(text='Hello, Kivy!')

TestApp().run()