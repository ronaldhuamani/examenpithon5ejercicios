def calcularnota():
    #datos de entrada
    primeraunidad = float(input("ingrese la nota de la primera unidad:"))
    segundaunidad = float(input("ingrese la nota de la primera unidad:"))
    terceraunidad = float(input("ingrese la nota de la tercera unidad:"))
    #proceso
    nota = primeraunidad*0.1 + segundaunidad*0.15 + terceraunidad*0.25
    #datos de salida
    print("la nota promedio del 50% es:" , nota)

calcularnota()
