''' 
3. Construir un programa para ir de compras en un supermercado que permita la construcción del siguiente MENU:

1. Digitar 1 para recibir {código, nombre, precio} de un producto (+0.8)
2. Digitar 2 para mostrar todos los productos registrados (+0.8)
3. Digitar 0 para SALIR
'''
i=1
productos=[]
print("***MENÚ DE COMPRAS***")
print("1. Agregar productos a la canasta: ")
print("2. Mostrar los productos ingresados a la canasta: ")
print("0. Salir")

while(i!=0):

    producto={}
    i=int(input("Digite una opción del menú: "))
    if(i==1):
        print("Agregando productos a la canasta\n")
        producto['codigo']=input(f'Ingrese el código del producto: ')      
        producto['nombre']=input(f'Ingrese el nombre del producto: ')
        producto['precio']=input(f'Ingrese el precio del producto: ')
        productos.append(producto)
    elif(i==2):
        print("Mostrando los productos ingresados a la canasta\n")
        print(productos)
    elif(i==0):
        break
    else:
        print("Digite una opción correcta: ")