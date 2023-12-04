from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.core.window import Window


class BaseLayout(GridLayout):
    pass

class BaseApp(App):
    def build(self):
        Window.size = (1100, 600)
        return BaseLayout()

if __name__ == '__main__':
    BaseApp().run()
