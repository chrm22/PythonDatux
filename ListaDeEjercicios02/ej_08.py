def IngresarNumero(_texto):
    while True:
        try:
            _num=int(input(_texto))
        except:
            print("ERROR: Tipo de dato ingresado no válido.")
        else:
            break
    return _num

inicioRango=-1
finRango=-1
step=-1

while inicioRango<0 or inicioRango>10**5-1:
    inicioRango=IngresarNumero("Ingrese el valor de inicio del rango: ")
    if inicioRango<0:
        print("ERROR: el valor de inicio del rango debe ser mayor o igual a 0.")
    elif inicioRango>10**5:
        print("ERROR: valor máximo (10^5) alcanzado o desbordado.")


while finRango<=inicioRango or finRango>10**5:
    finRango=IngresarNumero("Ingrese el valor de fin del rango: ")
    if finRango<=inicioRango:
        print("ERROR: el valor de fin del rango debe ser mayor al valor de inicio del rango.")
    elif finRango>10**5:
        print("ERROR: valor máximo (10^5) desbordado.")

while step<=0:
    step=IngresarNumero("Ingrese el step del rango: ")
    if step<=0:
        print("ERROR: step debe ser mayor a 0.")

listaPrimos=[]

for i in range(inicioRango,finRango+1,step): # finRango+1 para que también considere al valor final del rango
    if i>3: 
        for j in range(2,i//2+2):
            if i%j==0:
                break
            if j==i//2+1 and i%j!=0:
                listaPrimos.append(i)
    elif i==2:
        listaPrimos.append(i)

print(f"La lista de números primos en el rango [{inicioRango}; {finRango}] con un step de {step} es:\n\t",listaPrimos)