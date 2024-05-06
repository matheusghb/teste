from kivy.app import App
from kivy.uix.image import Image

class MinhaApp(App):
    def build(self):
     
     return Image(source='https://www.google.com/imgres?q=bolo%20santosi&imgurl=https%3A%2F%2Fimage.api.playstation.com%2Fcdn%2FEP0082%2FBLES00517_00%2F7L0LSfkuBR1RzDWQz8t8cOYPZN10KGkW.png%3Fw%3D440%26thumb%3Dfalse&imgrefurl=https%3A%2F%2Fpsprices.com%2Fregion-tr%2Fgame%2F732958%2Fbolo-santosi%3Flang%3Dpt-BR&docid=ZP3xOVjan-1T8M&tbnid=n0EGmFuwKXXqHM&vet=12ahUKEwiXuqnQ4PmFAxVqppUCHWdrDvsQM3oECFIQAA..i&w=240&h=240&hcb=2&itg=1&ved=2ahUKEwiXuqnQ4PmFAxVqppUCHWdrDvsQM3oECFIQAA')
if __name__ == "__main__":
    MinhaApp().run()
