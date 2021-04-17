
from kivymd.app import MDApp

from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty, NumericProperty

from kivymd.uix import MDAdaptiveWidget

class Token(FloatLayout, MDAdaptiveWidget):
    weight = NumericProperty(0)
    count = NumericProperty(0)

    def money(self):
        return float(self.weight)*float(self.count)
        

class Poker(FloatLayout, MDAdaptiveWidget):
    black_token = ObjectProperty(None)
    orange_token = ObjectProperty(None)
    green_token = ObjectProperty(None)
    yellow_token = ObjectProperty(None)
    blue_token = ObjectProperty(None)

    def money_sum(self):
        return self.black_token.money() + self.orange_token.money() + self.green_token.money() + self.yellow_token.money() + self.blue_token.money() 

    def money_label_update(self):
        self.money_label.text = "money: " + str(self.money_sum())

    def count_plus_one(self, token):
        token.count += 1
        self.money_label_update()

    def count_minus_one(self, token):
        if token.count != 0: 
            token.count -= 1
        self.money_label_update()

class TokenSettings(FloatLayout, MDAdaptiveWidget):
    pass

class Hands(FloatLayout, MDAdaptiveWidget):
    pass

class PokerApp(MDApp):
    pass

PokerApp().run()
