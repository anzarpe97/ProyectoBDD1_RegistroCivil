import funciones
from DBC import DAO

import tkinter as tk 
from tkinter import ttk
from tkinter import *

a = DAO()
root = tk.Tk()

# FUNCIONES

def actaNacimiento ():
    """
    
    `nro_acta` int(11) NOT NULL,                    # AUTOINCREMENTABLE
    `nombres` varchar(50) NOT NULL,                 # LISTO
    `apellidos` varchar(50) NOT NULL,               # LISTO
    `fecha_nacimiento` date NOT NULL,               # LISTO
    `hora_nacimiento` time NOT NULL,                # LISTO
    `sexo` varchar(10) NOT NULL,                    # LISTO
    `cedula_padre` int(11) NOT NULL,                # LISTO
    `nombre_padre` varchar(50) NOT NULL,            # LISTO
    `apellido_padre` varchar(50) NOT NULL,          # LISTO
    `cedula_madre` int(11) NOT NULL,                # LISTO
    `nombre_madre` varchar(50) NOT NULL,            # LISTO 
    `apellido_madre` varchar(50) NOT NULL,          # LISTO
    `id_prefectura` int(11) NOT NULL,               # LISTO
    `nombre_registro_civil` varchar(100) NOT NULL,  # LLAVE FORANEA
    `dir_registro_nmbr` varchar(50) NOT NULL,       # LLAVE FORANEA
    `dir_registro_aplld` varchar(50) NOT NULL       # LLAVE FORANEA
  
    """

    nombrepadre = tk.StringVar()

    # NO TOCAR
    
    frameInicio = tk.Frame(root, background = "#209cb4", height = 656, width = 1057)
    frameInicio.place(x = 143, y = 5)
    
    inicioLabel = tk.Label(frameInicio, text = "Formulario Acta De Nacimiento")
    inicioLabel.configure(font = ("roboto", 14, "bold"), fg="#209cb4", background="WHITE")
    inicioLabel.place (x = 420, y = 10)

    # NOMBRES BEBE

    nombresLabel = tk.Label (frameInicio, text = "Nombres: ")
    nombresLabel.configure(font = ("roboto", 12, "bold"), fg="WHITE", background="#209cb4")
    nombresLabel.place (x = 60, y = 90)

    nombresEntry = tk.Entry(frameInicio, relief="flat")
    nombresEntry.place (x = 142, y = 93)
    
    # APELLIDO BEBE

    apellidosLabel = tk.Label (frameInicio, text = "Apellidos: ")
    apellidosLabel.configure(font = ("roboto", 12, "bold"), fg="WHITE", background="#209cb4")
    apellidosLabel.place (x = 60, y = 130)

    apellidosEntry= tk.Entry(frameInicio, relief="flat")
    apellidosEntry.place (x = 142, y = 133)

    # SEXO BEBE

    sexoBebeLabel = tk.Label (frameInicio, text = "Sexo: ")
    sexoBebeLabel.configure (font = ("roboto", 12, "bold"), fg = "WHITE", background = "#209cb4")
    sexoBebeLabel.place (x = 92, y = 170)#x = 100, y = 210
    
    sexoBebeOpcion = ttk.Combobox (frameInicio,values = ["Masculino", "Femenino"],width=17)
    sexoBebeOpcion.place (x = 141,y = 173)#x = 275, y = 213

    # CEDULA PADRE

    cedulaPadreLabel = tk.Label (frameInicio, text = "Cedula Padre: ")
    cedulaPadreLabel.configure(font = ("roboto", 12, "bold"), fg = "WHITE", background = "#209cb4")
    cedulaPadreLabel.place (x = 380, y = 90)

    cedulaPadreEntry = tk.Entry(frameInicio, relief="flat")
    cedulaPadreEntry.place (x = 500, y = 93)

    # NOMBRE PADRE

    nombrePadreLabel = tk.Label (frameInicio, text = "Nombres Padre: ")
    nombrePadreLabel.configure(font = ("roboto", 12, "bold"), fg = "WHITE", background = "#209cb4")
    nombrePadreLabel.place (x = 368, y = 130)

    nombrePadreEntry = tk.Entry(frameInicio, relief="flat", textvariable = nombrepadre)
    nombrePadreEntry.place (x = 500, y = 133)

    # APELLIDO PADRE

    apellidoPadreLabel = tk.Label (frameInicio, text = "Apellidos Padre: ")
    apellidoPadreLabel.configure(font = ("roboto", 12, "bold"), fg = "WHITE", background = "#209cb4")
    apellidoPadreLabel.place (x = 368, y = 170)

    apellidoPadreEntry = tk.Entry(frameInicio, relief="flat")
    apellidoPadreEntry.place (x = 500, y = 173)

    # CEDULA MADRE

    cedulaMadreLabel = tk.Label (frameInicio, text = "Cedula Madre: ")
    cedulaMadreLabel.configure(font = ("roboto", 12, "bold"), fg = "WHITE", background = "#209cb4")
    cedulaMadreLabel.place (x = 700, y = 90)

    cedulaMadreEntry = tk.Entry(frameInicio, relief="flat")
    cedulaMadreEntry.place (x = 820, y = 93)

    # NOMBRE MADRE

    nombreMadreLabel = tk.Label (frameInicio, text = "Nombres Madre: ")
    nombreMadreLabel.configure(font = ("roboto", 12, "bold"), fg = "WHITE", background = "#209cb4")
    nombreMadreLabel.place (x = 685, y = 130)

    nombreMadreEntry = tk.Entry(frameInicio, relief="flat")
    nombreMadreEntry.place (x = 820, y = 133)

    # APELLIDO MADRE

    apellidoMadreLabel = tk.Label (frameInicio, text = "Apellidos Madre: ")
    apellidoMadreLabel.configure(font = ("roboto", 12, "bold"), fg = "WHITE", background = "#209cb4")
    apellidoMadreLabel.place (x = 685, y = 170)

    apellidoMadreEntry = tk.Entry(frameInicio, relief="flat")
    apellidoMadreEntry.place (x = 820, y = 173)

    # FECHA DE NACIMIENTO

    FechaNacimientoLabel = tk.Label (frameInicio, text = "Fecha Nacimiento: ")
    FechaNacimientoLabel.configure(font = ("roboto", 11, "bold"), fg = "WHITE", background = "#209cb4")
    FechaNacimientoLabel.place (x = 7, y = 210)

    FechaNacimientoEntry = tk.Entry(frameInicio, relief="flat")
    FechaNacimientoEntry.place (x = 142, y = 213)

    FormatoHNLabel = tk.Label(frameInicio, text = "Formato (aaaa-mm-dd) ")
    FormatoHNLabel.configure(font = ("roboto", 8, "bold"), fg ="WHITE", background="#209cb4")
    FormatoHNLabel.place (x = 140, y = 233)

    #  UBICACION 

    ubicacionLabel = tk.Label (frameInicio, text = "Lugar Nacimiento: ")
    ubicacionLabel.configure (font = ("roboto", 12, "bold"), fg = "WHITE", background = "#209cb4")
    ubicacionLabel.place (x = 675, y = 210)

    ubicacionEntry = tk.Entry (frameInicio, relief="flat")
    ubicacionEntry.place (x = 820, y = 213)

    # HORA DE NACIMIENTO

    horaNacimientoLabel = tk.Label (frameInicio, text = "Hora Nacimiento: ")
    horaNacimientoLabel.configure(font = ("roboto", 12, "bold"), fg = "WHITE", background = "#209cb4")
    horaNacimientoLabel.place (x = 362, y = 210)

    horaNacimientoEntry = tk.Entry(frameInicio, relief="flat")
    horaNacimientoEntry.place (x = 500, y = 213)

    FormatoHNLabel = tk.Label(frameInicio, text = "Formato (hh:mm:ss) ")
    FormatoHNLabel.configure(font = ("roboto", 8, "bold"), fg ="WHITE", background="#209cb4")
    FormatoHNLabel.place (x = 504, y = 233)

    # PREFECTURAS 
    
    prefecturaLabel = tk.Label (frameInicio, text = "Registro Civil: ")
    prefecturaLabel.configure (font = ("roboto", 12, "bold"), fg = "WHITE", background = "#209cb4")
    prefecturaLabel.place (x = 25, y = 260)#x = 100, y = 240
    
    prefecturaOpcion = ttk.Combobox (frameInicio,values = ["Coquivacoa", "Chiquinquira", "Cacique Mara", "Olegarios Villalobos"],width=17)
    prefecturaOpcion.place (x = 141,y = 263)#x = 275, y = 213

    # BOTON AGREGAR 
    
    botonAgregar = tk.Button (frameInicio, text = "Guardar", height = 1, width = 7,relief="flat",command=lambda: funciones.guardarDatosAcNacimiento(nombresEntry.get(),apellidosEntry.get(),FechaNacimientoEntry.get(),horaNacimientoEntry.get(),sexoBebeOpcion.get(),cedulaPadreEntry.get(), nombrePadreEntry.get(),apellidoPadreEntry.get(),cedulaMadreEntry.get(),nombreMadreEntry.get(),apellidoMadreEntry.get(),ubicacionEntry.get(),prefecturaOpcion.get()))
    botonAgregar.configure (font = ("roboto", 10, "bold"), fg="WHITE", activebackground="#71acb7", activeforeground="WHITE", background="WHITE",foreground="#209cb4")
    botonAgregar.place (x = round(1057/2), y = 300)   

    boton = tk.Button (frameInicio, text = "Guardar", height = 1, width = 7,relief="flat",command=lambda: a.traerDatos())
    boton.configure (font = ("roboto", 10, "bold"), fg="WHITE", activebackground="#71acb7", activeforeground="WHITE", background="WHITE",foreground="#209cb4")
    boton.place (x = round(1057/2), y = 500)  

def cedula ():

    """
        `n_cedula` int(11) NOT NULL COMMENT,       # LISTO
        `acta_nacimiento` int(11) NOT NULL,        # LISTO
        `nombres` varchar(50) NOT NULL,            # LLAVE FORANEA 
        `apellidos` varchar(50) NOT NULL,          # LLAVE FORANEA
        `estado_civil` varchar(20) NOT NULL,       # LISTO
        `sexo` varchar(10) NOT NULL,               # LISTO
        `fecha_emision` date NOT NULL,             # LISTO
        `fecha_vencimiento` date NOT NULL,         # LISTO
        `nacionalidad` varchar(50) NOT NULL        # LISTO
    
    """


    # NO TOCAR

    frameInicio = tk.Frame(root, background = "#209cb4", height = 656, width = 1057)
    frameInicio.place(x = 143, y = 5)
    
    # TITULO 
    
    cedulaLabel = tk.Label(frameInicio, text = "Formulario Cedula")
    cedulaLabel.configure(font = ("roboto", 14, "bold"), fg="#209cb4", background="WHITE")
    cedulaLabel.place (x = 450, y = 10)

    # NUMERO DE ACTA DE NACIMIENTO 

    numActaNacimiento = tk.Label(frameInicio, text = "Numero Acta Nacimiento: ")
    numActaNacimiento.configure(font = ("roboto", 12, "bold"), fg = "WHITE", background = "#209cb4")
    numActaNacimiento.place (x = 18, y = 90)

    numActaNacimientoE = tk.Entry(frameInicio, relief = "flat")
    numActaNacimientoE.place (x = 220, y = 93)
    
    # NUMERO DE CEDULA 
    
    NumCedulaLabel = tk.Label(frameInicio, text = "Numero De Cedula: ")
    NumCedulaLabel.configure(font = ("roboto", 12, "bold"), fg = "WHITE", background = "#209cb4")
    NumCedulaLabel.place (x = 64, y = 127)

    NumCedulaEntry = tk.Entry(frameInicio, relief = "flat")
    NumCedulaEntry.place (x = 220, y = 130)

    # FECHA DE EMISION

    FEmisionLabel = tk.Label (frameInicio, text = "Fecha Emision: ")
    FEmisionLabel.configure (font = ("roboto", 12, "bold"), fg = "WHITE", background = "#209cb4")
    FEmisionLabel.place (x = 400, y = 90)

    FEmisionEntry = tk.Entry(frameInicio, relief = "flat")
    FEmisionEntry.place (x = 525, y = 93)

    FormatoELabel = tk.Label(frameInicio, text = "Formato (aa/mm/dd) ")
    FormatoELabel.configure(font = ("roboto", 8, "bold"), fg = "WHITE", background = "#209cb4")
    FormatoELabel.place (x = 525, y = 70)

    # FECHA DE VENCIMIENTO

    FVencimientoLabel = tk.Label (frameInicio, text = "Fecha Vencimiento: ")
    FVencimientoLabel.configure(font = ("roboto", 10, "bold"), fg = "WHITE", background = "#209cb4")
    FVencimientoLabel.place (x = 392, y = 130)

    FVencimientoEntry = tk.Entry(frameInicio, relief = "flat")
    FVencimientoEntry.place (x = 525, y = 132)

    FormatoELabel = tk.Label(frameInicio, text = "Formato (aa/mm/dd) ")
    FormatoELabel.configure(font = ("roboto", 8, "bold"), fg = "WHITE", background = "#209cb4")
    FormatoELabel.place(x = 529, y = 155)
    
    # ESTADO CIVIL
    
    EdoCivilLabel = tk.Label (frameInicio, text = "Estado Civil: ")
    EdoCivilLabel.configure (font = ("roboto", 12, "bold"), fg = "WHITE", background = "#209cb4")
    EdoCivilLabel.place (x = 725, y = 90)
    
    EdoCivilOpcion = ttk.Combobox (frameInicio,values = ["Soltero/a", "Casado/a", "Divorciado","Viudo/a"])
    EdoCivilOpcion.place(x = 830, y = 92)

    # NACIONALIDAD 

    nacionalidadlLabel = tk.Label (frameInicio, text = "Nacionalidad: ")
    nacionalidadlLabel.configure (font = ("roboto", 12, "bold"), fg = "WHITE", background = "#209cb4")
    nacionalidadlLabel.place (x = 718, y = 130)
    
    nacionalidadOpcion = ttk.Combobox (frameInicio,values = ["Venezolano/a", "Extranjero/a"])
    nacionalidadOpcion.place(x = 830, y = 133)

    #  GENEROS

    generoLabel = tk.Label (frameInicio, text = "Genero: ")
    generoLabel.configure (font = ("roboto", 12, "bold"), fg = "WHITE", background = "#209cb4")
    generoLabel.place (x = 763, y = 170)
    
    generoOpcion = ttk.Combobox (frameInicio,values = ["Hombre", "Mujer", "No-Binario"])
    generoOpcion.place(x = 830, y = 173)
                                                                                                                        #fechaEmision,fechaVencimiento,nacionlidad
    botonAgregarCedula = tk.Button (frameInicio, text = "Guardar", height = 1, width = 7,relief="flat",command=lambda: funciones.guardarCedulaIdentidad(NumCedulaEntry.get(),numActaNacimientoE.get(),EdoCivilOpcion.get()  ,generoOpcion.get(),FEmisionEntry.get(),FVencimientoEntry.get(), nacionalidadOpcion.get()))
    botonAgregarCedula.configure (font = ("roboto", 10, "bold"), fg="WHITE", activebackground="#71acb7", activeforeground="WHITE", background="WHITE",foreground="#209cb4")
    botonAgregarCedula.place (x = round(1057/2), y = 300)

def actaMatrimonio ():

    """
    `nro_acta`                     # AUTO
    `fecha_acta`                   # LISTO
     `id_contrayente1`             # LISTO 
    `nmbr_contrayente1`            # LLAVE FORANEA
    `aplldo_contrayente1`          # LLAVE FORANEA
    `id_contrayente2`              # LISTO
    `nmbr_contrayente2`            # LLAVE FORANEA
    `aplldo_contrayente2`          # LLAVE FORANEA
    `id_registrador_civil`         # LISTO
    `nmbr_registrador`             # LLAVE FORANEA
    `aplldo_registrador`           # LLAVE FORANEA
    `id_testigo1`                  # LISTO
    `nmbr_testigo1`                # LLAVE FORANEA
    `apllido_testigo1`             # LLAVE FORANEA
    `id_testigo2`                  # LISTO
    `nmbr_testigo2`                # # LLAVE FORANEA
    `apllido_testigo2`             # LLAVE FORANEA
    `id_prefectura`                # LISTO
    `nombre_registro_civil`        # LLAVE FORANEA
    `dir_registro_nmbr`            # LLAVE FORANEA
    `dir_registro_aplld`           # LLAVE FORANEA
    
    """

    # NO TOCAR
    
    frameInicio = tk.Frame(root, background = "#209cb4", height = 656, width = 1057)
    frameInicio.place(x = 143, y = 5)

    MatrimonioLabel = tk.Label(frameInicio, text = "Formulario Acta De Matrimonio")
    MatrimonioLabel.configure(font = ("roboto", 14, "bold"), fg="#209cb4", background="WHITE")
    MatrimonioLabel.place (x = 390, y = 10)

    # ---- Contrayentes ------

    # PRIMER CONTRAYENTE

    # CEDULA

    PContrayente = tk.Label (frameInicio, text = "Cedula P Contrayente: ")
    PContrayente.configure(font = ("roboto", 10, "bold"), fg = "WHITE", background="#209cb4")
    PContrayente.place (x = 50, y = 90)
    
    PContrayenteE = tk.Entry(frameInicio, relief="flat")
    PContrayenteE.place (x =200, y = 93)
    
    # OCUPACION PRIMER CONTRAYENTE
    
    OPContrayente = tk.Label (frameInicio, text = "Ocupacion P Contrayente: ")
    OPContrayente.configure(font = ("roboto", 10, "bold"), fg = "WHITE", background = "#209cb4")
    OPContrayente.place (x = 380, y = 90)

    OPContrayenteE = tk.Entry(frameInicio, relief = "flat")
    OPContrayenteE.place (x = 555, y = 93)
    
    # DIRECCION PRIMER CONTRAYENTE
    
    direccionPLabel = tk.Label (frameInicio, text = "Direccion P Contrayente: ")
    direccionPLabel.configure (font = ("roboto", 10, "bold"), fg = "WHITE", background = "#209cb4")
    direccionPLabel.place (x = 735, y = 90)

    direccionPE = tk.Entry(frameInicio, relief = "flat")
    direccionPE.place (x = 900, y = 93)
    
    # SEGUNDO CONTRAYENTE
    
    # CEDULA SEGUNDO CONTRAYENTE

    SContrayente = tk.Label (frameInicio, text = "Cedula S Contrayente: ")
    SContrayente.configure(font = ("roboto", 10, "bold"), fg = "WHITE", background = "#209cb4")
    SContrayente.place (x = 50, y = 130)

    SContrayenteE = tk.Entry(frameInicio, relief = "flat")
    SContrayenteE.place (x = 200, y = 133)

    # OCUPACION SEGUNDO CONTRAYENTE

    OSContrayente = tk.Label (frameInicio, text = "Ocupacion S Contrayente: ")
    OSContrayente.configure (font = ("roboto", 10, "bold"), fg = "WHITE", background = "#209cb4")
    OSContrayente.place (x = 380, y = 130)

    OSContrayenteE = tk.Entry(frameInicio, relief = "flat")
    OSContrayenteE.place (x = 555, y = 133)
    
    # DIRECCION SEGUNDO CONTRAYENTE 
    
    direccionSLabel = tk.Label (frameInicio, text = "Direccion S Contrayente: ")
    direccionSLabel.configure (font = ("roboto", 10, "bold"), fg = "WHITE", background = "#209cb4")
    direccionSLabel.place (x = 735, y = 130)

    direccionSE = tk.Entry(frameInicio, relief = "flat")
    direccionSE.place (x = 900, y = 133)

    # TESTIGO 1
    
    TestigoLabel = tk.Label (frameInicio, text = "Cedula P Testigo: ")
    TestigoLabel.configure (font = ("roboto", 10, "bold"), fg = "WHITE", background = "#209cb4")
    TestigoLabel.place (x = 82, y = 170)

    testigoE = tk.Entry(frameInicio, relief = "flat")
    testigoE.place (x = 200, y = 173)
    
    # TESTIGO 2
    
    TestigoDosLabel = tk.Label (frameInicio, text = "Cedula S Testigo: ")
    TestigoDosLabel.configure (font = ("roboto", 10, "bold"), fg = "WHITE", background = "#209cb4")
    TestigoDosLabel.place (x = 435, y = 170)#x = 425, y = 170

    testigoDosEntry = tk.Entry(frameInicio, relief = "flat")
    testigoDosEntry.place (x = 555, y = 173)#x = 555, y = 173
    
    # REGISTRADOR
    
    registradorLabel = tk.Label (frameInicio, text = "Cedula Registrador: ")
    registradorLabel.configure (font = ("roboto", 10, "bold"), fg = "WHITE", background="#209cb4")
    registradorLabel.place (x = 768, y = 170)
    
    registradorEntry = tk.Entry(frameInicio, relief = "flat")
    registradorEntry.place (x = 900, y = 173)
    
    # FECHA DEL CASAMIENTO
    
    FActaMatrimonioLabel = tk.Label (frameInicio, text = "Fecha Casamiento: ")
    FActaMatrimonioLabel.configure(font = ("roboto", 10, "bold"), fg = "WHITE", background = "#209cb4")
    FActaMatrimonioLabel.place (x = 72, y = 210)

    FActaMatrimonioEntry = tk.Entry(frameInicio, relief = "flat")
    FActaMatrimonioEntry.place (x = 200, y = 213)

    FormatoFLabel = tk.Label(frameInicio, text = "Formato (aa-mm-dd) ")
    FormatoFLabel.configure(font = ("roboto", 8, "bold"), fg = "WHITE", background = "#209cb4")
    FormatoFLabel.place(x = 200, y = 233)
    
    # PREFECTURAS 
    
    prefecturasLabel = tk.Label (frameInicio, text = "Registro Civil: ")
    prefecturasLabel.configure (font = ("roboto", 10, "bold"), fg = "WHITE", background = "#209cb4")
    prefecturasLabel.place (x = 460, y = 210)
    
    prefecturasOpcion = ttk.Combobox (frameInicio,values = ["Coquivacoa", "Chiquinquira", "Cacique Mara", "Oregarios Villalobos"], width=17)
    prefecturasOpcion.place (x = 555,y = 210)
    
    
def actaDivorcio ():

    """
    `conyuge1_apellidos`      # LLAVE FORANEA
    `c_conyuge2`              # LISTO
    `conyuge2_nombres`        # LLAVE FORANEA
    `conyuge2_apellidos`      # LLAVE FORANEA
    `id_ab_conyuge1`          # LISTO
    `nombres_ab_conyuge1`     # LLAVE FORANEA
    `apellidos_ab_conyuge1    # LLAVE FORANEA
    `id_ab_conyuge2`          # LISTO
    `nombres_ab_conyuge2`     # LLAVE FORANEA
    `apellidos_ab_conyuge2`   # LLAVE FORANEA
    `id_hijo1`                # LISTO
    `nombres_hijo1`           # LLAVE FORANEA
    `apellidos_hijo1`         # LLAVE FORANEA
    `id_hijo2`                # LISTO
    `nombres_hijo2`           # LLAVE FORANEA
    `apellidos_hijo2`         # LLAVE FORANEA
    `id_prefectura`           # LISTO
    `nombre_registro_civil`   # LLAVE FORANEA
    `dir_registro_nmbr`       # LLAVE FORANEA
    `dir_registro_aplld       # LLAVE FORANEA
    
    """
    
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
    
    numActaMatrimonioEntry = tk.Entry(frameInicio, relief="flat")
    numActaMatrimonioEntry.place(x=200, y=93)
    
    # PRIMER ESPOSX

    PEsposo = tk.Label (frameInicio, text = "Cedula P Esposo/a: ")
    PEsposo.configure(font = ("roboto", 10, "bold"), fg = "WHITE", background="#209cb4")
    PEsposo.place (x = 70, y = 130)

    PContrayenteE = tk.Entry(frameInicio, relief="flat")
    PContrayenteE.place (x = 200, y = 133)
    
    #SEGUNDX ESPOSX
    
    SEsposo = tk.Label (frameInicio, text = "Cedula S Esposo/a: ")
    SEsposo.configure(font = ("roboto", 10, "bold"), fg = "WHITE", background = "#209cb4")
    SEsposo.place (x = 430, y =130)

    SEsposoE = tk.Entry(frameInicio, relief = "flat")
    SEsposoE.place (x = 560, y = 133)
    
    # DIRECCION PRIMER ESPOSX
    
    DireccionPELabel = tk.Label (frameInicio, text = "Direccion P Esposo/a: ")
    DireccionPELabel.configure(font = ("roboto", 10, "bold"), fg = "WHITE", background = "#209cb4")
    DireccionPELabel.place (x =57, y = 170)

    DireccionPELabeEntry = tk.Entry(frameInicio, relief = "flat")
    DireccionPELabeEntry.place (x = 200, y = 173)
    
    # DIRECCION SEGUNDO ESPOSX

    DireccionSELabeEntry = tk.Label (frameInicio, text = "Direccion S Esposo/a: ")
    DireccionSELabeEntry.configure (font = ("roboto", 10, "bold"), fg = "WHITE", background = "#209cb4")
    DireccionSELabeEntry.place (x = 416, y = 170)

    DireccionSELabeE = tk.Entry(frameInicio, relief = "flat")
    DireccionSELabeE.place (x = 560, y = 173)
    
    #ABOGADO PRIMER ESPOSX
    
    abogadoPLabel = tk.Label (frameInicio, text = "Cedula Abg P Esposo/a: ")
    abogadoPLabel.configure (font = ("roboto", 10, "bold"), fg = "WHITE", background = "#209cb4")
    abogadoPLabel.place (x = 43, y = 210)

    abogadoPE = tk.Entry(frameInicio, relief = "flat")
    abogadoPE.place (x = 200, y = 213)

    # ABOGADO SEGUNDX ESPOSX

    abogadoSLabel = tk.Label (frameInicio, text = "Cedula Abg S Esposo/a: ")
    abogadoSLabel.configure (font = ("roboto", 10, "bold"), fg = "WHITE", background = "#209cb4")
    abogadoSLabel.place (x = 402, y = 210)

    abogadoSE = tk.Entry(frameInicio, relief = "flat")
    abogadoSE.place (x = 560, y = 213)

    # HIJOS
        
    hijoUnoLabel = tk.Label (frameInicio, text = "Acta Nacimiento Hijo/a: ")
    hijoUnoLabel.configure (font = ("roboto", 10, "bold"), fg = "WHITE", background = "#209cb4")
    hijoUnoLabel.place (x = 750, y = 130)

    hijoUnoEntry = tk.Entry(frameInicio, relief = "flat")
    hijoUnoEntry.place (x = 910, y = 133)
    
    hijoDosLabel = tk.Label (frameInicio, text = "Acta Nacimiento Hijo/a: ")
    hijoDosLabel.configure (font = ("roboto", 10, "bold"), fg = "WHITE", background = "#209cb4")
    hijoDosLabel.place (x = 750, y = 170)

    hijoDosEntry = tk.Entry(frameInicio, relief = "flat")
    hijoDosEntry.place (x = 910, y = 173)
    
    # PREFECTURAS 
    
    prefecturasLabel = tk.Label (frameInicio, text = "Registro Civil: ")
    prefecturasLabel.configure (font = ("roboto", 10, "bold"), fg = "WHITE", background = "#209cb4")
    prefecturasLabel.place (x = 813, y = 210)
    
    prefecturasOpcion = ttk.Combobox (frameInicio,values = ["Coquivacoa", "Chiquinquira", "Cacique Mara", "Oregarios Villalobos"], width=17)
    prefecturasOpcion.place (x = 910,y = 210)
    

def actaDefuncion ():

    """
    
    `id_acta_defuncion`         # AUTO
    `a_nacimiento_fallecido     # LISTO
    `fallecido_nombres`         # LLAVE FORANEA
    `fallecido_apellidos`       # LLAVE FORANEA
    `edad_fallecido`            # LLAVE FORANEA
    `sexo_fallecido`            # LLAVE FORANEA
    `estado_civil_f`            # LISTO
    `fecha_defuncion`           # LISTO
    `hora_defuncion`            # LISTO
    `lugar_defuncion`           # LISTO
    `causa_muerte`              # LISTO
    `c_informante`              # LISTO
    `informante_nombre`         # LLAVE FORANEA
    `informante_apellido`       # LLAVE FORANEA
    `relacion_informante`       # LISTO
    `madre_nombres`             # LLAVE FORANEA
    `madre_apellidos`           # LLAVE FORANEA
    `padre_nombres`             # LLAVE FORANEA
    `padre_apellidos`           # LLAVE FORANEA
    
    """

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

    difuntoEntry = tk.Entry(frameInicio, relief = "flat")
    difuntoEntry.place (x = 225, y = 94)

    # CAUSA DE MUELTE

    CMuerteLabel = tk.Label (frameInicio, text = "Causa De Muerte: ")
    CMuerteLabel.configure (font = ("roboto", 12, "bold"), fg = "WHITE", background = "#209cb4")
    CMuerteLabel.place (x = 410, y = 90)

    CMuerteEntry = tk.Entry(frameInicio, relief = "flat")
    CMuerteEntry.place (x = 555, y = 93)

    # LUGAR DE MUELTE

    LMuerteLabel = tk.Label (frameInicio, text = "Lugar De Defuncion: ")
    LMuerteLabel.configure (font = ("roboto", 12, "bold"), fg = "WHITE", background = "#209cb4")
    LMuerteLabel.place (x = 735, y = 90)

    LMuerteEntry = tk.Entry(frameInicio, relief = "flat")
    LMuerteEntry.place (x = 900, y = 93)

    # INFORMANTE

    informanteLabel = tk.Label (frameInicio, text = "Cedula Informante: ")
    informanteLabel.configure(font = ("roboto", 12, "bold"), fg = "WHITE", background = "#209cb4")
    informanteLabel.place (x = 73, y = 130)

    informanteEntry = tk.Entry(frameInicio, relief = "flat")
    informanteEntry.place (x = 225, y = 133)

    # RELACION INFORMANTE
    
    RInformanteLabel = tk.Label (frameInicio, text = "Relacion Informante: ")
    RInformanteLabel.configure (font = ("roboto", 10, "bold"), fg = "WHITE", background = "#209cb4")
    RInformanteLabel.place (x = 413, y = 130)

    RInformanteEntry = tk.Entry(frameInicio, relief = "flat")
    RInformanteEntry.place (x = 555, y = 133)

    # FECHA DE DEFUNCION

    FMuerteLabel = tk.Label (frameInicio, text = "Fecha Defuncion: ")
    FMuerteLabel.configure (font = ("roboto", 12, "bold"), fg = "WHITE", background = "#209cb4")
    FMuerteLabel.place (x = 760, y = 130)

    FMuerteEntry = tk.Entry(frameInicio, relief = "flat")
    FMuerteEntry.place (x = 900, y = 133)

    FormatoMuLabel = tk.Label(frameInicio, text = "Formato (aa-mm-dd) ")
    FormatoMuLabel.configure(font = ("roboto", 8, "bold"), fg ="WHITE", background="#209cb4")
    FormatoMuLabel.place (x = 902, y = 153)
    
    # ESTADO CIVIL DEL MUELTO
    
    EdoCivilMLabel = tk.Label (frameInicio, text = "Estado Civil Difunto: ")
    EdoCivilMLabel.configure (font = ("roboto", 12, "bold"), fg = "WHITE", background = "#209cb4")
    EdoCivilMLabel.place (x = 62, y =170)
    
    EdoCivilMOpcion = ttk.Combobox (frameInicio,values = ["Soltero/a", "Casado/a", "Divorciado","Viudo/a"],width=17)
    EdoCivilMOpcion.place(x = 225, y = 173)

    # HORA DE DEFUNCION

    HMuerteLabel = tk.Label (frameInicio, text = "Hora De Defuncion: ")
    HMuerteLabel.configure (font = ("roboto", 12, "bold"), fg = "WHITE", background = "#209cb4")
    HMuerteLabel.place (x = 743, y = 180)

    HMuerteEntry = tk.Entry(frameInicio, relief = "flat")
    HMuerteEntry.place (x = 900, y = 183)

    FormatoHLabel = tk.Label(frameInicio, text = "Formato (hh:mm:ss) ")
    FormatoHLabel.configure(font = ("roboto", 8, "bold"), fg ="WHITE", background="#209cb4")
    FormatoHLabel.place (x = 902, y = 203)
  
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

