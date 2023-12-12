from kivy.config import Config
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.app import App
import platform


class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        # Verificar el sistema operativo
        if platform.system() == 'Windows':
            # Configuraciones específicas para Windows
            Config.set('graphics', 'width', '400')
            Config.set('graphics', 'height', '300')
            Config.set('graphics', 'dpi', '96')

            label_text = 'Estás en Windows'
        else:
            # Configuraciones específicas para macOS
            label_text = 'Estás en macOS'

        label = Label(text=label_text)
        button = Button(text='Mi botón')

        layout.add_widget(label)
        layout.add_widget(button)

        return layout

if __name__ == '__main__':
    MyApp().run()
