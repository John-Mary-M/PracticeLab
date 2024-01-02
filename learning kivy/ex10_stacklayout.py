'''In this script i practice the stack layout in kivy
    It arranges elements vertically or horizontally, as many as the layout
    can fit. sixe of individual elements dont have to be uniform
    In this implementation i implement the design from within the app main logic
    Date 28/12/2023
'''
from kivy.app import App
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button

class StackLayoutEx(App):
    def build(self):
        layout = StackLayout()
        
        for i in range(20):
            btn = Button(text= str(i), width = 40 + i * 5, size_hint = (None, 0.15))
            layout.add_widget(btn)
            
        return layout

if __name__ == "__main__":
    window = StackLayoutEx()
    window.run()
