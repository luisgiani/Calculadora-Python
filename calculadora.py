import flet as ft

def main (page: ft.Page):
    page.bgcolor = 'black'
    page.window.resizable = False
    page.window.width = 450
    page.window.height = 600
    page.title = 'Calculadora'
    page.window.always_on_top = True

    page.add(ft.Text("Calculadora", size=20, color="white"))




ft.app(target= main)