from tkinter import messagebox as MessageBox
from tkinter import *
from DBC import DAO

consul = DAO()    

def guardarDatosAcNacimiento (nombre, apellido, FechaNacimiento, horaNacimiento, sexo, cedulaPadre, nombrePadre, apellidoPadre, cedulaMadre, nombreMadre, apellidoMadre, lugarNacimiento):
    
    if nombre == "" or  apellido == "" or sexo == "" or lugarNacimiento == "" or FechaNacimiento == "" or horaNacimiento == "": 
        
        MessageBox.showwarning("Datos Incompletos", "Rellena los campos: \n\n- Nombres\n- Apellidos\n- Sexo\n- Lugar De Nacimiento\n- Prefectura\n\nY vuelve a intentarlo.")
     
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
            flag= True

        except ValueError:
             
             MessageBox.showwarning("Datos Incompletos","Debes ingresar un valor numerico en los campos: \n- Cedula Padre\n- Cedula Madre\n\n- Intentelo Nuevamente")
             flag =False

        # Diccionario Acta Nacimiento

        if flag == True:

            datosActaNacimiento = [nombre, apellido, FechaNacimiento, horaNacimiento, sexo, cedulaPadre, nombrePadre, apellidoPadre, cedulaMadre, nombreMadre, apellidoMadre, lugarNacimiento]
            consul.listaTablas(datosActaNacimiento)

            MessageBox.showinfo(message = "Resgistro Creado satisfactoriamente.", title = "Registro Civil")
    

