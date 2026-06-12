from countries_helpers import buscar_por_texto

# • Buscar un país por nombre (coincidencia parcial o exacta).
def buscar_pais(paises):
    nombre = input("Ingrese el nombre del pais buscado: ")
    resultados = buscar_por_texto(paises, 'nombre', nombre)

    if len(resultados) == 0:
        print(f"No se encontraron países con '{nombre.strip()}'.")
    else:
        print(f"Se encontraron {len(resultados)} resultado/s:")
        for pais in resultados:
            print(f"\nPais: {pais['nombre']} | Poblacion: {pais['poblacion']} | Superficie: {pais['superficie']} | Continente: {pais['continente']}")