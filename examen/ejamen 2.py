def calcularpuntosFRHH():
    #datos de entrada
    print('desempeño de los profesores:')
    print()
    print("""
    Menu: Seleccione una opcion
    1. puntos realizados de >50<100
    2. puntos realizados de >101<150
    3. puntos realizados de >151
    """)
    menu = int(input())
    #proceso
    if menu == 1:
        print("salario es igual a 10%:")
    elif menu == 2:
        print("salario es igual a 50%:")
    elif menu == 3:
        print("salario es igual a 80%:")
    else:
        print('Ingrese una opcion correcta.')
    #datos de salida
    print("es el monto que percibira el profesor")

calcularpuntosFRHH()
