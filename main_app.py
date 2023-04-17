from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from instructions import *
from ruffier import *
from seconds import *

class FinalScr(Screen):
    def __init__(self, name="final"):
        super().__init__(name=name)
        self.show_results = Button(text="Показать результат", size_hint=(1, 0.5), pos_hint={"center_y": 0.5})
        self.add_widget(self.show_results)
        self.show_results.on_press = self.show
    def show(self):
        global P1, P2, P3, userage
        self.remove_widget(self.show_results)
        index = neud_level(int(P1), int(P2), int(P3), int(userage))
        self.name_txt = username
        self.index_rufier = "Ваш индекс Руфье: " + str(((4 * (int(P1) + int(P2) + int(P3))) - 200) / 10)
        self.heart_work = "Работоспособность сердца: " + txt_res[index]
        self.name_lab = Label(text=self.name_txt)
        self.index_txt = Label(text=self.index_rufier)
        self.heart_txt = Label(text=self.heart_work)
        box = BoxLayout(orientation = "vertical")
        box.add_widget(self.name_lab)
        box.add_widget(self.index_txt)
        box.add_widget(self.heart_txt)
        self.add_widget(box)

class PulseScreen2(Screen):
    def __init__(self, name="fourth"):
        super().__init__(name=name)

        self.lab = Label(text=txt_test3, size_hint=(1, 13))

        firstBox = BoxLayout()
        self.first_answer = Label(text="Результат:")
        self.ti_first = TextInput(text="", halign="left", focus=False, multiline=False)
        firstBox.add_widget(self.first_answer)
        firstBox.add_widget(self.ti_first)

        secondBox = BoxLayout()
        self.second_answer = Label(text="Результат после отдыха:")
        self.ti_second = TextInput(text="", halign="left", focus=False, multiline=False)
        secondBox.add_widget(self.second_answer)
        secondBox.add_widget(self.ti_second)

        self.btn = Button(text="Завершить", size_hint=(0.3, 3), pos_hint={"center_x": 0.5})

        main_box = BoxLayout(orientation="vertical", spacing=10, padding=30)
        main_box.add_widget(self.lab)
        main_box.add_widget(firstBox)
        main_box.add_widget(secondBox)
        main_box.add_widget(self.btn)

        self.add_widget(main_box)

        self.btn.on_press = self.next

    def next(self):
        global P2
        global P3
        P2 = self.ti_first.text
        P3 = self.ti_second.text
        self.manager.transition.direction = "left"
        self.manager.current = "final"


class SitsScreen(Screen):
    def __init__(self, name="third"):
        super().__init__(name=name)

        self.sits_lab = Label(text=txt_sits, size_hint=(1, 20))
        self.btn = Button(text="Дальше", size_hint=(0.3, 3), pos_hint={"center_x": 0.5})

        main_box = BoxLayout(orientation="vertical")
        main_box.add_widget(self.sits_lab)
        main_box.add_widget(self.btn)

        self.add_widget(main_box)

        self.btn.on_press = self.next

    def next(self):
        self.manager.transition.direction = "left"
        self.manager.current = "fourth"
class PulseScreen1(Screen):
    def __init__(self, name="second"):
        super().__init__(name=name)
        self.next_screen = False 
        self.lbl_sec = Seconds(15)

        self.lab = Label(text=txt_test1, size_hint=(1, 10))        
        ti_box = BoxLayout()
        self.answer = Label(text="Введите результат:")
        self.ti_answer = TextInput(text="", halign="left", focus=False, multiline=False)
        ti_box.add_widget(self.answer)
        ti_box.add_widget(self.ti_answer)

        self.btn = Button(text = "Старт", size_hint=(0.3, 3), pos_hint={"center_x": 0.5})

        self.main_box = BoxLayout(orientation="vertical", spacing = 10, padding=30)

        self.main_box.add_widget(self.lab)
        self.main_box.add_widget(ti_box)
        self.main_box.add_widget(self.btn)

        self.timer = Label(text=self.lbl_sec.text)
        self.main_box.add_widget(self.timer)

        self.add_widget(self.main_box)

        self.ti_answer.set_disabled(True)

        self.btn.on_press = self.next
        self.lbl_sec.bind(done=self.sec_finished)
    
    def sec_finished(self, a, b):#создал а и б т.к без них вызывалась ошибка с аргументами(они не влияют на функционал)
        self.next_screen = True
        self.btn.set_disabled(False)
        self.ti_answer.set_disabled(False)
        self.btn.text = "Дальше"
    def next(self):
        global P1
        if not self.next_screen:
            self.btn.set_disabled(True)
            self.lbl_sec.start()
            self.main_box.add_widget(self.lbl_sec)
        else:
            P1 = self.ti_answer.text
            self.manager.transition.direction = "left"
            self.manager.current = "third"

class InstrScr(Screen):
    def __init__(self, name="instr"):
        super().__init__(name=name)
        self.instruc = Label(text = txt_instruction, size_hint=(1, 1.3))

        first_box = BoxLayout(size_hint=(1, 0.15))
        self.name_txt = Label(text="Введите имя:")
        self.ti_name = TextInput(text="", halign="left", focus=False, multiline=False)
        first_box.add_widget(self.name_txt)
        first_box.add_widget(self.ti_name)
        

        second_box = BoxLayout(size_hint=(1, 0.15))
        self.age = Label(text="Введите возраст:")
        self.ti_age = TextInput(text="", halign="left", focus=False, multiline=False)
        second_box.add_widget(self.age)
        second_box.add_widget(self.ti_age)

        self.btn = Button(text = "Дальше", size_hint=(0.3, 0.3), pos_hint={"center_x": 0.5})

        main_box = BoxLayout(orientation="vertical", spacing=10, padding=50)
        main_box.add_widget(self.instruc)
        main_box.add_widget(first_box)
        main_box.add_widget(second_box)
        main_box.add_widget(self.btn)

        self.add_widget(main_box)

        self.btn.on_press = self.next

    def next(self):
        global username
        global userage
        username += self.ti_name.text
        userage += int(self.ti_age.text)
        self.manager.transition.direction = "left"
        self.manager.current = "second"

userage = 0
username = ""
P1 = 0
P2 = 0
P3 = 0
class HeartCheckApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(InstrScr(name="instr"))
        sm.add_widget(PulseScreen1(name="second"))
        sm.add_widget(SitsScreen(name="third"))
        sm.add_widget(PulseScreen2(name="fourth"))
        sm.add_widget(FinalScr(name="final"))
        return sm

HeartCheckApp().run()

# class ScrButton(Button):
#     def __init__(self, screen, direction="right", goal="main", **kwargs):
#         super().__init__(**kwargs)
#         self.screen = screen
#         self.direction = direction
#         self.goal = goal
#     def on_press(self):
#         self.screen.manager.transition.direction = self.direction
#         self.screen.manager.current = self.goal

# class ScrFirstButton(Screen):
#     def __init__(self, name="first"):
#         super().__init__(name=name)
#         first_box = BoxLayout()
#         skala = Image(source = r'C:\Users\Misha\Desktop\Разные_коды\images\skala.jpg')
#         btn_first = ScrButton(self, direction = "left", goal = "main", text = "back", size_hint=(0.3, 1))
#         btn_first.on_press = btn_first.on_press
#         first_box.add_widget(skala)
#         first_box.add_widget(btn_first)
#         self.add_widget(first_box)

# class ScrSecondButton(Screen):
#     def __init__(self, name="second"):
#         super().__init__(name=name)
#         second_box = BoxLayout(orientation="vertical")
#         pump = VideoPlayer(source = r"C:\Users\Misha\Videos\Captures\esskeetit.mp4", state='play', options={'fit_mode': 'contain'})
#         #pump.state = "play"
#         #pump.options = {"eos": "loop"}
#         #pump.allow_stretch = True
#         #pump.options = {'fit_mode': 'contain'}
#         #btn_second = ScrButton(self, direction = "up", goal = "main", text = "back", size_hint=(1, 0.3))
#         #btn_second.on_press = btn_second.on_press
#         second_box.add_widget(pump)
#         #second_box.add_widget(btn_second)
#         self.add_widget(second_box)

# class ScrThirdButton(Screen):
#     def __init__(self, name="third"):
#         super().__init__(name=name)
#         btn_third = ScrButton(self, direction = "down", goal = "main", text = "back")
#         btn_third.on_press = btn_third.on_press
#         self.add_widget(btn_third)

# class ScrFourthButton(Screen):
#     def __init__(self, name="fourth"):
#         super().__init__(name=name)
#         fourth_box = BoxLayout()
#         shrek = Image(source = r'C:\Users\Misha\Desktop\Разные_коды\images\shrek.jpg')
#         btn_fourth = ScrButton(self, direction = "right", goal = "main", text = "back", size_hint=(0.3, 1))
#         btn_fourth.on_press = btn_fourth.on_press
#         fourth_box.add_widget(btn_fourth)
#         fourth_box.add_widget(shrek)
#         self.add_widget(fourth_box)

# class MainScreen(Screen):
#     def __init__(self, name="main"):
#         super().__init__(name=name)
#         main_box = BoxLayout(orientation = "horizontal")#padding = 8 spacing = 8)
#         first_box = BoxLayout(orientation = 'vertical')
#         second_box = BoxLayout(orientation = "vertical")
#         third_box = BoxLayout(orientation = "vertical")
#         btn1 = ScrButton(self, direction = "right", goal = "first", text = "1")
#         btn1.on_press = btn1.on_press
#         btn2 = ScrButton(self, direction = "down", goal = "second", text = "2")
#         btn2.on_press = btn2.on_press
#         btn3 = ScrButton(self, direction = "up", goal = "third", text = "3")
#         btn3.on_press = btn3.on_press
#         btn4 = ScrButton(self, direction = "left", goal = "fourth", text = "4")
#         btn4.on_press = btn4.on_press
#         first_box.add_widget(btn1)
#         second_box.add_widget(btn2)
#         second_box.add_widget(btn3)
#         third_box.add_widget(btn4)
#         main_box.add_widget(first_box)
#         main_box.add_widget(second_box)
#         main_box.add_widget(third_box)
#         self.add_widget(main_box)

# class MyApp(App):
#     def build(self):
#         #return Button()
#         sm = ScreenManager()
#         sm.add_widget(MainScreen(name = "main"))
#         sm.add_widget(ScrFirstButton(name = "first"))
#         sm.add_widget(ScrSecondButton(name = "second"))
#         sm.add_widget(ScrThirdButton(name = "third"))
#         sm.add_widget(ScrFourthButton(name = "fourth"))
#         return sm

# MyApp().run()