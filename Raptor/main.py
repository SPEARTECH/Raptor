from kivymd.app import MDApp
from kivy.core.window import Window

class Main(MDApp):
    def build(self):
        Window.fullscreen='auto'
        pass

if __name__ == '__main__':
    Main().run()