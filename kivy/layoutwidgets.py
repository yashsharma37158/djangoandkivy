from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import Button

class LayoutExampleApp(App):
    def build(self):
        # BoxLayout Example
        box_layout = BoxLayout(orientation='vertical', spacing=10)
        box_layout.add_widget(Button(text='Button 1'))
        box_layout.add_widget(Button(text='Button 2'))

        # GridLayout Example
        grid_layout = GridLayout(cols=2, spacing=10)
        for i in range(1, 5):
            grid_layout.add_widget(Button(text=f'Button {i}'))

        # FloatLayout Example
        float_layout = FloatLayout()
        float_layout.add_widget(Button(text='Button 5', size_hint=(0.3, 0.3), pos_hint={'center_x': 0.5, 'center_y': 0.5}))

        # RelativeLayout Example
        relative_layout = RelativeLayout()
        relative_layout.add_widget(Button(text='Button 6', size_hint=(0.2, 0.2), pos=(100, 100)))

        # Root layout combining all the layouts
        root_layout = BoxLayout(orientation='vertical')
        root_layout.add_widget(box_layout)
        root_layout.add_widget(grid_layout)
        root_layout.add_widget(float_layout)
        root_layout.add_widget(relative_layout)

        return root_layout

if __name__ == '__main__':
    LayoutExampleApp().run()
