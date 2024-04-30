from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class MinhaApp(App):
    def build (self):
        layout = BoxLayout(orientation="vertical", spacing=10)

        btn1 = Button(text='Botão 1', background_color= (0.2,0.7,0.3,1), font_size=20)
        btn2 = Button(text='Clique aqui!', halign='center')
        btn3 = Button(text='Clique para continuar', background_color=(0.9, 0.5, 0.1, 1), font_size=20)
        
        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(btn3)
        
        def acao_botao(instance):
            instance.text = 'Botão pressionado!'

        btn4 = Button(text="Botão 4")
        btn4.bind(on_press=acao_botao)
        layout.add_widget(btn4)

        info_label = Label(text="Pressione para observar as diferentes propriedades de um botão.")
        layout.add_widget(info_label)

        return layout
    
if __name__ == "__main__":
    MinhaApp().run()