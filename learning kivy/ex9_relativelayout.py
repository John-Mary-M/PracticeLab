'''In this script I practice using the relative layout in kivy
    implementing it using the .kv file and design language.
    Date 27/12/2023
'''
from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout


class MyRelativeLayout(RelativeLayout):
    pass


class RelativeLayoutEx(App):
    def build(self):
        return MyRelativeLayout()


if __name__ == "__main__":
    window = RelativeLayoutEx()
    window.run()
