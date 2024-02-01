def opcion1(biblioteca):
    titulo = input("Ingrese el título del libro: ")
    autor = input("Ingrese el autor del libro: ")
    genero = input("Ingrese el género del libro: ")
    disponibilidad = True
    libro = {"titulo": titulo, "autor": autor, "genero": genero, "disponibilidad": disponibilidad}
    biblioteca.append(libro)
    print(f'Libro "{titulo}" agregado a la biblioteca.')
    
def opcion2(biblioteca):
    titulo = input("Ingrese el título del libro a prestar: ")
    encontrado = False
    for libro in biblioteca:
        if libro["titulo"] == titulo and libro["disponibilidad"]:
            libro["disponibilidad"] = False
            print(f'Libro "{titulo}" prestado con éxito.')
            encontrado = True
            break
    if not encontrado:
        print(f'Libro "{titulo}" no disponible para préstamo.')
        
def opcion3(biblioteca):
    titulo = input("Ingrese el título del libro a devolver: ")
    encontrado = False
    for libro in biblioteca:
        if libro["titulo"] == titulo and not libro["disponibilidad"]:
            libro["disponibilidad"] = True
            print(f'Libro "{titulo}" devuelto con éxito.')
            encontrado = True
            break
    if not encontrado:
        print(f'No se puede devolver el libro "{titulo}".')