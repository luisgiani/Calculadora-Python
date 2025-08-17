import flet as ft

def main (page: ft.Page):
    page.btcolor = 'black'
    page.window_resizable = False
    page.window_width = 250
    page.window_height = 300
    page.title = 'Calculadora'







ft.app(target= main)