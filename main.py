import tkinter as tk

root = tk.Tk()

# Configuracion Ventana

root.geometry("1200x650")
root.title("Registro Civil")
root.iconbitmap("Images/pen.ico")
root.config(background="White")
root.resizable(0,0)

# Imagenes Botones

nacimientoPhoto = tk.PhotoImage(file="Images/ImagenesBotones/chupete.png")
nacimientoImage = nacimientoPhoto.subsample(1, 1)

cedulaPhoto = tk.PhotoImage(file="Images/ImagenesBotones/cedula.png")
cedulaImage = cedulaPhoto.subsample(1, 1)

matrimonioPhoto = tk.PhotoImage(file="Images/ImagenesBotones/Anillo SVG.png")
matrimonioImage = matrimonioPhoto.subsample(3, 3)

divorcioPhoto = tk.PhotoImage(file="Images/ImagenesBotones/broken.png")
divorcioImage = divorcioPhoto.subsample(1, 1)

defuncionPhoto = tk.PhotoImage(file="Images/ImagenesBotones/MuelteChikita.png")
defuncionImage = defuncionPhoto.subsample(1, 1)

# Botones

buttonActaNacimiento = tk.Button (root, text="\nActa \nde Nacimiento",image = nacimientoImage,compound = tk.TOP)
buttonActaNacimiento.config(height = 125, width = 130)
buttonActaNacimiento.grid(row=0,column =0)

buttonCedula = tk.Button (root, text="Cedula",image = cedulaImage,compound = tk.TOP)
buttonCedula.config(height = 125, width = 130)
buttonCedula.grid(row=1,column =0)

buttonActaMatrimonio = tk.Button (root, text="Acta\nde Matrimonio",image = matrimonioImage,compound = tk.TOP)
buttonActaMatrimonio.config(height = 125, width = 130)
buttonActaMatrimonio.grid(row=2,column =0)

buttonActaDivorcio = tk.Button (root, text="Acta \nde Divorcio", image = divorcioImage,compound = tk.TOP)
buttonActaDivorcio.config(height = 125, width = 130)
buttonActaDivorcio.grid(row=3,column =0)

buttonActaDefuncion = tk.Button (root, text="\nActa \nde Defuncion", image = defuncionImage,compound = tk.TOP, relief= tk.FLAT, background= "Blue")
buttonActaDefuncion.config(height = 125, width = 130)
buttonActaDefuncion.grid(row=4,column =0)

#dollarPhoto = PhotoImage(file="Dolar.png")
#dollarimage = dollarPhoto.subsample(7, 7)
#callButton = Button(menuFrame, text= "Dolares",image = dollarimage, height = 150, width = 120,compound = TOP,background="WHITE").grid(row = 0, column = 0)

root.mainloop()