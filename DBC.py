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
        
    def insertarActaNacimiento (self,DAN):

        if  self.connection.is_connected():

            cursor = self.connection.cursor(buffered=True)  #nro_acta, nombres, apellidos, fecha_nacimiento, hora_nacimiento, lugar_nacimiento, sexo, cedula_padre, nombre_padre, apellido_padre, cedula_madre, nombre_madre, apellido_madre, id_prefectura
            sql = "INSERT INTO acta_nacimiento(nro_acta, nombres, apellidos, fecha_nacimiento, hora_nacimiento, lugar_nacimiento, sexo, cedula_padre, nombre_padre, apellido_padre, cedula_madre, nombre_madre, apellido_madre, id_prefectura) VALUES (null,'{0}','{1}','{2}','{3}','{4}','{5}',{6},'{7}','{8}',{9},'{10}','{11}',{12})"
        
            cursor.execute(sql.format(DAN[0], DAN[1], DAN[2], DAN[3], DAN[4], DAN[5], DAN[6], DAN[7], DAN[8], DAN[9], DAN[10], DAN[11],DAN[12]))
            
            self.connection.commit()

            cursor.close()

    def insertarCedula (self,DC):

        if  self.connection.is_connected():

            cursor = self.connection.cursor()
            
            sql = "INSERT INTO cedula(n_cedula, acta_nacimiento, nombres, apellidos, estado_civil, sexo, fecha_emision, fecha_vencimiento, nacionalidad) VALUES ({0}, {1},'{2}','{3}','{4}','{5}','{6}','{7}','{8}')"

            #sql = "INSERT INTO cedula (n_cedula,acta_nacimiento, estado_civil, sexo, fecha_emision, fecha_vencimiento, nacionalidad) VALUES ({0}, {1}, '{2}', '{3}', '{4}', '{5}', '{6}')"
            
            cursor.execute(sql.format(DC[0],DC[1],DC[2],DC[3],DC[4],DC[5],DC[6],DC[7],DC[8]))

            self.connection.commit()

    def insertarActaMatrimonio(self,DAM):

        cursor = self.connection.cursor(buffered=True)  

        sql = "INSERT INTO acta_matrimonio (nro_acta, fecha_acta, id_contrayente1, ocupacion_contrayente1, direccion_contrayente1, id_contrayente2, ocupacion_contrayente2, direccion_contrayente2, id_registrador_civil, id_testigo1, id_testigo2, id_prefectura) VALUES (null,'{0}', {1}, '{2}', '{3}', {4}, '{5}', '{6}', {7}, {8}, {9}, {10})"
        cursor.execute (sql.format(DAM[0], DAM[1], DAM[2], DAM[3], DAM[4], DAM[5], DAM[6], DAM[7], DAM[8], DAM[9], DAM[10]))
            
        self.connection.commit()

    def insertarActaDivorcio(self,DAD):

        cursor = self.connection.cursor(buffered=True)  

        sql = "INSERT INTO acta_divorcio(n_acta, Id_acta_matrimonio, c_conyuge1, direccion_esposo1, c_conyuge2, direccion_esposo2, id_ab_conyuge1, id_ab_conyuge2, id_hijo1, id_hijo2, id_prefectura) VALUES (null,{0},{1}, '{2}', {3},'{4}', {5}, {6}, {7}, {8}, {9})"
        cursor.execute (sql.format(DAD[0], DAD[1], DAD[2], DAD[3], DAD[4], DAD[5], DAD[6], DAD[7], DAD[8], DAD[9]))
            
        self.connection.commit()

    def insertarActaDefuncion (self,AD):

        cursor = self.connection.cursor(buffered=True)  
                                                                                                                                                                                                                                        #(a_nacimiento_fallecido, edad_fallecido, sexo_fallecido, estado_civil_f, fecha_defuncion, hora_defuncion, lugar_defuncion, causa_muerte, c_informante, relacion_informante                        
        sql = "INSERT INTO acta_defuncion(id_acta_defuncion, a_nacimiento_fallecido, edad_fallecido, sexo_fallecido, estado_civil_f, fecha_defuncion, hora_defuncion, lugar_defuncion, causa_muerte, c_informante, relacion_informante) VALUES (null,{0}, {1}, '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', {8}, '{9}')"
        cursor.execute (sql.format(AD[0], AD[1], AD[2], AD[3], AD[4], AD[5], AD[6], AD[7], AD[8], AD[9]))
                
        self.connection.commit()

    # CONSULTAS DE TABLAS

    def consultaActaNacimiento (self):
        
        if  self.connection.is_connected():

            cursor = self.connection.cursor(buffered=True)  
                    

            sql = "SELECT a.nro_acta,a.nombres,a.apellidos,a.fecha_nacimiento,a.hora_nacimiento,a.lugar_nacimiento, a.sexo, a.cedula_padre,a.nombre_padre, a.apellido_padre, a.cedula_madre, a.nombre_madre, a.apellido_madre, p.nombre_registro, p.estado, p.municipio, p.parroquia, p.direccion, p.director_nombre, p.director_apellido FROM acta_nacimiento a JOIN prefecturas p ON a.id_prefectura = p.id_prefectura"

            cursor.execute(sql)
            
            myresult = cursor.fetchall()
            
            return myresult

    def ConsultaCedula (self):

        if  self.connection.is_connected():

            cursor = self.connection.cursor(buffered=True)  
            
            sql = "SELECT c.n_cedula, c.nombres, c.apellidos, c.estado_civil, c.sexo, a.fecha_nacimiento, c.fecha_emision, c.fecha_vencimiento, c.nacionalidad FROM cedula c JOIN acta_nacimiento a ON c.acta_nacimiento = a.nro_acta"

            cursor.execute(sql)
            
            myresult = cursor.fetchall()
            
            return myresult   

    def ConsultaMatrimonio (self):

        if  self.connection.is_connected():

            cursor = self.connection.cursor(buffered=True)  
            
            sql = "SELECT a.nro_acta, a.fecha_acta, a.id_contrayente1, c1.nombres, c1.apellidos, a.ocupacion_contrayente1, a.direccion_contrayente1,a.id_contrayente2, c2.nombres, c2.apellidos, a.ocupacion_contrayente2, a.direccion_contrayente2, a.id_registrador_civil, c3.nombres, c3.apellidos, a.id_testigo1, c4.nombres, c4.apellidos, a.id_testigo2, c5.nombres, c5.apellidos, p.nombre_registro, p.estado, p.municipio, p.parroquia, p.direccion, p.director_nombre, p.director_apellido FROM acta_matrimonio a JOIN cedula c1 ON a.id_contrayente1 = c1.n_cedula JOIN cedula c2 ON a.id_contrayente2 = c2.n_cedula JOIN cedula c3 ON a.id_registrador_civil = c3.n_cedula JOIN cedula c4 ON a.id_testigo1 = c4.n_cedula JOIN cedula c5 ON a.id_testigo2 = c5.n_cedula JOIN prefecturas p ON a.id_prefectura = p.id_prefectura"

            cursor.execute(sql)
            
            myresult = cursor.fetchall()
            
            return myresult

    def consultarActaDivorcio(self):
        
        if  self.connection.is_connected():

                cursor = self.connection.cursor(buffered=True)  
                
                sql = "SELECT a.n_acta,  a.c_conyuge1, c1.nombres, c1.apellidos, a.direccion_esposo1, a.c_conyuge2, c2.nombres, c2.apellidos, a.direccion_esposo2, a.id_ab_conyuge1, c3.nombres, c3.apellidos, a.id_ab_conyuge2, c4.nombres, c4.apellidos, a.id_hijo1, an1.nombres, an1.apellidos, a.id_hijo2, an2.nombres, an2.apellidos, a.id_prefectura, p.nombre_registro, p.estado, p.municipio, p.parroquia, p.direccion, p.director_nombre, p.director_apellido FROM acta_divorcio a JOIN cedula c1 ON a.c_conyuge1 = c1.n_cedula JOIN cedula c2 ON a.c_conyuge2 = c2.n_cedula JOIN cedula c3 ON a.id_ab_conyuge1 = c3.n_cedula JOIN cedula c4 ON a.id_ab_conyuge2 = c4.n_cedula JOIN acta_nacimiento an1 ON a.id_hijo1 = an1.nro_acta JOIN acta_nacimiento an2 ON a.id_hijo2 = an2.nro_acta JOIN prefecturas p ON a.id_prefectura = p.id_prefectura"

                cursor.execute(sql)
                
                myresult = cursor.fetchall()
                
                return myresult

    def consultarAD (self):

        if  self.connection.is_connected():

                cursor = self.connection.cursor(buffered=True)  
                
                sql = "SELECT ad.id_acta_defuncion,an.nombres,an.apellidos,ad.edad_fallecido,ad.sexo_fallecido,ad.estado_civil_f,ad.fecha_defuncion,ad.hora_defuncion,ad.lugar_defuncion,ad.causa_muerte,ad.c_informante,c.nombres,c.apellidos, ad.relacion_informante, an.nombre_madre, an.apellido_madre, an.nombre_padre, an.apellido_padre FROM acta_defuncion ad JOIN acta_nacimiento an ON ad.a_nacimiento_fallecido = an.nro_acta JOIN cedula c ON ad.c_informante = c.n_cedula"

                cursor.execute(sql)
                
                myresult = cursor.fetchall()
                
                return myresult

    # CONSULTAS PRUEBAS

    def consultaVCedula (self):

        if  self.connection.is_connected():

            cursor = self.connection.cursor(buffered=True)  
                    
            sql = "SELECT n_cedula FROM cedula"

            cursor.execute(sql)
            
            myresult = cursor.fetchall()

            cursor.close()

            return myresult
         
    def consultaVActaNacimiento(self):


        if  self.connection.is_connected():

            cursor = self.connection.cursor(buffered=True)  
                    
            sql = "SELECT nro_acta FROM acta_nacimiento"

            cursor.execute(sql)
            
            myresult = cursor.fetchall()

            cursor.close()

            return myresult

    def consultaVActaMatrimonio (self):

        cursor = self.connection.cursor(buffered=True)  
                    
        sql = "SELECT nro_acta FROM acta_matrimonio"

        cursor.execute(sql)
            
        myresult = cursor.fetchall()

        cursor.close()

        return myresult

    # UPDATES

    def actaNacimientoUpdate(self, DAN):
        
        if  self.connection.is_connected():

            cursor = self.connection.cursor()  #nro_acta, nombres, apellidos, fecha_nacimiento, hora_nacimiento, lugar_nacimiento, sexo, cedula_padre, nombre_padre, apellido_padre, cedula_madre, nombre_madre, apellido_madre, id_prefectura
            
            sql = "UPDATE acta_nacimiento SET nombres = '{0}', apellidos = '{1}', fecha_nacimiento = '{2}', hora_nacimiento = '{3}', lugar_nacimiento = '{4}', sexo = '{5}', cedula_padre = {6}, nombre_padre = '{7}', apellido_padre = '{8}', cedula_madre = {9}, nombre_madre = '{10}', apellido_madre = '{11}', id_prefectura = {12} WHERE nro_acta = {13}"
                                              #nombres         apellidos          fecha_nacimiento          hora_nacimiento          lugar_nacimiento           sexo          cedula_padre        nombre_padre          apellido_padre         cedula_madre        nombre_madre,         apellido_madre            id_prefectura

            cursor.execute(sql.format(DAN[0], DAN[1], DAN[2], DAN[3], DAN[4], DAN[5], DAN[6], DAN[7], DAN[8], DAN[9], DAN[10], DAN[11],DAN[12],DAN[13]))
            
            self.connection.commit()

            cursor.close()

    def cedulaUptate(self,DC):

        if  self.connection.is_connected():

            cursor = self.connection.cursor()
            
            sql = "UPDATE cedula SET n_cedula = {0}, nombres = '{1}', apellidos = '{2}', estado_civil = '{3}', sexo = '{4}', fecha_emision = '{5}', fecha_vencimiento = '{6}', nacionalidad = '{7}' WHERE n_cedula = {0}"

            cursor.execute(sql.format(DC[0],DC[2],DC[3],DC[4],DC[5],DC[6],DC[7],DC[8]))
            
            self.connection.commit()


