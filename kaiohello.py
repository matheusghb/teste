from kivy.app import App  
from kivy.uix.label import Label 
from kivy.utils import get_color_from_hex 
from kivy.uix.button import Button 
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.image import Image, AsyncImage
from kivy.uix.slider import Slider

def btnpress(instance):
    print('oioies')
class app(App):
    def build(self):
        
        layout = BoxLayout(orientation='horizontal', padding=50, size = 50)  
        self.oi = Label(
            text="oie",
            size=(100,200),
            font_size=100,
            font_name='arial',
            halign='right',
            valign='top',
            color= get_color_from_hex('FF0076'),
            italic= 'true')
        self.oi2 = ui = Button(
            size=(50,30),
            text="olis",
            font_size=50,
            font_name='arial',
            color = get_color_from_hex('ffffff'),
            background_color = get_color_from_hex('639E42'),
            halign='left',
            valign='top')
           
        
        self.oi3 = Image( 
            
            source = "/Users/aluno.sesipaulista/Downloads/oi.jpg")

        slider = Slider( min=0, max=100, value= 50, step=1) 
        
        layout.add_widget(self.oi)
        layout.add_widget(self.oi2)
        layout.add_widget(self.oi3)
        layout.add_widget(slider)
        return layout       

if __name__ == '__main__':
    app().run()
