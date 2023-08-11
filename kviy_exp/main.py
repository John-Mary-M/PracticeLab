from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGrid(GridLayout):
    """Creates design layout"""
    def __init__(self, **kwargs):
        """Initialize grid elements"""
        super(MyGrid, self).__init__(**kwargs)
        
        self.inside = GridLayout()
        self.inside.colss = 2
        
        self.cols = 1 # set number of columns to display
        # Add some widgets
        self.inside.add_widget(Label(text="First Name: "))
        self.first_name = TextInput(multiline=False)
        self.inside.add_widget(self.first_name)

        self.inside.add_widget(Label(text="Last Name: "))
        self.last_name = TextInput(multiline=False)
        self.inside.add_widget(self.last_name)
        
        self.inside.add_widget(Label(text="Email: "))
        self.mail = TextInput(multiline=False)
        self.inside.add_widget(self.mail)
        
        self.submit = Button(text='Submit', font_size=40)
        self.add_widget(self.submit)
        
        self.add_widget(self.inside)
        
class MyApp(App):
    def build(self):
        return MyGrid()
    
if __name__ == "__main__":
    MyApp().run()