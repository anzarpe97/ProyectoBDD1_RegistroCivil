import datetime

fecha_nacimiento = input("Introduce tu fecha de nacimiento (YYYY-MM-DD): ")

fecha_nacimiento = datetime.datetime.strptime(fecha_nacimiento, '%Y-%m-%d')

edad = datetime.datetime.now().year - fecha_nacimiento.year


print("Tu edad es:", edad)