from kivy.app import App
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout


class RV(RecycleView):
    def _init_(self, **kwargs):
        super(RV, self)._init_(**kwargs)
        self.data = [{'text': str(x)} for x in range(100)]


class MyLabel(RecycleDataViewBehavior, Label):
    pass


class RecycleViewApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        rv = RV(viewclass='MyLabel', data=[{'text': str(x)} for x in range(100)])
        layout.add_widget(rv)
        return layout


if __name__ == '_main_':
    RecycleViewApp().run()