password=input("Ingrese una contraseña: ")
password1=input("Vuelva a ingresar la contraseña: ")

# No serán consideradas las mayúsculas y minúsculas
if (password.upper()==password1.upper()):
    print("Las contraseñas coinciden.")
else:
    print("Las contraseñas no coinciden.")