from kivy.app import App
from kivy.uix.checkbox import CheckBox
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image

class MinhaApp(App):
    def build(self):
        layout = BoxLayout(orientation="vertical")
        self.chk = CheckBox(active=False)
        self.img = Image(source="/Users/aluno.sesipaulista/Downloads/eehe.jpg", size_hint=(0.5,0.5))
        layout.add_widget(self.chk)
        layout.add_widget(self.img)
        return layout
    
if __name__ == "__main__":
    MinhaApp().run()