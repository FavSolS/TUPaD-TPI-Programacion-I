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


def agregar_csv(nuevo_pais):
    with open('countries.csv', 'a') as archivo:
        archivo.write(f"{nuevo_pais['nombre']},{nuevo_pais['poblacion']},{nuevo_pais['superficie']},{nuevo_pais['continente']}\n")


def actualizar_csv(paises):
    with open('countries.csv', 'w') as archivo:
        archivo.write("nombre,poblacion,superficie,continente\n")
        for pais in paises:
            linea = f"{pais['nombre']},{pais['poblacion']},{pais['superficie']},{pais['continente']}\n"
            archivo.write(linea)
