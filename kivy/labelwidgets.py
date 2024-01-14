import kivy
kivy.require('1.9.1')

from kivy.app import App

from kivy.uix.label import Label

class MyLabel(App):
	  def build(self):
             l2= Label(text="Label is Added on\n Screen!!:):) and its Multi\n Line", font_size='20sp',color=[0.41,0.42,0.74,1])
             return l2

label = MyLabel()
label.run()