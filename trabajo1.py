import os,time
trabajadores =[]

while True:

    os.system('cls')
    print("menu de trabajadores")
    print("""1.registrar trabajador
             2.lista de todos los trabajadores
             3.imprimir sueldos en la pantalla
             4.salir de programa""")
    opc = int(input("ingrese la opcion:"))
    os.system('cls')

    if opc == 1:
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
    elif opc == 2:
        pass

    elif opc ==3:
        pass

    else:
        print("adios")
        break
    time.sleep(3)
