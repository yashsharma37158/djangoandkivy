import kivy
from kivy.app import App
from kivy.uix.button import Button
kivy.require('1.9.1')

class ButtonApp(App):
    def build(self):
        btn = Button(text ="Submit")
        return btn

root = ButtonApp()
root.run()
