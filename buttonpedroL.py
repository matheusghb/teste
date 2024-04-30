from kivy.app import App
from kivy.uix.button import Button

class MinhaApp(App):
    def build(self):
        return Button(text='Clique Aqui')
    
if __name__ == '__main__':
    MinhaApp().run() 
