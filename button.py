from kivy.app import App 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.utils import get_color_from_hex
from kivy.uix.checkbox import CheckBox
from kivy.uix.image import Image


class MinhaApp(App):
    def build(self):
     
     layout = BoxLayout(orientation="vertical")

     self.imag = Image(source='Users/aluno.sesipaulista/Downloads/praia.jpg')
     self.chkb = CheckBox(active=False)
     self.btn = Button(text='Clique Aqui')
     self.btn.bind(on_press=self.botao_pressionado, font_size=50, background_color=get_color_from_hex('#3498db'), size_hint=(0.5, 0.2))

     layout.add_widget(self.imag)
     layout.add_widget(self.chkb)
     layout.add_widget(self.btn)

     return layout
    
    def botao_pressionado(self, instance):
     print("Botão pressionado!")

if __name__ == "__main__":
 MinhaApp().run()