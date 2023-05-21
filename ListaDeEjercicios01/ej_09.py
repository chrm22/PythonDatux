listaPython=[]
listaSQL=[]
listaPowerBI=[]

op=0
print("\nMenú")
print("1. Añadir a lista de Python")
print("2. Añadir a lista de SQL")
print("3. Añadir a lista de PowerBI")
op = int(input("Ingrese una opción: "))
match op:
    case 1:
        listaPython.append(input("Ingrese el objeto a añadir a la lista de Python: "))
    case 2:
        listaSQL.append(input("Ingrese el objeto a añadir a la lista de SQL: "))
    case 3:
        listaPowerBI.append(input("Ingrese el objeto a añadir a la lista de PowerBI: "))
    case _:
        print("La opción ingresada no es válida.")
print("Elementos de la lista de Python: ",listaPython)
print("Elementos de la lista de SQL: ",listaSQL)
print("Elementos de la lista de PowerBI: ",listaPowerBI)

# Solo se ejecuta una vez