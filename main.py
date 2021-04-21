
from kivymd.app import MDApp

from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty, NumericProperty, ListProperty

from kivymd.uix import MDAdaptiveWidget

class Token(FloatLayout, MDAdaptiveWidget):
    value = NumericProperty(0)
    count = NumericProperty(0)

    def money(self):
        return float(self.value)*float(self.count)

class TokenSettings(FloatLayout, MDAdaptiveWidget):
    values = ListProperty([0,0,0,0,0])

    def increase_value(self, i):
        if self.values[i] < 100:
            self.values[i] += 5
        elif self.values[i] < 1000:
            self.values[i] += 50
        elif self.values[i] < 10000:
            self.values[i] += 500
        elif self.values[i] < 100000:
            self.values[i] += 5000

    def decrease_value(self, i):
        if self.values[i] != 0: 
            if self.values[i] <= 100:
                self.values[i] -= 5
            elif self.values[i] <= 1000:
                self.values[i] -= 50
            elif self.values[i] <= 10000:
                self.values[i] -= 500
            elif self.values[i] <= 100000:
                self.values[i] -= 5000


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


class Hands(FloatLayout, MDAdaptiveWidget):
    pass

class PokerApp(MDApp):
    values = [0,0,0,0,0]
    def get_token_values(self, values):
        self.values = values

    def set_token_values(self, screen):
        screen.black_token.value = self.values[0]/100
        screen.orange_token.value = self.values[1]/100
        screen.green_token.value = self.values[2]/100
        screen.yellow_token.value = self.values[3]/100
        screen.blue_token.value = self.values[4]/100

if __name__ == "__main__":
    PokerApp().run()
