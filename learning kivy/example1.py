from kivy.app import App
from kivy.uix.label import Label

class Window(App):
    def build(self):
        return Label(text = "Hello Kivy app", font_size = "25sp")

if __name__ == "__main__":
    window = Window()
    window.run()