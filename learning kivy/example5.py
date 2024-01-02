'''In this file i learn about the boxlayout
    which arranges chiuldren in either vertical
    or horizontal orientation
'''
from kivy.app import App
# from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


class MyBoxLayout(BoxLayout):
    pass


class BoxLayoutEx(App):
    def build(self):
        return MyBoxLayout()

if __name__ == '__main__':
    window = BoxLayoutEx()
    window.run()