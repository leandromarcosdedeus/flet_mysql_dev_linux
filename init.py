import flet as ft
from flet import Page, Row, DataTable, DataColumn, DataRow, DataCell, Column
from database import conn

def main(page: Page):
    page.title = "Cadastro de Funcionário"

    headers = conn.tableHeader()

    dict_values = {
        'name': '', 'email': '', 'password': ''
    }

    def create(e):
        page.controls.clear()
        
        def register(e):

            conn.insert_user(str(dynamic_fields[0].value), str(dynamic_fields[1].value),str(dynamic_fields[2].value))
            print(conn.getAll())

        dynamic_fields = [ft.TextField(label=i, width=100) for i in headers]
        page.add(Row(controls=[
            *dynamic_fields,
            ft.ElevatedButton(text="Cadastrar", on_click=register),
        ]))
        page.update()

    def get(e):
        data = conn.getAll()
        print(data)
        page.controls.clear()

        # Criar as colunas dinamicamente com base nos headers
        columns = [DataColumn(label=ft.Text(header)) for header in headers]

        # Criar as linhas de dados
        rows = [
            DataRow(cells=[DataCell(ft.Text(str(cell))) for cell in row])
            for row in data
        ]

        # Adiciona a tabela na página
        page.add(
            DataTable(
                columns=columns,
                rows=rows,
                width=700
            )
        )
        page.update()

    # Adiciona os botões "Cadastrar" e "Listar"
    page.add(Column(controls=[
        ft.ElevatedButton(text="Cadastrar", on_click=create),
        ft.ElevatedButton(text="Listar", on_click=get)
    ]))

    page.update()

ft.app(target=main)
