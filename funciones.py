from tkinter import messagebox as MessageBox
from tkinter import *


def guardarDatosAcNacimiento (nombre, apellido, nombrePadre, CPadre, nombreMadre, CMadre, sexo, ubicacion, prefectura):
    
    if nombre == "" or  apellido == "" or sexo == "" or ubicacion == "" or prefectura == "": 
        
        MessageBox.showwarning("Datos Incompletos", "Rellena los campos: \n\n- Nombres\n- Apellidos\n- Sexo\n- Lugar De Nacimiento\n- Prefectura\n\nY vuelve a intentarlo.")
     
    else:

        # Acomodar Nombres
        nombreF = nombre.title()
        apellidoF = apellido.title()
        nombrePadreF =nombrePadre.title()
        nombreMadreF = nombreMadre.title()

        #Diccionario Acta Nacimiento
        ActaNacimientoDic = {"nombreBebe" : nombreF,
                "apellidoBebe": apellidoF,
                "sexoBebe": sexo,
                "ubicacionParto" : ubicacion,
                "prefectura" : prefectura,
                "nombrePadre" : nombrePadreF,
                "cedulaPadre" : CPadre,
                "nombreMadre" : nombreMadreF,
                "cedulaMadre" : CMadre,
                }
        
        print(ActaNacimientoDic)
    

