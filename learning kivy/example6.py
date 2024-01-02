'''using the anchor layout directly without a kv file'''
from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class AnchorLayoutEx(App):
    def build(self):
        anLayout1= AnchorLayout(anchor_x = 'right', anchor_y='bottom')
        btn = Button(text='Click One', size_hint = (0.3,0.3))
        
        anLayout2 = AnchorLayout(anchor_x = 'right', anchor_y='top')
        btn1 = Button(text='Click Two', size_hint = (0.2,0.2))
        
        anLayout1.add_widget(btn)
        anLayout2.add_widget(btn1)
        
        boxLayout = BoxLayout()
        boxLayout.add_widget(anLayout1)
        boxLayout.add_widget(anLayout2)
        
        return boxLayout

if __name__ == '__main__':
    window = AnchorLayoutEx()
    window.run()