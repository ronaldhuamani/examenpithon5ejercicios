def calcularnotafinal():
    #datos de entrada
    primeraunidad=float(input("ingrese la nota de la primera unidad:"))
    segundaunidad=float(input("ingrese la nota de la segunda unidad:"))
    terceraunidad=float(input("ingrese la nota de la tercera unidad:"))
    trabajofinal=float(input("ingrese el 50%  de la nota del trabajo: "))
    #proceso
    nota = primeraunidad*0.1+segundaunidad*0.15+terceraunidad*0.25+trabajofinal*0.5
    #datos de salida
    print("la nota del del estidiante es: " , nota)

calcularnotafinal()
