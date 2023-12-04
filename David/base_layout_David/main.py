
from kivy.app import App
from kivy.utils import QueryDict,rgba
from kivy.metrics import dp

from kivy.lang import Builder

class MainWindow(App):
    colors = QueryDict()
    colors.primary = rgba('#4E71C1')
    colors.secondary = rgba('#F3E3E2')
    colors.success = rgba('#4CAF20')
    colors.warning = rgba('#EE9830')
    colors.danger = rgba('#F44336')
    fonts=QueryDict()
    fonts.size=QueryDict()
    #Fonts Sizes for the app 
    fonts.size.h1=dp(24)
    fonts.size.h2=dp(22)
    fonts.size.h3=dp(18)
    fonts.size.h4=dp(16)
    fonts.size.h5=dp(14)
    fonts.size.h6=dp(12)

    fonts.heading='assets/fonts/Roboto-Bold.ttf'
    fonts.subheading='assets/fonts/Roboto-Medium.ttf'
    fonts.body='assets/fonts/Roboto-Light.ttf'

    def build(self):
        return MainWindow()
