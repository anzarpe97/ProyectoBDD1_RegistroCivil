import mysql.connector
from mysql.connector import Error

class DAO ():
    
    def __init__ (self):

        try:

            self.connection = mysql.connector.connect(
                host = "localhost",
                port = 3306,
                user = "root",
                db="registrocivilbdd")
            
            if self.connection.is_connected():

                print("Se ha conectado a la base de datos satisfactoriamente.")

        except Error as ex:

            print("Error al conectar la base de datos: {0}".format(ex))

    def listaTablas (self):

        if self.connection.is_connected():
        
            try:

                cursor = self.connection.cursor()
                cursor.execute("SELECT * FROM acta_nacimiento ORDER BY nombres ASC")

                result = cursor.fetchall()

                return result

            except Error as ex:

                print("Error al conectar la base de datos: {0}".format(ex))