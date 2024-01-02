'''using the anchor layout with a kv file'''
from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class MyAnchorLayout(AnchorLayout):
    pass

class AnchorLayoutEx(App):
    def build(self):
        return MyAnchorLayout()

if __name__ == '__main__':
    window = AnchorLayoutEx()
    window.run()