'''In this script i implement the gridlayout using the .kv file
    & kv design language.
    Date 27/12/2023
'''
from kivy.app import App
from kivy.uix.gridlayout import GridLayout

class MyGridLayout(GridLayout):
    pass

class GridLayoutEx(App):
    def build(self):
        return MyGridLayout()



if __name__ == "__main__":
    window = GridLayoutEx()
    window.run()
