import kivy
from kivy.app import App
from kivy.uix.slider import Slider
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class SliderApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20)

        # Create multiple sliders with distinct labels
        for i in range(3):
            slider_label = Label(text=f"Slider {i+1} Value: 0")
            slider = Slider(min=0, max=100, value=50)
            slider.bind(value=slider_label.setter('text'))  # Bind directly to label text
            layout.add_widget(slider_label)
            layout.add_widget(slider)

        return layout

if __name__ == '__main__':
    SliderApp().run()
