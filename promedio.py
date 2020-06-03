alumno = input("¿Cómo te llamas? ")
asignatura_1 = float(input("Escribe tu primer calificación "))
asignatura_2 = float(input("Escribe tu segunda calificación "))
asignatura_3 = float(input("Escribe tu tercera calificación "))
promedio = (asignatura_1 + asignatura_2 + asignatura_3) / 3

if promedio >= 7:
    print("Felicidades ", alumno, " aprobaste, tu nota es de ", promedio)
else:
    print("Lo sentimos ", alumno, " No aprobaste, tu nota es de ", promedio)