'''Date 29/12/2023
	Practicing layouts with kivy and trying to build
	interfaces
'''
from kivy.app import App
from kivy.metrics import dp
from kivy.properties import StringProperty
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout

class WidgetEx(GridLayout):
    count = 0
    my_text = StringProperty("0")
    
    def on_button_click(self):
        print("Button Clicked")
        self.count += 1
        self.my_text = str(self.count)
        
    def on_toggle_button_state(self, widget):
        print("Toggle State:" + widget.state)
        
class StackLayoutEx(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # seting orientation directly
        #self.orientation = "lr-tb"
        # using padding/ internal margin
        for _ in range(0, 100):
            b = Button(text=str(_ + 1), size_hint=(None, None), size=(dp(100), dp(100)))
            self.add_widget(b)
            

# classs GridLayoutEx(GridLayout):
    # pass

class AnchorLayoutEx(AnchorLayout):
    pass

class BoxLayoutExample(BoxLayout):
    pass
'''
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # change orientation of elements on the layout
        self.orientation = "vertical"
        
        b1 = Button(text = "A")
        b2 = Button(text = "B")
        
        # adding the buttons to the widget
        self.add_widget(b1)
        self.add_widget(b2)
        
'''

class MainWidget(Widget):
    pass
    
class MyApp(App):
    pass
    
   
MyApp().run()