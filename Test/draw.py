from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.graphics import Line

class ImageLineWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(ImageLineWidget, self).__init__(**kwargs)

        # Añade las imágenes a la interfaz
        for i in range(1, 6):
            img = Image(source=f'imagen{i}.png')
            self.add_widget(img)

        # Dibuja líneas entre las imágenes
        with self.canvas:
            for i in range(4):
                Line(points=[self.children[i].center_x, self.children[i].center_y,
                             self.children[i+1].center_x, self.children[i+1].center_y])

    # Función para cambiar la escala de las imágenes
    def change_scale(self, scale):
        for child in self.children:
            child.scale = scale

class MyApp(App):
    def build(self):
        image_line_widget = ImageLineWidget()
        return image_line_widget

if __name__ == '__main__':
    MyApp().run()
