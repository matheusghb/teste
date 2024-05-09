from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import AsyncImage
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
class log(Screen):
    def __init__(self, **kwargs):
        super(log, self).__init__(**kwargs)
        
        self.orientation = 'vertical'
        self.padding = [50, 20, 50, 20]
        self.spacing = [10]

        self.textol = Label(text="login")
        self.add_widget(self.textol)

        self.imagem = AsyncImage(source = 'https://cdn-icons-png.flaticon.com/512/1144/1144760.png' )
        self.nome = TextInput(hint_text = 'seu nome')
        self.butreg= Button(text="registrar")
        self.butreg.bind(on_press=self.open_second_window)
        self.add_widget(self.textol)
        self.add_widget(self.imagem)
        self.add_widget(self.)
        self.add_widget(self.butreg)
        Window.clearcolor = [1,1,1,1]

    def open_second_window(self, instance):
        self.manager.current = 'second'


class SecondWindow(Screen):
    def __init__(self, **kwargs):
        super(SecondWindow, self).__init__(**kwargs)

        self.textoc = Label(text="registrar")
        self.add_widget(self.textoc)

        self.back_button = Button(text="Go Back")
        self.back_button.bind(on_press=self.go_back)
        self.add_widget(self.back_button)

    def voltar(self, instance):
        self.manager.current = 'main'


class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(log(name='main'))
        sm.add_widget(SecondWindow(name='second'))
        return sm


if __name__ == "__main__":
    MyApp().run()
