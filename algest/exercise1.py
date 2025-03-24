name = input("Introduce tu nombre: ")
edad = int(input("Introduce tu edad: "))
if edad >= 0 and edad < 12:
    print("Eres un niño")
elif edad >= 12 and edad < 18:
    print("Eres un adolescente")
elif edad >= 18 and edad < 60:
    print("Eres un adulto")
elif edad >= 60:
    print("Eres un adulto mayor")
else:
    print("Edad no válida")