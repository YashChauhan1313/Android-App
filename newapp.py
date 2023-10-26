from pip import main
import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Lable
from kivy.uix.texinput import TexInput
from kivy.uix.button import Button

class ChildApp(GridLayout):
    def __init__(self, **kwargs):
        super(childApp, self).__init__()
        self.cols = 2
        self.add_widget(Lable(text = 'Student Name'))
        self.s_name = TextInput()
        self.add_widget(self.s_name)

        self.add_widget(Lable(text = 'Student Marks'))
        self.s_marks = TextInput()
        self.add_widget(self.s_marks)

        self.add_widget(Lable(text = 'Student Gender'))
        self.s_gender = TextInput()
        self.add_widget(self.s_gender)

class parentApp(App):
    def build(self):
        return childApp()


if __name__ == '__main__':
    parentApp().run()
    
