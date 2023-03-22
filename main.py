import tkinter as tk

root = tk.Tk()

# Configuracion Ventana

root.geometry("1200x666")
root.title("Registro Civil")
root.iconbitmap("Images/Pen.ico")
root.config(background="#ADAAAB")
root.resizable(0,0)

# Imagenes Botones

nacimientoPhoto = tk.PhotoImage(file="Images/ImagenesBotones/chupete.png")
nacimientoImage = nacimientoPhoto.subsample(1, 1)

cedulaPhoto = tk.PhotoImage(file="Images/ImagenesBotones/cedula.png")
cedulaImage = cedulaPhoto.subsample(1, 1)

matrimonioPhoto = tk.PhotoImage(file="Images/ImagenesBotones/Anillo SVG.png")
matrimonioImage = matrimonioPhoto.subsample(3, 3)

divorcioPhoto = tk.PhotoImage(file="Images/ImagenesBotones/a.png")
divorcioImage = divorcioPhoto.subsample(3, 3)

defuncionPhoto = tk.PhotoImage(file="Images/ImagenesBotones/MuelteChikita.png")
defuncionImage = defuncionPhoto.subsample(1, 1)

# Botones

buttonActaNacimiento = tk.Button (root, text="\nActa\nde\nNacimiento",image = nacimientoImage,compound = tk.TOP, background= "WHITE")
buttonActaNacimiento.config(height = 125, width = 130, font=("DM Sans", 10, "bold"))
buttonActaNacimiento.grid(row=0,column =0)

buttonCedula = tk.Button (root, text="\nCedula",image = cedulaImage,compound = tk.TOP,background= "WHITE")
buttonCedula.config(height = 125, width = 130, font=("Comfortaa", 10, "bold"))
buttonCedula.grid(row=1,column =0)

buttonActaMatrimonio = tk.Button (root, text="\nActa\nde\nMatrimonio",image = matrimonioImage,compound = tk.TOP, background= "WHITE")
buttonActaMatrimonio.config(height = 125, width = 130, font=("Garet Book", 10, "bold"))
buttonActaMatrimonio.grid(row=2,column =0)

buttonActaDivorcio = tk.Button (root, text="\nActa \nde\nDivorcio", image = divorcioImage,compound = tk.TOP,background= "WHITE")
buttonActaDivorcio.config(height = 125, width = 130, font=("nunito", 10, "bold"))
buttonActaDivorcio.grid(row=3,column =0)

buttonActaDefuncion = tk.Button (root, text="\nActa \nde\nDefuncion", image = defuncionImage,compound = tk.TOP, relief= tk.FLAT, background= "WHITE")
buttonActaDefuncion.configure(height = 125, width = 130, font=("Rubik", 10, "normal"))
buttonActaDefuncion.grid(row = 4,column = 0)

root.mainloop()