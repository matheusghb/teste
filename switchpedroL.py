from kivy.app import App
from kivy.uix.switch import Switch

class MinhaApp(App):
    def build(self):
        return Switch(active=False)
    
if __name__ == "__name__":
    MinhaApp().run()
