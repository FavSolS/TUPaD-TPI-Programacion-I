# Funciones relacionadas con lectura, escritura y modificacion del csv

# Metodo para crear el archivo por primera vez, se usa el with para garantizar que se cierre correctamente despues de escribir
def leer_csv():
    paises = []
    with open("countries.csv", "r") as archivo:
        next(archivo)  # saltea el encabezado
        for linea in archivo:
            nombre, poblacion, superficie, continente = linea.strip().split(',')
            pais = {
                'nombre': nombre,
                'poblacion': int(poblacion),
                'superficie': int(superficie),
                'continente': continente
            }
            paises.append(pais)

    print(f"\nSe cargaron {len(paises)} países correctamente.")

    return paises
