from kivy.app import App
from kivy.uix.label import Label
from kivy.utils import get_color_from_hex
class MyApp(App):
    def build(self):
        return Label(text="Olá SENAI", font_size=100, font_name='Papyrus',color=get_color_from_hex('#38024F'))
if __name__ == '__main__':
    MyApp().run()
