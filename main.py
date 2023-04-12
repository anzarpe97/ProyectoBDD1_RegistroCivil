import funciones

import tkinter as tk 
from tkinter import ttk
from tkinter import *

root = tk.Tk()

# MOSTRAR DATOS ACTA NACIMIENTO

def MostrarDatosAC (frameInicio):

    Vscrollbar = ttk.Scrollbar (orient = tk.HORIZONTAL)

    DatosActa = ttk.Treeview (frameInicio, columns = ("#1", "#2", "#3", "#4", "#5", "#6", "#7", "#8", "#9", "#10", "#11", "#12", "#13", "#14", "#15", "#16", "#17", "#18", "#19"), yscrollcommand = Vscrollbar.set)
    Vscrollbar.config (command = DatosActa.xview)
    Vscrollbar.place(x = 163, y = 637, width = 1000) 

    DatosActa.column ("#0", width = 120)
    DatosActa.column ("#1", width = 120)
    DatosActa.column ("#2", width = 120)
    DatosActa.column ("#3", width = 120)
    DatosActa.column ("#4", width = 120)
    DatosActa.column ("#5", width = 120)
    DatosActa.column ("#6", width = 120)
    DatosActa.column ("#7", width = 120)
    DatosActa.column ("#8", width = 120)
    DatosActa.column ("#9", width = 120)
    DatosActa.column ("#10", width = 120)
    DatosActa.column ("#11", width = 120)
    DatosActa.column ("#12", width = 120)
    DatosActa.column ("#13", width = 250)
    DatosActa.column ("#14", width = 120)
    DatosActa.column ("#15", width = 120)
    DatosActa.column ("#16", width = 120)
    DatosActa.column ("#17", width = 450)
    DatosActa.column ("#18", width = 120)
    DatosActa.column ("#19", width = 120)

    DatosActa.heading ("#0", text = "Num Acta", anchor = "center")
    DatosActa.heading ("#1", text = "Nombre Bebe", anchor = "center")
    DatosActa.heading ("#2", text ="Apellido Bebe", anchor = "center")
    DatosActa.heading ("#3", text = "Fecha Nacimiento", anchor = "center")
    DatosActa.heading ("#4", text = "Hora Nacimiento", anchor = "center")
    DatosActa.heading ("#5", text = "Lugar Nacimiento", anchor = "center")
    DatosActa.heading ("#6", text = "Sexo Bebe", anchor = "center")
    DatosActa.heading ("#7", text = "Cedula Padre", anchor = "center")
    DatosActa.heading ("#8", text = "Nombre Padre", anchor = "center")
    DatosActa.heading ("#9", text = "Apellido Padre", anchor = "center")
    DatosActa.heading ("#10", text = "Cedula Madre", anchor = "center")
    DatosActa.heading ("#11", text = "Nombre Madre", anchor = "center")
    DatosActa.heading ("#12", text = "Apellido Madre", anchor = "center")
    DatosActa.heading ("#13", text = "Registro Civil", anchor = "center")
    DatosActa.heading ("#14", text = "Estado", anchor = "center")
    DatosActa.heading ("#15", text = "Ciudad", anchor = "center")
    DatosActa.heading ("#16", text = "Parroquia", anchor = "center")
    DatosActa.heading ("#17", text = "Direccion Registo Civil", anchor = "center")
    DatosActa.heading ("#18", text = "Nombre Director", anchor = "center")
    DatosActa.heading ("#19", text = "Apellido Director", anchor = "center")

    DAN = funciones.consultarActaNacimiento()

    for x in DAN:
        
        DatosActa.insert("", END, text = x[0], values = (x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8], x[9], x[10], x[11], x[12], x[13], x[14], x[15], x[16], x[17], x[18], x[19]))
        
    DatosActa.place(x = 20, y = 350, width = 1000, height = 280)

#MOSTRAR DATOS CEDULA

def MostrarDatosC (frameInicio): 

    Vscrollbar = ttk.Scrollbar (orient = tk.HORIZONTAL)

    DatoCedula = ttk.Treeview (frameInicio, columns = ("#1","#2","#3","#4","#5","#6","#7","#8"), yscrollcommand = Vscrollbar.set)
    Vscrollbar.config (command = DatoCedula.xview)
    Vscrollbar.place (x = 163, y = 637, width = 1000) 

    DatoCedula.column("#0", width = 120)
    DatoCedula.column("#1", width = 120)
    DatoCedula.column("#2", width = 120)
    DatoCedula.column("#3", width = 120)
    DatoCedula.column("#4", width = 120)
    DatoCedula.column("#5", width = 120)
    DatoCedula.column("#6", width = 120)
    DatoCedula.column("#7", width = 120)
    DatoCedula.column("#8", width = 120)

    DatoCedula.heading("#0", text = "Cedula", anchor = "center")
    DatoCedula.heading("#1", text = "Nombres", anchor = "center")
    DatoCedula.heading("#2", text = "Apellidos", anchor = "center")
    DatoCedula.heading("#3", text = "Estado Civil", anchor = "center")
    DatoCedula.heading("#4", text = "Genero", anchor = "center")
    DatoCedula.heading("#5", text = "Fecha Nacimiento", anchor = "center")
    DatoCedula.heading("#6", text = "Fecha Emision", anchor = "center")
    DatoCedula.heading("#7", text = "Fecha Vencimiento", anchor = "center")
    DatoCedula.heading("#8", text = "Nacionalidad", anchor = "center")

    Cedula = funciones.consultarCedulas()

    for x in Cedula:

        DatoCedula.insert("", END, text = x[0], values = (x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8]))

    DatoCedula.place(x = 20, y = 260, width = 1000, height = 370)

# MOSTRAR DATOS ACTA DE MATRIMONIO

def MostrarDatosAM (frameInicio):
    
    Vscrollbar = ttk.Scrollbar (orient = tk.HORIZONTAL)

    DatoActaMatrimonio = ttk.Treeview (frameInicio, columns = ("#1","#2","#3","#4","#5","#6","#7","#8","#9","#10","#11","#12","#13","#14","#15","#16","#17","#18","#19","#20","#21","#22","#23","#24","#25","#26","#27"), yscrollcommand = Vscrollbar.set)
    Vscrollbar.config (command = DatoActaMatrimonio.xview)
    Vscrollbar.place (x = 163, y = 637, width = 1000) 

    DatoActaMatrimonio.column("#0", width = 200)
    DatoActaMatrimonio.column("#1", width = 120)
    DatoActaMatrimonio.column("#2", width = 120)
    DatoActaMatrimonio.column("#3", width = 120)
    DatoActaMatrimonio.column("#4", width = 120)
    DatoActaMatrimonio.column("#5", width = 120)
    DatoActaMatrimonio.column("#6", width = 120)
    DatoActaMatrimonio.column("#7", width = 120)
    DatoActaMatrimonio.column("#8", width = 120)
    DatoActaMatrimonio.column("#9", width = 120)
    DatoActaMatrimonio.column("#10", width = 120)
    DatoActaMatrimonio.column("#11", width = 120)
    DatoActaMatrimonio.column("#12", width = 120)
    DatoActaMatrimonio.column("#13", width = 120)
    DatoActaMatrimonio.column("#14", width = 120)
    DatoActaMatrimonio.column("#15", width = 120)
    DatoActaMatrimonio.column("#16", width = 120)
    DatoActaMatrimonio.column("#17", width = 120)
    DatoActaMatrimonio.column("#18", width = 120)
    DatoActaMatrimonio.column("#19", width = 120)
    DatoActaMatrimonio.column("#20", width = 120)
    DatoActaMatrimonio.column("#21", width = 120)
    DatoActaMatrimonio.column("#22", width = 120)
    DatoActaMatrimonio.column("#23", width = 120)
    DatoActaMatrimonio.column("#24", width = 120)
    DatoActaMatrimonio.column("#25", width = 500)
    DatoActaMatrimonio.column("#26", width = 120)
    DatoActaMatrimonio.column("#27", width = 120)

    # DATOS ACTA 

    DatoActaMatrimonio.heading("#0", text = "Numero Acta Matrimonio", anchor = "center")
    DatoActaMatrimonio.heading("#1", text = "Fecha Matrimonio", anchor = "center")

    # DATOS PRIMER CONTRAYENTE

    DatoActaMatrimonio.heading("#2", text = "Cedula P Contrayente", anchor = "center")
    DatoActaMatrimonio.heading("#3", text = "Nombres P Contrayente", anchor = "center")
    DatoActaMatrimonio.heading("#4", text = "Apellidos P Contrayente", anchor = "center")
    DatoActaMatrimonio.heading("#5", text = "Ocupacion P Contrayente", anchor = "center")
    DatoActaMatrimonio.heading("#6", text = "Direccion P Contrayente", anchor = "center")

    # DATOS SEGUNDO CONTRAYENTE

    DatoActaMatrimonio.heading("#7", text = "Cedula S Contrayente", anchor = "center")
    DatoActaMatrimonio.heading("#8", text = "Nombres S Contrayente", anchor = "center")
    DatoActaMatrimonio.heading("#9", text = "Apellidos S Contrayente", anchor = "center")
    DatoActaMatrimonio.heading("#10", text = "Ocupacion S Contrayente", anchor = "center")
    DatoActaMatrimonio.heading("#11", text = "Direccion S Contrayente", anchor = "center")

    # DATOS REGISTRADOR CIVIL

    DatoActaMatrimonio.heading("#12", text = "Cedula Registrador Civil", anchor = "center")
    DatoActaMatrimonio.heading("#13", text = "Nombres Registrador Civil", anchor = "center")
    DatoActaMatrimonio.heading("#14", text = "Apellidos Registrador Civil", anchor = "center")

    # DATOS PRIMER TESTIGO

    DatoActaMatrimonio.heading("#15", text = "Cedula P Testigo", anchor = "center")
    DatoActaMatrimonio.heading("#16", text = "Nombres P Testigo", anchor = "center")
    DatoActaMatrimonio.heading("#17", text = "Apellidos P Testigos", anchor = "center")

    # DATOS SEGUNGO TESTIGO

    DatoActaMatrimonio.heading("#18", text = "Cedula S Testigo", anchor = "center")
    DatoActaMatrimonio.heading("#19", text = "Nombres S Testigo", anchor = "center")
    DatoActaMatrimonio.heading("#20", text = "Apellidos S Testigo", anchor = "center")

    #DATOS REGISTROS

    DatoActaMatrimonio.heading("#21", text = "Nombre Registro", anchor = "center")
    DatoActaMatrimonio.heading("#22", text = "Estado", anchor = "center")
    DatoActaMatrimonio.heading("#23", text = "Municipio", anchor = "center")
    DatoActaMatrimonio.heading("#24", text = "Parroquia", anchor = "center")
    DatoActaMatrimonio.heading("#25", text = "Direccion ", anchor = "center")
    DatoActaMatrimonio.heading("#26", text = "Nombre Director", anchor = "center")
    DatoActaMatrimonio.heading("#27", text = "Apellidos Director", anchor = "center")

    ActaMatrimonio = funciones.consultarActaMatrimonio()

    for x in ActaMatrimonio:

        DatoActaMatrimonio.insert("", END, text = x[0], values = (x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8], x[9], x[10], x[11], x[12], x[13], x[14], x[15], x[16], x[17], x[18], x[19], x[20], x[21], x[22], x[23], x[24], x[25],x[26],x[27]))

    DatoActaMatrimonio.place(x = 20, y = 295, width = 1000, height = 339)

# MOSTRAR DATOS ACTA DE DIVORCIO

def MostrarDatosADi (frameInicio):

    Vscrollbar = ttk.Scrollbar (orient = tk.HORIZONTAL)

    DatoActaDivorcio = ttk.Treeview (frameInicio, columns = ("#1","#2","#3","#4","#5","#6","#7","#8","#9","#10","#11","#12","#13","#14","#15","#16","#17","#18","#19","#20","#21","#22","#23","#24","#25","#26","#27","#28","#29"), yscrollcommand = Vscrollbar.set)
    Vscrollbar.config (command = DatoActaDivorcio.xview)
    Vscrollbar.place (x = 163, y = 637, width = 1000) 

    DatoActaDivorcio.column("#0", width = 200)
    DatoActaDivorcio.column("#1", width = 120)
    DatoActaDivorcio.column("#2", width = 120)
    DatoActaDivorcio.column("#3", width = 120)
    DatoActaDivorcio.column("#4", width = 120)
    DatoActaDivorcio.column("#5", width = 120)
    DatoActaDivorcio.column("#6", width = 120)
    DatoActaDivorcio.column("#7", width = 120)
    DatoActaDivorcio.column("#8", width = 120)
    DatoActaDivorcio.column("#9", width = 120)
    DatoActaDivorcio.column("#10", width = 120)
    DatoActaDivorcio.column("#11", width = 120)
    DatoActaDivorcio.column("#12", width = 120)
    DatoActaDivorcio.column("#13", width = 120)
    DatoActaDivorcio.column("#14", width = 120)
    DatoActaDivorcio.column("#15", width = 120)
    DatoActaDivorcio.column("#16", width = 120)
    DatoActaDivorcio.column("#17", width = 120)
    DatoActaDivorcio.column("#18", width = 120)
    DatoActaDivorcio.column("#19", width = 120)
    DatoActaDivorcio.column("#20", width = 120)
    DatoActaDivorcio.column("#21", width = 120)
    DatoActaDivorcio.column("#22", width = 120)
    DatoActaDivorcio.column("#23", width = 120)
    DatoActaDivorcio.column("#24", width = 120)
    DatoActaDivorcio.column("#25", width = 120)
    DatoActaDivorcio.column("#26", width = 120)
    DatoActaDivorcio.column("#27", width = 120)
    DatoActaDivorcio.column("#28", width = 120)
    DatoActaDivorcio.column("#29", width = 120)

    # DATOS ACTA 

    DatoActaDivorcio.heading("#0", text = "Numero Acta Divorcio", anchor = "center")

    # DATOS PRIMER ESPOSO

    DatoActaDivorcio.heading("#1", text = "Cedula Primer Esposx", anchor = "center")
    DatoActaDivorcio.heading("#2", text = "Nombres Primer Esposx", anchor = "center")
    DatoActaDivorcio.heading("#3", text = "Apellidos Primer Esposx", anchor = "center")
    DatoActaDivorcio.heading("#4", text = "Direccion Primer Esposo", anchor = "center")

    # DATOS SEGUNDO ESPOSO

    DatoActaDivorcio.heading("#5", text = "Cedula Segundo Esposx", anchor = "center")
    DatoActaDivorcio.heading("#6", text = "Nombres Segundo Esposx", anchor = "center")
    DatoActaDivorcio.heading("#7", text = "Apellidos Segundo Esposx", anchor = "center")
    DatoActaDivorcio.heading("#8", text = "Direccion Segundo Esposx", anchor = "center")

    # DATOS ABOGADO PRIMER ESPOSO

    DatoActaDivorcio.heading("#9", text = "Cedula Abogado P Esposx", anchor = "center")
    DatoActaDivorcio.heading("#10", text = "Nombres Abodado P Esposx", anchor = "center")
    DatoActaDivorcio.heading("#11", text = "Apellidos Abogado P Esposo", anchor = "center")

    # DATOS ABOGADO SEGUNDO ESPOSO

    DatoActaDivorcio.heading("#12", text = "Cedula Abogado S Esposx", anchor = "center")
    DatoActaDivorcio.heading("#13", text = "Nombres Abodado S Esposx", anchor = "center")
    DatoActaDivorcio.heading("#14", text = "Apellidos Abogado S Esposo", anchor = "center")

    # DATOS PRIMER TESTIGO

    DatoActaDivorcio.heading("#15", text = "Acta Nacimiento Primer Hijo", anchor = "center")
    DatoActaDivorcio.heading("#16", text = "Nombres Primer Hijo", anchor = "center")
    DatoActaDivorcio.heading("#17", text = "Apellidos Primer Hijo", anchor = "center")

    # DATOS SEGUNGO TESTIGO

    DatoActaDivorcio.heading("#18", text = "Acta Nacimiento Segundo Hijo", anchor = "center")
    DatoActaDivorcio.heading("#19", text = "Nombres Segundo Hijo", anchor = "center")
    DatoActaDivorcio.heading("#20", text = "Apellidos Segundo Hijo", anchor = "center")

    #DATOS REGISTROS

    DatoActaDivorcio.heading("#21", text = "Nombre Registro", anchor = "center")
    DatoActaDivorcio.heading("#22", text = "Estado", anchor = "center")
    DatoActaDivorcio.heading("#23", text = "Municipio", anchor = "center")
    DatoActaDivorcio.heading("#24", text = "Parroquia", anchor = "center")
    DatoActaDivorcio.heading("#25", text = "Direccion ", anchor = "center")
    DatoActaDivorcio.heading("#26", text = "Nombre Director", anchor = "center")
    DatoActaDivorcio.heading("#27", text = "Apellidos Director", anchor = "center")

    ActaDivorcio = funciones.consultarActaDivorcio()

    for x in ActaDivorcio:

        DatoActaDivorcio.insert("", END, text = x[0], values = (x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8], x[9], x[10], x[11], x[12], x[13], x[14], x[15], x[16], x[17], x[18], x[19], x[20], x[21], x[22], x[23], x[24], x[25],x[26],x[27],x[28]))

    DatoActaDivorcio.place(x = 20, y = 295, width = 1000, height = 335)

# MOSTRAR DATOS ACTA DEFUNNCION

def MostrarDatosAD (frameInicio):

    Vscrollbar = ttk.Scrollbar (orient = tk.HORIZONTAL)

    DatoActaDefuncion = ttk.Treeview (frameInicio, columns = ("#1","#2","#3","#4","#5","#6","#7","#8","#9","#10","#11","#12","#13","#14","#15","#16","#17"), yscrollcommand = Vscrollbar.set)
    Vscrollbar.config (command = DatoActaDefuncion.xview)
    Vscrollbar.place (x = 163, y = 637, width = 1000) 

    DatoActaDefuncion.column("#0", width = 120)
    DatoActaDefuncion.column("#1", width = 120)
    DatoActaDefuncion.column("#2", width = 120)
    DatoActaDefuncion.column("#3", width = 120)
    DatoActaDefuncion.column("#4", width = 120)
    DatoActaDefuncion.column("#5", width = 120)
    DatoActaDefuncion.column("#6", width = 120)
    DatoActaDefuncion.column("#7", width = 120)
    DatoActaDefuncion.column("#8", width = 120)
    DatoActaDefuncion.column("#9", width = 120)
    DatoActaDefuncion.column("#10", width = 120)
    DatoActaDefuncion.column("#11", width = 120)
    DatoActaDefuncion.column("#12", width = 120)
    DatoActaDefuncion.column("#13", width = 120)
    DatoActaDefuncion.column("#14", width = 120)
    DatoActaDefuncion.column("#15", width = 120)
    DatoActaDefuncion.column("#16", width = 120)
    DatoActaDefuncion.column("#17", width = 120)

    DatoActaDefuncion.heading("#0", text = "Numero Acta", anchor = "center")
    DatoActaDefuncion.heading("#1", text = "Nombres", anchor = "center")
    DatoActaDefuncion.heading("#2", text = "Apellidos", anchor = "center")
    DatoActaDefuncion.heading("#3", text = "Edad", anchor = "center")
    DatoActaDefuncion.heading("#4", text = "Genero", anchor = "center")
    DatoActaDefuncion.heading("#5", text = "Estado Civil", anchor = "center")
    DatoActaDefuncion.heading("#6", text = "Fecha Defuncion", anchor = "center")
    DatoActaDefuncion.heading("#7", text = "Hora Defuncion", anchor = "center")
    DatoActaDefuncion.heading("#8", text = "Lugar Defuncion", anchor = "center")
    DatoActaDefuncion.heading("#9", text = "Causa Defuncion", anchor = "center")
    DatoActaDefuncion.heading("#10", text = "Cedula Informante", anchor = "center")
    DatoActaDefuncion.heading("#11", text = "Relacion Informante", anchor = "center")
    DatoActaDefuncion.heading("#12", text = "Nombres Informante", anchor = "center")
    DatoActaDefuncion.heading("#13", text = "Apellidos Informante", anchor = "center")
    DatoActaDefuncion.heading("#14", text = "Nombres Madre", anchor = "center")
    DatoActaDefuncion.heading("#15", text = "Apellidos Madre", anchor = "center")
    DatoActaDefuncion.heading("#16", text = "Nombres Padre", anchor = "center")
    DatoActaDefuncion.heading("#17", text = "Apellidos Padre", anchor = "center")

    ActaDefuncionD = funciones.consultarActaDeuncion()

    for x in ActaDefuncionD:

        DatoActaDefuncion.insert("", END, text = x[0], values = (x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8], x[9], x[10], x[11], x[12], x[13], x[14], x[15], x[16], x[17]))

    DatoActaDefuncion.place(x = 20, y = 280, width = 1000, height = 350)

# FRAMES

def actaNacimiento ():

    def reiniciarCampos():

        nombres.set("")
        apellidos.set("")
        sexoBebe.set("")
        cedulaPadre.set(0)
        nombrePadre.set("")
        apellidoPadre.set("")
        cedulaMadre.set(0)
        nombreMadre.set("")
        apellidoMadre.set("")
        fechaNacimiento.set("")
        horaNacimiento.set("")
        ubicacion.set("")
        prefectura.set("")
        numeroActa.set(0)

    # VARIABLES

    nombres = StringVar ()
    apellidos = StringVar ()
    sexoBebe = StringVar ()
    cedulaPadre = IntVar ()
    nombrePadre = StringVar ()
    apellidoPadre = StringVar ()
    cedulaMadre = IntVar ()
    nombreMadre = StringVar ()
    apellidoMadre = StringVar ()
    fechaNacimiento = StringVar ()
    horaNacimiento = StringVar ()
    ubicacion = StringVar ()
    prefectura =StringVar ()
    numeroActa = IntVar ()

    # NO TOCAR
    
    frameInicio = tk.Frame (root, background = "#209cb4", height = 656, width = 1057)
    frameInicio.place (x = 143, y = 5)
    
    inicioLabel = tk.Label(frameInicio, text = "Formulario Acta De Nacimiento")
    inicioLabel.configure(font = ("roboto", 14, "bold"), fg = "#209cb4", background = "WHITE")
    inicioLabel.place (x = 420, y = 10)

    # NOMBRES BEBE

    nombresLabel = tk.Label (frameInicio, text = "Nombres: ")
    nombresLabel.configure (font = ("roboto", 12, "bold"), fg = "WHITE", background = "#209cb4")
    nombresLabel.place (x = 60, y = 90)

    nombresEntry = tk.Entry (frameInicio, relief = "flat",textvariable = nombres)
    nombresEntry.place (x = 142, y = 93)
    
    # APELLIDO BEBE

    apellidosLabel = tk.Label (frameInicio, text = "Apellidos: ")
    apellidosLabel.configure (font = ("roboto", 12, "bold"), fg = "WHITE", background = "#209cb4")
    apellidosLabel.place (x = 60, y = 130)

    apellidosEntry= tk.Entry (frameInicio, relief = "flat", textvariable = apellidos)
    apellidosEntry.place (x = 142, y = 133)

    # SEXO BEBE

    sexoBebeLabel = tk.Label (frameInicio, text = "Sexo: ")
    sexoBebeLabel.configure (font = ("roboto", 12, "bold"), fg = "WHITE", background = "#209cb4")
    sexoBebeLabel.place (x = 92, y = 170)#x = 100, y = 210
    
    sexoBebeOpcion = ttk.Combobox (frameInicio,values = ["Masculino", "Femenino"], width = 17, textvariable = sexoBebe)
    sexoBebeOpcion.place (x = 141,y = 173)
 
    # CEDULA PADRE

    cedulaPadreLabel = tk.Label (frameInicio, text = "Cedula Padre: ")
    cedulaPadreLabel.configure (font = ("roboto", 12, "bold"), fg = "WHITE", background = "#209cb4")
    cedulaPadreLabel.place (x = 380, y = 90)

    cedulaPadreEntry = tk.Entry (frameInicio, relief="flat", textvariable = cedulaPadre)
    cedulaPadreEntry.place (x = 500, y = 93)

    # NOMBRE PADRE

    nombrePadreLabel = tk.Label (frameInicio, text = "Nombres Padre: ")
    nombrePadreLabel.configure (font = ("roboto", 12, "bold"), fg = "WHITE", background = "#209cb4")
    nombrePadreLabel.place (x = 368, y = 130)

    nombrePadreEntry = tk.Entry(frameInicio, relief = "flat", textvariable = nombrePadre)
    nombrePadreEntry.place (x = 500, y = 133)

    # APELLIDO PADRE

    apellidoPadreLabel = tk.Label (frameInicio, text = "Apellidos Padre: ")
    apellidoPadreLabel.configure (font = ("roboto", 12, "bold"), fg = "WHITE", background = "#209cb4")
    apellidoPadreLabel.place (x = 368, y = 170)

    apellidoPadreEntry = tk.Entry (frameInicio, relief = "flat", textvariable = apellidoPadre)
    apellidoPadreEntry.place (x = 500, y = 173)

    # CEDULA MADRE

    cedulaMadreLabel = tk.Label (frameInicio, text = "Cedula Madre: ")
    cedulaMadreLabel.configure (font = ("roboto", 12, "bold"), fg = "WHITE", background = "#209cb4")
    cedulaMadreLabel.place (x = 700, y = 90)

    cedulaMadreEntry = tk.Entry (frameInicio, relief = "flat",textvariable = cedulaMadre)
    cedulaMadreEntry.place (x = 820, y = 93)

    # NOMBRE MADRE

    nombreMadreLabel = tk.Label (frameInicio, text = "Nombres Madre: ")
    nombreMadreLabel.configure (font = ("roboto", 12, "bold"), fg = "WHITE", background = "#209cb4")
    nombreMadreLabel.place (x = 685, y = 130)

    nombreMadreEntry = tk.Entry (frameInicio, relief = "flat", textvariable = nombreMadre)
    nombreMadreEntry.place (x = 820, y = 133)

    # APELLIDO MADRE

    apellidoMadreLabel = tk.Label (frameInicio, text = "Apellidos Madre: ")
    apellidoMadreLabel.configure (font = ("roboto", 12, "bold"), fg = "WHITE", background = "#209cb4")
    apellidoMadreLabel.place (x = 685, y = 170)

    apellidoMadreEntry = tk.Entry (frameInicio, relief = "flat", textvariable = apellidoMadre)
    apellidoMadreEntry.place (x = 820, y = 173)

    # FECHA DE NACIMIENTO

    FechaNacimientoLabel = tk.Label (frameInicio, text = "Fecha Nacimiento: ")
    FechaNacimientoLabel.configure (font = ("roboto", 11, "bold"), fg = "WHITE", background = "#209cb4")
    FechaNacimientoLabel.place (x = 7, y = 210)

    FechaNacimientoEntry = tk.Entry(frameInicio, relief = "flat",textvariable = fechaNacimiento)
    FechaNacimientoEntry.place (x = 142, y = 213)

    FormatoHNLabel = tk.Label(frameInicio, text = "Formato (dd-mm-aaaa) ")
    FormatoHNLabel.configure(font = ("roboto", 8, "bold"), fg ="WHITE", background="#209cb4")
    FormatoHNLabel.place (x = 140, y = 233)

    # HORA DE NACIMIENTO

    horaNacimientoLabel = tk.Label (frameInicio, text = "Hora Nacimiento: ")
    horaNacimientoLabel.configure(font = ("roboto", 12, "bold"), fg = "WHITE", background = "#209cb4")
    horaNacimientoLabel.place (x = 362, y = 210)

    horaNacimientoEntry = tk.Entry(frameInicio, relief="flat",textvariable=horaNacimiento)
    horaNacimientoEntry.place (x = 500, y = 213)

    FormatoHNLabel = tk.Label(frameInicio, text = "Formato (hh:mm:ss) ")
    FormatoHNLabel.configure(font = ("roboto", 8, "bold"), fg ="WHITE", background="#209cb4")
    FormatoHNLabel.place (x = 504, y = 233)

    #  UBICACION 

    ubicacionLabel = tk.Label (frameInicio, text = "Lugar Nacimiento: ")
    ubicacionLabel.configure (font = ("roboto", 12, "bold"), fg = "WHITE", background = "#209cb4")
    ubicacionLabel.place (x = 675, y = 210)

    ubicacionEntry = tk.Entry (frameInicio, relief="flat",textvariable=ubicacion)
    ubicacionEntry.place (x = 820, y = 213)

    # PREFECTURAS 
    
    prefecturaLabel = tk.Label (frameInicio, text = "Registro Civil: ")
    prefecturaLabel.configure (font = ("roboto", 12, "bold"), fg = "WHITE", background = "#209cb4")
    prefecturaLabel.place (x = 25, y = 260)#x = 100, y = 240
    
    prefecturaOpcion = ttk.Combobox (frameInicio,values = ["Coquivacoa", "Chiquinquira", "Cacique Mara", "Olegarios Villalobos"], textvariable= prefectura,width = 17)
    prefecturaOpcion.place (x = 141,y = 263)#x = 275, y = 213

    numActaLabel = tk.Label (frameInicio, text = "Num Acta Nacimiento: ")
    numActaLabel.configure (font = ("roboto", 10, "bold"), fg = "WHITE", background = "#209cb4")
    numActaLabel.place (x = 675, y = 260)

    numActaEntry = tk.Entry (frameInicio, relief="flat",textvariable = numeroActa)
    numActaEntry.place (x = 820, y = 263)

    ActaLabel = tk.Label (frameInicio, text = "Solo para actualizar ")
    ActaLabel.configure (font = ("roboto", 9, "bold"), fg = "WHITE", background = "#209cb4")
    ActaLabel.place (x = 820, y = 285)

    # BOTON AGREGAR 

    botonAgregar = tk.Button (frameInicio, text = "Guardar", height = 1, width = 9,relief="flat", command = lambda: funciones.guardarDatosAcNacimiento(nombres.get(),apellidos.get(),fechaNacimiento.get(),horaNacimiento.get(), ubicacion.get(), sexoBebe.get(), cedulaPadre.get(), nombrePadre.get(),apellidoPadre.get(),cedulaMadre.get(),nombreMadre.get(),apellidoMadre.get(),prefectura.get()))
    botonAgregar.configure (font = ("roboto", 10, "bold"), fg="WHITE", activebackground="#71acb7", activeforeground="WHITE", background="WHITE",foreground="#209cb4")
    botonAgregar.place (x = 565, y = 315)

    # BOTON ACTUALIZAR 

    botonActualizar = tk.Button (frameInicio, text = "Actualizar Datos", height = 1, width = 14,relief="flat", command = lambda: funciones.actualizarActaNacimiento(nombres.get(),apellidos.get(),fechaNacimiento.get(),horaNacimiento.get(), ubicacion.get(), sexoBebe.get(), cedulaPadre.get(), nombrePadre.get(),apellidoPadre.get(),cedulaMadre.get(),nombreMadre.get(),apellidoMadre.get(),prefectura.get(),numeroActa.get()))
    botonActualizar.configure (font = ("roboto", 10, "bold"), fg="WHITE", activebackground="#71acb7", activeforeground="WHITE", background="WHITE",foreground="#209cb4")
    botonActualizar.place (x = 655, y = 315)

    # BOTON REINICIAR CAMPO

    botonReiniciar = tk.Button (frameInicio, text = "Reiniciar Campos", height = 1, width = 14,relief="flat", command = lambda: reiniciarCampos())
    botonReiniciar.configure (font = ("roboto", 10, "bold"), fg="WHITE", activebackground="#71acb7", activeforeground="WHITE", background="WHITE",foreground="#209cb4")
    botonReiniciar.place (x = 785, y = 315)

    # BOTON MOSTRAR DATOS

    botonMostrar = tk.Button (frameInicio, text = "Mostrar Datos", height = 1, width = 12,relief="flat", command = lambda: MostrarDatosAC(frameInicio))
    botonMostrar.configure (font = ("roboto", 10, "bold"), fg="WHITE", activebackground="#71acb7", activeforeground="WHITE", background="WHITE",foreground="#209cb4")
    botonMostrar.place (x = 915, y = 315)

    # REPORTE DATOS

    botonReporte = tk.Button (frameInicio, text = "Genera Reporte", height = 1, width = 14,relief="flat", command = lambda: funciones.generarReporteActaNacimiento())
    botonReporte.configure (font = ("roboto", 10, "bold"), fg="WHITE", activebackground = "#71acb7", activeforeground="WHITE", background="WHITE",foreground="#209cb4")
    botonReporte.place (x = 20, y = 315)

def cedula ():

    def reiniciarCampos():

        numCedula.set("")
        numActaNacimiento.set("")
        nombres.set("")
        apellidos.set("")
        EstadoCivil.set("")
        genero.set("")
        nacionalidad.set("")
        fechaEmision.set("")

    # Variables

    numCedula = IntVar()
    numActaNacimiento = IntVar()
    nombres = StringVar()
    apellidos = StringVar()
    EstadoCivil = StringVar()
    genero = StringVar()
    nacionalidad = StringVar()
    fechaEmision= StringVar()

    # NO TOCAR

    frameInicio = tk.Frame(root, background = "#209cb4", height = 656, width = 1057)
    frameInicio.place(x = 143, y = 5)
    
    # TITULO 
    
    numCedulaLabel = tk.Label(frameInicio, text = "Formulario Cedula")
    numCedulaLabel.configure(font = ("roboto", 14, "bold"), fg="#209cb4", background="WHITE")
    numCedulaLabel.place (x = 450, y = 10)

    # NUMERO DE ACTA DE NACIMIENTO 

    numActaNacimientoLabel = tk.Label(frameInicio, text = "Numero Acta Nacimiento: ")
    numActaNacimientoLabel.configure(font = ("roboto", 12, "bold"), fg = "WHITE", background = "#209cb4")
    numActaNacimientoLabel.place (x = 18, y = 90)

    numActaNacimientoEntry = tk.Entry(frameInicio, relief = "flat",textvariable=numActaNacimiento)
    numActaNacimientoEntry.place (x = 220, y = 93)
    
    # NUMERO DE CEDULA 
    
    NumCedulaLabel = tk.Label(frameInicio, text = "Numero De Cedula: ")
    NumCedulaLabel.configure(font = ("roboto", 12, "bold"), fg = "WHITE", background = "#209cb4")
    NumCedulaLabel.place (x =390, y = 90)

    NumCedulaEntry = tk.Entry(frameInicio, relief = "flat", textvariable=numCedula)
    NumCedulaEntry.place (x = 545, y = 93)

    # NOMBRE CIUDADANO

    nombreLabel = tk.Label (frameInicio, text = "Nombres: ")
    nombreLabel.configure (font = ("roboto", 12, "bold"), fg = "WHITE", background = "#209cb4")
    nombreLabel.place (x = 140, y = 130)

    nombreEntry = tk.Entry(frameInicio, relief = "flat",textvariable=nombres)
    nombreEntry.place (x = 220, y = 133)

    # APELLIDO CIUDADANO

    apellidoLabel = tk.Label (frameInicio, text = "Apellidos: ")
    apellidoLabel.configure (font = ("roboto", 12, "bold"), fg = "WHITE", background = "#209cb4")
    apellidoLabel.place (x = 460, y = 130)

    apellidoEntry = tk.Entry(frameInicio, relief = "flat",textvariable=apellidos)
    apellidoEntry.place (x = 545, y = 133)

    # FECHA DE EMISION

    FEmisionLabel = tk.Label (frameInicio, text = "Fecha Emision: ")
    FEmisionLabel.configure (font = ("roboto", 12, "bold"), fg = "WHITE", background = "#209cb4")
    FEmisionLabel.place (x = 705, y = 130)

    FEmisionEntry = tk.Entry(frameInicio, relief = "flat",textvariable=fechaEmision)
    FEmisionEntry.place (x = 830, y = 133)

    FormatoELabel = tk.Label(frameInicio, text = "Formato (dd-mm-aaaa) ")
    FormatoELabel.configure(font = ("roboto", 8, "bold"), fg = "WHITE", background = "#209cb4")
    FormatoELabel.place(x = 825, y=113)

    # ESTADO CIVIL
    
    EdoCivilLabel = tk.Label (frameInicio, text = "Estado Civil: ")
    EdoCivilLabel.configure (font = ("roboto", 12, "bold"), fg = "WHITE", background = "#209cb4")
    EdoCivilLabel.place (x = 117, y = 167)#
    
    EdoCivilOpcion = ttk.Combobox (frameInicio,values = ["Soltero/a", "Casado/a", "Divorciado","Viudo/a"],textvariable=EstadoCivil,width=17)
    EdoCivilOpcion.place(x = 220, y = 170)

    #  GENEROS

    generoLabel = tk.Label (frameInicio, text = "Genero: ")
    generoLabel.configure (font = ("roboto", 12, "bold"), fg = "WHITE", background = "#209cb4")
    generoLabel.place (x =478, y = 170)
    
    generoOpcion = ttk.Combobox (frameInicio,values = ["Hombre", "Mujer", "No-Binario"], textvariable=genero, width=17)
    generoOpcion.place(x = 545, y = 173)

    # NACIONALIDAD 

    nacionalidadlLabel = tk.Label (frameInicio, text = "Nacionalidad: ")
    nacionalidadlLabel.configure (font = ("roboto", 12, "bold"), fg = "WHITE", background = "#209cb4")
    nacionalidadlLabel.place (x = 718, y = 170)
    
    nacionalidadOpcion = ttk.Combobox (frameInicio,values = ["Venezolano/a", "Extranjero/a"], textvariable = nacionalidad,width=17)
    nacionalidadOpcion.place(x = 830, y = 173)

    # BOTON AGREGAR CEDULA

    botonAgregarCedula = tk.Button (frameInicio, text = "Guardar", height = 1, width = 9,relief="flat",command = lambda: funciones.guardarCedulaIdentidad(numCedula.get(), numActaNacimiento.get(),nombres.get(),apellidos.get(),EstadoCivil.get(),genero.get(),fechaEmision.get(), nacionalidad.get()))
    botonAgregarCedula.configure (font = ("roboto", 10, "bold"), fg="WHITE", activebackground="#71acb7", activeforeground="WHITE", background="WHITE",foreground="#209cb4")
    botonAgregarCedula.place (x = 565, y = 225)

    # BOTON ACTUALIZAR 

    botonActualizar = tk.Button (frameInicio, text = "Actualizar Datos", height = 1, width = 14,relief="flat", command=lambda: funciones.actualizarCedula(numCedula.get(), numActaNacimiento.get(),nombres.get(),apellidos.get(),EstadoCivil.get(),genero.get(),fechaEmision.get(), nacionalidad.get()))
    botonActualizar.configure (font = ("roboto", 10, "bold"), fg="WHITE", activebackground="#71acb7", activeforeground="WHITE", background="WHITE",foreground="#209cb4")
    botonActualizar.place (x = 655, y = 225)

    # REINICIAR CAMPOS

    botonReiniciar = tk.Button (frameInicio, text = "Reiniciar Campos", height = 1, width = 14,relief="flat", command = lambda: reiniciarCampos())
    botonReiniciar.configure (font = ("roboto", 10, "bold"), fg="WHITE", activebackground="#71acb7", activeforeground="WHITE", background="WHITE",foreground="#209cb4")
    botonReiniciar.place (x = 785, y = 225)

    # BOTON MOSTRAR DATOS

    botonConsultaCedula = tk.Button (frameInicio, text = "Mostrar Datos", height = 1, width = 12,relief="flat",command = lambda: MostrarDatosC(frameInicio))
    botonConsultaCedula.configure (font = ("roboto", 10, "bold"), fg="WHITE", activebackground="#71acb7", activeforeground="WHITE", background="WHITE",foreground="#209cb4")
    botonConsultaCedula.place (x = 915, y = 225)

    # REPORTE DATOS

    botonReporte = tk.Button (frameInicio, text = "Genera Reporte", height = 1, width = 14,relief="flat", command = lambda: funciones.generarReporteCedula())
    botonReporte.configure (font = ("roboto", 10, "bold"), fg="WHITE", activebackground = "#71acb7", activeforeground="WHITE", background="WHITE",foreground="#209cb4")
    botonReporte.place (x = 20, y = 225)

def actaMatrimonio ():

    def reiniciarCampos():
        
        PContrayente.set(0)
        OPContrayente.set("")
        DPContrayente.set("")
        SContrayente.set(0)
        OSContrayente.set("")
        DSContrayente.set("")
        PTestigo.set(0)
        STestigo.set(0)
        registrador.set(0)
        FechaAM.set("")
        prefectura.set("")
        numActaMatrimonio.set(0)

    numActaMatrimonio = IntVar()
    PContrayente = IntVar()
    OPContrayente = StringVar()
    DPContrayente = StringVar()

    SContrayente = IntVar()
    OSContrayente = StringVar()
    DSContrayente = StringVar()

    PTestigo = IntVar()
    STestigo = IntVar()
    registrador = IntVar()

    FechaAM = StringVar()
    prefectura = StringVar()

    # NO TOCAR
    
    frameInicio = tk.Frame(root, background = "#209cb4", height = 656, width = 1057)
    frameInicio.place(x = 143, y = 5)

    MatrimonioLabel = tk.Label(frameInicio, text = "Formulario Acta De Matrimonio")
    MatrimonioLabel.configure(font = ("roboto", 14, "bold"), fg="#209cb4", background="WHITE")
    MatrimonioLabel.place (x = 390, y = 10)

    # ---- Contrayentes ------

    # PRIMER CONTRAYENTE

    # CEDULA

    PContrayenteLabel = tk.Label (frameInicio, text = "Cedula P Contrayente: ")
    PContrayenteLabel.configure(font = ("roboto", 10, "bold"), fg = "WHITE", background="#209cb4")
    PContrayenteLabel.place (x = 50, y = 90)
    
    PContrayenteEntry = tk.Entry(frameInicio, relief="flat",textvariable = PContrayente)
    PContrayenteEntry.place (x =200, y = 93)
    
    # OCUPACION PRIMER CONTRAYENTE
    
    OPContrayenteLabel = tk.Label (frameInicio, text = "Ocupacion P Contrayente: ")
    OPContrayenteLabel.configure(font = ("roboto", 10, "bold"), fg = "WHITE", background = "#209cb4")
    OPContrayenteLabel.place (x = 380, y = 90)

    OPContrayenteEntry = tk.Entry(frameInicio, relief = "flat", textvariable = OPContrayente)
    OPContrayenteEntry.place (x = 555, y = 93)
    
    # DIRECCION PRIMER CONTRAYENTE
    
    DPContrayenteLabel = tk.Label (frameInicio, text = "Direccion P Contrayente: ")
    DPContrayenteLabel.configure (font = ("roboto", 10, "bold"), fg = "WHITE", background = "#209cb4")
    DPContrayenteLabel.place (x = 735, y = 90)

    DPContrayenteEntry = tk.Entry(frameInicio, relief = "flat", textvariable = DPContrayente)
    DPContrayenteEntry.place (x = 900, y = 93)
    
    # SEGUNDO CONTRAYENTE
    
    # CEDULA SEGUNDO CONTRAYENTE

    SContrayenteLabel = tk.Label (frameInicio, text = "Cedula S Contrayente: ")
    SContrayenteLabel.configure(font = ("roboto", 10, "bold"), fg = "WHITE", background = "#209cb4")
    SContrayenteLabel.place (x = 50, y = 130)

    SContrayenteEntry = tk.Entry(frameInicio, relief = "flat", textvariable = SContrayente)
    SContrayenteEntry.place (x = 200, y = 133)

    # OCUPACION SEGUNDO CONTRAYENTE

    OSContrayenteLabel = tk.Label (frameInicio, text = "Ocupacion S Contrayente: ")
    OSContrayenteLabel.configure (font = ("roboto", 10, "bold"), fg = "WHITE", background = "#209cb4")
    OSContrayenteLabel.place (x = 380, y = 130)

    OSContrayenteEntry = tk.Entry(frameInicio, relief = "flat", textvariable = OSContrayente)
    OSContrayenteEntry.place (x = 555, y = 133)
    
    # DIRECCION SEGUNDO CONTRAYENTE 
    
    DSContrayenteLabel = tk.Label (frameInicio, text = "Direccion S Contrayente: ")
    DSContrayenteLabel.configure (font = ("roboto", 10, "bold"), fg = "WHITE", background = "#209cb4")
    DSContrayenteLabel.place (x = 735, y = 130)

    DSContrayenteEntry = tk.Entry(frameInicio, relief = "flat", textvariable = DSContrayente)
    DSContrayenteEntry.place (x = 900, y = 133)

    # TESTIGO 1
    
    PTestigoLabel = tk.Label (frameInicio, text = "Cedula P Testigo: ")
    PTestigoLabel.configure (font = ("roboto", 10, "bold"), fg = "WHITE", background = "#209cb4")
    PTestigoLabel.place (x = 82, y = 170)

    PTestigoEntry = tk.Entry(frameInicio, relief = "flat",textvariable = PTestigo)
    PTestigoEntry.place (x = 200, y = 173)
    
    # TESTIGO 2
    
    STestigoLabel = tk.Label (frameInicio, text = "Cedula S Testigo: ")
    STestigoLabel.configure (font = ("roboto", 10, "bold"), fg = "WHITE", background = "#209cb4")
    STestigoLabel.place (x = 435, y = 170)#x = 425, y = 170

    STestigoEntry = tk.Entry(frameInicio, relief = "flat",textvariable= STestigo)
    STestigoEntry.place (x = 555, y = 173)#x = 555, y = 173
    
    # REGISTRADOR
    
    registradorLabel = tk.Label (frameInicio, text = "Cedula Registrador: ")
    registradorLabel.configure (font = ("roboto", 10, "bold"), fg = "WHITE", background="#209cb4")
    registradorLabel.place (x = 768, y = 170)
    
    registradorEntry = tk.Entry(frameInicio, relief = "flat",textvariable= registrador)
    registradorEntry.place (x = 900, y = 173)
    
    # FECHA DEL CASAMIENTO
    
    FechaAMLabel = tk.Label (frameInicio, text = "Fecha Casamiento: ")
    FechaAMLabel.configure(font = ("roboto", 10, "bold"), fg = "WHITE", background = "#209cb4")
    FechaAMLabel.place (x = 72, y = 210)

    FechaAMEntry = tk.Entry(frameInicio, relief = "flat",textvariable = FechaAM)
    FechaAMEntry.place (x = 200, y = 213)

    FormatoFLabel = tk.Label(frameInicio, text = "Formato (aa-mm-dd) ")
    FormatoFLabel.configure(font = ("roboto", 8, "bold"), fg = "WHITE", background = "#209cb4")
    FormatoFLabel.place(x = 200, y = 233)
    
    # PREFECTURAS 
    
    prefecturasLabel = tk.Label (frameInicio, text = "Registro Civil: ")
    prefecturasLabel.configure (font = ("roboto", 10, "bold"), fg = "WHITE", background = "#209cb4")
    prefecturasLabel.place (x = 460, y = 210)
    
    prefecturasOpcion = ttk.Combobox (frameInicio,values = ["Coquivacoa", "Chiquinquira", "Cacique Mara", "Olegarios Villalobos"], width=17,textvariable=prefectura)
    prefecturasOpcion.place (x = 555,y = 210)                                                                                                                                                                                                              

    numActaLabel = tk.Label (frameInicio, text = "Num Acta Nacimiento: ")
    numActaLabel.configure (font = ("roboto", 10, "bold"), fg = "WHITE", background = "#209cb4")
    numActaLabel.place (x = 753, y = 210)

    numActaEntry = tk.Entry (frameInicio, relief="flat",textvariable = numActaMatrimonio)
    numActaEntry.place (x = 900, y = 210)

    ActaLabel = tk.Label (frameInicio, text = "Solo para actualizar ")
    ActaLabel.configure (font = ("roboto", 9, "bold"), fg = "WHITE", background = "#209cb4")
    ActaLabel.place (x = 903, y = 233)

    # BOTON AGREGAR DATOS

    botonAgregarActaMatrimonio = tk.Button (frameInicio, text = "Guardar", height = 1, width = 9,relief="flat", command = lambda: funciones.guardarActaMatrimonio(FechaAM.get(), PContrayente.get(), OPContrayente.get(), DPContrayente.get(),SContrayente.get(),OSContrayente.get(),DSContrayente.get(),registrador.get(),PTestigo.get(),STestigo.get(),prefectura.get()))
    botonAgregarActaMatrimonio.configure (font = ("roboto", 10, "bold"), fg = "WHITE", activebackground = "#71acb7", activeforeground="WHITE", background="WHITE",foreground="#209cb4")
    botonAgregarActaMatrimonio.place (x =565, y = 260)

    # BOTON ACTUALIZAR 

    botonActualizar = tk.Button (frameInicio, text = "Actualizar Datos", height = 1, width = 14,relief="flat", command = lambda: funciones.actualizarActaMatrimonio(FechaAM.get(), PContrayente.get(), OPContrayente.get(), DPContrayente.get(),SContrayente.get(),OSContrayente.get(),DSContrayente.get(),registrador.get(),PTestigo.get(),STestigo.get(),prefectura.get(),numActaMatrimonio.get()))
    botonActualizar.configure (font = ("roboto", 10, "bold"), fg="WHITE", activebackground="#71acb7", activeforeground="WHITE", background="WHITE",foreground="#209cb4")
    botonActualizar.place (x = 655, y = 260)

    # REINICIAR CAMPOS

    botonReiniciar = tk.Button (frameInicio, text = "Reiniciar Campos", height = 1, width = 14,relief="flat", command = lambda: reiniciarCampos())
    botonReiniciar.configure (font = ("roboto", 10, "bold"), fg="WHITE", activebackground="#71acb7", activeforeground="WHITE", background="WHITE",foreground="#209cb4")
    botonReiniciar.place (x = 785, y = 260)

    # BOTON MOSTRAR DATOS

    botonMostrarAD = tk.Button (frameInicio, text = "Mostrar Datos", height = 1, width = 12,relief="flat", command = lambda: MostrarDatosAM(frameInicio))
    botonMostrarAD.configure (font = ("roboto", 10, "bold"), fg = "WHITE", activebackground = "#71acb7", activeforeground="WHITE", background="WHITE",foreground="#209cb4")
    botonMostrarAD.place (x = 915, y = 260)

    # REPORTE DATOS

    botonReporte = tk.Button (frameInicio, text = "Genera Reporte", height = 1, width = 14,relief="flat", command = lambda: funciones.generarReporteActaMatrimonio())
    botonReporte.configure (font = ("roboto", 10, "bold"), fg="WHITE", activebackground = "#71acb7", activeforeground="WHITE", background="WHITE",foreground="#209cb4")
    botonReporte.place (x = 20, y = 260)
    
def actaDivorcio ():
    
    def reiniciarCampos():

        NumActaMatrimonio.set(0)
        CedulaPrimerEsposo.set(0)
        DireccionPrimerEsposo.set("")
        CedulaSegundoEsposo.set(0)
        DireccionSegundoEsposo.set("")
        CedulaAbogadoPE.set(0)
        CedulaAbogadoSE.set(0)
        ActaNacimientoPHijo.set(0)
        ActaNacimientoSHijo.set(0)
        Prefectura.set("")
        numActaDivorcio.set()

    NumActaMatrimonio = IntVar ()
    CedulaPrimerEsposo = IntVar ()
    DireccionPrimerEsposo = StringVar()

    CedulaSegundoEsposo = IntVar()
    DireccionSegundoEsposo =StringVar()

    CedulaAbogadoPE = IntVar()
    CedulaAbogadoSE = IntVar()
    numActaDivorcio = IntVar()
    ActaNacimientoPHijo = IntVar()
    ActaNacimientoSHijo = IntVar()

    Prefectura = StringVar()

    #--------- NO TOCAR ------------------------------------------------------------------
    
    frameInicio = tk.Frame(root, background = "#209cb4", height = 656, width = 1057)
    frameInicio.place(x = 143, y = 5)

    DivorcioLabel = tk.Label (frameInicio, text = "Formulario Acta De Divorcio")
    DivorcioLabel.configure (font = ("roboto", 14, "bold"), fg="#209cb4", background="WHITE")
    DivorcioLabel.place (x = 390, y = 10)
    
    # NUMERO ACTA MATRIMONIO
    
    numActaMatrimonioLabel = tk.Label(frameInicio, text = "Numero Acta Matrimonio: ")
    numActaMatrimonioLabel.configure (font = ("roboto", 10, "bold"), fg="WHITE", background="#209cb4")
    numActaMatrimonioLabel.place(x = 30, y=90)
    
    numActaMatrimonioEntry = tk.Entry(frameInicio, relief="flat", textvariable=NumActaMatrimonio)
    numActaMatrimonioEntry.place(x=200, y=93)
    
    # PRIMER ESPOSX

    PEsposo = tk.Label (frameInicio, text = "Cedula P Esposo/a: ")
    PEsposo.configure(font = ("roboto", 10, "bold"), fg = "WHITE", background="#209cb4")
    PEsposo.place (x = 70, y = 130)

    PContrayenteE = tk.Entry(frameInicio, relief="flat",textvariable=CedulaPrimerEsposo)
    PContrayenteE.place (x = 200, y = 133)
    
    #SEGUNDX ESPOSX
    
    SEsposo = tk.Label (frameInicio, text = "Cedula S Esposo/a: ")
    SEsposo.configure(font = ("roboto", 10, "bold"), fg = "WHITE", background = "#209cb4")
    SEsposo.place (x = 430, y =130)

    SEsposoE = tk.Entry(frameInicio, relief = "flat",textvariable=CedulaSegundoEsposo)
    SEsposoE.place (x = 560, y = 133)
    
    # DIRECCION PRIMER ESPOSX
    
    DireccionPELabel = tk.Label (frameInicio, text = "Direccion P Esposo/a: ")
    DireccionPELabel.configure(font = ("roboto", 10, "bold"), fg = "WHITE", background = "#209cb4")
    DireccionPELabel.place (x =57, y = 170)

    DireccionPELabeEntry = tk.Entry(frameInicio, relief = "flat",textvariable=DireccionPrimerEsposo)
    DireccionPELabeEntry.place (x = 200, y = 173)
    
    # DIRECCION SEGUNDO ESPOSX

    DireccionSELabeEntry = tk.Label (frameInicio, text = "Direccion S Esposo/a: ")
    DireccionSELabeEntry.configure (font = ("roboto", 10, "bold"), fg = "WHITE", background = "#209cb4")
    DireccionSELabeEntry.place (x = 416, y = 170)

    DireccionSELabeE = tk.Entry(frameInicio, relief = "flat",textvariable=DireccionSegundoEsposo)
    DireccionSELabeE.place (x = 560, y = 173)
    
    #ABOGADO PRIMER ESPOSX
    
    abogadoPLabel = tk.Label (frameInicio, text = "Cedula Abg P Esposo/a: ")
    abogadoPLabel.configure (font = ("roboto", 10, "bold"), fg = "WHITE", background = "#209cb4")
    abogadoPLabel.place (x = 43, y = 210)

    abogadoPE = tk.Entry(frameInicio, relief = "flat",textvariable=CedulaAbogadoPE)
    abogadoPE.place (x = 200, y = 213)

    # ABOGADO SEGUNDX ESPOSX

    abogadoSLabel = tk.Label (frameInicio, text = "Cedula Abg S Esposo/a: ")
    abogadoSLabel.configure (font = ("roboto", 10, "bold"), fg = "WHITE", background = "#209cb4")
    abogadoSLabel.place (x = 402, y = 210)

    abogadoSE = tk.Entry(frameInicio, relief = "flat", textvariable=CedulaAbogadoSE)
    abogadoSE.place (x = 560, y = 213)

    # HIJOS
        
    hijoUnoLabel = tk.Label (frameInicio, text = "Acta Nacimiento Hijo/a: ")
    hijoUnoLabel.configure (font = ("roboto", 10, "bold"), fg = "WHITE", background = "#209cb4")
    hijoUnoLabel.place (x = 750, y = 130)

    hijoUnoEntry = tk.Entry(frameInicio, relief = "flat", textvariable=ActaNacimientoPHijo)
    hijoUnoEntry.place (x = 910, y = 133)
    
    hijoDosLabel = tk.Label (frameInicio, text = "Acta Nacimiento Hijo/a: ")
    hijoDosLabel.configure (font = ("roboto", 10, "bold"), fg = "WHITE", background = "#209cb4")
    hijoDosLabel.place (x = 750, y = 170)

    hijoDosEntry = tk.Entry(frameInicio, relief = "flat", textvariable=ActaNacimientoSHijo)
    hijoDosEntry.place (x = 910, y = 173)
    
    # PREFECTURAS 
    
    prefecturasLabel = tk.Label (frameInicio, text = "Registro Civil: ")
    prefecturasLabel.configure (font = ("roboto", 10, "bold"), fg = "WHITE", background = "#209cb4")
    prefecturasLabel.place (x = 813, y = 210)
    
    prefecturasOpcion = ttk.Combobox (frameInicio, values = ["Coquivacoa", "Chiquinquira", "Cacique Mara", "Olegarios Villalobos"], width = 17, textvariable = Prefectura)
    prefecturasOpcion.place (x = 910,y = 210)
    
    # ACTA DIVORCIO NUMERO
    
    numActaLabel = tk.Label (frameInicio, text = "Num Acta Divorcio: ")
    numActaLabel.configure (font = ("roboto", 10, "bold"), fg = "WHITE", background = "#209cb4")
    numActaLabel.place (x = 780, y = 90)

    numActaEntry = tk.Entry (frameInicio, relief="flat",textvariable = numActaDivorcio)
    numActaEntry.place (x = 910, y = 93)

    ActaLabel = tk.Label (frameInicio, text = "Solo para actualizar ")
    ActaLabel.configure (font = ("roboto", 9, "bold"), fg = "WHITE", background = "#209cb4")
    ActaLabel.place (x = 910, y = 65)
    
    # BOTON AGREGAR

    botonAgregarActaDivorcio = tk.Button (frameInicio, text = "Guardar", height = 1, width = 9,relief="flat", command = lambda: funciones.guardarActaDivorcio(NumActaMatrimonio.get(),CedulaPrimerEsposo.get(),DireccionPrimerEsposo.get(),CedulaSegundoEsposo.get(),DireccionSegundoEsposo.get(), CedulaAbogadoPE.get(),CedulaAbogadoSE.get(),ActaNacimientoPHijo.get(),ActaNacimientoSHijo.get(),Prefectura.get()))
    botonAgregarActaDivorcio.configure (font = ("roboto", 10, "bold"), fg = "WHITE", activebackground = "#71acb7", activeforeground="WHITE", background="WHITE",foreground="#209cb4")
    botonAgregarActaDivorcio.place (x = 565, y = 260)

    # BOTON ACTUALIZAR 

    botonActualizar = tk.Button (frameInicio, text = "Actualizar Datos", height = 1, width = 14,relief="flat", command = lambda: funciones.actualizarActaDivorcio(NumActaMatrimonio.get(),CedulaPrimerEsposo.get(),DireccionPrimerEsposo.get(),CedulaSegundoEsposo.get(),DireccionSegundoEsposo.get(), CedulaAbogadoPE.get(),CedulaAbogadoSE.get(),ActaNacimientoPHijo.get(),ActaNacimientoSHijo.get(),Prefectura.get(),numActaDivorcio.get()))
    botonActualizar.configure (font = ("roboto", 10, "bold"), fg="WHITE", activebackground="#71acb7", activeforeground="WHITE", background="WHITE",foreground="#209cb4")
    botonActualizar.place (x = 655, y = 260)

    # REINICIAR CAMPOS

    botonReiniciar = tk.Button (frameInicio, text = "Reiniciar Campos", height = 1, width = 14,relief="flat", command = lambda: reiniciarCampos())
    botonReiniciar.configure (font = ("roboto", 10, "bold"), fg="WHITE", activebackground="#71acb7", activeforeground="WHITE", background="WHITE",foreground="#209cb4")
    botonReiniciar.place (x = 785, y = 260)

    # MOSTRAR DATOS

    boton = tk.Button (frameInicio, text = "Mostrar Datos", height = 1, width = 12,relief="flat", command = lambda: MostrarDatosADi(frameInicio))
    boton.configure (font = ("roboto", 10, "bold"), fg = "WHITE", activebackground = "#71acb7", activeforeground="WHITE", background="WHITE",foreground="#209cb4")
    boton.place (x = 915, y = 260)

def actaDefuncion ():

    def reiniciarCampos():

        ActaDifunto.set(0)
        generoDifunto.set("")
        EstadoCivilDifunto.set("")
        FechaDefuncionDifunto.set("")
        HoraDefuncionDifunto.set("")
        LugarDefuncionDifunto.set("")
        CausaDeMuerte.set("")
        CedulaInformante.set(0)
        RelacionInformante.set("")
        numAD.set(0)

    ActaDifunto = IntVar()
    generoDifunto = StringVar()
    EstadoCivilDifunto = StringVar()
    FechaDefuncionDifunto = StringVar()
    HoraDefuncionDifunto = StringVar()
    LugarDefuncionDifunto = StringVar()
    CausaDeMuerte = StringVar()
    CedulaInformante = IntVar()
    RelacionInformante = StringVar()
    numAD = IntVar()
    # NO TOCAR 
    
    frameInicio = tk.Frame(root, background = "#209cb4", height = 656, width = 1057)
    frameInicio.place(x = 143, y = 5)

    inicioLabel = tk.Label(frameInicio, text = "Formulario Acta De Defuncion")
    inicioLabel.configure(font = ("roboto", 14, "bold"), fg = "#209cb4", background = "WHITE")
    inicioLabel.place (x = 390, y = 10)

    #  ACTA DE NACIMIENTO DEL MUELTO

    difuntoLabel = tk.Label (frameInicio, text = "Acta Nacimiento Difunto: ")
    difuntoLabel.configure(font = ("roboto", 12, "bold"), fg = "WHITE", background = "#209cb4")
    difuntoLabel.place (x = 30, y = 90)

    difuntoEntry = tk.Entry(frameInicio, relief = "flat", textvariable = ActaDifunto)
    difuntoEntry.place (x = 225, y = 94)

    # CAUSA DE MUELTE

    CMuerteLabel = tk.Label (frameInicio, text = "Causa De Muerte: ")
    CMuerteLabel.configure (font = ("roboto", 12, "bold"), fg = "WHITE", background = "#209cb4")
    CMuerteLabel.place (x = 410, y = 90)

    CMuerteEntry = tk.Entry(frameInicio, relief = "flat",textvariable=CausaDeMuerte)
    CMuerteEntry.place (x = 555, y = 93)

    # LUGAR DE MUELTE

    LMuerteLabel = tk.Label (frameInicio, text = "Lugar De Defuncion: ")
    LMuerteLabel.configure (font = ("roboto", 12, "bold"), fg = "WHITE", background = "#209cb4")
    LMuerteLabel.place (x = 735, y = 90)

    LMuerteEntry = tk.Entry(frameInicio, relief = "flat",textvariable=LugarDefuncionDifunto)
    LMuerteEntry.place (x = 900, y = 93)

    # INFORMANTE

    informanteLabel = tk.Label (frameInicio, text = "Cedula Informante: ")
    informanteLabel.configure(font = ("roboto", 12, "bold"), fg = "WHITE", background = "#209cb4")
    informanteLabel.place (x = 73, y = 130)

    informanteEntry = tk.Entry(frameInicio, relief = "flat", textvariable = CedulaInformante)
    informanteEntry.place (x = 225, y = 133)

    # RELACION INFORMANTE
    
    RInformanteLabel = tk.Label (frameInicio, text = "Relacion Informante: ")
    RInformanteLabel.configure (font = ("roboto", 10, "bold"), fg = "WHITE", background = "#209cb4")
    RInformanteLabel.place (x = 413, y = 130)

    RInformanteEntry = tk.Entry(frameInicio, relief = "flat", textvariable = RelacionInformante)
    RInformanteEntry.place (x = 555, y = 133)

    # FECHA DE DEFUNCION

    FMuerteLabel = tk.Label (frameInicio, text = "Fecha Defuncion: ")
    FMuerteLabel.configure (font = ("roboto", 12, "bold"), fg = "WHITE", background = "#209cb4")
    FMuerteLabel.place (x = 760, y = 130)

    FMuerteEntry = tk.Entry(frameInicio, relief = "flat", textvariable=FechaDefuncionDifunto)
    FMuerteEntry.place (x = 900, y = 133)

    FormatoMuLabel = tk.Label(frameInicio, text = "Formato: dd-mm-aaaa ")
    FormatoMuLabel.configure(font = ("roboto", 8, "bold"), fg ="WHITE", background="#209cb4")
    FormatoMuLabel.place (x = 902, y = 153)
    
    # ESTADO CIVIL DEL MUELTO
    
    EdoCivilMLabel = tk.Label (frameInicio, text = "Estado Civil Difunto: ")
    EdoCivilMLabel.configure (font = ("roboto", 12, "bold"), fg = "WHITE", background = "#209cb4")
    EdoCivilMLabel.place (x = 62, y =170)
    
    EdoCivilMOpcion = ttk.Combobox (frameInicio, values = ["Soltero/a", "Casado/a", "Divorciado","Viudo/a"], width = 17, textvariable = EstadoCivilDifunto)
    EdoCivilMOpcion.place(x = 225, y = 173)

    # HORA DE DEFUNCION

    HMuerteLabel = tk.Label (frameInicio, text = "Hora De Defuncion: ")
    HMuerteLabel.configure (font = ("roboto", 12, "bold"), fg = "WHITE", background = "#209cb4")
    HMuerteLabel.place (x = 743, y = 180)

    HMuerteEntry = tk.Entry(frameInicio, relief = "flat",textvariable=HoraDefuncionDifunto)
    HMuerteEntry.place (x = 900, y = 183)

    FormatoHLabel = tk.Label(frameInicio, text = "Formato: hh:mm:ss ")
    FormatoHLabel.configure(font = ("roboto", 8, "bold"), fg ="WHITE", background="#209cb4")
    FormatoHLabel.place (x = 902, y = 203)


    #FECHA EXPEDICION ACTA  

    generoLabel = tk.Label (frameInicio, text = "Genero Difunto: ")
    generoLabel.configure (font = ("roboto", 12, "bold"), fg = "WHITE", background = "#209cb4")
    generoLabel.place (x = 425, y = 170)

    generoOpcion = ttk.Combobox (frameInicio,values = ["Hombre", "Mujer", "No-Binario"], width=17,textvariable=generoDifunto)
    generoOpcion.place(x = 555, y = 173)

    numActaLabel = tk.Label (frameInicio, text = "Num Acta Defuncion: ")
    numActaLabel.configure (font = ("roboto", 12, "bold"), fg = "WHITE", background = "#209cb4")
    numActaLabel.place (x = 57, y = 210)

    numActaEntry = tk.Entry (frameInicio, relief="flat",textvariable = numAD)
    numActaEntry.place (x = 225, y = 213)

    ActaLabel = tk.Label (frameInicio, text = "Solo para actualizar ")
    ActaLabel.configure (font = ("roboto", 9, "bold"), fg = "WHITE", background = "#209cb4")
    ActaLabel.place (x = 225, y = 233)

    # GUARDAR DATOS

    botonAgregarActaDefuncion = tk.Button (frameInicio, text = "Guardar", height = 1, width = 9,relief="flat", command = lambda: funciones.guardarActaDefuncion(ActaDifunto.get(), generoDifunto.get(), EstadoCivilDifunto.get(), FechaDefuncionDifunto.get(), HoraDefuncionDifunto.get(), LugarDefuncionDifunto.get(), CausaDeMuerte.get(),CedulaInformante.get(),RelacionInformante.get()))
    botonAgregarActaDefuncion.configure (font = ("roboto", 10, "bold"), fg = "WHITE", activebackground = "#71acb7", activeforeground="WHITE", background="WHITE",foreground="#209cb4")
    botonAgregarActaDefuncion.place (x = 565, y = 240)           
    
    # BOTON ACTUALIZAR 

    botonActualizar = tk.Button (frameInicio, text = "Actualizar Datos", height = 1, width = 14,relief="flat", command = lambda: funciones.actualizarActaDefuncion(ActaDifunto.get(), generoDifunto.get(), EstadoCivilDifunto.get(), FechaDefuncionDifunto.get(), HoraDefuncionDifunto.get(), LugarDefuncionDifunto.get(), CausaDeMuerte.get(),CedulaInformante.get(),RelacionInformante.get(),numAD.get()))
    botonActualizar.configure (font = ("roboto", 10, "bold"), fg="WHITE", activebackground="#71acb7", activeforeground="WHITE", background="WHITE",foreground="#209cb4")
    botonActualizar.place (x = 655, y = 240)

    # REINICIAR CAMPOS

    botonReiniciar = tk.Button (frameInicio, text = "Reiniciar Campos", height = 1, width = 14,relief="flat", command = lambda: reiniciarCampos())
    botonReiniciar.configure (font = ("roboto", 10, "bold"), fg="WHITE", activebackground="#71acb7", activeforeground="WHITE", background="WHITE",foreground="#209cb4")
    botonReiniciar.place (x = 785, y = 240)

    # MOSTRAR DATOS

    botonMostrarAD = tk.Button (frameInicio, text = "Mostrar Datos", height = 1, width = 12,relief="flat", command = lambda: MostrarDatosAD(frameInicio))
    botonMostrarAD.configure (font = ("roboto", 10, "bold"), fg = "WHITE", activebackground = "#71acb7", activeforeground="WHITE", background="WHITE",foreground="#209cb4")
    botonMostrarAD.place (x = 915, y = 240)
  
# Configuracion Ventana

# TAMAÑO Y POSICIONAMIENTO DE LA VENTANA

ancho = 1205
alto = 666

posicionX = round(ancho/2 - ancho/2)
posicionY = round(alto/2 - alto/2)

r = str (posicionX) + "+" + str (posicionY)

root.geometry("1205x666"+"+"+r)
root.title("Registro Civil")
root.iconbitmap("Images/ImagenesFunciones/Pen.ico")
root.config(background="WHITE")
root.resizable(0,0)

# Frames

frameMenu = tk.Frame(root)
frameMenu.pack(side=tk.LEFT)

frameInicio = tk.Frame(root,background="WHITE",height = 666, width = 1062,highlightbackground="WHITE",highlightthickness=5)
frameInicio.pack(side=tk.TOP)

# Imagenes Botones

nacimientoPhoto = tk.PhotoImage(file="Images/ImagenesBotones/Nacimiento.png")
nacimientoImage = nacimientoPhoto.subsample(1, 1)

cedulaPhoto = tk.PhotoImage(file="Images/ImagenesBotones/Cedula.png")
cedulaImage = cedulaPhoto.subsample(1, 1)

matrimonioPhoto = tk.PhotoImage(file="Images/ImagenesBotones/Matrimonio.png")
matrimonioImage = matrimonioPhoto.subsample(1, 1)

divorcioPhoto = tk.PhotoImage(file="Images/ImagenesBotones/Divorcio.png")
divorcioImage = divorcioPhoto.subsample(1, 1)

defuncionPhoto = tk.PhotoImage(file="Images/ImagenesBotones/Difunto.png")
defuncionImage = defuncionPhoto.subsample(1, 1)

# Botones

buttonActaNacimiento = tk.Button (frameMenu, text = "\nActa\nde\nNacimiento", image = nacimientoImage, compound = tk.TOP, background= "#209cb4", relief= tk.FLAT,command=actaNacimiento)
buttonActaNacimiento.config(height = 125, width = 130, font=("roboto", 10, "normal",),fg="WHITE",activebackground="#71acb7",activeforeground="WHITE")
buttonActaNacimiento.grid(row = 0,column = 0)

buttonCedula = tk.Button (frameMenu, text = "\nCedula", image = cedulaImage, compound = tk.TOP, background= "#209cb4", relief= tk.FLAT,command=cedula)
buttonCedula.config (height = 125, width = 130, font=("roboto", 10, "normal"), fg="WHITE",activebackground="#71acb7",activeforeground="WHITE")
buttonCedula.grid (row=1,column =0)

buttonActaMatrimonio = tk.Button (frameMenu, text = "\nActa\nde\nMatrimonio", image = matrimonioImage, compound = tk.TOP, background= "#209cb4", relief= tk.FLAT,command=actaMatrimonio)
buttonActaMatrimonio.config(height = 125, width = 130, font=("roboto", 10, "normal"),fg="WHITE",activebackground="#71acb7",activeforeground="WHITE")
buttonActaMatrimonio.grid(row=2,column =0)

buttonActaDivorcio = tk.Button (frameMenu, text = "\nActa \nde\nDivorcio", image = divorcioImage, compound = tk.TOP, background= "#209cb4", relief= tk.FLAT,command=actaDivorcio)
buttonActaDivorcio.config(height = 125, width = 130, font=("roboto", 10, "normal"),fg="WHITE", activebackground="#71acb7",activeforeground="WHITE")
buttonActaDivorcio.grid(row=3,column =0)

buttonActaDefuncion = tk.Button (frameMenu, text = "\nActa \nde\nDefuncion", image = defuncionImage, compound = tk.TOP, relief= tk.FLAT, background= "#209cb4",command=actaDefuncion)
buttonActaDefuncion.configure(height = 126, width = 130, font=("roboto", 10, "normal"),fg="WHITE", activebackground="#71acb7", activeforeground="WHITE")
buttonActaDefuncion.grid(row = 4,column = 0)

root.mainloop()