import mysql.connector

cnx = mysql.connector.connect(user="dataUser",
                              password="urubu100", 
                              host="localhost", 
                              database="dadosMaquina", 
                              autocommit=True)

def insert(query): 
    try:
        cnx.reconnect()
        cursor = cnx.cursor()
        cursor.execute(query)
    except mysql.connector.connector.Error as error:
        print("ERRO {}".format(error))
    finally:
        if cnx.is_connected():
            cursor.close()
            cnx.close()
            return cursor.rowcount

def select(query, isAllRequested = False):
    try:
        cnx.reconnect()
        cursor = cnx.cursor()
        cursor.execute(query)
        if isAllRequested:
            dados = cursor.fetchall()
        else:
            dados = cursor.fetchone()
    except mysql.connector.Error as error:
        print('Erro')
        dados = error
    finally:
        if cnx.is_connected():
            cursor.close()
            cnx.close()
            return dados