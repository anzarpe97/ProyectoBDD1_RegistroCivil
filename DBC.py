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

    def traerDatos(self):
        
        if self.connection.is_connected():

            cursor = self.connection.cursor()

            sql = "SELECT nombre_registro, director_nombre, director_apellido FROM prefecturas WHERE id_prefecturas = 4"
            
            cursor.execute(sql)
            
            datosPrefecturas = cursor.fetchone()
            
            print(datosPrefecturas[0])
            print(datosPrefecturas[1])
            print(datosPrefecturas[2])
            
            return datosPrefecturas
    
    def insertarActaNacimiento (self,DAN):

        if  self.connection.is_connected():

            cursor = self.connection.cursor()
            sql = "INSERT INTO acta_nacimiento (nro_acta, nombres, apellidos, fecha_nacimiento, hora_nacimiento, sexo, cedula_padre, nombre_padre, apellido_padre, cedula_madre,nombre_madre, apellido_madre,id_prefectura, nombre_registro_civil, dir_registro_nmbr, dir_registro_aplld) VALUES (null,'{0}', '{1}', '{2}', '{3}', '{4}', {5}, '{6}', '{7}', {8}, '{9}', '{10}', '{11}')"
            cursor.execute(sql.format(DAN[0],DAN[1],DAN[2],DAN[3],DAN[4],DAN[5],DAN[6],DAN[7],DAN[8],DAN[9],DAN[10],DAN[11]))
            self.connection.commit()

        else: 
             
            print("Puto")

    def insertarCedula (self,DC):

        if  self.connection.is_connected():
            print(DC[5])
            cursor = self.connection.cursor()
            sql = "INSERT INTO cedula (n_cedula,acta_nacimiento, estado_civil, sexo, fecha_emision, fecha_vencimiento, nacionalidad) VALUES ({0}, {1}, '{2}', '{3}', '{4}', '{5}', '{6}')"
            cursor.execute(sql.format(DC[0],DC[1],DC[2],DC[3],DC[4],DC[5],DC[6]))
            self.connection.commit()

        else: 
             
            print("Puto")


        