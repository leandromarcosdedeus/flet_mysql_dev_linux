#instale 
#se nao rodar: sudo apt update sudo apt install libmpv-dev
#se 
import flet as ft

def main(page: ft.Page):
    page.add(ft.Text("Olá, Flet!"))

ft.app(target=main)
