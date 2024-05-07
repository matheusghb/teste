from kivy.app import App  
from kivy.uix.label import Label 
from kivy.utils import get_color_from_hex 
from kivy.uix.button import Button 
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.image import Image
from kivy.uix.slider import Slider
from kivy.uix.floatlayout import FloatLayout

def btnpress(instance):
    print('oioies')
class app(App):
    def build(self):
        
        layout = FloatLayout()  
        self.oi = Label(
            text="oie",
            size=(100,50),
            size_hint = (None, None),
            font_size=100,
            font_name='arial',
            pos_hint={'x': 0.6, 'y': 0.8},
            color= get_color_from_hex('FF0076'),
            italic= 'true')
        self.oi2 = ui = Button(
            size=(50,30),
            size_hint = (None, None),
            text="olis",
            font_size=50,
            font_name='arial',
            color = get_color_from_hex('ffffff'),
            background_color = get_color_from_hex('639E42'),
            pos_hint = {'center_x': 0.9, 'center_y': 0.5})
           
        self.oi3 = Image( 
            source = "/Users/aluno.sesipaulista/Downloads/oi.jpg",
            size_hint = (None, None),
            size=(50,30),
            )

        slider = Slider( size= (100, 50), size_hint = (None, None), min=0, max=100, value= 50, step=1,
                        pos_hint={'x':0.1, 'right': 0.5}) 
        
        layout.add_widget(self.oi)
        layout.add_widget(self.oi2)
        layout.add_widget(self.oi3)
        layout.add_widget(slider)
        return layout       

if __name__ == '__main__':
    app().run()
