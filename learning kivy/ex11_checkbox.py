'''In this script i learn how to create a checkbox widget in kivy
    Using direct implementation from within the main logic
    Date: 28/12/2023
    '''

from tkinter import Label
from kivy.app import App
from kivy.uix.checkbox import CheckBox
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

class CheckBoxClass(GridLayout):
    def __init__(self):
        super().__init__()
        
        self.cols = 2
        
        self.add_widget(Label(text="Python"))
        self.check = CheckBox(active = True)
        self.add_widget(self.check)
        
        self.add_widget(Label(text="C++"))
        self.check = CheckBox(active = True)
        self.add_widget(self.check)
        
        self.add_widget(Label(text="Java"))
        self.check = CheckBox(active = True)
        self.add_widget(self.check)
        
        self.add_widget(Label(text="Pearl"))
        self.check = CheckBox(active = True)
        self.add_widget(self.check)
        
        # Handle Click Events
        self.myLabel = Label(text = "Label")
        self.add_widget(self.myLabel)
        
        # binding the on_checkbox_active method to the checkbox
        self.check.bind(active = self.on_checkbox_active)
        
    def on_checkbox_active(self, checkbox, value):
        if value:
            self.myLabel.text = "The Checkbox is Active"
        else:
            self.myLabel.text = "The Checkbox is inactive"
            

class CheckBoxEX(App):
    def build(self):
    
        return CheckBoxClass()

if __name__ == "__main__":
    window = CheckBoxEX()
    window.run()