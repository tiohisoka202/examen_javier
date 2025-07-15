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