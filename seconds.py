from kivy.app import App
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.properties import BooleanProperty

class Seconds(Label):
    done = BooleanProperty(defaultvalue=False)
    def __init__(self, total, **kwargs):
        self.done = False
        self.total = total
        self.current = 0
        #self.text = "Прошло секунд: " + str(self.current)
        super().__init__(text=self.text)
    def restart(self, total, **kwargs):
        self.done = False
        self.total = total
        self.current = 0
        self.start()
        
    def start(self):
        Clock.schedule_interval(self.change, 1)
    def change(self, dt):
        self.current += 1
        self.text = "Прошло секунд: " + str(self.current)
        if self.current >= self.total:
            self.done = True
            return False