'''In this script i experiment with the kivy float layout
    27/12/2023. This specific script implements the float layout 
    directly within the main py file/ logic
'''

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button

class FloatLayoutEx(App):
    def build(self):
        layout = FloatLayout(size = (300, 300))
        button = Button(text = 'Click me', size_hint = (.5, .25), pos = (30, 30))
        layout.add_widget(button)
        
        return layout
    
if __name__ == "__main__":
    window = FloatLayoutEx()
    window.run()