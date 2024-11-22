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
    exclude_columns = {'remember_token', 'created_at', 'updated_at', 'email_verified_at'}  
    column_names = []

    for linha in cursor.description:
        if linha[0] not in exclude_columns:  
            column_names.append(linha[0])

    cursor.nextset()

    return column_names

def getAll():
    cursor.execute('select * from users')
    results = cursor.fetchall()
    headers = tableHeader()  
    
    data = [[row[i] for i in range(len(headers))] for row in results]
    
    cursor.nextset()
    return data



def insert_user(name, email, password):
    # Criptografar o password
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    query = """
    INSERT INTO users (name, email, password)
    VALUES (%s, %s, %s)
    """

    cursor.execute(query, (name, email, hashed_password))

    conn.commit()
    cursor.nextset()
    return "Usuário " + name+ " inserido com sucesso!"
