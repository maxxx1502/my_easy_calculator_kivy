from kivy.app import App
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '500')

class Calculator(BoxLayout):
    label = ObjectProperty(None)
    first_number = None
    operand = None

    def write_number(self,instance):
        if(self.operand != '='):
            self.label.text = self.label.text + instance.text
            if self.first_number == None:
                self.first_number = 0

    def add(self):
        if self.first_number == None:
            return
        if self.operand == '=':
            self.operand = None
        if self.operand != None:
            return
        self.first_number = int(self.label.text)
        self.label.text = ''
        self.operand = '+'

    def subtract(self):
        if self.first_number == None:
            return
        if self.operand == '=':
            self.operand = None
        if self.operand != None:
            return
        self.first_number = int(self.label.text)
        self.label.text = ''
        self.operand = '-'

    def multiply(self):
        if self.first_number == None:
            return
        if self.operand == '=':
            self.operand = None
        if self.operand != None:
            return
        self.first_number = int(self.label.text)
        self.label.text = ''
        self.operand = '*'

    def division(self):
        if self.first_number == None:
            return
        if self.operand == '=':
            self.operand = None
        if self.operand != None:
            return
        self.first_number = int(self.label.text)
        self.label.text = ''
        self.operand = '/'

    def equal(self):
        if self.operand == '=' or self.first_number == None:
            return
        if self.first_number != None and self.operand != None and \
                self.operand == '+':
            self.label.text = str(self.first_number + int(self.label.text))
        elif self.first_number != None and self.operand != None and \
                self.operand == '-':
            self.label.text = str(self.first_number - int(self.label.text))
        elif self.first_number != None and self.operand != None and \
                self.operand == '*':
            self.label.text = str(self.first_number * int(self.label.text))
        elif self.first_number != None and self.operand != None and \
                self.operand == '/' and self.label.text != '0':
            self.label.text = str(self.first_number // int(self.label.text))
        self.operand = '='

    def clear(self):
        self.first_number = None
        self.operand = None
        self.label.text = ''

class CalcApp(App):
    def build(self):
        calculator = Calculator()
        return calculator

if __name__ == '__main__':
    CalcApp().run()