def tipovacunaFRH():
    #datos de entrada
    print('tipos de vacuna A,B,C:')
    print()
    print("""
    Menu: Seleccione una opcion
    1. si es mayor a 70 años ya sea mujer o hombre 
    2. si tiene entre los 16 a 69 años si es mujer 
    3. si tiene entre los 16 a 69 años si es hombre 
    4. si tiene menor de 16 años 
    """)
    menu = int(input())
    #proceso
    if menu ==1:
        print("se le aplicara el tipo de vacuna C:")
    elif menu==2:
        print("se le apicara el tipo de vacuna B:")
    elif menu==3:
        print("se le aplicara el tipo de vacuna A:")
    elif menu==4:
        print("se le aplicara el tipo de vacuna A :")
    else:
        print("ingrese la opcion correcta:")
    #datos de salida
    print("es el tipo de vacuna que se le aplicara al pasiente:")

tipovacunaFRH()
