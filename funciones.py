trabajadores =[]

def opcion_1():
    print("regristrar trabajador")
    nombre = input("ingrese su nombre y apellido por favor:")
    cargo = int(input("ingrese su cargo(1:ceo,2:desarollador,3:analista)"))
    sueldo = int(input("ingrese sueldo bruto:"))
    desc_salud = round(sueldo *0.07)
    desc_afp = round(sueldo*0.12)
    sueldo_liquido = sueldo-desc_afp-desc_salud
    trabajador = [nombre,cargo,sueldo,desc_salud,desc_afp,sueldo_liquido]
    trabajadores.append(trabajador)
    print("trabajador agregado con exito")
def opcion_2():
    if len(trabajadores) ==0:
        print("no existen trabajdores,elija la opcion 1")
    else:
        print("\tlista de trabajadores")
        print("trabajador:\tsueldo bruto:\tdescuento salud:\tdescuento AFP:\t sueldo liquido:")
        for t in trabajadores:#t:seria cada trabajadore de la lista
            print(f"{t[0]}\t{t[1]}\t{t[2]}\t\t\t{t[3]}\t\t{t[4]}\t\t{t[5]}")
def opcion_3():
    if len(trabajadores) ==0:
        print("no existen trabajdores,elija la opcion 1")
    else:
        opc2 = int(input("que cargo desea imprimir (1:ceo , 2:desarollador, 3:analista)"))
        if opc2 ==4:
            with open("todos_trabajadores.txt","w", newline="\n") as archivo:
                for t in trabajadores: 
                    archivo.write(f"{t[0]}{t[1]}{t[2]}{t[3]}{t[4]}{t[5]}")
        else:           
            with open("trabajadores_por_cargo.txt","w", newline="\n") as archivo:
                for t in trabajadores:
                    if opc2 == t[1]:
                        archivo.write(f"{t[0]}{t[1]}{t[2]}{t[3]}{t[4]}{t[5]}")
    print("archivo creado con exito")
def opcion_4():
    print("adios")
    exit()