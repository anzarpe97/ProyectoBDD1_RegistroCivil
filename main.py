import funciones

import tkinter as tk 
from tkinter import ttk
from tkinter import *

root = tk.Tk()

# ---- Funciones ----

def actaNacimiento ():
    
    # ----- Variables -------------

    nombre_bebe_acta = StringVar()
    #apellidos_bebe_acta = StringVar()
    #sexo_bebe = StringVar()
    #lugar_nacimiento = StringVar()
    #cedula_padre_acta = IntVar()
    #cedula_madre_acta = IntVar()
    #prefectura = StringVar()
    

    #--------- NO TOCAR ------------------------------------------------------------------
    
    frameInicio = tk.Frame(root, background = "#209cb4", height = 656, width = 1057)
    frameInicio.place(x = 143, y = 5)
    
    #---------------------------------------------------------------------------
    
    inicioLabel = tk.Label(frameInicio, text = "Formulario Acta De Nacimiento")
    inicioLabel.configure(font = ("roboto", 14, "bold"), fg="#209cb4", background="WHITE")
    inicioLabel.place (x = 420, y = 10)

    # ---- NOMBRES Y APELLIDOS ----

    nombresLabel = tk.Label (frameInicio, text = "Nombres: ")
    nombresLabel.configure(font = ("roboto", 12, "bold"), fg="WHITE", background="#209cb4")
    nombresLabel.place (x = 60, y = 90)

    nombresEntry = tk.Entry(frameInicio, relief="flat",textvariable=nombre_bebe_acta)
    nombresEntry.place (x = 142, y = 93)
    
    apellidosLabel = tk.Label (frameInicio, text = "Apellidos: ")
    apellidosLabel.configure(font = ("roboto", 12, "bold"), fg="WHITE", background="#209cb4")
    apellidosLabel.place (x = 60, y = 130)

    apellidosEntry= tk.Entry(frameInicio, relief="flat")
    apellidosEntry.place (x = 142, y = 133)

    # ---- Cedulas Padres ----

    # PADRE

    cedulaPadreLabel = tk.Label (frameInicio, text = "Cedula Padre: ")
    cedulaPadreLabel.configure(font = ("roboto", 12, "bold"), fg = "WHITE", background = "#209cb4")
    cedulaPadreLabel.place (x = 380, y = 90)

    cedulaPadreEntry = tk.Entry(frameInicio, relief="flat")
    cedulaPadreEntry.place (x = 500, y = 93)

    nombrePadreLabel = tk.Label (frameInicio, text = "Nombre Padre: ")
    nombrePadreLabel.configure(font = ("roboto", 12, "bold"), fg = "WHITE", background = "#209cb4")
    nombrePadreLabel.place (x = 373, y = 130)

    nombrePadreEntry = tk.Entry(frameInicio, relief="flat")
    nombrePadreEntry.place (x = 500, y = 133)

    # #MADRE

    cedulaMadreLabel = tk.Label (frameInicio, text = "Cedula Madre: ")
    cedulaMadreLabel.configure(font = ("roboto", 12, "bold"), fg = "WHITE", background = "#209cb4")
    cedulaMadreLabel.place (x = 700, y = 90)

    cedulaMadreEntry = tk.Entry(frameInicio, relief="flat")
    cedulaMadreEntry.place (x = 820, y = 93)

    nombreMadreLabel = tk.Label (frameInicio, text = "Nombre Madre: ")
    nombreMadreLabel.configure(font = ("roboto", 12, "bold"), fg = "WHITE", background = "#209cb4")
    nombreMadreLabel.place (x = 695, y = 130)

    nombreMadreEntry = tk.Entry(frameInicio, relief="flat")
    nombreMadreEntry.place (x = 820, y = 133)

    # ---- Sexo Bebe (2) -----

    sexoBebeLabel = tk.Label (frameInicio, text = "Sexo: ")
    sexoBebeLabel.configure (font = ("roboto", 12, "bold"), fg = "WHITE", background = "#209cb4")
    sexoBebeLabel.place (x = 92, y = 170)#x = 100, y = 210
    
    sexoBebeOpcion = ttk.Combobox (frameInicio,values = ["Masculino", "Femenino"],width=17)
    sexoBebeOpcion.place (x = 143,y = 173)#x = 275, y = 213

    prefecturaLabel = tk.Label (frameInicio, text = "Prefectura: ")
    prefecturaLabel.configure (font = ("roboto", 12, "bold"), fg = "WHITE", background = "#209cb4")
    prefecturaLabel.place (x = 405, y = 170)
    
    prefecturaOpcion = ttk.Combobox (frameInicio,values = ["Manzanillo", "Olegario Villalobos", "Delicias", "El Bajo"],width=17)
    prefecturaOpcion.place (x = 499, y = 173)

    # ---- UBICACION -----

    ubicacionLabel = tk.Label (frameInicio, text = "Lugar De Nacimiento: ")
    ubicacionLabel.configure (font = ("roboto", 10, "bold"), fg = "WHITE", background = "#209cb4")
    ubicacionLabel.place (x = 675, y = 170)

    ubicacionEntry = tk.Entry (frameInicio, relief="flat")
    ubicacionEntry.place (x = 820, y = 171)

    botonAgregar = tk.Button (frameInicio, text = "Guardar", height = 1, width = 7,relief="flat",command=lambda: funciones.guardarDatosAcNacimiento(nombresEntry.get(),apellidosEntry.get(),nombrePadreEntry.get(),cedulaPadreEntry.get(),nombreMadreEntry.get(),cedulaMadreEntry.get(),sexoBebeOpcion.get(),ubicacionEntry.get(),prefecturaOpcion.get()))
    botonAgregar.configure (font = ("roboto", 10, "bold"), fg="WHITE", activebackground="#71acb7", activeforeground="WHITE", background="WHITE",foreground="#209cb4")
    botonAgregar.place (x = round(1057/2), y = 230)

def cedula ():

    frameInicio = tk.Frame(root, background = "#209cb4", height = 656, width = 1057)
    frameInicio.place(x = 143, y = 5)
    
    # --- TITULO ----
    
    cedulaLabel = tk.Label(frameInicio, text = "Formulario Cedula")
    cedulaLabel.configure(font = ("roboto", 14, "bold"), fg="#209cb4", background="WHITE")
    cedulaLabel.place (x = 450, y = 10)

    # ---- NUMERO DE ACTA DE NACIMIENTO ----

    numActaNacimiento = tk.Label(frameInicio, text = "Numero Acta De Nacimiento: ")
    numActaNacimiento.configure(font = ("roboto", 12, "bold"), fg="WHITE", background="#209cb4")
    numActaNacimiento.place (x = 80, y = 90)

    numActaNacimientoE = tk.Entry(frameInicio, relief="flat")
    numActaNacimientoE.place (x = 310, y = 93)
    
    # ---- NUMERO DE CEDULA -----
    
    NumCedulaLabel = tk.Label(frameInicio, text = "Numero De Cedula: ")
    NumCedulaLabel.configure(font = ("roboto", 12, "bold"), fg="WHITE", background="#209cb4")
    NumCedulaLabel.place (x = 150, y = 127)

    NumCedulsEntry = tk.Entry(frameInicio, relief="flat")
    NumCedulsEntry.place (x =310, y = 130)
    
    # ---- ESTADO CIVIL -----
    
    EdoCivilLabel = tk.Label (frameInicio, text = "Estado Civil: ")
    EdoCivilLabel.configure (font = ("roboto", 12, "bold"), fg = "WHITE", background = "#209cb4")
    EdoCivilLabel.place (x = 600, y = 90)
    
    EdoCivilOpcion = ttk.Combobox (values = ["Soltero/a", "Casado/a", "Viudo/a"])
    EdoCivilOpcion.place(x = 850, y = 97)

    # ----- NACIONALIDAD ------

    nacionalidadlLabel = tk.Label (frameInicio, text = "Nacionalidad: ")
    nacionalidadlLabel.configure (font = ("roboto", 12, "bold"), fg = "WHITE", background = "#209cb4")
    nacionalidadlLabel.place (x = 595, y = 130)
    
    nacionalidadOpcion = ttk.Combobox (values = ["Venezolano/a", "Extranjero/a"])
    nacionalidadOpcion.place(x = 850, y = 135)
    #putita
    # ----- GENEROS (2) -----

    generoLabel = tk.Label (frameInicio, text = "Genero: ")
    generoLabel.configure (font = ("roboto", 12, "bold"), fg = "WHITE", background = "#209cb4")
    generoLabel.place (x = 637, y = 170)
    
    generoOpcion = ttk.Combobox (values = ["Hombre", "Mujer", "No-Binario"])
    generoOpcion.place(x = 850, y = 177)

    # ----- FECHAS DE EMISION Y VENCIMIENTO -------

    # FECHA DE EMISION

    FEmisionLabel = tk.Label (frameInicio, text = "Fecha De Emision: ")
    FEmisionLabel.configure (font = ("roboto", 12, "bold"), fg = "WHITE", background = "#209cb4")
    FEmisionLabel.place (x = 155, y = 166)

    FEmisionEntry = tk.Entry(frameInicio, relief = "flat")
    FEmisionEntry.place (x = 310, y = 170)

    FormatoELabel = tk.Label(frameInicio, text = "Formato (aa/mm/dd) ")
    FormatoELabel.configure(font = ("roboto", 8, "bold"), fg ="WHITE", background="#209cb4")
    FormatoELabel.place (x = 312, y = 193)

    # FECHA DE VENCIMIENTO

    FVencimientoLabel = tk.Label (frameInicio, text = "Fecha De Vencimiento: ")
    FVencimientoLabel.configure(font = ("roboto", 12, "bold"), fg="WHITE", background="#209cb4")
    FVencimientoLabel.place (x = 123, y =217)

    FVencimientoEntry = tk.Entry(frameInicio, relief="flat")
    FVencimientoEntry.place (x = 310, y = 220)

    FormatoELabel = tk.Label(frameInicio, text = "Formato (aa/mm/dd) ")
    FormatoELabel.configure(font = ("roboto", 8, "bold"), fg ="WHITE", background="#209cb4")
    FormatoELabel.place (x = 314, y = 242)

def actaMatrimonio ():

    #--------- NO TOCAR ------------------------------------------------------------------
    
    frameInicio = tk.Frame(root, background = "#209cb4", height = 656, width = 1057)
    frameInicio.place(x = 143, y = 5)
    
    #---------------------------------------------------------------------------

    MatrimonioLabel = tk.Label(frameInicio, text = "Formulario Acta De Matrimonio")
    MatrimonioLabel.configure(font = ("roboto", 14, "bold"), fg="#209cb4", background="WHITE")
    MatrimonioLabel.place (x = 390, y = 10)

    # ---- Contrayentes ------

    # Primer Contrayente Cedula

    PContrayente = tk.Label (frameInicio, text = "Cedula P Contrayente: ")
    PContrayente.configure(font = ("roboto", 10, "bold"), fg = "WHITE", background="#209cb4")
    PContrayente.place (x = 50, y = 90)
    
    PContrayenteE = tk.Entry(frameInicio, relief="flat")
    PContrayenteE.place (x =200, y = 93)
    #----------------------------------------------------------
    
    # Segundo Contrayente Cedula

    SContrayente = tk.Label (frameInicio, text = "Cedula S Contrayente: ")
    SContrayente.configure(font = ("roboto", 10, "bold"), fg = "WHITE", background = "#209cb4")
    SContrayente.place (x = 400, y = 90)

    SContrayenteE = tk.Entry(frameInicio, relief = "flat")
    SContrayenteE.place (x = 550, y = 93)
    #----------------------------------------------------------
    
    # OCUPACION 
    
    OPContrayente = tk.Label (frameInicio, text = "Ocupacion P Contrayente: ")
    OPContrayente.configure(font = ("roboto", 10, "bold"), fg = "WHITE", background = "#209cb4")
    OPContrayente.place (x = 25, y = 130)

    OPContrayenteE = tk.Entry(frameInicio, relief = "flat")
    OPContrayenteE.place (x = 200, y = 133)

    OSContrayente = tk.Label (frameInicio, text = "Ocupacion S Contrayente: ")
    OSContrayente.configure (font = ("roboto", 10, "bold"), fg = "WHITE", background = "#209cb4")
    OSContrayente.place (x = 378, y = 130)

    OSContrayenteE = tk.Entry(frameInicio, relief = "flat")
    OSContrayenteE.place (x = 550, y = 133)
    
    # ---- DIRECCION CONTRAYENTES -------
    
    direccionPLabel = tk.Label (frameInicio, text = "Direccion P Contrayente: ")
    direccionPLabel.configure (font = ("roboto", 10, "bold"), fg = "WHITE", background = "#209cb4")
    direccionPLabel.place (x = 34, y = 170)

    direccionPE = tk.Entry(frameInicio, relief = "flat")
    direccionPE.place (x = 200, y = 173)

    
    direccionSLabel = tk.Label (frameInicio, text = "Direccion S Contrayente: ")
    direccionSLabel.configure (font = ("roboto", 10, "bold"), fg = "WHITE", background = "#209cb4")
    direccionSLabel.place (x = 385, y = 170)

    direccionSE = tk.Entry(frameInicio, relief = "flat")
    direccionSE.place (x = 550, y = 174)

    # ---- TESTIGO -----
    
    TestigoLabel = tk.Label (frameInicio, text = "Cedula Testigo: ")
    TestigoLabel.configure (font = ("roboto", 10, "bold"), fg = "WHITE", background = "#209cb4")
    TestigoLabel.place (x = 760, y = 90)

    testigoE = tk.Entry(frameInicio, relief = "flat")
    testigoE.place (x = 865, y = 93)

    direccionTLabel = tk.Label (frameInicio, text = "Direccion Testigo: ")
    direccionTLabel.configure (font = ("roboto",10, "bold"), fg = "WHITE", background = "#209cb4")
    direccionTLabel.place (x = 745,y = 130)

    direccionTE = tk.Entry(frameInicio, relief = "flat")
    direccionTE.place (x = 865, y = 133)

    prefecturaMLabel = tk.Label (frameInicio, text = "Prefectura: ")
    prefecturaMLabel.configure (font = ("roboto", 10, "bold"), fg = "WHITE", background = "#209cb4")
    prefecturaMLabel.place (x = 788, y = 170)
    
    prefecturaME = ttk.Combobox (frameInicio, values = ["Olegario Villalobos", "El Enterrado"],width=17)
    prefecturaME.place(x = 865, y = 170)

    # ---- UBICACION PREFECTURA ------

    estadoLabel = tk.Label (frameInicio, text = "Estado: ")
    estadoLabel.configure (font = ("roboto", 10, "bold"), fg = "WHITE", background = "#209cb4")
    estadoLabel.place (x = 147, y = 210)

    estadoE = tk.Entry(frameInicio, relief = "flat")
    estadoE.place (x = 200, y = 213)# OPContrayente.place (x = 25, y = 130)

    parroquiaLabel = tk.Label (frameInicio, text = "Parroquia: ")
    parroquiaLabel.configure (font = ("roboto", 10, "bold"), fg = "WHITE", background = "#209cb4")
    parroquiaLabel.place (x = 260, y = 260)

    parroquiaE = tk.Entry(frameInicio, relief = "flat")
    parroquiaE.place (x = 350, y = 264)

    municicpioLabel = tk.Label (frameInicio, text = "Municipio: ")
    municicpioLabel.configure (font = ("roboto", 10, "bold"), fg = "WHITE", background = "#209cb4")
    #municicpioLabel.place (x = 520, y = 260)

    municicpioE = tk.Entry(frameInicio, relief = "flat")
    #municicpioE.place (x = 610, y = 264)

    hijosParejaLabel = tk.Label(frameInicio, text = "Hijos: ")
    hijosParejaLabel.configure (font = ("roboto", 10, "bold"), fg = "WHITE", background = "#209cb4")
    #hijosParejaLabel.place(x = 350, y = 306)
    
def actaDivorcio ():

    #--------- NO TOCAR ------------------------------------------------------------------
    
    frameInicio = tk.Frame(root, background = "#209cb4", height = 656, width = 1057)
    frameInicio.place(x = 143, y = 5)
    
    #---------------------------------------------------------------------------

    DivorcioLabel = tk.Label (frameInicio, text = "Formulario Acta De Divorcio")
    DivorcioLabel.configure (font = ("roboto", 14, "bold"), fg="#209cb4", background="WHITE")
    DivorcioLabel.place (x = 390, y = 10)

    # ---- Esposos -------

    PEsposo = tk.Label (frameInicio, text = "Cedula Primer Esposo/a: ")
    PEsposo.configure(font = ("roboto", 12, "bold"), fg = "WHITE", background="#209cb4")
    PEsposo.place (x = 80, y = 90)

    PContrayenteE = tk.Entry(frameInicio, relief="flat")
    PContrayenteE.place (x = 275, y = 93)
    
    SEsposo = tk.Label (frameInicio, text = "Cedula Segundo Esposo/a: ")
    SEsposo.configure(font = ("roboto", 12, "bold"), fg = "WHITE", background = "#209cb4")
    SEsposo.place (x = 548, y = 90)

    SEsposoE = tk.Entry(frameInicio, relief = "flat")
    SEsposoE.place (x = 765, y = 93)
    
    # ---- DIRECCION ESPOSOS ----
    
    DireccionPELabel = tk.Label (frameInicio, text = "Direccion Primer Esposo/a: ")
    DireccionPELabel.configure(font = ("roboto", 12, "bold"), fg = "WHITE", background = "#209cb4")
    DireccionPELabel.place (x =60, y = 130)

    DireccionPELabeEntry = tk.Entry(frameInicio, relief = "flat")
    DireccionPELabeEntry.place (x = 275, y = 133)

    DireccionSELabeEntry = tk.Label (frameInicio, text = "Direccion Segundo Esposo/a: ")
    DireccionSELabeEntry.configure (font = ("roboto", 12, "bold"), fg = "WHITE", background = "#209cb4")
    DireccionSELabeEntry.place (x = 530, y = 130)

    DireccionSELabeE = tk.Entry(frameInicio, relief = "flat")
    DireccionSELabeE.place (x = 765, y = 133)
    
    # ---- CEDULAS ABOGADOS -------
    
    abogadoPLabel = tk.Label (frameInicio, text = "Cedula Abg Primer Esposo/a: ")
    abogadoPLabel.configure (font = ("roboto", 12, "bold"), fg = "WHITE", background = "#209cb4")
    abogadoPLabel.place (x = 43, y = 170)

    abogadoPE = tk.Entry(frameInicio, relief = "flat")
    abogadoPE.place (x = 275, y = 174)

    abogadoSLabel = tk.Label (frameInicio, text = "Cedula Abg Segundo Esposo/a: ")
    abogadoSLabel.configure (font = ("roboto", 12, "bold"), fg = "WHITE", background = "#209cb4")
    abogadoSLabel.place (x = 515, y = 170)

    abogadoSE = tk.Entry(frameInicio, relief = "flat")
    abogadoSE.place (x = 765, y = 174)

    # -------------- Direccion abogados ----------------------------
    
    DabogadoPLabel = tk.Label (frameInicio, text = "Direccion Abg Primer Esposo/a: ")
    DabogadoPLabel.configure (font = ("roboto", 12, "bold"), fg = "WHITE", background = "#209cb4")
    DabogadoPLabel.place (x = 24, y = 210)

    DabogadoPE = tk.Entry(frameInicio, relief = "flat")
    DabogadoPE.place (x = 275, y = 214)

    DabogadoSLabel = tk.Label (frameInicio, text = "Direccion Abg Segundo Esposo/a: ")
    DabogadoSLabel.configure (font = ("roboto", 12, "bold"), fg = "WHITE", background = "#209cb4")
    DabogadoSLabel.place (x = 497, y = 210)

    DabogadoSE = tk.Entry(frameInicio, relief = "flat")
    DabogadoSE.place (x = 766, y = 214)

    # ---- UBICACION PREFECTURA ------

    estadoLabel = tk.Label (frameInicio, text = "Estado: ")
    estadoLabel.configure (font = ("roboto", 12, "bold"), fg = "WHITE", background = "#209cb4")
    estadoLabel.place (x = 25, y = 260)

    estadoE = tk.Entry(frameInicio, relief = "flat")
    estadoE.place (x = 103, y = 264)

    parroquiaLabel = tk.Label (frameInicio, text = "Parroquia: ")
    parroquiaLabel.configure (font = ("roboto", 12, "bold"), fg = "WHITE", background = "#209cb4")
    parroquiaLabel.place (x = 260, y = 260)

    parroquiaE = tk.Entry(frameInicio, relief = "flat")
    parroquiaE.place (x = 350, y = 264)

    municicpioLabel = tk.Label (frameInicio, text = "Municipio: ")
    municicpioLabel.configure (font = ("roboto", 12, "bold"), fg = "WHITE", background = "#209cb4")
    municicpioLabel.place (x = 520, y = 260)

    municicpioE = tk.Entry(frameInicio, relief = "flat")
    municicpioE.place (x = 610, y = 264)

    prefecturaMLabel = tk.Label (frameInicio, text = "Prefectura: ")
    prefecturaMLabel.configure (font = ("roboto", 12, "bold"), fg = "WHITE", background = "#209cb4")
    prefecturaMLabel.place (x = 770, y = 260)
    
    prefecturaME = ttk.Combobox (values = ["Olegario Villalobos", "El Enterrado"])
    prefecturaME.place(x = 1010, y = 266)

def actaDefuncion ():

    #--------- NO TOCAR -----------------------------------------------------------
    
    frameInicio = tk.Frame(root, background = "#209cb4", height = 656, width = 1057)
    frameInicio.place(x = 143, y = 5)
    
    #---------------------------------------------------------------------------

    inicioLabel = tk.Label(frameInicio, text = "Formulario Acta De Defuncion")
    inicioLabel.configure(font = ("roboto", 14, "bold"), fg = "#209cb4", background = "WHITE")
    inicioLabel.place (x = 390, y = 10)

    # ------- Cedula Difunto ------------------- 

    difuntoLabel = tk.Label (frameInicio, text = "Cedula Difunto: ")
    difuntoLabel.configure(font = ("roboto", 12, "bold"), fg = "WHITE", background = "#209cb4")
    difuntoLabel.place (x = 130, y = 90)

    difuntoEntry = tk.Entry(frameInicio, relief = "flat")
    difuntoEntry.place (x = 260, y = 93)

    # ----------- Informante --------------------

    informanteLabel = tk.Label (frameInicio, text = "Cedula Informante: ")
    informanteLabel.configure(font = ("roboto", 12, "bold"), fg = "WHITE", background = "#209cb4")
    informanteLabel.place (x = 595, y = 90)

    informanteEntry = tk.Entry(frameInicio, relief = "flat")
    informanteEntry.place (x = 750, y = 93)

    # ------------ Relacion Informante -------------
    
    RInformanteLabel = tk.Label (frameInicio, text = "Relacion Informante: ")
    RInformanteLabel.configure (font = ("roboto", 12, "bold"), fg = "WHITE", background = "#209cb4")
    RInformanteLabel.place (x = 585, y = 130)

    RInformanteEntry = tk.Entry(frameInicio, relief = "flat")
    RInformanteEntry.place (x = 750, y = 133)

    # ----------- Causa De Muerte ---------------

    CMuerteLabel = tk.Label (frameInicio, text = "Causa De Muerte: ")
    CMuerteLabel.configure (font = ("roboto", 12, "bold"), fg = "WHITE", background = "#209cb4")
    CMuerteLabel.place (x = 115, y = 130)

    CMuerteEntry = tk.Entry(frameInicio, relief = "flat")
    CMuerteEntry.place (x = 260, y = 133)

    # ---------- Lugar De muerte ---------------

    LMuerteLabel = tk.Label (frameInicio, text = "Lugar De Defuncion: ")
    LMuerteLabel.configure (font = ("roboto", 12, "bold"), fg = "WHITE", background = "#209cb4")
    LMuerteLabel.place (x = 90, y = 170)

    LMuerteEntry = tk.Entry(frameInicio, relief = "flat")
    LMuerteEntry.place (x = 260, y = 173)

    # ---------- Fecha de Defuncion -----------

    FMuerteLabel = tk.Label (frameInicio, text = "Fecha De Defuncion: ")
    FMuerteLabel.configure (font = ("roboto", 12, "bold"), fg = "WHITE", background = "#209cb4")
    FMuerteLabel.place (x = 90, y = 210)#90 220

    FMuerteEntry = tk.Entry(frameInicio, relief = "flat")
    FMuerteEntry.place (x = 260, y = 213) #260 220

    FormatoMuLabel = tk.Label(frameInicio, text = "Formato (aa/mm/dd) ")
    FormatoMuLabel.configure(font = ("roboto", 8, "bold"), fg ="WHITE", background="#209cb4")
    FormatoMuLabel.place (x = 262, y = 233)

    # ------------- Hora de Defuncion --------

    HMuerteLabel = tk.Label (frameInicio, text = "Hora De Defuncion: ")
    HMuerteLabel.configure (font = ("roboto", 12, "bold"), fg = "WHITE", background = "#209cb4")
    HMuerteLabel.place (x = 592, y = 170)#90 220

    HMuerteEntry = tk.Entry(frameInicio, relief = "flat")
    HMuerteEntry.place (x = 750, y = 173) #260 220

    FormatoHLabel = tk.Label(frameInicio, text = "Formato (hh/mm/ss) ")
    FormatoHLabel.configure(font = ("roboto", 8, "bold"), fg ="WHITE", background="#209cb4")
    FormatoHLabel.place (x = 750, y = 193)

#putita    
# Configuracion Ventana

# TAMAÑO Y POSICIONAMIENTO DE LA VENTANA

ancho = 1205
alto = 666

posicionX = round(ancho/2-ancho/2)
posicionY = round(alto/2-alto/2)

r = str(posicionX)+"+"+str(posicionY)

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

