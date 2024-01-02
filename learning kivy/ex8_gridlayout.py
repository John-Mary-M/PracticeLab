'''In this script i practice the gridlayout in kivy
    implementing it in the main logic (as a class)
    Date 27/12/2023
'''
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class GridLayoutEx(App):
    def build(self):
        layout = GridLayout(cols = 2)
        layout.add_widget(Button(text = "Click One", size_hint_x = None, width = 100))
        layout.add_widget(Button(text = "Click Two", size_hint_x = None, width = 100))
        layout.add_widget(Button(text = "Click Three"))
        layout.add_widget(Button(text = "Click Four"))
        
        return layout



if __name__ == "__main__":
    window = GridLayoutEx()
    window.run()
