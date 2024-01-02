'''In this script i learn to use the kivy float layout
    using the kv file and design language
    27/12/2023
'''

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout

class MyFloatLayout(FloatLayout):
    pass

class FloatLayoutEx(App):
    def build(self):
        return MyFloatLayout()


if __name__ == "__main__":
    window = FloatLayoutEx()
    window.run()