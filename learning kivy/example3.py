'''Making a big button
    and using the bind method for event handling/ callbacks
'''

from kivy.app import App
from kivy.uix.button import Button

class Window(App):
    def build(self):
        button = Button(text = "click me")
        button.bind(on_press = self.click_me)
        return button

    def click_me(self, value):
        print("You clicked Me")
if __name__ == "__main__":
    window = Window()
    window.run()