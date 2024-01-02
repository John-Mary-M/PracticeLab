'''In this script i practice the stack layout in kivy
    It arranges elements vertically or horizontally, as many as the layout
    can fit. sixe of individual elements dont have to be uniform
    In this script I implement the design using a .kv file using the kv design
    language
    Date 28/12/2023
'''
from kivy.app import App
from kivy.uix.stacklayout import StackLayout

class MyStackLayout(StackLayout):#inheriting from StackLayout
    pass

class StackLayoutEx(App):
    def build(self):
        return MyStackLayout()
    
    
if __name__ == "__main__":
    window = StackLayoutEx()
    window.run()