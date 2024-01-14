from kivy.app import App
from kivy.uix.pagelayout import PageLayout
from kivy.uix.button import Button

class PageLayoutExampleApp(App):
    def build(self):
        # Create a PageLayout
        page_layout = PageLayout()

        # Add pages to the PageLayout
        for i in range(1, 6):
            page = Button(text=f'Page {i}')
            page_layout.add_widget(page)

        return page_layout

if __name__ == '__main__':
    PageLayoutExampleApp().run()
