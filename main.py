from kivymd.uix.screen import MDScreen
from kivy.core.window import Window
from kivymd.uix.card import MDCard
from kivymd.app import MDApp
from kivy.lang import Builder


# resize the window
Window.size = (375,667)

# main screen of the application
class Application(MDScreen):
    pass
    
class MainApp(MDApp):
    def build(self):
        # changes the primary pallete and set the color to Purple-700
        self.theme_cls.primary_palette = 'Purple'
        self.theme_cls.primary_hue = '700'
        return Application()

Builder.load_file('application.kv')

if __name__ == "__main__":
    MainApp().run()
