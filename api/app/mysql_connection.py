import mysql.connector
import sys

def get_connection():


    if 'pytest' in sys.modules:
        host = '127.0.0.1'
    else:
        host = 'tc_database'

    connection = mysql.connector.connect(
                user='root',
                password='ROOTPASS',
                host=host, # Deve ser o mesmo nome do serviço/container criado no docker-compose.yml, (ou verificar no docker network)
                port=3306,
                database='TechChallenge'
            )
    
    cursor = connection.cursor(dictionary=True)
    return connection, cursor


    