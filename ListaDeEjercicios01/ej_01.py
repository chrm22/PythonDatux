nombres = input("Ingrese sus nombres: ")
apellidos = input("Ingrese sus apellidos: ")
edad = int(input("Ingrese su edad: "))

print("Nombres y apellidos: " + nombres + ' ' + apellidos)
print(f"Edad: {edad} años")

"""
Otras formas:
print("Edad: "+str(edad)+" años")
print("Edad: {} años".format(edad))

"""