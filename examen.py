productos ={'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
            '2175HD': ['Acer', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
            'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
            'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
            'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
            '123FHD': ['Acer', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
            '342FHD': ['Acer', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
            'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],}
stock ={'8475HD': [387990,10],
        '2175HD': [327990,4],
        'JjfFHD': [424990,1],
        'fgdxFHD': [664990,21],
        'GF75HD': [749990,2],
        '123FHD': [290890,32],
        '342FHD': [444990,7],
        'UWU131HD': [349990,1], }
Acer=43
HP=31
Asus=3
Dell=1
def stock_marca():
    op=input('Igrese marca a consultar: ').lower
    if op=='Acer' or 'acer':
        print('El stock es: 43')
    elif op=='HP' or 'hp':
        print('El stock es: 31',)
    elif op=='Asus' or 'asus':
        print('El stock es: 3',)
    elif op=='Dell' or 'dell':
        print('El stock es: 1',)
    else:
        print('Marca no disponible')

def busqueda_RAM():
    RAMmi=int(input('Ingrese RAM mínima: '))
    RAMma=int(input('Ingrese RAM máxima: '))
    if RAMma>=RAMmi:
        print('vas bien')
    else:
        print('No es valido')

def eliminar_producto():
    marca=input('Ingrese producto a eliminar: ')
    if marca in productos:
        del productos[marca]
        print('Producto eliminado')
    else:
        print('El modelo no existe')

while True:
    print('***Menu Principal***')
    print('====================')
    print('1. Stock marca.')
    print('2. Búsqueda por RAM y precio.')
    print('3. Eliminar producto.')
    print('4. Salir.')
    opc=input('Ingrese Opción: ')
    if opc=='1':
        stock_marca()
    elif opc=='2':
        busqueda_RAM()
    elif opc=='3':
        eliminar_producto()
    elif opc=='4':
        print('Programa finalizado')
        break
    else:
        print('Debe seleccionar una opción válida!!')