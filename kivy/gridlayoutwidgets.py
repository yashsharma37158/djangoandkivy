from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class GridLayoutExampleApp(App):
    def build(self):
        # Create a GridLayout with 3 columns
        grid_layout = GridLayout(cols=3, spacing=10, padding=10)

        # Add buttons to the GridLayout
        for i in range(1, 10):
            button = Button(text=f'Button {i}', size_hint=(None, None), size=(100, 40))
            grid_layout.add_widget(button)

        return grid_layout

if __name__ == '__main__':
    GridLayoutExampleApp().run()
