# main.py
from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        return Label(text="Hello from Kivy on Android!")

MyApp().run()
