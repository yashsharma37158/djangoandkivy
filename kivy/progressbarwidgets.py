import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.progressbar import ProgressBar
from kivy.clock import Clock

class ProgressApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.progress_bar = ProgressBar(max=100, value=0)
        layout.add_widget(self.progress_bar)

        Clock.schedule_interval(self.update_progress, 0.1)

        return layout

    def update_progress(self, dt):
        self.progress_bar.value += 1
        if self.progress_bar.value >= 100:
            Clock.unschedule(self.update_progress)

if __name__ == '__main__':
    ProgressApp().run()
