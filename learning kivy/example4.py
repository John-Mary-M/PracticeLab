'''Making my own widgets
    I have modified window.kv for this exercise
    and created My_widget(base) that has a button with several rules
'''
from kivy.app import App
from kivy.uix.widget import Widget

class My_Widget(Widget):
    def click_me(self):
        print("The Button is pressed")
        self.my_label.text = "This is the new text"


class Window(App):
    def build(self):
        return My_Widget()


if __name__ == "__main__":
    window = Window()
    window.run()