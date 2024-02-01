import opciones

biblioteca = []

while True:
    print("\n1. Agregar libro")
    print("2. Prestar libro")
    print("3. Devolver libro")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        opciones.opcion1(biblioteca)

    elif opcion == "2":
        opciones.opcion2(biblioteca)
        
        
    elif opcion == "3":
        opciones.opcion3(biblioteca)

    elif opcion == "4":
        print("Saliendo del programa.")
        break

    else:
        print("Opción no válida. Por favor, seleccione una opción correcta.")