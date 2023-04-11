from tkinter import messagebox as MessageBox
from tkinter import *
from DBC import DAO

consul = DAO()    

# CONSULTA VERIFICAR DATOS

def verificarCedula (numCedula):
    
    a = 0     
    
    cedulas = consul.consultaVCedula()
    
    b = len(cedulas)

    for x in cedulas:
         
        if numCedula == x[0]:
             
            MessageBox.showwarning("Registro Civil", "- Haz colocado una cedula ya ingresada\n\n       Corrige y vuelve a intentarlo.")
              
            return False
              
        if a == (b-1):
            
            return True

        a = a + 1

def verificarActaNacimiento(numActaN):
     
    a = 0     
    
    acta = consul.consultaVActaNacimiento()
    
    b = len(acta)

    for x in acta:
         
        if numActaN == x[0]:
             
            MessageBox.showwarning("Registro Civil", "- Haz colocado un acta de nacimiento ya ingresada\n\n       Corrige y vuelve a intentarlo.")
              
            return False
              
        if a == (b - 1):
            
            return True

        a = a + 1

def cedulaExiste (cedula):
     
    a = 0     
    
    cedulas = consul.consultaVCedula()
    
    b = len(cedulas)

    for x in cedulas:
         
        if cedula == x[0]:
               
            return True
              
        if a == (b-1):

            return False

        a = a + 1

def actaNacimientoExiste (numActaNa):
    
    a = 0     
    
    numActaN = consul.consultaVActaNacimiento()
    
    b = len(numActaN)

    for x in numActaN:
         
        if numActaNa == x[0]:
               
            return True
              
        if a == (b-1):
            
            MessageBox.showwarning("Registro Civil", "El numero de acta no existe, revise y vuelva a intentar")

            return False

        a = a + 1

def VerificarActaMatrimonio(actaMatrimonio):
     
    a = 0     
    
    numActaM = consul.consultaVActaMatrimonio()
    print(numActaM)
    b = len(numActaM)

    for x in numActaM:
         
        if actaMatrimonio == x[0]:

            MessageBox.showwarning("Datos Incompletos","- Este Numero de acta ya se le realizó el divoricio, intente con otro.")

            return False
              
        if a == (b-1):
    
            return True

        a = a + 1

def actaMatrimonioExiste(num):
    a = 0     
    
    numActa = consul.consultaVActaMatrimonio()
    
    b = len(numActa)

    for x in numActa:
         
        if num == x[0]:
            
            return True
              
        if a == (b-1):

            MessageBox.showwarning("Datos Incompletos", "- El numero de acta no existe, revise y vuelva a intentarlo.")

            return False

        a = a + 1

# GUARDAR DATOS

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
        
        # VERIFICAMOS SI NO SE COLOCA LA MISMA CEDULA EN AMBOS CAMPOS DE CEDULA
        
        if flag == True:
             
            if cedulaPadre == cedulaMadre:
                 
                MessageBox.showwarning("Datos Incompletos", "No debes colocar la misma cedula en los campos Cedula Padre y Cedula Madre\n\n Revisa y vuelve a intentarlo.")
                
                flag = False 
 
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
        
        # VERIFICAMOS SI LA CEDULA YA FUE INGRESADA

        if flag == True:
             
            flag = verificarCedula(numCedula)

        # ACOMODAMOS LOS NOMBRES Y APELLIDOS

        if flag == True:
             
             nombres = nombres.title()
             apellidos = apellidos.title()

        # ACOMODAMOS FECHA

        if flag == True:

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

                # VERIFICAMOS GENERO
        
        # VERIFICAMOS GENERO

        if flag == True:

            if sexo == "Hombre" or sexo == "Mujer" or sexo == "No-Binario":
                 
                flag = True

            else:
             
                MessageBox.showwarning("Registro Civil","- Haz ingresado un genero incorrecto\n\nVerifica e intenta de nuevo")

        # VERIFICAMOS ESTADO CIVIL

        if flag == True:

            if estadoCivil == "Soltero/a" or estadoCivil == "Casado/a" or estadoCivil == "Divorciado" or estadoCivil == "Viudo/a":
                 
                flag = True

            else:
             
                MessageBox.showwarning("Registro Civil","- Haz ingresado un estado civil incorrecto\n\nVerifica e intenta de nuevo")

        # VERIFICAMOS NACIONALIDAD

        if flag == True:

            if nacionlidad == "Venezolano/a" or nacionlidad == "Extranjero/a":
                 
                flag = True

            else:
             
                MessageBox.showwarning("Registro Civil","- Haz ingresado un estado civil incorrecto\n\nVerifica e intenta de nuevo")

        # INGRESAMOS DATOS

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
                
                MessageBox.showwarning("Registo Civil","- Debes ingresar valores numericos en los campos: \n\n Cedula P contrayente \nCedula S Contrayente \n Cedula Registrador Civil \nPrimer Testigo \nSegundo Testigo")
                flag = False

        # VERIFICAMOS CEDULAS INGRESADAS

        if flag == True:
            
            # VERIFICAMOS SI EXISTE LA CEDULA DEL PRIMER CONTRAYENTE

            flag = cedulaExiste(Pcontrayente)

            if flag == True:
                
                # VERIFICAMOS SI EXTISTE LA CEDULA DEL SEGUNDO CONTRAYENTE

                flag = cedulaExiste(SContrayente)

                if flag == True:

                    # VERIFICAMOS SI EXISTE LA CEDULA DEL REGISTRADOR CIVIL

                    flag = cedulaExiste(registradorCivil)

                    if flag == True:
                        
                        # VERIFICAMOS SI EXISTE LA CEDULA DEL PRIMER TESTIGO

                        flag = cedulaExiste (PTestigo)

                        if flag == True:
                            
                             # VERIFICAMOS SI EXISTE LA CEDULA DEL SEGUNDO TESTIGO

                            flag = cedulaExiste (STestigo)

                            if flag == False:
                                 
                                MessageBox.showwarning("Registo Civil","- La cedula del segundo testigo no existe.\n\n Debes ingresarla antes de realizar el acta de matrimonio.")

                        else:

                             MessageBox.showwarning("Registo Civil","- La cedula del primer testigo no existe.\n\n Debes ingresarla antes de realizar el acta de matrimonio.") 
                    
                    else:
                         
                        MessageBox.showwarning("Registo Civil","- La cedula del registrador civil no existe.\n\n Debes ingresarla antes de realizar el acta de matrimonio.")

                else:

                    MessageBox.showwarning("Registo Civil","- La cedula del segundo contrayente no existe.\n\n Debes ingresarla antes de realizar el acta de matrimonio.")

            else:
                 
                MessageBox.showwarning("Registo Civil","- La cedula del primer primer contrayente no existe.\n\n Debes ingresarla antes de realizar el acta de matrimonio.")
 
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

        # VERIFICAMOS SI EL ACTA DE MATRIMONIO EXISTE

        if flag == True:

            flag = actaMatrimonioExiste(Id_acta_matrimonio) 

        # VERIFICAMOS SI EL ACTA DE MATRIMONIO YA SE INGRESO

        if flag == True:
            
            flag = VerificarActaMatrimonio(Id_acta_matrimonio)

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
                
                MessageBox.showwarning("Registro Civil","Debes ingresar un valor numerico en los campos: \n- Cedula Padre\n- Cedula Madre\n\n- Intentelo Nuevamente")
                
                flag =False 

        # VERIFICAMOS QUE LAS CEDULAS ESTEN BIEN

        if flag == True:
             
            flag = cedulaExiste(c_conyuge1) 

            if flag == True:
                 
                flag = cedulaExiste(c_conyuge2)
                
                if flag == True:
                     
                    flag = cedulaExiste(id_ab_conyuge1)

                    if flag == True:
                       
                       flag = cedulaExiste(id_ab_conyuge2)

                       if flag == False:
                        
                        MessageBox.showwarning("Registo Civil","- La cedula del abodado segundo Esposx no existe.\n\n Debes ingresarla antes de realizar el acta de divorcio.")
                    
                    else:
                
                        MessageBox.showwarning("Registo Civil","- La cedula del abogado primer Esposx no existe.\n\n Debes ingresarla antes de realizar el acta de divorcio.")
                
                else:

                    MessageBox.showwarning("Registo Civil","- La cedula del segundo Esposx no existe.\n\n Debes ingresarla antes de realizar el acta de divorcio.")

            else:

                MessageBox.showwarning("Registo Civil","- La cedula del primer Esposx no existe.\n\n Debes ingresarla antes de realizar el acta de divorcio.")

        # VERIFICAMOS QUE LAS ACTAS DE NACIMIENTO ESTEN BIEN

        if flag == True:
             
            flag = actaNacimientoExiste(id_hijo1)

            if flag == True:
                 
                flag = actaNacimientoExiste(id_hijo2)

                if flag == False:
                     
                    MessageBox.showwarning("Registo Civil","- El acta de nacimiento del segundo hijo no existe.\n\n Debes ingresarla antes de realizar el acta de divorcio.")

            else:
                 
                MessageBox.showwarning("Registo Civil","- El acta de nacimiento del primer hijo no existe.\n\n Debes ingresarla antes de realizar el acta de divorcio.")

        # ESCOGEMOS LA PREFECTURA ID

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


        #VERIFICAMOS SI EL ACTA EXISTE

        if flag == True:
             
            flag = actaNacimientoExiste(a_nacimiento_fallecido)

            if flag == False:
                 
                MessageBox.showwarning("Datos Incompletos","- El acta de nacimiento que se ingresó no existe\n\n Verifique el acta e intente de nuevo")
                 
        # VERIFICAMOS SI EL LA CEDULA DEL TESTIGO EXSISTE

        if flag == True:
             
             flag= cedulaExiste(c_informante)

             if flag == False:
                  
                  MessageBox.showwarning("Datos Incompletos","- El acta del testigo que se ingresó no existe\n\n Verifique el acta e intente de nuevo")

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

def consultarActaDivorcio ():
     
    dato = consul.consultarActaDivorcio()

    return dato

def consultarActaDeuncion():

    dato = consul.consultarAD()

    return dato

# ACTUALIZAR DATOS

def actualizarActaNacimiento (nombre, apellido, FechaNacimiento, horaNacimiento, lugarNacimiento, sexo, cedulaPadre, nombrePadre, apellidoPadre, cedulaMadre, nombreMadre, apellidoMadre,  prefectura, numActa):
    
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
        
        # VERIFICAMOS SI NO SE COLOCA LA MISMA CEDULA EN AMBOS CAMPOS DE CEDULA
        
        if flag == True:
             
            if cedulaPadre == cedulaMadre:
                 
                MessageBox.showwarning("Datos Incompletos", "No debes colocar la misma cedula en los campos Cedula Padre y Cedula Madre\n\n Revisa y vuelve a intentarlo.")
                
                flag = False 
 
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
            
            datosActaNacimiento = [nombre, apellido, FechaNacimiento, horaNacimiento, lugarNacimiento, sexo, cedulaPadre, nombrePadre, apellidoPadre, cedulaMadre, nombreMadre, apellidoMadre,  prefectura, numActa]

            consul.actaNacimientoUpdate(datosActaNacimiento)

            MessageBox.showinfo(message = "Se ha actualizado el registro satisfactoriamente.", title = "Registro Civil")

def actualizarCedula (numCedula,numActaNacimiento,nombres,apellidos,estadoCivil,sexo,fechaEmision,nacionlidad):
     
    flag = True
    
    # VERIFICAMOS SI LOS DATOS IMPORTANTES SE INGRESARON

    if numCedula == "" or numActaNacimiento== "" or estadoCivil== "" or sexo == ""  or fechaEmision == ""  or nacionlidad == "":
 
        MessageBox.showwarning("Registro Civil","Debes ingresar un valor numerico en los campos: \n- Numero Acta Nacimiento\n- Numero Cedula\n- Fecha Emision\n- Fecha Vencimiento\n- Estado Civil\n- Nacionalidad\n- Genero\n\n- Intentelo Nuevamente")

    else: 

        # VERIFICAMOS SI LA CEDULA YA FUE INGRESADA

        if flag == True:
             
            flag = cedulaExiste(numCedula)

            if flag == False:
                  
                  MessageBox.showwarning("Registro Civil","- La cedula Ingresada para actualizar los datos no existe \n\n    Verifique e intente de nuevo")

        # VERIFICAMOS SI EL ACTA DE NACIMIENTO FUE INGRESADO

        if flag == True:
             
            flag = actaNacimientoExiste(numActaNacimiento)

            if flag == False:

                MessageBox.showwarning("Registro Civil","- El acta de nacimiento ingresado no existe\n\n    Verifique e intente de nuevo")

        # ACOMODAMOS LOS NOMBRES Y APELLIDOS

        if flag == True:
             
             nombres = nombres.title()
             apellidos = apellidos.title()

        # ACOMODAMOS FECHA

        if flag == True:

            dia = fechaEmision[0:2]
            mes = fechaEmision[3:5]
            anio = fechaEmision[6:10]

            fechaEmision = anio + "-" + mes +"-"+ dia
    
            try:
                    
                dia = int (dia)
                mes = int (mes)
                anio = int (anio)

                anio = anio + 10

                fechaVencimiento = str(anio) + "-" + str (mes)+ "-" + str (dia)

            except ValueError:
                    
                MessageBox.showwarning("Registro Civil","-El formato que ha ingresado es incorrecto, debe ingresar la fecha en el formato: \n\n             DD-MM-AAAA\n\n- Intentelo Nuevamente")
                    
                flag = False

        # VERIFICAMOS GENERO
        
        if flag == True:

            if sexo == "Hombre" or sexo == "Mujer" or sexo == "No-Binario":
                 
                flag = True

            else:
             
                MessageBox.showwarning("Registro Civil","- Haz ingresado un genero incorrecto\n\nVerifica e intenta de nuevo")

        # VERIFICAMOS ESTADO CIVIL

        if flag == True:

            if estadoCivil == "Soltero/a" or estadoCivil == "Casado/a" or estadoCivil == "Divorciado" or estadoCivil == "Viudo/a":
                 
                flag = True

            else:
             
                MessageBox.showwarning("Registro Civil","- Haz ingresado un estado civil incorrecto\n\nVerifica e intenta de nuevo")

        # VERIFICAMOS NACIONALIDAD

        if flag == True:

            if nacionlidad == "Venezolano/a" or nacionlidad == "Extranjero/a":
                 
                flag = True

            else:
             
                MessageBox.showwarning("Registro Civil","- Haz ingresado un estado civil incorrecto\n\nVerifica e intenta de nuevo")
        

        # INGRESAMOS DATOS

        if flag == True:


                datosCedula = [numCedula,numActaNacimiento, nombres,apellidos, estadoCivil, sexo, fechaEmision, fechaVencimiento, nacionlidad]
            
                consul.insertarCedula (datosCedula)
                    
                MessageBox.showinfo(message = "Resgistro Creado satisfactoriamente.", title = "Registro Civil")
     
