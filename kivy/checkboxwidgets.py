from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox


class CheckboxDemo(GridLayout):
    def _init_(self, **kwargs):
        super()._init_(**kwargs)
        self.cols = 2

        self.add_widget(Label(text='Python'))
        self.check_python = CheckBox(active=True)
        self.add_widget(self.check_python)

        self.add_widget(Label(text='C'))
        self.check_c = CheckBox(active=False)
        self.add_widget(self.check_c)

        self.add_widget(Label(text='C++'))
        self.check_cpp = CheckBox(active=False)
        self.add_widget(self.check_cpp)

        self.add_widget(Label(text='Java'))
        self.check_java = CheckBox(active=True)
        self.add_widget(self.check_java)

        self.add_widget(Label(text='Other'))
        self.check_other = CheckBox(active=False)
        self.add_widget(self.check_other)


class CheckBoxApp(App):
    def build(self):
        return CheckboxDemo()


if __name__ == '_main_':
    CheckBoxApp().run()