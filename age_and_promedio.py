edad = int(input("Escribe tu edad: "))

if edad > 0:
    if edad < 12:
        print("Estas en la escuela")
    elif edad >= 12 and edad <= 18:
        print("Estas en secundaria")
    elif edad > 18 and < edad 23:
        print("Estas en la universidad")
    elif edad > 23:
        print("Eres un profesional")
    else:
        print("No naciste")