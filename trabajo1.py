import os,time
from funciones import*



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
        opcion_1()
    elif opc == 2:
        opcion_2()
    elif opc ==3:
        opcion_3()
    else:
        opcion_4()
    time.sleep(3)
