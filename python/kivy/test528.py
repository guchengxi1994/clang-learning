# import kivy
# kivy.require("1.0.6")

from kivy.app import App 
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class TestApp(App):
    def build(self):
        return Button(text="i")

class TestApp2(App):
    def build(self):
        return Label(text="123")

class LoginScreen(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='User Name'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
        self.add_widget(Label(text='password'))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)

class LoginApp(App):
    def build(self):
        return LoginScreen()


if __name__ == "__main__":
    LoginApp().run()