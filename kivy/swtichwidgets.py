import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.switch import Switch
from kivy.properties import StringProperty
from kivy.uix.label import Label


class SwitchApp(App):
    switch_state = StringProperty('Switch is Off')

    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=20, padding=20)

        # Create the Switch widget
        self.switch = Switch(active=False)  # Initially set to off
        self.switch.bind(active=self.on_switch_active)

        # Create a label to display the switch state
        self.label = Label(text=self.switch_state)

        layout.add_widget(self.switch)
        layout.add_widget(self.label)

        return layout

    def on_switch_active(self, instance, value):
        if value:
            self.switch_state = 'Switch is On'
        else:
            self.switch_state = 'Switch is Off'

        self.label.text = self.switch_state

if __name__ == '__main__':
    SwitchApp().run()
