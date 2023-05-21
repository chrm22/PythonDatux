num=0
while (num<=0):
    num=int(input("Ingrese un número entero positivo: "))
    if (num<=0):
        print("Error. Número no válido.")

suma=0
for i in range(num+1):
    suma+=i
    
print("La suma de todos los números enteros entre 0 y "+str(num)+" es "+str(suma))