def menu ():
    menu = """1)Agregar nombre del estudiante
2)Listado de alumnos
3)buscar alumnos por nivel
4)salir
""" #definir segun enunciado
    print(menu, end ="")


def opcion_seleccionada():
    while True:
        try:
            opc = int(input())
            if opc>0 or opc<5:
                return opc
            else:
                print("Ingrese una de las opciones")
        except ValueError:
            print("Ingrese una opción númerica")

def agregar ():
    nombre = input("Ingrese el nombre: ")
    nivel = input("Ingrese las nivel: ")
    notas = input("Ingrese las notas: ")
    prom_notas = input( (sum(notas+notas)"Promedio del estudiante")
    
    

    res = {"nombre":nombre,"nivel":nivel,"notas":notas}
    return res

def lista_Nombres(lista):
    for i in range(len(lista)):
        print(f"Nombres {i+1}:")
        print(f"nombre{lista[i]["nombre"]}")
        print(f"nivel{lista[i]["nivel"]}")
        print(f"notas{lista[i]["notas"]}")
        
        
        print("--------------------------------------------------")

def encontrar_Nombres(lista):
    cu = input("Ingrese el nombre del Estudiante")
    enc = False

    for i in range(len(lista)):
        if cu == lista[i]["nombre"]:
            res = lista[i]
            enc = True

    if enc:
        print(f"nombres {i+1}:")
        print(f"nombre{res["nombre"]}")
        print(f"nivel{res["nivel"]}")
        print(f"notas{res["notas"]}")
       
    else:
        print("Estudiante no encontrado")   
        

def archivo (lista):
    with open("lista_Nombres.txt","w") as archivo:
        for i in range (lista):
            res = i["nombre"]+", "+i["nivel"]+", "+i["nota"]+", "+"\n"
            archivo.write(res)
