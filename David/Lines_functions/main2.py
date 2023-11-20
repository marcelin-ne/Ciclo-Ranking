# main.py
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from line_drawer import LineDrawer
from myforms import MyForm
from results import MyResults
from kivy.core.window import Window
from delimeter import Delimiter
from calculator import Rankine_P_Close

class MainApp(BoxLayout):
    def __init__(self, **kwargs):
        super(MainApp, self).__init__(**kwargs)

        delimiter_instance = Delimiter()
        # Instancia de LineDrawer
        self.line_drawer = LineDrawer()
        self.myforms = MyForm()
        #self.results = MyResults()
        # Agregar elementos al diseño (BoxLayout)
        self.add_widget(self.line_drawer)
        self.add_widget(self.myforms)
        #self.line_drawer.draw_base()



    def modify_line(self, instance):
        # Modificar la línea al presionar el botón
        self.line_drawer.modify_line('my_line', [100, 100, 500, 300])

    def animate_line(self, instance):
        # Animar la línea al presionar el botón
        self.line_drawer.animate_line('my_line', [100, 100, 300, 500])

class MyApp(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        Window.fullscreen = True
        delimiter_instance = Delimiter()
        myform=MyForm()
        return MainApp()

if __name__ == '__main__':
    MyApp().run()
