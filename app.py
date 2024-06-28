import utilidades

op = 0
Nombres = [] #lista
#codigo,nombre,categoria,director,actores,año

while op !=4:
    utilidades.menu()
    op = utilidades.opcion_seleccionada()

    if op == 1:
        nombre.append(utilidades.agregar())
    elif op == 2:
        utilidades.lista_Nombres(nombre)
    elif op == 3:
        Nombres.encontrar_nombre(nombre)
    

utilidades.crear_archivo(nombre)
