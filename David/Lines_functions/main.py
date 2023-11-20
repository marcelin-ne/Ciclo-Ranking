from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from line_drawer import LineDrawer
from myforms import MyForm

Builder.load_file('main.kv')

class MainApp(BoxLayout):
    class MainApp(BoxLayout):
        pass

class MyApp(App):
    def build(self):
        return MainApp()

if __name__ == '__main__':
    MyApp().run()