import archivo2

lista=[]

for i in range(0,2):
    numero=int(input("ingrese un numero: "))
    lista.append(numero)

A = lista[0]

B = lista[1]

archivo2.sumar(A,B)