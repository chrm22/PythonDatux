# Lo trabajé de esta manera porque la función input() devuelve siempre una cadena

var1="Hola mundo"
var2=16
var3=3.1416
var4=True

op=0
while (op != 5):
    print("\nMenú")
    print("1. Ver tipo de la variable var1 = " + var1)
    print("2. Ver tipo de la variable var2 = " + str(var2))
    print("3. Ver tipo de la variable var3 = " + str(var3))
    print("4. Ver tipo de la variable var4 = " + str(var4))
    print("5. Salir\n")
    op = int(input("Ingrese una opción: "))
    if (op != 5):
        if (op == 1):
            print("La variable var1 es del tipo " + str(type(var1)))
        if (op == 2):
            print("La variable var2 es del tipo " + str(type(var2)))
        if (op == 3):
            print("La variable var3 es del tipo " + str(type(var3)))
        if (op == 4):
            print("La variable var4 es del tipo " + str(type(var4)))
print("\nEjecución finalizada\n")