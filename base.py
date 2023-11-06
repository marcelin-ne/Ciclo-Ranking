import kivy
from kivy.app import App
from kivy.uix.widget import Widget #To use the Widget class
from kivy.properties import ObjectProperty #To use the ObjectProperty class
from kivy.lang import Builder
from kivy.core.window import Window
#from kivy.uix.image import Image


#The first way to load the file
Builder.load_file('base.kv')
#Construct the Layout
class MyLayout(Widget):
    pass
    #Create press function

#Call the class
class AwesomeApp(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        return MyLayout()

if __name__ == '__main__':
    AwesomeApp().run()


