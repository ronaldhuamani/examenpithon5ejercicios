def tiposalario():
    #datos de entrada
    print("bono profesor")
    print()
    print("""
    Menu: Seleccione una opcion
    1. calcular los puntos >50>100
    2. Calcular los puntos >101<150
    3. calcular los puntos >151
    """)
    menu = int(input())
    #proceso
    if menu == 1:
        print("salario minimo es a 10%: ")
    elif menu == 2:
        print("salario minimo es a 50%): ")
    elif menu == 3:
        print("salrio minimo es a 80%:")
    else:
        print("Ingrese una opcion correcta.")
        print()
    #datos de salida

tiposalario()
