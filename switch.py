from kivy.app import App
from kivy.uix.switch import Switch
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class MinhaApp(App):
    def build(self):
        layout = BoxLayout(orientation="vertical")
        self.sw = Switch(active=False)
        self.sw.bind(on_press=self.texto)
        self.la = Label(color=[1,0,0,1])
        layout.add_widget(self.sw)
        layout.add_widget(self.la)
        return layout
    
    def texto(self,instance):
        match self.sw.active:
         case True:
            valor = "ativado"
         case False:
            valor = "desativado"

        mensagem = (f"O switch atualmente está: {valor}")
        print (mensagem)
        self.la.text = mensagem

if __name__ == "__main__":
    MinhaApp().run()