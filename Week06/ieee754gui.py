import flet
from flet import Page, Icon, icons, Text, IconButton, Row, Dropdown, dropdown, Slider, TextField
from ieee754 import *


class IEEE754GUI:
    def __init__(self):
        self.lengths = {"min": 16, "max": 256, "value": 64}
        self.exponents = {"min": 5, "max": 19, "value": 11}
        self.mantissas = {"min": 10, "max": 236, "value": 52}
        self.length_list = [16, 32, 64, 128, 256]
        self.exponent_list = [5, 8, 11, 15, 19]
        self.mantissa_list = [10, 23, 52, 112, 236]
        self.app_icon = Icon(name=icons.MEMORY)
        self.app_title = Text(value="IEEE754 Precision Converter", style="displaySmall")
        self.theme_switcher = IconButton(icon=icons.SUNNY,
                                         tooltip="Switch Dark/Light Theme",
                                         on_click=self.switch_theme)
        self.precision = Dropdown(options=[dropdown.Option(key=0, text="Half Precision"),
                                           dropdown.Option(key=1, text="Single Precision"),
                                           dropdown.Option(key=2, text="Double Precision"),
                                           dropdown.Option(key=3, text="Quadruple Precision"),
                                           dropdown.Option(key=4, text="Octuple Precision")],
                                  label="Predefined Precisions", on_change=self.precision_change)
        self.precision.value = 2
        self.length = Slider(min=self.lengths["min"],
                             max=self.lengths["max"],
                             value=self.lengths["value"],
                             divisions=self.lengths["max"]-self.lengths["min"],
                             label="{value} bits",
                             on_change=self.precision_change)
        self.exponent = Slider(min=self.exponents["min"],
                               max=self.exponents["max"],
                               value=self.exponents["value"],
                               divisions=self.exponents["max"]-self.exponents["min"],
                               label="{value} bits",
                               on_change=self.precision_change)
        self.mantissa = Slider(min=self.mantissas["min"],
                               max=self.mantissas["max"],
                               value=self.mantissas["value"],
                               divisions=self.mantissas["max"]-self.mantissas["min"],
                               label="{value} bits",
                               on_change=self.precision_change)
        self.length_input = TextField(label="Total Bits",
                                      value=str(self.lengths["value"]),
                                      disabled=True, width=100)
        self.sign_input = TextField(label="Sign Bit",
                                    value="1",
                                    disabled=True, width=100)
        self.exponent_input = TextField(label="Exponent Bits",
                                        value=str(self.exponents["value"]),
                                        disabled=True, width=100)
        self.mantissa_input = TextField(label="Mantissa Bits",
                                        value=str(self.mantissas["value"]),
                                        disabled=True, width=100)
        self.integer = TextField(label="Integer Part",
                                 value="13",
                                 keyboard_type="number", width=200,
                                 text_align="right", text_size=30)
        self.dot = Text(value=".", size=60, weight="bold")
        self.decimal = TextField(label="Decimal Part",
                                 value="375",
                                 keyboard_type="number", width=200,
                                 text_size=30)
        self.convert_button = IconButton(icon=icons.ARROW_DOWNWARD,
                                         tooltip="Convert Number",
                                         on_click=self.convert)
        self.result = Text(value="", size=20, weight="bold", text_align="center")
        self.result_hex = Text(value="", size=20, weight="bold")

    def init_window(self):
        self.page.window_title_bar_hidden = False
        self.page.window_frameless = False
        self.page.window_always_on_top = True
        self.page.window_focused = True
        self.page.window_center()
        self.page.theme_mode = "light"
        self.page.title = "IEEE754 Precision Converter"

    def switch_theme(self, _):
        self.page.theme_mode = "light" if self.page.theme_mode == "dark" else "dark"
        self.page.update()

    def precision_change(self, e):
        if isinstance(e.control, Dropdown):
            self.length.value = self.length_list[int(self.precision.value)]
            self.exponent.value = self.exponent_list[int(self.precision.value)]
            self.mantissa.value = self.mantissa_list[int(self.precision.value)]
        self.length_input.value = str(int(self.length.value))
        self.exponent_input.value = str(int(self.exponent.value))
        self.mantissa_input.value = str(int(self.mantissa.value))
        self.page.update()

    def convert(self, _):
        def find_bias(exponent):
            return 2**(exponent-1)-1
        float_number = float(self.integer.value + "." + self.decimal.value)
        b = IEEE754(float_number,
                    force_length=int(self.length.value),
                    force_exponent=int(self.exponent.value),
                    force_mantissa=int(self.mantissa.value),
                    force_bias=find_bias(int(self.exponent.value)))
        self.result.value = f"{b}"
        self.result_hex.value = f"{b.str2hex().upper()}"
        self.page.update()

    def __call__(self, flet_page: Page):
        self.page = flet_page
        self.init_window()
        self.page.add(
            Row(
                wrap=False,
                alignment="spaceBetween",
                controls=[
                    Row(
                        wrap=False,
                        controls=[
                            self.app_icon,
                            self.app_title
                        ]
                    ),
                    self.theme_switcher
                ]
            )
        )
        self.page.add(self.precision)
        self.page.add(self.length)
        self.page.add(self.exponent)
        self.page.add(self.mantissa)
        self.page.add(
            Row(
                wrap=False,
                alignment="center",
                controls=[
                    self.length_input,
                    self.sign_input,
                    self.exponent_input,
                    self.mantissa_input
                ]
            )
        )
        self.page.add(
            Row(
                wrap=False,
                alignment="center",
                controls=[
                    self.integer,
                    self.dot,
                    self.decimal
                ]
            )
        )
        self.page.add(
            Row(
                wrap=False,
                alignment="center",
                controls=[
                    self.convert_button
                ]
            )
        )
        self.page.add(
            Row(
                wrap=True,
                alignment="center",
                width=self.page.width,
                controls=[
                    self.result
                ]
            )
        )
        self.page.add(
            Row(
                wrap=True,
                alignment="center",
                width=self.page.width,
                controls=[
                    self.result_hex
                ]
            )
        )
        self.page.update()


if __name__ == '__main__':
    flet.app(target=IEEE754GUI())  # view=flet.WEB_BROWSER
