def DibujarCuadrado(_num):
    print('\n')
    for i in range(_num):
        for j in range(_num):
            print('*',end="   ")
        print('\n')
    print('\n')

op=0
listaNumeros=[89,22,36,-4,37,8,504,100,93]
listaPersonas=[["Gabriela",17],["Camila",19],["Gianmarco",28],["Ernesto",12],["Marco",5],["Flor",59]]
while op!=4:
    while True:
        print("= = = = M E N Ú = = = =")
        print("Opciones:\n[1]\n[2]\n[3]\n[4] Salir")
        try:
            op=int(input("Seleccione una opción: "))
        except:
            op=-1
        else:
            break
    if op!=4:
        print('\n')
        match op:
            case 1:
                while True:
                    try:
                        num=int(input("Ingrese el tamaño del cuadrado (1 - 8): "))
                    except:
                        num=-1
                    if num>=1 and num<=8:
                        break
                    else:
                        print("Valor ingresado inválido.")
                DibujarCuadrado(num)
            case 2:
                pos=0
                print("La lista original es:",listaNumeros)
                print("Los números de la lista que son múltiplos de 2 son: ",end="")
                for i in range(2):
                    if i==0:
                        for j in range(len(listaNumeros)):
                            if listaNumeros[j]%2==0:
                                pos=j # Guardar la posición del último número múltiplo de 2
                    else:
                        for j in range(len(listaNumeros)):
                            if listaNumeros[j]%2==0:
                                if j+1<pos:
                                    print(listaNumeros[j],end=", ")
                                elif j+1==pos:
                                    print(listaNumeros[j],end=" y ")
                                else:
                                    print(listaNumeros[j])
                print('\n')
            case 3:
                pos=0
                print("La lista de personas mayores de edad son:")
                for i in range(len(listaPersonas)):
                    if listaPersonas[i][1]>=18:
                        print(f"Nombre: {listaPersonas[i][0]}, edad: {listaPersonas[i][1]} años")
                print('\n')
            case _:
                print("Opción inválida.\n")
    else:
        print("Ejecución finalizada.")