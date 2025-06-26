from mysql.connector import MySQLConnection

HOST = 'localhost'
USER = 'root'
PASSWORD = 'Mantenhaofoco125#'

def get_connection(database: str = "casaviva") -> MySQLConnection:
    try:
        connection = MySQLConnection(
            host=HOST,
            user=USER,
            password='Mantenhaofoco125#',
            database="casaviva"
        )
        
        return connection
    
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None
    