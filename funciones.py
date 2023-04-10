from tkinter import messagebox as MessageBox
from tkinter import *
from DBC import DAO

consul = DAO()    

def guardarDatosAcNacimiento (nombre, apellido, FechaNacimiento, horaNacimiento, lugarNacimiento, sexo, cedulaPadre, nombrePadre, apellidoPadre, cedulaMadre, nombreMadre, apellidoMadre,  prefectura):
    
    if nombre == "" or  apellido == "" or sexo == "" or lugarNacimiento == "" or FechaNacimiento == "" or horaNacimiento == "": 
        
        MessageBox.showwarning("Datos Incompletos", "Rellena los campos: \n\n- Nombres\n- Apellidos\n- Sexo\n- Lugar De Nacimiento\n- Hora De nacimiento\n- Fecha de Nacimiento\n\nY vuelve a intentarlo.")
     
    else:

        flag = True

        # ACOMODAMOS lOS NOMBRES

        if flag == True:
        
        # Acomodar Nombres

            nombre = nombre.title()
            apellido = apellido.title()

            nombrePadre = nombrePadre.title()
            apellidoPadre = apellidoPadre.title() 

            nombreMadre = nombreMadre.title()
            apellidoMadre = apellidoMadre.title()

            lugarNacimiento = lugarNacimiento.title()

        # ACOMODAMOS LA FECHA

        if flag == True:

            # Acomodar Fecha

            dia = FechaNacimiento[0:2]
            mes = FechaNacimiento[3:5]
            anio = FechaNacimiento[6:10]

            FechaNacimiento = anio + "-" + mes +"-"+ dia
 
            try:
                
                dia = int(dia)
                mes = int (mes)
                anio = int (anio)

                if dia < 1 or dia > 31:
                    MessageBox.showwarning("Formato Incorrecto","- El dia que ingreso no es valido \n\n- Intentelo Nuevamente")
                    flag = False

                if mes < 1 or mes > 12:
                    
                    MessageBox.showwarning("Formato Incorrecto","- El mes que ingreso no es valido \n\n- Intentelo Nuevamente")
                    flag = False

                if mes == 2 and dia > 28:
                    MessageBox.showwarning("Formato Incorrecto","El mes de febrero solo llega hasta el dia 28\n\n- Intentelo Nuevamente")
                    flag = False

            except ValueError:
                
                MessageBox.showwarning("Formato Incorrecto","-El formato que ha ingresado es incorrecto, debe ingresar la fecha en el formato: \n\n             DD-MM-AAAA\n\n- Intentelo Nuevamente")
                
                flag = False
        
        # VERIFICAMOS SI LA CEDULAS SON TIPO INT

        if flag == True:

            try:
                
                cedulaPadre = int(cedulaPadre)
                cedulaMadre = int(cedulaMadre)

                if cedulaMadre == "" or cedulaPadre == "":
                    
                    if cedulaPadre == "":
                        cedulaPadre = 0
                    
                    else:
                        cedulaMadre = 0 
                        
                flag= True
                

            except ValueError:
                
                MessageBox.showwarning("Datos Incompletos","Debes ingresar un valor numerico en los campos: \n- Cedula Padre\n- Cedula Madre\n\n- Intentelo Nuevamente")
                flag =False 

        # ESCOJEMOS LA PREFECTURA ID

        if flag == True:

            if prefectura == "Coquivacoa":
                    
                    prefectura = 1
                    
            elif prefectura == "Chiquinquira":
                    
                    prefectura = 2
                        
            elif prefectura ==  "Cacique Mara":
                    
                    prefectura = 3
                    
            elif prefectura == "Olegarios Villalobos":
                    
                    prefectura = 4
            
            else:
                
                flag = False
                MessageBox.showinfo(message = "- Haz ingresado una prefectura Incorrecta\n\n- Vuelve a intentarlo", title = "Registro Civil")

        # Diccionario Acta Nacimiento
        
        if flag == True :
            
            datosActaNacimiento = [nombre, apellido, FechaNacimiento, horaNacimiento, lugarNacimiento, sexo, cedulaPadre, nombrePadre, apellidoPadre, cedulaMadre, nombreMadre, apellidoMadre,  prefectura]

            consul.insertarActaNacimiento(datosActaNacimiento)

            MessageBox.showinfo(message = "Resgistro Creado satisfactoriamente.", title = "Registro Civil")
                     
def guardarCedulaIdentidad (numCedula,numActaNacimiento,nombres,apellidos,estadoCivil,sexo,fechaEmision,nacionlidad):
    
    flag = True
    
    # VERIFICAMOS SI LOS DATOS IMPORTANTES SE INGRESARON

    if numCedula == "" or numActaNacimiento== "" or estadoCivil== "" or sexo == ""  or fechaEmision == ""  or nacionlidad == "":
 
        MessageBox.showwarning("Datos Incompletos","Debes ingresar un valor numerico en los campos: \n- Numero Acta Nacimiento\n- Numero Cedula\n- Fecha Emision\n- Fecha Vencimiento\n- Estado Civil\n- Nacionalidad\n- Genero\n\n- Intentelo Nuevamente")
    
    else: 
        
        try:
            
            numCedula = int(numCedula)
            numActaNacimiento = int (numActaNacimiento)

        except ValueError:
                
                MessageBox.showwarning("Datos Incompletos","- Debes ingresar valores numericos en los campos: \n\n- Numero Acta Nacimiento\n- Numero Cedula")
                flag = False

            
        if flag == True:
             
             nombres = nombres.title()
             apellidos = apellidos.title()

            # Acomodar Fecha

        if flag == True:

                # Acomodar Fecha

            dia = fechaEmision[0:2]
            mes = fechaEmision[3:5]
            anio = fechaEmision[6:10]

            fechaEmision = anio + "-" + mes +"-"+ dia
    
            try:
                    
                dia = int(dia)
                mes = int (mes)
                anio = int (anio)

                anio = anio + 10

                fechaVencimiento = str(anio) + "-" + str (mes)+ "-" + str (dia)

            except ValueError:
                    
                MessageBox.showwarning("Formato Incorrecto","-El formato que ha ingresado es incorrecto, debe ingresar la fecha en el formato: \n\n             DD-MM-AAAA\n\n- Intentelo Nuevamente")
                    
                flag = False

        if flag == True:


                datosCedula = [numCedula,numActaNacimiento, nombres,apellidos, estadoCivil, sexo, fechaEmision, fechaVencimiento, nacionlidad]
            
                consul.insertarCedula (datosCedula)
                    
                MessageBox.showinfo(message = "Resgistro Creado satisfactoriamente.", title = "Registro Civil")

def guardarActaMatrimonio (fechaActa, Pcontrayente, PDireccion, POcupacion, SContrayente, SDireccion, SOcupacion, registradorCivil, PTestigo, STestigo, prefectura):
     
    flag = True
    
    # VERIFICAMOS SI LOS DATOS IMPORTANTES SE INGRESARON

    if fechaActa == "" or Pcontrayente == 0 or PDireccion == "" or POcupacion == "" or SContrayente == 0 or SDireccion == "" or SOcupacion == "" or registradorCivil == 0 or  PTestigo == 0 or STestigo == 0:
 
        MessageBox.showwarning("Datos Incompletos","Debes ingresar un valor numerico en los campos: \n- Numero Acta Nacimiento\n- Numero Cedula\n- Fecha Emision\n- Fecha Vencimiento\n- Estado Civil\n- Nacionalidad\n- Genero\n\n- Intentelo Nuevamente")
    
    else: 
        
        #PASAMOS LAS CEDULAS A INT

        try:

            Pcontrayente = int (Pcontrayente)
            SContrayente = int (SContrayente)
            registradorCivil = int (registradorCivil)
            PTestigo = int (PTestigo)
            STestigo = int (STestigo)


        except ValueError:
                
                MessageBox.showwarning("Datos Incompletos","- Debes ingresar valores numericos en los campos: \n\n Cedula P contrayente \nCedula S Contrayente \n Cedula Registrador Civil \nPrimer Testigo \nSegundo Testigo")
                
                flag = False

        # ACOMODAR TEXTO INGRESADO            
        
        if flag == True:
             
            PDireccion = PDireccion.title()
            POcupacion = POcupacion.title()
            SDireccion = SDireccion.title()
            SOcupacion = SOcupacion.title()

        # Acomodar Fecha

        if flag == True:

            dia = fechaActa[0:2]
            mes = fechaActa[3:5]
            anio = fechaActa[6:10]

            fechaActa = anio + "-" + mes +"-"+ dia
    
            try:
                    
                dia = int(dia)
                mes = int (mes)
                anio = int (anio)

                anio = anio + 10

                fechaVencimiento = str(anio) + "-" + str (mes)+ "-" + str (dia)

            except ValueError:
                    
                MessageBox.showwarning("Formato Incorrecto","-El formato que ha ingresado es incorrecto, debe ingresar la fecha en el formato: \n\n             DD-MM-AAAA\n\n- Intentelo Nuevamente")
                    
                flag = False

        # SELECIONAR PREFECTURA

        if flag == True:

            if prefectura == "Coquivacoa":
                    
                    prefectura = 1
                    
            elif prefectura == "Chiquinquira":
                    
                    prefectura = 2
                        
            elif prefectura ==  "Cacique Mara":
                    
                    prefectura = 3
                    
            elif prefectura == "Olegarios Villalobos":
                    
                    prefectura = 4
            
            else:
                
                flag = False
                MessageBox.showinfo(message = "- Haz ingresado una prefectura Incorrecta\n\n- Vuelve a intentarlo", title = "Registro Civil")

        # HACER CONSULTA

        if flag == True:
             
            DatosActaMatrimonio =[fechaActa, Pcontrayente, PDireccion, POcupacion, SContrayente, SDireccion, SOcupacion, registradorCivil, PTestigo, STestigo, prefectura]
     
            consul.insertarActaMatrimonio(DatosActaMatrimonio)
                
            MessageBox.showinfo(message = "Resgistro Creado satisfactoriamente.", title = "Registro Civil")

def guardarActaDivorcio (Id_acta_matrimonio, c_conyuge1, direccion_esposo1, c_conyuge2, direccion_esposo2, id_ab_conyuge1, id_ab_conyuge2, id_hijo1, id_hijo2, prefectura):
     
    if Id_acta_matrimonio == 0 or  c_conyuge1 == 0 or direccion_esposo1 == "" or c_conyuge2 == 0 or direccion_esposo2 == "" or  id_ab_conyuge1 == 0 or  id_ab_conyuge2 == 0  or id_hijo1 == 0 or id_hijo2 == 0 or prefectura == "": 
        
     
        MessageBox.showwarning("Datos Incompletos", "Rellena los campos: \n\n- Numero Acta Matrimonio\n- Cedula P Esposo\n- Direccion P Esposo \n- Cedula S Esposo\n- Direccion S Esposo \n- Cedula Abg P Esposo \n- Cedula Abg S Esposo\n- Acta Nacimiento Hijo 1 \n- Acta Nacimiento Hijo 2 \n- Prefectura\n\nY vuelve a intentarlo.")
    else:

        flag = True

        # ACOMODAMOS DIRECCIONES

        if flag == True:
        
        # Acomodar Nombres

            direccion_esposo1 = direccion_esposo1.title()
            direccion_esposo2 = direccion_esposo2.title()
        
        # VERIFICAMOS SI LA CEDULAS SON TIPO INT

        if flag == True:

            try:
                
                Id_acta_matrimonio = int (Id_acta_matrimonio)
                c_conyuge1 = int (c_conyuge1)
                c_conyuge2 = int(c_conyuge2)
                id_ab_conyuge1 = int(id_ab_conyuge1)
                id_ab_conyuge2 = int (id_ab_conyuge2)
                id_hijo1 = int (id_hijo1)
                id_hijo2 = int (id_hijo2)
                
            except ValueError:
                
                MessageBox.showwarning("Datos Incompletos","Debes ingresar un valor numerico en los campos: \n- Cedula Padre\n- Cedula Madre\n\n- Intentelo Nuevamente")
                flag =False 

        # ESCOJEMOS LA PREFECTURA ID

        if flag == True:

            if prefectura == "Coquivacoa":
                    
                    prefectura = 1
                    
            elif prefectura == "Chiquinquira":
                    
                    prefectura = 2
                        
            elif prefectura ==  "Cacique Mara":
                    
                    prefectura = 3
                    
            elif prefectura == "Olegarios Villalobos":
                    
                    prefectura = 4
            
            else:
                
                flag = False
                MessageBox.showinfo(message = "- Haz ingresado una prefectura Incorrecta\n\n- Vuelve a intentarlo", title = "Registro Civil")

        # Diccionario Acta Nacimiento
        
        if flag == True :
            
            datosActaDivorcio = [Id_acta_matrimonio, c_conyuge1, direccion_esposo1, c_conyuge2, direccion_esposo2, id_ab_conyuge1, id_ab_conyuge2, id_hijo1, id_hijo2, prefectura]

            consul.insertarActaDivorcio(datosActaDivorcio)

            MessageBox.showinfo(message = "Resgistro Creado satisfactoriamente.", title = "Registro Civil")

def guardarActaDefuncion (a_nacimiento_fallecido, sexo_fallecido, estado_civil_f, fecha_defuncion, hora_defuncion, lugar_defuncion, causa_muerte, c_informante, relacion_informante):
     
    flag = True
    
    # VERIFICAMOS SI LOS DATOS IMPORTANTES SE INGRESARON

    if a_nacimiento_fallecido == 0 or sexo_fallecido == "" or estado_civil_f == "" or fecha_defuncion == "" or hora_defuncion == "" or lugar_defuncion == "" or causa_muerte == "" or c_informante == 0 or  relacion_informante == "":
 
        MessageBox.showwarning("Datos Incompletos","Debes ingresar un valor numerico en los campos: \n- Numero Acta Nacimiento\n- Numero Cedula\n- Fecha Emision\n- Fecha Vencimiento\n- Estado Civil\n- Nacionalidad\n- Genero\n\n- Intentelo Nuevamente")
    
    else: 
        
        #PASAMOS LAS CEDULAS A INT

        try:

            a_nacimiento_fallecido = int (a_nacimiento_fallecido)
            c_informante = int (c_informante)


        except ValueError:
                
                MessageBox.showwarning("Datos Incompletos","- Debes ingresar valores numericos en los campos: \n\n Cedula P contrayente \nCedula S Contrayente \n Cedula Registrador Civil \nPrimer Testigo \nSegundo Testigo")
                
                flag = False

        # ACOMODAR TEXTO INGRESADO            
        
        if flag == True:
             
            causa_muerte = causa_muerte.title()
            lugar_defuncion = lugar_defuncion.title()

        # Acomodar Fecha

        if flag == True:

            dia = fecha_defuncion[0:2]
            mes = fecha_defuncion[3:5]
            anio = fecha_defuncion[6:10]

            fecha_defuncion = anio + "-" + mes +"-"+ dia
    
            try:
                    
                dia = int(dia)
                mes = int (mes)
                anio = int (anio)

                edad_fallecido = 2023 - anio

            except ValueError:
                    
                MessageBox.showwarning("Formato Incorrecto","-El formato que ha ingresado es incorrecto, debe ingresar la fecha en el formato: \n\n             DD-MM-AAAA\n\n- Intentelo Nuevamente")
                    
                flag = False


        # HACER CONSULTA

        if flag == True:
             
            DatosActaDefuncion =[a_nacimiento_fallecido, edad_fallecido, sexo_fallecido, estado_civil_f, fecha_defuncion, hora_defuncion, lugar_defuncion, causa_muerte, c_informante, relacion_informante]
     
            consul.insertarActaDefuncion(DatosActaDefuncion)
            
            MessageBox.showinfo(message = "Resgistro Creado satisfactoriamente.", title = "Registro Civil")

# CONSULTAS

def consultarActaNacimiento ():
     
    datos = consul.consultaActaNacimiento()

    return datos

def consultarCedulas ():
     
    dato = consul.ConsultaCedula()

    return dato 

def consultarActaMatrimonio():
     
    dato = consul.ConsultaMatrimonio()

    return dato

def consultarActaDeuncion():
     
    dato = consul.consultarAD()

    return dato