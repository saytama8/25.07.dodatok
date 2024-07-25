from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.animation import Animation
from kivy.uix.image import Image
from dop import *

class Main(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        green = (.15,.20,.05,.5)
        Window.clearcolor =green
        image = Image(source="image.jpg")




        lineV = FloatLayout( size_hint=(1,1))
        line1= BoxLayout(size_hint=(1,0.4), pos_hint={"y":0.7, "center_x":0.5})
        line2= BoxLayout(size_hint=(0.5,0.05),pos_hint={"y":0.4, "center_x":0.5})
        line3= BoxLayout(size_hint=(0.5,0.05),pos_hint={"y":0.2, "center_x":0.5})
        line4= BoxLayout(size_hint=(0.25,0.1),pos_hint={"y":0, "center_x":0.5})
        
        label1 = Label(text=inst)
        line1.add_widget(label1)
        line1.add_widget(image)

        label2 = Label(text="Введіть назву риби , про яку ви хочете дізнатися ")
        name = TextInput(multiline = False)
        line2.add_widget(label2)
        line2.add_widget(name)
        red = (.255,.0,.0,1)
     
        self.age = TextInput(multiline = False,background_color=red)
        
              
        
        but1 = Button(text="Інформація",background_color=red)
        anim = Animation(background_color=(0, 0, 1, 1), font_size=60, duration=3.5)
        anim2 = Animation( font_size=60,duration=3.5)
        anim3 = anim + anim2
        anim3.start(but1)
        
        line4.add_widget(but1)

        lineV.add_widget(line1)
        lineV.add_widget(line2)

        lineV.add_widget(line4)

        self.add_widget(lineV)
        but1.on_press = self.next_win1

    def next_win1(self):
        global new_age
        new_age = int(self.age.text)
        self.manager.current = 'main2'
        self.manager.transition.direction = "up"

class Main2(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        label2 = Label(text = inst2, size_hint=(1,0.5),
                      pos_hint={"y":0.5, "center_x":0.5})

        label3 = Label(text = "Введіть результат", size_hint=(0.2,0.05),
                      pos_hint={"y":0.17, "x":0.1})

        self.rezalt = TextInput(multiline=False, size_hint=(0.35,0.05),
                      pos_hint={"y":0.17, "center_x":0.5})
                      
        but2 = Button(text = "Інформація", size_hint=(0.35,0.15),
                      pos_hint={"y":0.01, "center_x":0.5})

        lineF = FloatLayout(size_hint=(1,1))
        lineF.add_widget(label2)
        lineF.add_widget(label3)
        lineF.add_widget(self.rezalt)
        lineF.add_widget(but2)

        self.add_widget(lineF)
        but2.on_press = self.next_win

    def next_win(self):
        global p1
        p1 = int(self.rezalt.text)
        self.manager.current = 'main3'
        self.manager.transition.direction = "up"





class Win(App):
    def build(self):

        main_screen= ScreenManager()
        main_screen.add_widget(Main(name='main'))
        main_screen.add_widget(Main2(name='main2'))
        #main_screen.add_widget(Main3(name='main3'))
        #main_screen.add_widget(Main4(name='main4'))
        #main_screen.add_widget(Main5(name='main5'))
        return main_screen

app = Win()
app.run()