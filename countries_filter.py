# Filtrar países por:
# o Continente
# o Rango de población
# o Rango de superficie

from countries_helpers import leer_entero_no_negativo, buscar_por_texto

def _formatear_numero(numero):
    return f"{numero:,}".replace(",", ".")


def mostrar_resultados(resultados, descripcion_filtro):
    print(f"\n{'=' * 60}")

    if len(resultados) == 0:
        print(f"\nNo se encontraron países para el criterio indicado.")
        return

    cantidad = len(resultados)
    etiqueta = "país encontrado" if cantidad == 1 else "países encontrados"
    print(f"\n{cantidad} {etiqueta}:\n")
    print(f"  {'Nombre':<24} {'Población':>14} {'Superficie':>14}  Continente")
    print(f"  {'-' * 24} {'-' * 14} {'-' * 14}  {'-' * 12}")

    for pais in resultados:
        print(
            f"  {pais['nombre']:<24} "
            f"{_formatear_numero(pais['poblacion']):>14} "
            f"{_formatear_numero(pais['superficie']):>14}  "
            f"{pais['continente']}"
        )
    print()


def filtrar_por_continente(paises, continente):
    return buscar_por_texto(paises, 'continente', continente)


def filtrar_por_poblacion(paises, poblacion_min, poblacion_max):
    resultados = []
    for pais in paises:
        if poblacion_min <= pais['poblacion'] <= poblacion_max:
            resultados.append(pais)
    return resultados


def filtrar_por_superficie(paises, superficie_min, superficie_max):
    resultados = []
    for pais in paises:
        if superficie_min <= pais['superficie'] <= superficie_max:
            resultados.append(pais)
    return resultados


def filtrar_paises(paises):
    try:
        print("\n¿Por qué criterio desea filtrar?")
        print("1. Continente")
        print("2. Rango de población")
        print("3. Rango de superficie")
        criterio = int(input("Seleccione una opción: "))

        if criterio == 1:
            continente = input("Ingrese el continente a filtrar: ")
            if continente.strip() == "":
                raise ValueError("El continente no puede estar vacío.")
            resultados = filtrar_por_continente(paises, continente)
            mostrar_resultados(resultados, f"continente «{continente.strip()}»")

        elif criterio == 2:
            poblacion_min = leer_entero_no_negativo("Ingrese la población mínima: ", "población mínima")
            poblacion_max = leer_entero_no_negativo("Ingrese la población máxima: ", "población máxima")
            if poblacion_min > poblacion_max:
                raise ValueError("La población mínima no puede ser mayor que la máxima.")
            resultados = filtrar_por_poblacion(paises, poblacion_min, poblacion_max)
            mostrar_resultados(
                resultados,
                f"población entre {_formatear_numero(poblacion_min)} y {_formatear_numero(poblacion_max)} habitantes",
            )

        elif criterio == 3:
            superficie_min = leer_entero_no_negativo("Ingrese la superficie mínima: ", "superficie mínima")
            superficie_max = leer_entero_no_negativo("Ingrese la superficie máxima: ", "superficie máxima")
            if superficie_min > superficie_max:
                raise ValueError("La superficie mínima no puede ser mayor que la máxima.")
            resultados = filtrar_por_superficie(paises, superficie_min, superficie_max)
            mostrar_resultados(
                resultados,
                f"superficie entre {_formatear_numero(superficie_min)} y {_formatear_numero(superficie_max)} km²",
            )

        else:
            print("Opción inválida.")
            return

    except ValueError as e:
        print(f"Error: {e}. Volviendo al menú principal.")
