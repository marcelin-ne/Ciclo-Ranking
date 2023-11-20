from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label


class BaseLayout(GridLayout):
    pass

class BaseApp(App):
    def build(self):
        return BaseLayout()

if __name__ == '__main__':
    BaseApp().run()
