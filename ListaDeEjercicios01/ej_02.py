def AreaCirculo():
    pi=3.14
    radio=int(input("\nIngrese el radio del círculo: "))
    area=pi*radio*radio
    print("El área del círculo de radio " + str(radio) + " es " + str(area))

def AreaTriangulo():
    base=int(input("\nIngrese la longitud de la base del triángulo: "))
    altura=int(input("Ingrese la longitud de la altura del triángulo: "))
    area=0.5*base*altura
    print("El área del triángulo de base " + str(base) + " y altura " + str(altura) + " es " + str(area))

def AreaCuadrado():
    lado=int(input("\nIngrese el lado del cuadrado: "))
    area=lado*lado
    print("El área del cuadrado de lado " + str(lado) + " es " + str(area))

op=0
while (op != 4):
    print("\nMenú")
    print("1. Calcular área del círculo según radio")
    print("2. Calcular área del triángulo según base y altura")
    print("3. Calcular área del cuadrado según lado")
    print("4. Salir\n")
    op = int(input("Ingrese una opción: "))
    if (op != 4):
        if (op == 1):
            AreaCirculo()
        if (op == 2):
            AreaTriangulo()
        if (op == 3):
            AreaCuadrado()
print("\nEjecución finalizada\n")
