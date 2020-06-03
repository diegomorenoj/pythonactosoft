edad = int(input("Escribe tu edad: "))

if edad >= 18 or edad <= 23:
    print("Estas en la universidad")
elif edad > 23:
    print("Eres un profesional")
else:
    print("No sé en que nivel academico estás")