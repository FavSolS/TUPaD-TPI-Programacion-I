from countries_helpers import nombre_existe
from countries_csv import agregar_csv, actualizar_csv

# Agregar un país con todos los datos necesarios para almacenarse (No se permiten campos vacíos).

def alta_nuevo_pais(paises):
    try:
        nombre = input("Ingrese el nombre del nuevo país: ")

        if nombre.strip() == "":
            raise ValueError("El nombre no puede estar vacío.")
        
        # Llamo funcion auxiliar
        if nombre_existe(paises, nombre):
            raise ValueError(f"El pais '{nombre.strip()}' ya existe. No se puede volver a cargar.")

        poblacion_str = input(f"Ingrese la poblacion de '{nombre.strip()}': ")
        try:
            poblacion = int(poblacion_str)
        except ValueError:
            raise ValueError("La población debe ser un número entero.")
        
        if poblacion < 0:
            raise ValueError("La población no puede ser negativa.")

        superficie_str = input(f"Ingrese la superficie de '{nombre.strip()}': ")
        try:
            superficie = int(superficie_str)
        except ValueError:
            raise ValueError("La superficie debe ser un número entero.")
        
        if superficie < 0:
            raise ValueError("La superficie no puede ser negativa.")

        continente = input(f"Ingrese a que continente pertenece '{nombre.strip()}': ")

        if continente.strip() == "":
            raise ValueError("El continente no puede estar vacío.")

        nuevo_pais = {
            'nombre': nombre.strip(),
            'poblacion': poblacion,
            'superficie': superficie,
            'continente': continente.strip()
        }
        paises.append(nuevo_pais)
        agregar_csv(nuevo_pais)
        print(f"Pais '{nombre.strip()}' agregado correctamente.")

    except ValueError as e:
        print(f"Error: {e}. Volviendo al menú principal.")



# Actualizar los datos de Población y Superficie de un País.
from countries_helpers import nombre_existe
from countries_csv import actualizar_csv

def modificar_pais(paises):
    try:
        nombre = input("Ingrese el nombre del país a modificar: ")
        if nombre.strip() == "":
            raise ValueError("El nombre no puede estar vacío.")
        if not nombre_existe(paises, nombre):
            raise ValueError(f"El país '{nombre.strip()}' no existe.")

        # busco el pais en la lista
        for pais in paises:
            if pais['nombre'].lower() == nombre.strip().lower():
                
                poblacion_str = input(f"Ingrese la nueva población de '{pais['nombre']}': ")
                try:
                    poblacion = int(poblacion_str)
                except ValueError:
                    raise ValueError("La población debe ser un número entero.")
                if poblacion < 0:
                    raise ValueError("La población no puede ser negativa.")

                superficie_str = input(f"Ingrese la nueva superficie de '{pais['nombre']}': ")
                try:
                    superficie = int(superficie_str)
                except ValueError:
                    raise ValueError("La superficie debe ser un número entero.")
                if superficie < 0:
                    raise ValueError("La superficie no puede ser negativa.")

                pais['poblacion'] = poblacion
                pais['superficie'] = superficie
                break

        actualizar_csv(paises)
        print(f"País '{nombre.strip()}' actualizado correctamente.")

    except ValueError as e:
        print(f"Error: {e}. Volviendo al menú principal.")