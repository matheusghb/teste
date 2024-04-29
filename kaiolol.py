from kivy.app import App
from kivy.uix.label import Label

class myapp(App):
    def build(self):
        return Label(
            text="oie", font_size=100,
            halign='right',
            valign='bottom',)
       

if __name__ == '__main__':
    myapp().run()
