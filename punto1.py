'''
Construir un programa que permita ingresar 20 números enteros y cuente cuantos números negativos fueron ingresados (+1)
'''
print("***Programa para contar la cantidad de números neutros, positivos y negativos enteros***")

numeroentero = 1
neutros = 0
negativos = 0
positivos = 0
while (numeroentero<=20):
    n = int(input(f'Ingresa el número {numeroentero}: '))
    if(n==0):
        neutros+=1
    elif(n<0):
        negativos+=1
    else:
        positivos+=1
    numeroentero+=1

print(f'{neutros} son números son neutros')
print(f'{negativos} son números son negativos')
print(f'{positivos} son números son positivos')