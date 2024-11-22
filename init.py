import flet as ft
from flet import Page, Row, DataTable, DataColumn, DataRow, DataCell, Column
from database import conn

def main(page: Page):
    page.controls.clear()
    page.title = "Cadastro de Funcionário"

    headers = conn.tableHeader()

    dict_values = {
        'name': '', 'email': '', 'password': ''
    }

    #funcoes para cadastro
    def create(e):
        page.controls.clear()
        
        def register(e):
            insert = conn.insert_user(str(dynamic_fields[0].value), str(dynamic_fields[1].value),str(dynamic_fields[2].value))
            print(insert)
            page.add(ft.Text(insert))



        dynamic_fields = [ft.TextField(label=i, width=100) for i in headers]
        page.add(Row(controls=[
            *dynamic_fields,
            ft.ElevatedButton(text="Cadastrar", on_click=register),
            ft.ElevatedButton(text="Voltar", on_click=show_main_layout)
        ]))
        page.update()

    #main menu
    def show_main_layout(e):
        page.controls.clear()
        page.add(Column(controls=[
            ft.ElevatedButton(text="Cadastrar", on_click=create),
            ft.ElevatedButton(text="Listar", on_click=get)
        ]))
        page.update()

    def get(e):
        data = conn.getAll()
        page.controls.clear()

        print(data)
        columns = [DataColumn(label=ft.Text(header)) for header in headers]
        rows = [
            DataRow(cells=[DataCell(ft.Text(str(cell))) for cell in row])
            for row in data
        ]

        page.add(
            Column(controls=[
                ft.ListView(
                    controls=[
                        DataTable(
                            columns=columns,
                            rows=rows,
                            width=700
                        )
                    ],
                    height=400,  
                ),
                ft.ElevatedButton(text="Voltar", on_click=show_main_layout)
        ])
        )
        page.update()

    # Adiciona os botões "Cadastrar" e "Listar"
    page.add(Column(controls=[
        ft.ElevatedButton(text="Cadastrar", on_click=create),
        ft.ElevatedButton(text="Listar", on_click=get)
    ]))

    page.update()

ft.app(target=main)
