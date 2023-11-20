import kivy
from kivy.app import App
from kivy.uix.widget import Widget #To use the Widget class
from kivy.properties import ObjectProperty #To use the ObjectProperty class
from kivy.lang import Builder
from kivy.graphics import Line
from kivy.animation import Animation
from kivy.core.window import Window

from line_drawer import LineDrawer

#The first way to load the file
Builder.load_file('lines.kv')
#Construct the Layout
class MyLayout(Widget):

    def animate_it(self,widget, *args):
        #Define the animation change color
        animate=Animation(background_color=(0,0,1,1), duration=1) 
        #For second animations Opacity
        #animate+=Animation(opacity= 0 , duration=.5)
        #For third animations Change Size of the widget
        animate+=Animation(size_hint=(.8,.8), duration=.8)
        #For fourth animations Change Size of the widget
        animate+=Animation(size_hint=(.3,.3), duration=.8)
        #Aniamtion for change the position of the widget
        animate+=Animation(pos_hint={"center_x":.1, "center_y":.1}, duration=.8)
    #Star the animation
        animate.start(widget)
    #Create a callbakc
        animate.bind(on_complete=self.my_callback)

    def my_callback(self, *args):
        self.ids.my_label.text="Animation Completed"
#Call the class
class AwesomeApp(App):
    def build(self):
        Window.clearcolor = (0, 0, 0, 0)
        return MyLayout()

class LineDrawingApp(App):
    def build(self):
        line_drawer = LineDrawer()
        # Dibuja una línea desde (100, 100) hasta (300, 300) con el identificador 'my_line'
        line_drawer.draw_line(100, 100, 300, 300, 'my_line')
        return line_drawer

    def on_start(self):
        # Modifica la línea después de que la aplicación inicia
        self.root.modify_line('my_line', [100, 100, 500, 300])

        # Agrega una animación a la línea después de que la aplicación inicia
        self.root.animate_line('my_line', [100, 100, 300, 500])



if __name__ == '__main__':
    AwesomeApp().run()
    LineDrawingApp().run()


