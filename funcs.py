import mysql.connector, json

def conn_db():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='1234',
        database='database_ipo'
        )

    try:
        cursor = conn.cursor()
        if conn.is_connected():
            print('Conectado ao banco de dados')
            return cursor, conn
        else:
            print('Não foi possível conectar ao banco de dados')
            return None
            
    except Exception as e:
        print('Erro ao conectar com o banco de dados: ', e)
        return None

conn_db()
