import string
import random

while True:
    

    largo = int(input("Introdusca la caracteristica minima de su contraseña: "))

    caracteres = string.ascii_letters + string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

    contraseña = "".join(random.choice(caracteres)for _ in range(largo))
    print(f"Un viejo sabio dice que: {contraseña} Es tu contraseña")

    opcion = input("¿Quieres generar otra contraseña? (s/n): ")
    if opcion.lower() != "s":
        print("¡El mago dice adios!")
        break