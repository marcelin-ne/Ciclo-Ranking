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
    #Create calcular function
    def resolve(self):
        #Get the value from the TextInputs
        #Convert the value to a float
        #Add the values together
        #Print the sum to the console
        #self.ids.my_label.text = str(answer)
        pass
    #Create clear function
    def clear(self):
        #Clear the TextInputs
        #Clear the label
        pass
    

#Call the class
class AwesomeApp(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        return MyLayout()

if __name__ == '__main__':
    AwesomeApp().run()


