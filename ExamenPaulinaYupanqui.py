import random, math, csv
menora_800 = []
entre800y2M = []
mayoresa_2M = []
opc = 0

archTrabajadores = "archTrabajadores.csv"
def asignacionSueldos():
    with open (archTrabajadores, mode = "w", newline="") as file:
        writer = csv.writer(["nombre", "sueldo"])
        for trabajadores in archTrabajadores:
            sueldo = random.randint(300000, 25000000)
            writer.writerow([trabajadores, sueldo])
            print("Los sueldos han sido almacenados en csv")

def clasf_sueldos():
    sueldosTotales = 0
    with open(archTrabajadores, mode = "r") as file:
        reader = csv.reader(file)
        next(reader)
        print("La clasificación de sueldos es: ")
        for row in reader:
            nombre = row [0]
            sueldo = int(row[1])
            sueldosTotales += sueldo
            if sueldo <800000:
                menora_800.append(nombre, sueldo)
            elif sueldo <= 2000000:
                entre800y2M.append(nombre, sueldo)
            else:
                mayoresa_2M.append(nombre, sueldo)
    print("Los sueldos menores a $800.000 son: ",len(menora_800))
    print("Los sueldos entre $800.000 y $2.000.000 son: ", len (entre800y2M))
    print("Los sueldos mayores a $2.000.000 son: ", len(mayoresa_2M))
    

def menu(): 
    while True:
        print ("** Bienvenido **")
        print ("*******************")
        print ("* Menú opciones *")
        print("1) Asignación de sueldo ")
        print("2) Clasificación de su sueldo")
        print("3) Ver estadísticas de sueldos")
        print("4) Reporte de sueldos")
        print("5) Salir del programa")

        opc = int(input("Escoja una de las opciones: "))
        if opc == "1":
           asignacionSueldos()

        elif opc == 2:
            print("")

        elif opc == 3:
            print("")

        elif opc == 4: 
            print("")

        elif opc == "5":
            print("Saliendo...")
        break
menu()
