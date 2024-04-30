from kivy.app import App
from kivy.uix.label import Label
class MyApp(App):
    def build(self):
        return Label(text="Olá SENAI", font_size=100, font_name='Papyrus')
if __name__ == '__main__':
    MyApp().run()
