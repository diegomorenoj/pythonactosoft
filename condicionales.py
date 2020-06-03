# Dame tu calificación y te dire si aprobaste o no

nombre = input("¿Cómo te llamas? ")
nota = float(input("Escribe tu nota "))

if nota >= 6:
    print("Felicidades ", nombre, " Aprobaste")
else:
    print("Lo sentimos ", nombre, " No aprobaste :(")