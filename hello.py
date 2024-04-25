from kivy.app import App
from kivy.uix.label import Label
class MyApp(App):
    def build(self):
        return Label(text='oie', font_size=100, font_type="Arial")
if __name__ == '__main__':
    MyApp().run()