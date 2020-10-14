def calcularPrecioLapiz():
  #Datos Entrada
  cantidadL=int(input("Ingresa la cantidad de lapices a comprar:"))
  #Proceso
  if(cantidadL>=1400):
    costoPagar=cantidadL*0.1
  #Datos de salida
  print("El costo total a pagar es: ", costoPagar)

calcularPrecioLapiz()