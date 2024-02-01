import comprobacion

biblioteca = []

while True:
    print("\n1. Agregar libro")
    print("2. Prestar libro")
    print("3. Devolver libro")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")
    
    comprobacion.comprobacion(opcion)

