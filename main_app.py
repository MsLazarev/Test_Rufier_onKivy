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

def check_int(str_num):
    try:
        return int(str_num)
    except:
        return False

class BonusScr(Screen):
    def __init__(self, name="Bonus"):
        super().__init__(name=name)
        self.shrek = Image(source = r'sadShrek.jpeg')
        self.label = Label(text="Возраст должен быть от 7 до 16 лет")
        self.btn_back = Button(text="Вернуться")
        self.btn_exit = Button(text="Выход")
        self.v_box = BoxLayout(orientation="vertical")
        self.h_box = BoxLayout()
        self.h_box.add_widget(self.btn_exit)
        self.h_box.add_widget(self.btn_back)
        self.v_box.add_widget(self.label)
        self.v_box.add_widget(self.h_box)
        self.mainbox = BoxLayout()
        self.mainbox.add_widget(self.shrek)
        self.mainbox.add_widget(self.v_box)
        self.add_widget(self.mainbox)

        self.btn_back.on_press = self.back
        self.btn_exit.on_press = self.exit

    def back(self):
        self.manager.transition.direction = "up"
        self.manager.current = "instr"
    def exit(self):
        exit()

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

        self.stage = 0
        self.firstBox = BoxLayout()
        self.secondBox = BoxLayout()
        self.next_screen = False
        self.lbl_sec = Seconds(3)

        self.lab = Label(text=txt_test3, size_hint=(1, 3.5))
        self.first_answer = Label(text="Результат:")
        self.ti_first = TextInput(text="", halign="left", focus=False, multiline=False)
        self.firstBox.add_widget(self.first_answer)
        self.firstBox.add_widget(self.ti_first)

        self.relax = Label(text="Замеряйте пульс после нажатия кнопки")
        self.time_box = BoxLayout(orientation="vertical", spacing=3, size_hint=(1, 6))
        self.time_box.add_widget(self.relax)

        self.second_answer = Label(text="Результат после отдыха:")
        self.ti_second = TextInput(text="", halign="left", focus=False, multiline=False)
        self.secondBox.add_widget(self.second_answer)
        self.secondBox.add_widget(self.ti_second)

        self.btn = Button(text="Начать", size_hint=(0.3, 3), pos_hint={"center_x": 0.5})

        self.main_box = BoxLayout(orientation="vertical", spacing=10, padding=30)
        self.main_box.add_widget(self.lab)
        self.main_box.add_widget(self.time_box)
        self.main_box.add_widget(self.firstBox)
        self.main_box.add_widget(self.secondBox)
        self.main_box.add_widget(self.btn)

        self.add_widget(self.main_box)

        self.ti_first.set_disabled(True)
        self.ti_second.set_disabled(True)
        #self.btn.set_disabled(True)

        self.btn.on_press = self.next
        self.lbl_sec.bind(done=self.sec_finished)

    def sec_finished(self, a, b):
        if self.lbl_sec.done:
            if self.stage == 0:
                self.stage = 1
                self.relax.text = "Отдыхайте(30 сек)"
                self.lbl_sec.restart(5)
                self.ti_first.set_disabled(False)
            elif self.stage == 1:
                self.stage = 2
                self.lbl_sec.restart(5)
                self.relax.text = "Замеряйте пульс(15 сек)"
            elif self.stage == 2:
                self.relax.text = "Переходите к следующему экрану"
                self.btn.text = "Дальше"
                self.ti_second.set_disabled(False)
                self.btn.set_disabled(False)
    def next(self):
        global P2
        global P3
        if self.stage < 1:
            self.btn.set_disabled(True)
            self.lbl_sec.start()
            self.relax.text = "Замеряйте пульс(15 сек)"
            self.time_box.add_widget(self.lbl_sec)
        else:
            P2 = check_int(self.ti_first.text)
            P3 = check_int(self.ti_second.text)
            if P2 == False or P2 <= 0:
                P2 = 0
                self.ti_first.text = str(P2)
            if P3 == False or P3 <= 0:
                P3 = 0
                self.ti_second.text = str(P3)
            else:
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
        self.lbl_sec = Seconds(3)

        self.lab = Label(text=txt_test1, size_hint=(1, 10))
        self.ti_box = BoxLayout()
        self.answer = Label(text="Введите результат:")
        self.ti_answer = TextInput(text="", halign="left", focus=False, multiline=False)
        self.ti_box.add_widget(self.answer)
        self.ti_box.add_widget(self.ti_answer)

        self.time_box = BoxLayout()

        self.btn = Button(text = "Старт", size_hint=(0.3, 3), pos_hint={"center_x": 0.5})

        self.main_box = BoxLayout(orientation="vertical", spacing = 10, padding=30)

        self.main_box.add_widget(self.lab)
        self.main_box.add_widget(self.time_box)
        self.main_box.add_widget(self.ti_box)
        self.main_box.add_widget(self.btn)


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
            self.time_box.add_widget(self.lbl_sec)
        else:
            P1 = check_int(self.ti_answer.text)
            if P1 == False or P1 <= 0:
                P1 = 0
                self.ti_answer.text = str(P1)
            else:
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
        userage = check_int(self.ti_age.text)
        if userage == False or userage < 7 or userage > 16:
            self.manager.transition.direction = "down"
            self.manager.current = "Bonus"
        else:
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
        sm.add_widget(BonusScr(name="Bonus"))
        sm.add_widget(PulseScreen1(name="second"))
        sm.add_widget(SitsScreen(name="third"))
        sm.add_widget(PulseScreen2(name="fourth"))
        sm.add_widget(FinalScr(name="final"))
        return sm

HeartCheckApp().run()