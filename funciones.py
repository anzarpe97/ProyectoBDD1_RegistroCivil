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
            SOcupacion = SOcupacion.title

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

            #

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

        if flag == True:
             
            DatosActaMatrimonio =[fechaActa, Pcontrayente, PDireccion, POcupacion, SContrayente, SDireccion, SOcupacion, registradorCivil, PTestigo, STestigo, prefectura]
     
            consul.insertarCedula (DatosActaMatrimonio)
                
            MessageBox.showinfo(message = "Resgistro Creado satisfactoriamente.", title = "Registro Civil")

# CONSULTAS

def consultarActaNacimiento ():
     
    datos = consul.consultaActaNacimiento()

    return datos

def consultarCedulas ():
     
    dato = consul.ConsultaCedula()

    return dato 

def prueba(fechaActa, Pcontrayente, PDireccion, POcupacion, SContrayente, SDireccion, SOcupacion, registradorCivil, PTestigo, STestigo, prefectura):
     
    print(fechaActa, Pcontrayente, PDireccion, POcupacion, SContrayente, SDireccion, SOcupacion, registradorCivil, PTestigo, STestigo, prefectura)
