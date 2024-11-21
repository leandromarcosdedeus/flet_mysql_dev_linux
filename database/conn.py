#para instalar o mysql connector: pip install mysql-connector-python
#bcript para criptografar: pip install bcrypt

import mysql.connector
import bcrypt

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345678",
    database="forge"
)

cursor = conn.cursor()

def tableHeader():
    cursor.execute('select * from users')
    exclude_columns = {'id', 'remember_token', 'created_at', 'updated_at', 'email_verified_at'}  # Colunas a serem excluídas
    column_names = []

    for linha in cursor.description:
        if linha[0] not in exclude_columns:  # Verifica se a coluna não está na lista de exclusão
            column_names.append(linha[0])

    print(column_names)
    cursor.nextset()

    return column_names

def getAll():
    cursor.execute('select * from users')
    results = cursor.fetchall()
    headers = tableHeader()  # Obtemos os nomes das colunas
    data = []

    for row in results:
        row_data = {headers[i]: row[i] for i in range(len(headers))}  # Cria um dicionário com header como chave
        data.append(row_data)
    
    cursor.nextset()
    return data


def insert_user(name, email, password):
    # Criptografar o password
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    query = """
    INSERT INTO users (name, email, password)
    VALUES (%s, %s, %s)
    """

    # Executando a query com os valores
    cursor.execute(query, (name, email, hashed_password))

    conn.commit()
    cursor.nextset()

    print("Usuário inserido com sucesso!")
