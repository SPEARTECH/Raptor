from kivymd.uix.card import MDCard
from kivy.uix.behaviors import ButtonBehavior
from kivy.metrics import dp


class RCard(
    MDCard
):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.radius = [dp(4),dp(4),dp(4),dp(4)]
        self.style = 'elevated'


class RButton(
    MDCard, ButtonBehavior
):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.radius = [dp(4),dp(4),dp(4),dp(4)]
        self.style = 'outlined'
        self.focus_behavior = True
        self.ripple_behavior = True

