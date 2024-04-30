from kivy.app import App  
from kivy.uix.label import Label 
from kivy.utils import get_color_from_hex 
from kivy.uix.button import Button 
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.image import Image 
from kivy.uix.slider import Slider

class app(App):
    def build(self):
        
        layout = BoxLayout(orientation='vertical', padding=20)  # halign e valign nao funciona :3
        self.lab1 = Label(
            text="oie",
            size=(100,200),
            font_size=100,
            font_name='arial',
            halign='right',
            valign='top',
            color= get_color_from_hex('FF0076'),
            italic= 'true')
        self.lab2 = Button(
            size=(50,30),
            text="olis",
            font_size=50,
            font_name='arial',
            color = [1,0,0,1],
            halign='left',
            valign='top')

        slider = Slider( min=0, max=100, value= 50, step=1) # imagem crasha o app >.<
        
        layout.add_widget(self.lab1)
        layout.add_widget(self.lab2)
        layout.add_widget(slider)
        return layout       

if __name__ == '__main__':
    app().run()
