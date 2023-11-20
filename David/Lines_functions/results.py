from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.core.window import Window

# Cargamos el archivo KV
Builder.load_file('results.kv')  # Asegúrate de poner la ruta correcta

class MyResults(BoxLayout):
    def __init__(self, **kwargs):
        super(MyResults, self).__init__(**kwargs)

class MyApp(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        return MyResults()

if __name__ == '__main__':
    MyApp().run()
