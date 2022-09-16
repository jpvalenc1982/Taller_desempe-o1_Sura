'''
2. Leer información de 10 frutas {nombre, color, precio} para preparar un salpicón; 
el programa debe permitir mostrar las 10 frutas ingresadas al mismo tiempo+(1)
'''
print("***PREPARANDO UN SALPICÓN***")

frutas=[]

for i in range(10):
    fruta={}
    fruta['nombre']=input(f'Ingrese el nombre de la fruta: ')
    fruta['color']=input(f'Ingrese el color de la fruta: ')
    fruta['precio']=input(f'Ingrese el precio de la fruta: ')
    frutas.append(fruta)
    
print(frutas)