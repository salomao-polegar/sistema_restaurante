from app.mysql_connection import get_connection

def test_conexao_mysql():
    connection, cursor = get_connection()
    assert connection.is_connected() == True


