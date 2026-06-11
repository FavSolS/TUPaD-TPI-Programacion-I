from countries_helpers import obtener_nombre, obtener_poblacion, obtener_superficie

# Ordenar países por:
# o Nombre
# o Población
# o Superficie (ascendente o descendente)

def ordenar_paises(paises):
    print("¿Por qué campo desea ordenar?")
    print("1. Nombre")
    print("2. Población")
    print("3. Superficie")
    criterio = int(input("Seleccione una opción: "))

    print("¿En qué orden?")
    print("1. Ascendente")
    print("2. Descendente")
    orden = int(input("Seleccione una opción: \n"))
    ascendente = orden == 1

    if criterio == 1:
        resultado = sorted(paises, key=obtener_nombre, reverse=not ascendente)
    elif criterio == 2:
        resultado = sorted(paises, key=obtener_poblacion, reverse=not ascendente)
    elif criterio == 3:
        resultado = sorted(paises, key=obtener_superficie, reverse=not ascendente)
    else:
        print("Opción inválida.")
        return

    for pais in resultado:
        print(f"{pais['nombre']} | {pais['poblacion']} | {pais['superficie']} | {pais['continente']}")

        # DUDA tenemos que modificar el archivo csv?