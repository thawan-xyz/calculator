from kivy.config import Config

Config.set('graphics', 'width', '320')
Config.set('graphics', 'height', '500')

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

# @author: Thawan Ribeiro, 2024-03-14
# @project: Basic Arithmetic Calculator
# @version: 1.0.0
# @description: A simple calculator for basic arithmetic operations.
# @url: https://github.com/thawan-xyz

BLACK = (0, 0, 0, 1)
WHITE = (0.95, 0.95, 0.95, 1)
GREY = (0.8, 0.8, 0.8, 1)
PURPLE = (0.25, 0.14, 1, 1)
RED = (0.9, 0, 0.23, 1)

class MyCalculatorLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(MyCalculatorLayout, self).__init__(**kwargs)
        self.error = False
        self.orientation = 'vertical'

        self.display = TextInput(
            font_size = 64,
            background_normal = '',
            foreground_color = BLACK,
            background_color = WHITE,
            halign = 'right',
            size_hint_y = 0.4,
            readonly = True,
            is_focusable = False,
        )

        self.add_widget(self.display)

        buttons = [
            '7', '8', '9', ' / ',
            '4', '5', '6', ' * ',
            '1', '2', '3', ' - ',
            'C', '0', '=', ' + '
        ]

        background_colors = {'C': RED, '=': PURPLE}
        text_colors = {'C': WHITE, '=': WHITE}

        self.buttons = GridLayout(
            cols = 4,
            size_hint_y = 0.6,
            spacing = 4,
            padding = (4, 4)
        )

        for button in buttons:
            self.buttons.add_widget(
                Button(
                    font_size = 20,
                    text = button,
                    on_press = self.pressed,
                    background_normal = '',
                    # background_down = '',
                    background_color = background_colors.get(button, WHITE),
                    color = text_colors.get(button, BLACK)
                )
            )

        self.add_widget(self.buttons)

        Window.bind(on_key_down = self.key)

    def pressed(self, instance):
        expression = self.display.text
        button = instance.text

        if button == '=':
            try:
                self.display.text = str(int(eval(expression)))
            except:
                self.display.text = 'Error'
                self.error = True
        elif button == 'C':
            self.display.text = ''
            self.error = False
        elif not self.error:
            self.display.text += button

    def key(self, window, key, scancode, codepoint, modifier):
        pressed_key = ''
        if codepoint is not None:
            pressed_key = codepoint.upper()

        if key == 14 or pressed_key == 'T':
            self.display.text = 'by:\nThawan'
            self.error = True
        elif key == 8:
            self.display.text = self.display.text[:-1]
        elif key == 13 or key == 32:
            self.pressed(Button(text = '='))
        elif key == 61:
            self.pressed(Button(text = ' + '))
        elif key == 127 or pressed_key == 'C':
            self.pressed(Button(text = pressed_key))
        elif pressed_key in '0123456789':
            self.pressed(Button(text = pressed_key))
        elif pressed_key in '+-*/':
            self.pressed(Button(text = f' {pressed_key} '))

class MyCalculator(App):
    def build(self):
        self.title = 'Calculator'
        self.icon = './img/icon.png'
        return MyCalculatorLayout()

MyCalculator().run()
