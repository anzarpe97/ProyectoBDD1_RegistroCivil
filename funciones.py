

def imprimir_datos (nombre,apellido,CPadre,CMadre,sexo,ubicacion):
    
    # Acomodar Nombres

    nombreF = nombre.title()
    apellidoF = apellido.title()

    c = CPadre
    d = CMadre

    e = nombreF + " " + apellidoF

    print (e + " " + str(c) + " " + str(d))

    print(sexo)

