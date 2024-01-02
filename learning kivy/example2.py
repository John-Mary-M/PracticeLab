'''Seperating logic and kv design
    In a file called window.kv is were all the design implementation
    is going to be written in kv design language
'''
from kivy.app import App
from kivy.uix.label import Label

class Window(App):
    def build(self):
        return Label()

if __name__ == "__main__":
    window = Window()
    window.run()