import flet as ft
from flet import Colors

botoes = [
{'operador': 'AC', 'fonte': 'black', 'fundo': 'white'},
{'operador': '()', 'fonte': 'black', 'fundo': 'white'},
{'operador': '%', 'fonte': 'black', 'fundo': 'white'},
{'operador': '/', 'fonte': 'white', 'fundo': 'orange'},
{'operador': '7', 'fonte': 'white', 'fundo': ft.Colors.WHITE24},
{'operador': '8', 'fonte': 'white', 'fundo': ft.Colors.WHITE24},
{'operador': '9', 'fonte': 'white', 'fundo': ft.Colors.WHITE24},
{'operador': '*', 'fonte': 'white', 'fundo': 'orange'},
{'operador': '4', 'fonte': 'white', 'fundo': ft.Colors.WHITE24},
{'operador': '5', 'fonte': 'white', 'fundo': ft.Colors.WHITE24},
{'operador': '6', 'fonte': 'white', 'fundo': ft.Colors.WHITE24},
{'operador': '-', 'fonte': 'white', 'fundo': 'orange'},
{'operador': '1', 'fonte': 'white', 'fundo': ft.Colors.WHITE24},
{'operador': '2', 'fonte': 'white', 'fundo': ft.Colors.WHITE24},
{'operador': '3', 'fonte': 'white', 'fundo': ft.Colors.WHITE24},
{'operador': '+', 'fonte': 'white', 'fundo': 'orange'},
{'operador': '0', 'fonte': 'white', 'fundo': ft.Colors.WHITE24},
{'operador': '.', 'fonte': 'white', 'fundo': ft.Colors.WHITE24},
{'operador': '=', 'fonte': 'white', 'fundo': 'orange'}
]


def main (page: ft.Page):
    page.bgcolor = 'black'
    page.window.resizable = False
    page.window.width = 430
    page.window.height = 620
    page.title = 'Calculadora'
    page.window.always_on_top = True

    resultado = ft.Text('0', size=40, color='white')

    def calculate(operador, valor_atual):
        value = eval(valor_atual)

    def select(e):
        valor_atual = resultado.value if resultado.value != '0' else ''
        value = e.control.content.value

        if value.isdigit():
            value = valor_atual + value

        elif value == 'AC':
            value = '0'
        else:
            if valor_atual and valor_atual[-1] in ('/','*','-','+','.'):
                value = valor_atual[:-1]

            value = valor_atual + value

            if value[-1] in ('=', '%', '()'):
                value = calculate(operador=value[-1], valor_atual=valor_atual)

            resultado.value = value
            resultado.update()

    display = ft.Row(
        width=430,
        alignment='end',
        controls=[resultado]
    )

    botao = [ft.Container(
        content=ft.Text(value=btn['operador'], color=btn['fonte'], size=30),
        width=90,
        height=90,
        border_radius=100,
        bgcolor=btn['fundo'],
        alignment= ft.alignment.center,
        on_click = select
    ) for btn in botoes]

    keyboard = ft.Row(
        width=430,
        wrap= True,
        controls=botao,
        alignment= 'end'
    )

    page.add(display, keyboard)



ft.app(target= main)