from kivymd.uix.screen import MDScreen


class Application(MDScreen):
    pass


if __name__ == "__main__":
    from kivymd.app import MDApp
    from kivy.lang import Builder

    class MainApp(MDApp):
        def build(self):
            return Application()
    
    Builder.load_file('application.kv')

    MainApp().run()
