from tkinter import messagebox as MessageBox
from tkinter import *
from DBC import DAO

consul = DAO()    
                            #nombres, apellidos, fecha_nacimien, hora_nacimiento,lugar_nacimiento, sexo, cedulapadre, nombrepadre, apellidopadre, cedulamadre, nombremadre, apellidomadre, prefectura
def guardarDatosAcNacimiento (nombre, apellido, FechaNacimiento, horaNacimiento, lugarNacimiento, sexo, cedulaPadre, nombrePadre, apellidoPadre, cedulaMadre, nombreMadre, apellidoMadre,  prefectura):
    
    if nombre == "" or  apellido == "" or sexo == "" or lugarNacimiento == "" or FechaNacimiento == "" or horaNacimiento == "": 
        
        MessageBox.showwarning("Datos Incompletos", "Rellena los campos: \n\n- Nombres\n- Apellidos\n- Sexo\n- Lugar De Nacimiento\n- Hora De nacimiento\n- Fecha de Nacimiento\n\nY vuelve a intentarlo.")
     
    else:

        flag = True
        # Acomodar Nombres

        nombre = nombre.title()
        apellido = apellido.title()

        nombrePadre = nombrePadre.title()
        apellidoPadre = apellidoPadre.title() 

        nombreMadre = nombreMadre.title()
        apellidoMadre = apellidoMadre.title()

        lugarNacimiento = lugarNacimiento.title()
        
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
             
            

        if prefectura == "Coquivacoa":
                
                prefectura = 1
                
        elif prefectura == "Chiquinquira":
                
                prefectura = 2
                    
        elif prefectura ==  "Cacique Mara":
                
                prefectura = 3
                
        elif prefectura == "Olegarios Villalobos":
                
                prefectura = 4

        # Diccionario Acta Nacimiento
        
        if flag == True :

            datosPrefectura = consul.traerDatos(prefectura)

            nombrePrefectura = datosPrefectura[0]
            nombreDir = datosPrefectura[1]
            apellidoDir = datosPrefectura[2]
                                #(nombres, apellidos, fechanacimiento, horanacimiento, lugar_nacimiento, sexo, cedulapadre, nombrepadre, apellidopadre, cedulamadre, nombremadre, apellidomadre, prefectura, nombreregistrocivil, dirregistro_nmbr,dir_registroaplld)
            datosActaNacimiento = [nombre, apellido, FechaNacimiento, horaNacimiento, lugarNacimiento, sexo, cedulaPadre, nombrePadre, apellidoPadre, cedulaMadre, nombreMadre, apellidoMadre,  prefectura,nombrePrefectura,nombreDir,apellidoDir]

            consul.insertarActaNacimiento(datosActaNacimiento)

            MessageBox.showinfo(message = "Resgistro Creado satisfactoriamente.", title = "Registro Civil")
    
def guardarCedulaIdentidad (numCedula,numActaNacimiento,estadoCivil,sexo,fechaEmision,fechaVencimiento,nacionlidad):
    
    flag = True

    if numCedula == "" or numActaNacimiento== "" or estadoCivil== "" or sexo == ""  or fechaEmision == "" or fechaVencimiento == "" or nacionlidad == "":
 
        MessageBox.showwarning("Datos Incompletos", "Rellena los campos: \n\n- Numero Acta Nacimiento\n- Numero de Cedula\n- Fecha Emision\n- Fecha Vencimiento\n- Estado Civil\n- Nacionalidad\n- Genero \n\nY vuelve a intentarlo.")
    
    try:
         
        numCedula = int(numCedula)
        numActaNacimiento = int (numActaNacimiento)

    except ValueError:
             
            MessageBox.showwarning("Datos Incompletos","Debes ingresar un valor numerico en los campos: \n- Cedula Padre\n- Cedula Madre\n\n- Intentelo Nuevamente")
            flag =False

    if flag == True :

            datosCedula = [numCedula, numActaNacimiento, estadoCivil, sexo, fechaEmision, fechaVencimiento, nacionlidad]
            print(datosCedula)
            consul.insertarCedula (datosCedula)
            
            MessageBox.showinfo(message = "Resgistro Creado satisfactoriamente.", title = "Registro Civil")