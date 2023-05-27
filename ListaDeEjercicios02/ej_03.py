posNum=.0
numeros=[0,0]

def MayorNumero(_num1, _num2):
    # Retorna la posición del mayor número, y si no hay, retorna -1
    if _num1!=_num2:
        if _num1>_num2:
            return 0
        else:
            return 1
    else:
        return -1

for i in range(2):
    while True:
        try:
            numeros[i]=float(input(f"Ingrese el {i+1}° número: "))
        except:
            print("Valor ingresado no válido.")
        else:
            break

posNum=MayorNumero(numeros[0],numeros[1])

if posNum!=-1:
    print(f"El {posNum+1}° número ({numeros[posNum]}) es el mayor.")
else:
    print("Los dos números son iguales.")