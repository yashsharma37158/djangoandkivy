from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label

class ScrollApp(App):
    def build(self):
        # Create a BoxLayout as the root widget
        root = BoxLayout(orientation='vertical')

        # Create a ScrollView
        scroll_view = ScrollView()

        # Create a BoxLayout to hold the content of the ScrollView
        content_layout = BoxLayout(orientation='vertical', size_hint_y=None, spacing=5)

        # Add content to the ScrollView
        for i in range(50):
            label = Label(text=f"Label {i}", size_hint_y=None, height=40)
            content_layout.add_widget(label)

        # Add the content layout to the ScrollView
        scroll_view.add_widget(content_layout)

        # Add the ScrollView to the root layout
        root.add_widget(scroll_view)

        return root

if __name__ == '__main__':
    ScrollApp().run()
